# README

## About the Original Dataset

The files in this folder include datasets for each of the most intense hurricanes from the Atlantic Basin between 2000 and 2020, and a larger dataset that includes data for all tropical systems in the Atlantic Basin between 1851 and 2020. These files were derived from the ["Best Track Data (HURDAT2)"](https://www.nhc.noaa.gov/data/#hurdat) dataset, a product of the [National Hurricane Center](https://www.nhc.noaa.gov/data/).

For more information on how to read and utilize this data set, check out ["The revised Atlantic hurricane database (HURDAT2) November 2019"](https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-nov2019.pdf). The definition of "intense" we are using comes from [***Hurricanes and Typhoons: Past, Present, and Future*** (2004), edited by Richard J. Murname and Kam-Biu Liu](https://www.aoml.noaa.gov/hrd/Landsea/rpibook-final04.pdf) (full text available from NOAA at link), and indicated tropical cyclones with a minimum central pressure below 920 mb.

## About the Adapted Files

Included in this folder is the full [Atlantic hurricane database (HURDAT2) 1851-2020](https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2020-052921.txt), which includes all Best Track Hurricane Data for the Atlantic Basin from 1851 until May 29, 2021. The additional files in this folder represent [intense hurricanes in the Atlantic Basin 2000-2020](https://en.wikipedia.org/wiki/List_of_the_most_intense_tropical_cyclones#North_Atlantic_Ocean). 

To create these individual text files, we have taken the data listed in (HURDAT2), and copied it for individual storms into their own file. The file names include the the original markers used to delineate each storm listed in the database, and follow the naming  convention listing the ocean with which each hurricane is associated (first 2 space in file name), the recorded storm number (next two spaces), the year (next four spaces), as defined by in ["The revised Atlantic hurricane database (HURDAT2) November 2019"](https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-nov2019.pdf) by NHC's Chris Landsea and Jack Beven. In addition, we have added an underscore and the name given to each hurricane for the file name. No changes were made to the data included with each set.

Pursuant with [Disclaimer Requirements outlined by NOAA](https://www.weather.gov/disclaimer), the files in this directory are derived from official datasets. In the format presented here, these files are derivatives, and do NOT represent official information from the United Stated Goverment or the National Oceanic and Atmospheric Administration. For official datasets, please visit the [National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/#hurdat).

### Examples below show the a slice of the original dataset from the file nam, and how it was adapted for this project: ###

**Example slice from original dataset in file `hurdat2-1851-2020-052921.txt`:**
```console
user@computer:~$ cat hurdat2-1851-2020-052921.txt
20040830, 1800,  , TS, 37.6N,  71.4W,  45, 1008,    0,  125,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040831, 0000,  , TS, 39.9N,  71.3W,  35, 1011,    0,   40,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040831, 0600, L, TS, 41.5N,  70.9W,  35, 1012,    0,   25,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040831, 1200,  , EX, 43.1N,  70.5W,  25, 1014,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
AL092004,               IVAN,     94,
20040902, 1800,  , TD,  9.7N,  27.6W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0000,  , TD,  9.7N,  28.7W,  30, 1007,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0600,  , TS,  9.7N,  30.3W,  35, 1005,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1200,  , TS,  9.5N,  32.1W,  40, 1003,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1800,  , TS,  9.3N,  33.6W,  45, 1000,   60,  125,  125,   60,    0,    0,    0,    0,    0,    0,    0,    0,
```
**Example slice of adapted file `AL092004_ivan.txt`:**

```console
user@computer:~$ cat AL092004_ivan.txt
6W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0000,  , TD,  9.7N,  28.7W,  30, 1007,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0600,  , TS,  9.7N,  30.3W,  35, 1005,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1200,  , TS,  9.5N,  32.1W,  40, 1003,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1800,  , TS,  9.3N,  33.6W,  45, 1000,   60,  125,  125,   60,    0,    0,    0,    0,    0,    0,    0,    0,
20040904, 0000,  , TS,  9.1N,  35.0W,  45,  999,   60,  125,  125,   60,    0,    0,    0,    0,    0,    0,    0,    0,
20040904, 0600,  , TS,  8.9N,  36.5W,  50,  997,   60,  100,  100,   60,   25,   25,   25,   25,    0,    0,    0,    0,
20040904, 1200,  , TS,  8.9N,  38.2W,  50,  997,   60,  100,  100,   60,   20,   20,   20,   20,    0,    0,    0,    0,
20040904, 1800,  , TS,  9.0N,  39.9W,  55,  994,   60,  100,   60,   60,   20,   20,   20,   20,    0,    0,    0,    0,
```
