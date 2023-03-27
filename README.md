<!-- Output copied to clipboard! -->

<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.343 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Sun Mar 26 2023 21:29:51 GMT-0700 (PDT)
* Source doc: ReadMe GitHub
----->



# 
**Project: Classifying Non Profit Donor Strategy from Cultivating Volunteers**


## 
**Supervised Learning**


---


## **Overview**

In this project, we use supervised learning techniques to classify non profit donors as mid-level and high level donors. This classification will allow nonprofits to better compete for the attention of high-level donors, many of which can provide tremendous benefits when relationships are cultivated personably, and allow organizations to better allocate their time for fundraising ultimately to help more people. The data is collected and explored first, and pre-processing techniques are used to manipulate the data to a format which is workable for our use case. Several supervised learning models are trained and evaluated on the pre-processed data and a best suited model was selected based on the performance of the models.


## **Getting Started**

The purpose of this analytical research project is to leverage non profit volunteer databases to identify individuals who are likely to be high-level donors. The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income). The dataset was donated by Ron Kohavi and Barry Becker.

Our goal is to build a model that accurately predicts whether an individual makes more than 50K. This project will be very helpful for non-profits which survive on donations, knowing an individual’s income will help the organization to understand the amount of donation to request.


## **EDA and Pre-Processing**

There are 48842 observations and 15 features in the dataset. 

The features that are available are age, workclass, fnlwgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, and income. The exploratory data analysis includes exploring the data types of the dataset and checking the null values. The dataset did not have any null values but instead had ”?” in some of the columns like work-class and native-country. As the number of '?' values are relatively low compared to the length of the dataframe, those values are dropped. Columns like 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', ‘occupation', ’relationship’, and ‘race’ are all dropped which are not relevant, or valuable.  After dropping the irrelevant observation and features we now have 45232 observations with 7 features. The target variable ‘income’ shows an imbalance with the mid-level and high-level income which will be addressed in the modeling phase. The age ranges from 17 years to 90 years and the histogram shows a right skew with a large proportion of the individuals on the younger side of the range with the 50% percentile at 37 years old. The age is grouped based on the age range. The work-class, native-country, and marital status have too many categories; similar classes in these categorical features are combined in order to make the results more interpretable. 
