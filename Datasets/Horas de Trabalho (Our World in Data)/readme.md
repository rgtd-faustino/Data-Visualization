# Annual working hours per worker - Data package

This data package contains the data that powers the chart ["Annual working hours per worker"](https://ourworldindata.org/grapher/annual-working-hours-per-worker?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- Every remaining column is a data column, each one a time series. Downloaded with the "full data" option each corresponds to one time series below; with "only selected data visible in the chart" they are transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about each time series


### Working hours per worker
Average working hours per worker in a given year.
Last updated: August 5, 2025  
Next expected update: November 2026  
Date range: 1870–2023  
Unit: hours per worker  
Source: Feenstra et al. – Penn World Table (2025); Huberman and Minns (2005) – with major processing by Our World in Data  

#### How to cite this data

Feenstra et al. – Penn World Table (2025); Huberman and Minns (2005) – with major processing by Our World in Data

#### What you should know about this data
- This indicator combines data from Huberman and Minns (2005) (between 1870 and 1938) with the Penn World Table (1950 onward).
- The definitions of working hours differ between the sources: while Huberman and Minns focus on full-time production workers in non-agricultural activities, Penn World Table data includes all employees and self-employed people in the economy.
- Even considering these differences, the data from Huberman and Minns represents a good approximation of the average working hours in the past.

#### Notes on our processing step for this indicator
We selected the data from Huberman and Minns (2005) for the period between 1870 and 1938, and combined it with the entire Penn World Table dataset (indicator `avh`).


### World region according to OWID
Regions defined by Our World in Data, which are used in OWID charts and maps.
Last updated: January 1, 2023  
Date range: 2023–2023  
Source: Our World in Data  

#### How to cite this data

Our World in Data


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### Feenstra et al. – Penn World Table

PWT version 11.0 is a database with information on relative levels of income, output, input and productivity, covering 185 countries between 1950 and 2023.

Producer: Feenstra et al.  
Published: 2025-10-07  
Retrieved on: 2025-10-09  
Retrieved from: https://www.rug.nl/ggdc/productivity/pwt/  
Direct download: https://dataverse.nl/api/access/datafile/554105  
License: CC BY 4.0 (https://www.rug.nl/ggdc/productivity/pwt/)  

Citation: Feenstra, Robert C., Robert Inklaar and Marcel P. Timmer (2015), "The Next Generation of the Penn World Table" American Economic Review, 105(10), 3150-3182, available for download at www.ggdc.net/pwt

### Huberman and Minns – Working hours (Huberman and Minns, 2005)

This paper brings a long-term perspective to the debate on the causes of worktime differences among OECD countries. Exploiting new data sets on hours of work per week, days at work per year, and annual work hours between 1870 and 2000, we challenge the conventional view that Europeans began to labor fewer hours than Americans only in the 1980s. Like Australians and Canadians, Americans tended to work longer hours, after controlling for income, beginning around 1900. Labor power and inequality, which are held to be important determinants of worktime after 1970, had comparable effects in the period before 1913. To explain the longstanding predisposition of the New World to give more labor time, we examine the effects of three initial factors in 1870, culture, human capital, and geography on hours of work in 2000. We find that geography – the low population density of the New World that has led to shorter commutes and lower fixed costs of getting to work – has had an enduring impact on supply of labor time.

Producer: Huberman and Minns  
Published: 2005-10-01  
Retrieved on: 2025-08-05  
Retrieved from: https://ideas.repec.org/p/iis/dispap/iiisdp95.html  
License: © 2005 Huberman and Minns (https://ideas.repec.org/p/iis/dispap/iiisdp95.html)  

Citation: Huberman, M., & Minns, C. (2005). Hours of Work in Old and New Worlds: The Long View, 1870-2000. Tables 1, 2, and 3. The Institute for International Integration Studies Discussion Paper Series iiisdp95, IIIS.

### Our World in Data – Regions

Producer: Our World in Data  

    