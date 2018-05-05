# DBEX8-KFS
> by Kristian Flejsborg Sørensen (cph-kf96)

## Assignment 10: Modelling OECD data
Description of assignment can be found [here](https://github.com/datsoftlyngby/soft2018spring-databases-teaching-material/blob/master/lecture_notes/12-Security%20and%20advanced%20SQL.ipynb)   

### Entity Relationship Diagram
The data is cut up into 2 primary sources and 3 sub catagories, Subject and Location are constant pieces and are the primary key values of the content, subject/education and GDP are all sub catagories that can intertwine on the 2 primary types of data.
![](https://raw.githubusercontent.com/DanielHauge/DBEX10/master/Chenerdiagram1.png)   

### Data Model
The following tables showcases the physical data model   
![](https://i.gyazo.com/966a9e3fb4407475a1fc66fbc8c757dd.png)   
![](https://i.gyazo.com/c398e830310cd567e1e88fca4db3009f.png)   
![](https://i.gyazo.com/846b28826b1bf95213c0e1b85e2d377f.png)   
![](https://i.gyazo.com/4c31759023e93e8ad5a55a09f8e6efac.png)   
![](https://i.gyazo.com/752141e4c458c5ee8c0874c020ace434.png)   

### The Graph
all related quaries used to find and make the two graphs can be found [here](https://github.com/Retroperspect/DBEX8-KFS/blob/master/Jupyter%20Queries.ipynb)   

Brasilian education on X and life expectancy on Y   
![](https://i.gyazo.com/522e7de978e45d6685072ceb9566c0dd.png)   

Korea education on X and life expectancy on Y   
![](https://i.gyazo.com/8d7fbe9cd0e652ffe417369ee19654f7.png)
