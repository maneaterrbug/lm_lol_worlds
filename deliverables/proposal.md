### Questions/need:


* Can we use past regional league and World's performances of professional League of Legends teams **and** their players to predict future performances at World's using linear regression modeling?
* Esports fans and analysts can benefit from this modelling in that it can give them more information with which to make predictions
	* Potentially an esports publication or Riot themselves have contracted me to be able to have some analytics to reference in the upcoming 2021 World's

### Data Descriptions:

* I will be using a combination of the lol.fandom.com/wiki/ season overview, player stats, and team roster pages to build my datasets
* An individual sample unit could be a professional team by year, with associated stat by role and regional performance
	* team record (win/loss)
	* potentially team placement in regions playoffs
	* potentially some kind of stat break down by player/role, eg k/d/a for toplaner (there will be 5 of these)
* the target will ideally be the historical placement of teams in the League of Legends World Championship

### Tools

* seaborn
* matplotlib
* sklearn
* SQL

![](../resources/worlds2019.png)
