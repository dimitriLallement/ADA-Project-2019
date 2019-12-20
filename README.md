# Trains, Delays and Network

CS-401 Applied Data Analysis, Autumn 2019, EPFL Santiago Anton Moreno, Dimitri Lallement, Maria Pandele, Ejub Talovic

## Abstract

Transport is a key factor in today's society. We have to move often and fast in our daily lives. We also need to consider the impact some types of transport have on our ecosystem.  
Public transport and the train system in Switzerland is constantly trying to improve for us to be able to move efficiently. The main issue that arise in every train system is the schedule and the delay the passengers have to cope with. It’s one of the drawbacks that deter some people from using trains instead of their cars.  
The SBB division of passenger transport offers open data about train arrivals, departures, delays, etc. We want to use this data to understand the network of railway stations in Switzerland.  
Our goal is to investigate where are the problematic stations located and quantify the delay depending on the location and time of a train. We also want to provide a tool that allows the user to predict a delay for his ride.

## Prerequisites

- Python 3.6.5 or later
- Pandas 0.24.2 or later
- Numpy 1.17.2 or later
- seaborn 0.9.0 or later
- sklearn 0.21.2 or later
- geopy 1.20.0 or later

## Usage

### General analysis

All our analysis are in the `Project1.ipynb` notebook.

### Predict the probability of delay for a trip

Go to the `Project1.ipynb` and run all the cells until reaching the `Predictive model` section and then run the cell and put your information to get a prediction.

### Recreate the full SBB dataset

You need to download the full SBB dataset from [here](https://drive.google.com/open?id=1SVa68nJJRL3qgRSPKcXY7KuPN9MuHVhJ). These files are constantly updated and we only worked with the data from January 2018 to September 2019.
For the year 2018, first month and first day it should have the following format: 18\_01/2018-01-01istdaten.csv'
Go to the `data` folder and run the `RecreateDataset.ipynb` notebook. You can also check the description for each step in this notebook.  
Otherwise you can run the `RecreateDataset.py` script with the command : `python RecreateDataset.py`. We uploaded the final results [here](https://drive.google.com/open?id=1AqcITx6nEO3NpvudkiqXCZ017k44Qfvz).

## Research questions

* Analyze general patterns of delays in swiss stations. For example, in which stations the delays are the most frequent? what are the hours with the highest risk of delay, what type of trains have a late departure, etc.
* Visualize the network as a graph
* ~~Compare the Swiss train system with other countries~~  
    => *(Milestone 2 update) The dataset provided by SNCF (French train company) doesn't fit with our investigation. So we will not compare the Swiss train system to other countries.*
* Which nodes in the network are key for the whole system and if disrupted can cause huge effects on the rest of the railway network.
* ~~Check if there is any correlation between delays and external factors such as weather (<https://opendata.swiss/en/dataset?keywords_en=weather>)~~  
    => *(Milestone 2 update) More complicated than expected, we will just focus on the provided reasons for delay from SBB (heavy rains, construction...).*
* What the probability for an user that is train is delayed? The user indicate his information (location, date, hour) and we provide an estimation of delay.
* *Milestone 3 update: What are the most common reasons for train delays?*

## Dataset

We will mainly use the datasets provided by the SBB and maybe other trains companies as the SNCF. We can find the data for the SBB at <https://data.sbb.ch/pages/home/>.  
The main dataset that we will be using is the ist-daten-sbb which contains every train arrival and departure scheduled time and real time in the SBB network. We can also link it with the database passagierfrequenz which encapsulate the frequency of passenger in every train station.  
One of the difficulties is that the API only provides the information of the day and so we will have to build our own dataset by adding the data each day or by contacting the company directly.
*Milestone 2 update: After contacting SBB company, they have provide us access to a Google Drive with the last two years data: 2018 complete and first 9 months in 2019 (146.5 GB). We want to modify this
dataset since it also contains information about busses and other railway networks like Deutsche Bahn and hopefuly it will significantly reduce in size. Also, we want to enrich it by adding the geo locations
of all train stations for future visualization. These can be taken from <https://data.sbb.ch/pages/home/>. One good aspect is that all the csv files have the same format and columns and we can use 
the same data reconstruction pipeline for all. We expect to have 50 GB in the end.*

## A list of internal milestones up until project milestone 2

* Checking visualization tools for networks. *=> Done*
* Investigate how to get the history of the provided data (checking the API, contact SBB?, etc.) *=> Done*
* Seeing how to cleanly implement networks in python and how to use graphs algorithms. *=> Aborpted*

## A list of internal milestones up until project milestone 3

* Implement a machine learning model that predict the probability of delay for a given ride. *=> Done*
* Set-up a platform for the visualization of our data *=> Done*
* Construct the new dataset from the data provided by SBB *=> Done*
* Create a datastory to describe our results and analysis (if possible with interactive interface) *=> Aborpted, we followed the TA reviews advice and we changed to a report*
* Analyze the delay reasons *=> Done*

## Contributions

**Maria:** recreating the full dataset, investigating geoposition and per station delay analysis, writting up the report, preparing the final presentation;  
**Dimitri:** Data preprocessing and exploration, investigating delay analysis, plotting railway network, writting up the report, preparing the final presentation;  
**Ejub:** Investigating the delay reasons, coding the predictive model, writting up the report, preparing the final presentation;  
**Santiago:** Getting the data from SBB, coding the predictive model, done some early data formatting and exploration, writting up the report, preparing the final presentation. 
