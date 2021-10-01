# Predicting Used Car List-prices
Matt Ryan

## Abstract
To aid the efforts of our car listing team, we are tasked with designing a regression model using historic used car listing data to improve both the accuracy and efficiency in pricing used cars.  Using data collected via web scraping from listings found on [carmax](https://www.carmax.com), we performed thorough feature selection and engineering to design a model which, given a list of car features and specifications, we believe will greatly improve quoting accuracy and efficiency for the listing team.

## Design

This project is premised on the hypothetical that carmax.com is exploring improvements to their used car listing and quotation processes and is reaching out to our consulting firm to aid in developing a tool to improve accuracy and efficiency via automation. Such a tool would allow the team to get a "head-start" on their estimtated price quote, freeing up time for them to more thoroughly investigate and list cars individually.

## Data

The dataset contains 1,293 datapoints with 25 features for each, with each unique datapoint representing one car listing. A few key features include manufacturer, model, year, mpg, and miles driven; however, many of the features were either categorical in nature or needed some level of cleaning/transformation to become viable for modeling. Of these 25, 16 features were chosen as having some significant correlation with the price and were used for further analysis. 

## Algorithms
*Feature Engineering*
- Manually scaled time variables
- Imputed the median by feature for all null values (only applied to features with <= 35% missingness)
- Performed logarithmic transformation on features that appeared to have a logarithmic relationship with the target variable (mileage, highway MPG, age of model)
- Created binary dummy variables to represent categorical feature variables
- Collapsed some binary dummy variables into bucket dummy variables that appeared to have a stronger correlation with the target variable (collapse of car manufacturer into an is_luxury binary variable)
- Applied a correlation strength filter to select for features with a DataFrame.corr() of magnitude greater than a certain absolute value

*Models*

OLS linear, lasso, and ridge regression models  were all entertained in the modeling stage, but, because of the high degree of interactivity between some of the features with strong target correlation, we opted to focus on models providing some level of regularization and complexity optimisation. We ultimately settled on a ridge regression model due to its strength in handling multi-collinearity.


*Model eval and selection*

Before performing any analysis, we split the entire dataset into 80-20 training and testing subsets. We then used the KFold method to split our training data into 5 randomly selected folds for which we trained and cross-validated our model against each fold. Finally, when assured that we had appropriately tuned our model, we applied our fit to the held-out test data. 


**5-fold test data**
* Mean of R2s: 0.596
* Stdev of R2s: 0.109
* MAE: $1696.23
* RMSE: $2165.50

**Held-out Test Data**
* R2: 0.620
* MAE: $1540.54
* RMSE: $1929.74

## Tools
- Numpy and Pandas for EDA and data processing
- Selenium and BeautifulSoup for web-scraping/data collection
- Scikit-learn for modeling
- Matplotlib and Seaborn for plotting

## Communication

In addition to the commentary made included in the slides and accompanying presentation, we note here our confidence in the tool developed. However, for the time being, use of this tool should be restricted to cars within $25k or less range, and cars estimated aorund the window should be more thoroughly individually assessed before listing. Going forward, this tool can be further improved via either further feature selection and engineering to potentially account for higher variance at higher price-points or possible implementation of a new learning model. 