# ESPN CricInfo Scrapper

A very simple scrapper to scrape and export player information as CSV dataset. 

## Kaggle 
Dataset is published on [Kaggle](https://www.kaggle.com/exilour/cricinfo-cricketer/) can be updated using this script.


## Dataset information
* Source: [Espn CricInfo](https://www.espncricinfo.com/)
* Number of columns: 89
* Number of rows: 39229

## Data format
the column names are in this format

**player_name, country, {[#record_type][#record_of][#record_tag]}**

* <record_type>: 
    * **bf** = batting and fielding
    * **bw** = bowling
* <record_of>: 
    * **odi** = one day international
    * **tests** = test matches
    * **t20s** = T20 matches

* <record_tag>:     
    * **match** = no. of matches
    * **innings** = no. of innings
    * **no** = not out
    * **runs** = total runs
    * **hs** = highest score
    * **ave** = average score
    * **bf** = balls faced
    * **sr** = strike rate
    * **100** = no of 100s
    * **50** = no of 50s 
    * **4** = no of 4 scored
    * **6** = no of 6 scores
    * **ct** = catch taken
    * **st** = stamping taken
    * **balls** = no. of balls delivered
    * **runs** = runs given
    * **wkts** = wickets taken
    * **bbi** = best innings bowling
    * **bbm** = best match bowling
    * **ave** = bowling average
    * **econ** = economy rate
    * **sr** = strike rate
    * **4w** = 4 wickets a match taken
    * **5w** = 5 wickets a match taken
    * **10** = 10 wickets a match taken

> A TAG is added on each row before each type of data. as bfodi_tag, bftests_tag.

## About the respository and code
This codes are done way before. I wasn't sure if I am to share this code then since the data was scrapped just as a night's fun interest. Now since people are still downloading this after ~3 years (back in 2017) I think some may want the updated data. Hence sharing the code.

## Code files and description

* [cricscraper.py](cricscraper.py): Contains the crawler and scrapper function. Set the global variable as many player you like to scrape. As of now the limits are set from first of archive to last. May change over time. It has a 15ms delay before each call, because espncripinfo [expects](https://www.espncricinfo.com/robots.txt) this delay for scrapper and we should respect that.
* [structure.py](structure.py): Contains the code to filter and clear the data scrapped from web. Should have been done inside crawler. But I am lazy and wanted to have the data safe and sound first. LOL
* [update.py](update.py): will crawl and scrape through all player profiles. Run this to update entire dataset

### Usage

#### Requirements
* Python 3.6+
* and package required is beautifulsoup4 you can install it manually or from *requirements.txt* file.

`pip install -r requirements.txt`

#### Running
* You may run [test.py](test.py) first to check if everything is working. This will crawl first 5 profile and dump data to show if all methods are working. 
* Then just run [update.py](update.py). This will crawl the entire thing and dump into files named after the date. 

Hope the dataset comes to any use if you downloaded.
