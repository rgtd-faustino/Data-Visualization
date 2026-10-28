import pandas as pd
import numpy as np
import matplotlib as plt

DATASETS_DIR = "D:/FCUL/Visualização de Dados/tp/Data-Visualization/Datasets"

working_hours = pd.read_csv(
    DATASETS_DIR + "/Horas de Trabalho (Our World in Data)/annual-working-hours-per-worker.csv"
)
happiness = pd.read_csv(
    DATASETS_DIR + "/World Happiness Report (Kaggle)/happy.csv",
    sep=";", # we need this to indicate that the columns are separated by semicolons, otherwise pandas would interpret each line as one column
    decimal="," # and we use this to indicate that decimal numbers use commas, so pandas converts them correctly to float
)
gdp_per_capita = pd.read_csv(
    DATASETS_DIR + "/PIB per Capita (World Bank Open Data)/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_468810.csv",
    # we have to skip the first 4 lines because they contain metadata and pandas would try to parse them as data
    skiprows=4
)

# we make copies so that we don't "ruin" or compromise the original datasets
working_hours_copy = working_hours.copy()
happiness_copy = happiness.copy()
gdp_per_capita_copy = gdp_per_capita.copy()

# in this "working hours" dataset the year column has a capital Y so we can rename it so they all have the same column's name
working_hours_copy = working_hours_copy.rename(columns={"Year": "year"})
# for the "happy" dataset the date contains the year, so we extract it into a new column
happiness_copy["year"] = pd.to_datetime(
    happiness_copy["Data"],
    format="%d/%m/%Y" # the dates are written in this order
).dt.year # extract only the year

# this is where we have a problem because there isn't a year column, the dataset has columns for every year
gdp_per_capita_copy = gdp_per_capita_copy.melt(
    # so we can keep the columns that identify each country and the indicator and associate them with the values we want
    # the country code is different for every country and works like a primary key as in SQL
    # we also keep the country name, indicator name and indicator code because we don't want to delete any information yet
    id_vars=[
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code"
    ],
    # and this indicates which columns have to be converted into lines
    # if the column name contains only digits then it means we found a year column
    value_vars=[
        column for column in gdp_per_capita_copy.columns
        if str(column).isdigit()
    ],
    # with this we tell pandas to grab the columns' names which are the years and transform them into a new column named "year"
    var_name="year",
    # but we can't forget about the values that would be inside those columns, namely the gdp per capita so this grabs those values
    # and puts them in a new column named gdp_per_capita
    value_name="gdp_per_capita"
)

# with this we can go from this:
# Country Name | Country Code | 2021 | 2022 | 2023
# Portugal     | PRT          | ...  | ...  | ...
# to this:
# Country Name | Country Code | year | gdp_per_capita
# Portugal     | PRT          | 2021 | ...

# but we still have to convert them into numerical values for later calculations and operations and things like that
gdp_per_capita_copy["year"] = pd.to_numeric(
    gdp_per_capita_copy["year"],
).astype(int)

# we dont do the same for the GDP values because they're already numbers, the years were text because they were the columns' names

print("\n")
print("======================================= Working Hours dataset =======================================")
print("\n")

print("Median working hours: ", np.median(working_hours_copy["Working hours per worker"]))
print("Mean working hours: ", np.mean(working_hours_copy["Working hours per worker"]))
print("Number of countries:", working_hours_copy["Code"].nunique())

print("\n")
print('Working Hours dataset head:')
print(working_hours_copy.head())
print("\n")

working_hours_copy_continent = (
# observed=True avoids showing unused categorical combinations.
    working_hours_copy.groupby("World region according to OWID", observed=True) 
    .agg(
        mean_working_hours=("Working hours per worker", "mean")
    )
    #.reset_index() # else "World region according to OWID" would be the table's index
)

print(working_hours_copy_continent)

working_hours_copy_country = (
# observed=True avoids showing unused categorical combinations.
    working_hours_copy.groupby("Entity", observed=True) 
    .agg(
        mean_working_hours=("Working hours per worker", "mean")
    )
    #.reset_index() # else "World region according to OWID" would be the table's index
)

print(working_hours_copy_country)


#print('\nWorld Happiness dataset:')
#print(happiness_copy.head())

#print('\nGDP per Capita dataset:')
#print(gdp_per_capita_copy.head())

print("\n")
print("======================================= World Happiness dataset =======================================")
print("\n")


print("\nWorld Happiness dataset head:")
print(happiness_copy.head())

print("\nCountries:")
print(happiness_copy["Country name"].head())

print("\n")
print("Median happiness score: ", np.median(happiness_copy["Ladder score"]))
print("Mean happiness score: ", np.mean(happiness_copy["Ladder score"]))

print("\n")
print('Happiness dataset head:')
print(happiness_copy.head())
print("\n")

happiness_copy_table = (
# observed=True avoids showing unused categorical combinations.
    happiness_copy.groupby("Country name", observed=True) 
    .agg(
        rank=("Rank", "mean"),
        life_choices_mean=("Explained by: Freedom to make life choices", "mean"),
        ladder_score_mean=("Ladder score", "mean"),
        social_support_mean=("Explained by: Social support", "mean")
    )
    #.reset_index() # else "Country name" would be the table's index
    #.sort_values(by="ladder_score_mean", ascending=False)
    .sort_values(by="rank", ascending=True)
)

print(happiness_copy_table)





print("\n")
print("======================================= GDP Per Capita dataset =======================================")
print("\n")

print("\nGDP Per Capita dataset head:")
print(gdp_per_capita_copy.head())
print("\n")

print("\nCountries:")
print(gdp_per_capita_copy["Country Code"].head())
print("\n")

gdp_per_capita_copy_table = (
# observed=True avoids showing unused categorical combinations.
    gdp_per_capita_copy.groupby(["Country Name", "year"], observed=True)
    .agg(
        gdp_per_capita=("gdp_per_capita", "mean")
    )
    #.reset_index() # else "Country Name" would be the table's index
    .sort_values(by=["year", "gdp_per_capita"], ascending=[True, False], na_position="last")
)

print(gdp_per_capita_copy_table)



print("\n")
print("======================================= JUNTAR OS DATASETS ATRAVÉS DOS ANOS =======================================")
print("\n")

combined_datasets = pd.merge(
    happiness_copy,
    working_hours_copy,
    left_on=["Country name", "year"],
    right_on=["Entity", "year"],
    how="inner"
)
combined_datasets = pd.merge(
    combined_datasets,
    gdp_per_capita_copy[["Country Name", "year", "gdp_per_capita"]],
    left_on=["Country name", "year"],
    right_on=["Country Name", "year"],
    how="inner"
)
print(combined_datasets)

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(combined_datasets["years"], alpha=0.65, color="#4c78a8")
plt.show()