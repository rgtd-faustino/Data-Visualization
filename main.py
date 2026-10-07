import pandas as pd
import numpy as np

DATASETS_DIR = "D:/FCUL/Visualização de Dados/tp/Data-Visualization/Datasets"

working_hours = pd.read_csv(
    DATASETS_DIR + "/Horas de Trabalho (Our World in Data)/annual-working-hours-per-worker.csv"
)
happiness = pd.read_csv(
    DATASETS_DIR + "/World Happiness Report (Kaggle)/happy.csv"
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



working_hours_copy["median"] = np.mean(working_hours_copy["Working hours per worker"])
print("Number of countries:", working_hours_copy["Code"].nunique())

print("\n")
print('Working Hours dataset:')
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
