import pandas as pd
import numpy as np
from pathlib import Path 
from IPython.display import display

try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    # Jupyter Notebook 环境下没有 __file__ 变量
    BASE_DIR = Path.cwd()


DATASETS_DIR = BASE_DIR / "Datasets"

working_hours = pd.read_csv(
    DATASETS_DIR / "Horas de Trabalho (Our World in Data)/annual-working-hours-per-worker.csv"
)
happiness = pd.read_csv(
    DATASETS_DIR / "World Happiness Report (Kaggle)/happy.csv"
)
gdp_per_capita = pd.read_csv(
    DATASETS_DIR / "PIB per Capita (World Bank Open Data)/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_468810.csv",
    # we have to skip the first 4 lintes because they're are about metadata because pandas was trying to parse them as data
    skiprows=4
)

# we make copies so that we don't "ruin" or compromise the original datasets
working_hours_copy = working_hours.copy()
happiness_copy = happiness.copy()
gdp_per_capita_copy = gdp_per_capita.copy()


# clean gdp_per_capita data

gdp_per_capita_copy = gdp_per_capita.copy()
# display(gdp_per_capita_copy.head())

# Delete unnecessary columns. 
gdp_clean = gdp_per_capita_copy.drop(
    columns=["Indicator Name", "Indicator Code", "Unnamed: 70"], 
    errors='ignore'
    )
# Convert the years from columns to rows.
gdp_clean = gdp_clean.melt(
    id_vars =["Country Name", "Country Code"],
    var_name = "Year",
    value_name = "GDP_per_capita"
)
# convert the year from str to num
gdp_clean["Year"]= pd.to_numeric(gdp_clean["Year"])

# select data after 2005
gdp_clean = gdp_clean[gdp_clean["Year"] >= 2005]

display(gdp_clean.head())
# display(gdp_clean[gdp_clean["Country Code"] == "ABW"].head())

print(gdp_clean.isna().sum())
print(gdp_clean.shape)

missing_gdp = gdp_clean[gdp_clean["GDP_per_capita"].isna()]

display(missing_gdp.head())
