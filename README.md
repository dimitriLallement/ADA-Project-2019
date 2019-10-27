# Trains, Delays and Network

## Abstract

Transport is a key factor in today's society. We have to move often and fast in our daily lives. We also need to consider the impact some types of transport have on our ecosystem.  
Public transport and the train system in Switzerland is constantly trying to improve for us to be able to move efficiently. The main issue that arise in every train system is the schedule and the delay the passengers have to cope with. It’s one of the drawbacks that deter some people from using trains instead of their cars.  
The SBB division of passenger transport offers open data about train arrivals, departures, delays, etc. We want to use this data to understand the network of railways and the passenger flow between stations in Switzerland.  
Our goal is to investigate where are the problematic stations located and quantify the delay depending on the location and time of a train.

## Research questions

* Analyze general patterns of delays in swiss stations. For example, in which stations the delays are the most frequent? what are the hours with the highest risk of delay, what type of trains have a late departure, passenger frequency, etc.
* Visualize the network as a graph
* Compare the Swiss train system with other countries
* Which nodes in the network are key for the whole system and if disrupted can cause huge effects on the rest of the railway network.
* Maybe use graph algorithms to compute shortest paths, maximum flows, etc.
* Check if there is any correlation between delays and external factors such as weather (<https://opendata.swiss/en/dataset?keywords_en=weather>)

## Dataset

We will mainly use the datasets provided by the SBB and maybe other trains companies as the SNCF. We can find the data for the SBB at <https://data.sbb.ch/pages/home/>.  
The main dataset that we will be using is the ist-daten-sbb which contains every train arrival and departure scheduled time and real time in the SBB network. We can also link it with the database passagierfrequenz which encapsulate the frequency of passenger in every train station.  
One of the difficulties is that the API only provides the information of the day and so we will have to build our own dataset by adding the data each day or by contacting the company directly.

## A list of internal milestones up until project milestone 2

* Checking visualization tools for networks.
* Investigate how to get the history of the provided data (checking the API, contact SBB?, etc.)
* Seeing how to cleanly implement networks in python and how to use graphs algorithms.

## Questions for TAa

* Should we focus more on data visualization or data analysis?
* Is our idea fitting to the “social good” topic?
* Since the API does not provide the history of their data, we will have to build our dataset from current data. Will the analysis period be problematic (too few data, not representative of the annual traffic ...)?
