# Trains, Delays and Network

## Abstract

Transport is a key factor in today's society. We have to move often and fast in our daily lives. We also need to consider the impact some types of transport have on our ecosystem.  
Public transport and the train system in Switzerland is constantly trying to improve for us to be able to move efficiently. The main issue that arise in every train system is the schedule and the delay the passengers have to cope with. It’s one of the drawbacks that deter some people from using trains instead of their cars.  
The SBB division of passenger transport offers open data about train arrivals, departures, delays, etc. We want to use this data to understand the network of railway stations in Switzerland.  
Our goal is to investigate where are the problematic stations located and quantify the delay depending on the location and time of a train.
*Milestone 2 update: We want to provide a tool that allows the user to predict a delay for his ride.*

## Research questions

* Analyze general patterns of delays in swiss stations. For example, in which stations the delays are the most frequent? what are the hours with the highest risk of delay, what type of trains have a late departure, etc.
* Visualize the network as a graph
* ~~Compare the Swiss train system with other countries~~  
    => *(Milestone 2 update) The dataset provided by SNCF (French train company) doesn't fit with our investigation. So we will not compare the Swiss train system to other countries.*
* Which nodes in the network are key for the whole system and if disrupted can cause huge effects on the rest of the railway network.
* ~~Check if there is any correlation between delays and external factors such as weather (<https://opendata.swiss/en/dataset?keywords_en=weather>)~~  
    => *(Milestone 2 update) More complicated than expected, we will just focus on the provided reasons for delay from SBB (heavy rains, construction...).*
* *Milestone 2 update: What the probability for an user that is train is delayed? The user indicate his information (location, date, hour) and we provide an estimation of delay.*

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

* Implement a machine learning model that predict the probability of delay for a given ride.
* Set-up a platform for the visualization of our data
* Construct the new dataset from the data provided by SBB
* Create a datastory to describe our results and analysis (if possible with interactive interface)
* Analyze the delay reasons

## Questions for TAs

### Milestone 1
* Should we focus more on data visualization or data analysis?  
    => TA answer: *Both should be a focus for the project.*
* Is our idea fitting to the “social good” topic?  
    => TA answer: *To fit better into the "social good" theme, you could think how your idea has implications for people that are impacted from the Swiss train system. But the exact idea is up to you!*
* Since the API does not provide the history of their data, we will have to build our dataset from current data. Will the analysis period be problematic (too few data, not representative of the annual traffic ...)?  
    => TA answer: *This is something you can only answer, but, yes, only having current data might limit possibilities of a historical analysis.*

### Milestone 2
* Since we changed our main idea by adding the delay prediction, is that a problem if we dropped some research questions (external features impact, shortest path, etc.)?  
