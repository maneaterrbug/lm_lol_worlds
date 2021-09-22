### Questions/need:


* With the League of Legends World 2021 Championship right around the corner, can we use past regional league and World's performances of professional League e-sports teams **and** their players/roles to predict future performances at World's using linear regression modeling?
	* Looking to predict placement in the tournament alone appears to be more of a classification problem--as such we can look to change our target to something more predictable with a linear regression model such as the total games won over the course of the best-of-one group-stage and best-of-five knock-out stage of the tournament
* Esports fans and analysts can benefit from this modelling in that it can give them more information with which to make predictions
	* Potentially an esports publication or Riot themselves have contracted me to be able to have some analytics to reference in the upcoming 2021 World's

### Data Descriptions:

* I will be using a combination of the lol.fandom.com/wiki/ season overview (a sample regional season's player stats can be found [here](https://lol.fandom.com/wiki/LCS/2019_Season/Summer_Season/Player_Statistics)), player stats, and team roster pages to build my datasets, and the data will be obtained by web-scraping using either Selenium
* An individual sample unit would be a professional player by year, their team with associated team role, team regional performance, as well as 16 individual player performance stats

* the target will the number of individual games the player's team won over the course of a year's World Championship tournament

### Tools

* numpy and Pandas for data processing and manipulation
* seaborn and matplotlib for visualization
* sklearn
* Selenium and BeautifulSoup for scraping
* SQLite for storing and high-level exploration of data

![](../resources/worlds2019.png)

