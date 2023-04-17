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
**Project: Classifying Non Profit Donor Strategy for Cultivating Volunteers**


## 
**Supervised Learning**


---



## **Project Description**

This application used supervised learning techniques to classify potential non profit donors as midlevel or high-level donors. The applcation aims to allow nonprofits to better compete for the attention of highlevel donors, many of which can provide tremendous benefits when relationships are cultivated personably, and allow organizations to better allocate their time for fundraising ultimately to help more people. 

## **Getting Started**

The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income). The dataset was donated by Ron Kohavi and Barry Becker.

In this dataset, the income field is used to determine if an individual is likely to be a high-level or midlevel donor. Individuals with an income greater than $50,000 are determined to be potential high-level donors and all other individuals are determined to be potential midlevel donors. 

## How to use this application
The application is hosted on streamlit.io and available to all users with a web browser without any installation. <https://sregiphilip-ads599-sp23-team1-appdonor-app-a7oh1p.streamlit.app>
The application asks for basic information about an individual and will return a classification of either midlevel or high-level to describe the predicted donor type of that individual.

The code and whitepaper of how this application was developed is contained in the main.ipynb jupyter notebook file. The live code used for the deployed application is contained in the app folder.

## **Table of Contents**

### Code Library Folder
Within the Code Library folder, you will find jupyter notebook files which contain code that was used for exploration and development of the application. 

* EDA_PreProcessing.ipynb - a jupyter notebook file containing python code detailing the exploratory data analysis and preprocessing steps for this dataset. 

* Modeling.ipynb - a jupyter notebook file containing python code detailing the model building and evaluation steps of this application.

###  Image Folder
The image folder contains various pdf images of plots that were deemed to be significant during the exploratory data analysis of the dataset. These images are for reference to understand the dataset that was used.

### app
The app folder contains a python file and requirements file that is used by streamlit.io to deploy our naive bayes classification model. These files are essential for streamlit.io to launch our application.

### data
The data folder contains the csv file of the UCI MLE repository dataset used for this analysis. [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income)

### reports
The reports folder contains a pdf article detailing the purpose of this application and the objective we were attempting solve. Please refer to the article to understand the decision making process of this application.


## **References**

Kohavi, R. & Becker, B (1996). UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/datasets/census+income]. Irvine, CA: University of California, School of Information and Computer Science.
