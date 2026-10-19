import pandas as pd
import numpy as np

DATASETS_DIR = "D:/FCUL/Visualização de Dados/tp/Data-Visualization/Datasets"

working_hours = pd.read_csv(
    DATASETS_DIR + "/Horas de Trabalho (Our World in Data)/annual-working-hours-per-worker.csv"
)
happiness = pd.read_csv(
    DATASETS_DIR + "/World Happiness Report (Kaggle)/happy.csv",
    sep=";", # precisamos disto para indicar que as colunas estão separadas por ponto e vírgula senão o pandas interpretava cada linha como uma coluna
    decimal="," # e usamos isto para dizer que os números decimais usam vírgula e assim o pandas converte corretamente para float
)
gdp_per_capita = pd.read_csv(
    DATASETS_DIR + "/PIB per Capita (World Bank Open Data)/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_468810.csv",
    # we have to skip the first 4 lintes because they're are about metadata because pandas was trying to parse them as data
    skiprows=4
)

# we make copies so that we don't "ruin" or compromise the original datasets
working_hours_copy = working_hours.copy()
happiness_copy = happiness.copy()
gdp_per_capita_copy = gdp_per_capita.copy()

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
    gdp_per_capita_copy.groupby("Country Name", observed=True) 
    .agg(
        year_2022=("2022", "mean"),
        year_2023=("2023", "mean"),
        year_2024=("2024", "mean"),
        year_2025=("2025", "mean")
    )
    #.reset_index() # else "Country Name" would be the table's index
    .sort_values(by="year_2025", ascending=False, na_position="last")
)

print(gdp_per_capita_copy_table)

