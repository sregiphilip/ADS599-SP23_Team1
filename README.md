<!-- Output copied to clipboard! -->

<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.31 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Sat Apr 15 2023 17:21:06 GMT-0700 (PDT)
* Source doc: ReadMe GitHub
----->



# 
**Project: Classifying Non Profit Donor Strategy from Cultivating Volunteers**


## 
**Supervised Learning**


---


## **Overview**

This application used supervised learning techniques to classify potential non profit donors as midlevel or high-level donors. The applcation aims to allow nonprofits to better compete for the attention of highlevel donors, many of which can provide tremendous benefits when relationships are cultivated personably, and allow organizations to better allocate their time for fundraising ultimately to help more people. 

## **Getting Started**

The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income). The dataset was donated by Ron Kohavi and Barry Becker.

In this dataset, the income field is used to determine if an individual is likely to be a high-level or midlevel donor. Individuals with an income greater than $50,000 are determined to be potential high-level donors and all other individuals are determined to be potential midlevel donors. 


## **EDA and Pre-Processing**

There are 48842 observations and 15 features in the dataset. 

The features that are available are age, workclass, fnlwgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, and income. The exploratory data analysis includes exploring the data types of the dataset and checking the null values. The dataset did not have any null values but instead had ”?” in some of the columns like work-class and native-country. As the number of '?' values are relatively low compared to the length of the dataframe, those values are dropped. Columns like 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', ‘occupation', ’relationship’, and ‘race’ are all dropped which are not relevant, or valuable.  After dropping the irrelevant observation and features we now have 45232 observations with 7 features. The target variable ‘income’ shows an imbalance with the mid-level and high-level income which will be addressed in the modeling phase. The age ranges from 17 years to 90 years and the histogram shows a right skew with a large proportion of the individuals on the younger side of the range with the 50% percentile at 37 years old. The work-class, native-country, and marital status have too many categories; similar classes in these categorical features are combined in order to make the results more interpretable. 


## **Modeling**

To build our desired solution for donor selection, we   trained   and   tuned   several   classification models that would be able to consider characteristics of a given individual and predict whether they are likely to be a high-level or mid-level donor. The models were trained using differing classification techniques that include logistic regression, decision trees, random forest, naïve bayes, and  K nearest neighbor.  Each  of these models were trained using the partitioned training  data which  consists  of  80%  of  the original dataset. The models were then evaluated with the remaining  20%  hold out test data. Furthermore, each of these models had different hyperparameters   that   were   evaluated   and   tuned with different user selected values, ultimately to better fit the data.


## **Model Outcome and Deployment**

After the model building and tuning with the five different classification techniques, the best performing models of each technique were then evaluated and compared against each other using a selection performance metrics that include recall, F1, accuracy, precision, and kappa, in that order of significance. After calculating the performance metrics of each of the five models,  the naïve bayes model was chosen given that it had the highest score for recall and the second highest score for F1. Naive Bayes was used to deploy an App, which allows a user to input basic information about an individual, and will then predict if the individual is likely to be a high level or mid level donor.

## **References**

Kohavi, R. & Becker, B (1996). UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/datasets/census+income]. Irvine, CA: University of California, School of Information and Computer Science.
