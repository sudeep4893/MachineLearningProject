# Machine Learning
![ML3.jpg](image/ML3.jpg)

Machine Learning is the field of study that gives computers the capability to learn without being explicitly programmed. ML is one of the most exciting technologies that one would have ever come across.<br>
Machine Learning : __The ability to learn.__

### Repository Overview

This repository is about different Machine Learning algorithm approaches as per the industry practices.


### Project

1. Fast Food Restaurants data analysis
2. Avocado data price prediction
3. Sales store item forecast


### 1. Fast Food Restaurants data analysis

<b>Problem Statement</b><br>
The Fast Food Restaurants dataset we are analyzing and providing Ranking of Top City having Fast Food Restaurants in United States of America


<b>Introduction</b><br>
In the Exploratory Data Analysis we are using Python skills on a structured data set including loading, inspecting, wrangling, exploring, and drawing conclusions from data. The notebook has observations with each step in order to explain thoroughly how to approach the data set. Based on the observation some questions also are answered in the notebook for the reference though not all of them are explored in the analysis.


#### <center>Data
| COLUMN | DATA TYPES |
| --- | --- |
| `ADDRESS`    |    OBJECT|
| `CITY`       |    OBJECT|
| `COUNTRY`    |    OBJECT|
| `KEYS`       |    OBJECT|
| `LATITUDE`   |    FLOAT64|
| `LONGITUDE`  |    FLOAT64|
| `NAME`       |    OBJECT|
| `POSTALCODE` |    OBJECT|
| `PROVINCE`   |    OBJECT|
| `WEBSITES`   |    OBJECT|


<b>Observations</b><br>
* Name : We found there are spelling mistakes(upper, lower and punctuation) on name column, we can group similar names.
* Keys : We noticed keys include country, province, city and address were present, all keys are considered as unique.
* Websites : We have 465 websites missing.<br>
Other than Websites we don't have any missing data.
* Standardize all column headers to lower case (to prevent typos!)
* Divided our data into 4 Zones with respect to province.<br>
East_zone = ["CT", "MA", "ME", "NH", "NJ", "NY", "PA", "RI", "VT", "Co Spgs"]<br>
West_zone = ["AK", "AZ", "CA", "CO", "HI", "ID", "MT", "NM", "NV", "OR", "UT", "WA", "WY"]<br>
South_zone = ["AL", "AR", "DC", "DE", "FL", "GA", "KY", "LA", "MD", "MS", "NC", "OK", "SC", "TN", "TX", "VA", "WV"]<br>
Central_zone = ["IA", "IL", "IN", "KS", "MI", "MN", "MO", "ND", "NE", "OH", "SD", "WI"]<br>


<b>Conclusion</b><br>
* The Fast Food Restaurant Survey being conducted in US to helps and understand the place where the Fast food is highly consumed. By removing the punctuation on Name column we came to know that Mc Donald's count being the highest.
* Cincinnati City in Ohio being the Top ranking in US having highest number of restaurants.
* CA (California) state being the Top ranking in US having highest number of restaurants.TX (Texas) being the second highest in US, both states come under range of 600 - 700 restaurants count.
* McDonalds being the Top ranking in US having highest number of fast food restaurants, count is 2105. Burger King being the second highest in US, restaurant count is 1154.
* If we compare 4 Zones in US, South Zone being the Top ranking in US having highest number of fast food restaurants 41.7%. East Zone having 10.8% Fast Food restaurant in US, they are less eating Fast Food people rather than South Zone.
