#!/usr/bin/env python
# coding: utf-8

# # Classifying Non Profit Donor Strategy from Cultivating Volunteers

# In[107]:


import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB

# @st.cache_data
DATA_URL = "data/census.csv"
#DATA_URL = "../data/census.csv"

census = pd.read_csv(DATA_URL)

## keep copy of original dataframe in case we need to revert back later
census_original = census

# ## Data PreProcessing
## drop columns that are not likely to be valuable or relevant
census = census.drop(columns=['fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week',
                              'occupation', 'relationship', 'race'])
## drop '?' values
## The census dataset uses '?' in place of null values
census = census.drop(census.loc[census['workclass'] == '?'].index)
census = census.drop(census.loc[census['native-country'] == '?'].index)

# ### Encode Target Variable
## This project will be using income as the indicator for if someone is likely to be a mid-level or high-level donor
census['income'] = census['income'].replace({'<=50K': 'Mid-Level', '>50K': 'High-Level'})

# ### Process Categorical Variables
# #### Process Marital Status
census['marital-status'] = census['marital-status'].replace({'Married-civ-spouse': 'Married',
                                                             'Married-spouse-absent': 'Married',
                                                             'Married-AF-spouse': 'Married'})
# census['marital-status'].value_counts()

census['marital-status'] = census['marital-status'].replace({'Never-married': 'Single',
                                                             'Divorced': 'Single', 'Separated': 'Single',
                                                             'Widowed': 'Single'})
# census['marital-status'].value_counts()

# #### Process Workclass
census['workclass'] = census['workclass'].replace({'Local-gov': 'Government',
                                                   'Federal-gov': 'Government',
                                                   'State-gov': 'Government',

                                                   'Self-emp-not-inc': 'Self-emp',
                                                   'Self-emp-inc': 'Self-emp',

                                                   'Without-pay': 'No-income',
                                                   'Never-worked': 'No-income',

                                                   '?': 'Unknown'})

# census['workclass'].value_counts()

# #### Process Native Country
census['native-country'] = np.where((census['native-country'] != 'United-States') &
                                    (census['native-country'] != '?'), 'Non-US', census['native-country'])

census['native-country'] = census['native-country'].replace({'?': 'Unknown'})

# census['native-country'].value_counts()

# #### Process Education
census['education'] = census['education'].replace({'10th': 'DNF HS',
                                                   '7th-8th': 'DNF HS',
                                                   '9th': 'DNF HS',
                                                   '11th': 'DNF HS',
                                                   '9th': 'DNF HS',
                                                   '12th': 'DNF HS',
                                                   '5th-6th': 'DNF HS',
                                                   '1st-4th': 'DNF HS',
                                                   'Preschool': 'DNF HS',

                                                   'HS-grad': 'HS',
                                                   'Some-college': 'HS',

                                                   'Assoc-voc': 'Assoc',
                                                   'Assoc-acdm': 'Assoc'})

# census['education'].value_counts()

# ### Hot Encode Categorical Features
## saving a new dataframe with one hot encoding for categorical features
census_encoded = pd.get_dummies(data=census, columns=['workclass', 'education', 'marital-status', 'sex',
                                                      'native-country'])

## must remove one encoded column to avoid multicollinearity due to dummy variable trap
census_encoded = census_encoded.drop(columns=['workclass_Private', 'education_HS',
                                              'marital-status_Single', 'sex_Male',
                                              'native-country_United-States'])

# ## Modeling
## Train/Split with 20% witheld for testing
train, test = train_test_split(census_encoded, test_size=0.2, random_state=42, stratify=census_encoded['income'])

## Used for column headers
census_X = census_encoded.drop(columns=['income'])

X_train = train.drop(columns=['income'])
X_test = test.drop(columns=['income'])

y_train = train['income']
y_test = test['income']

## Target Variable Classes
classes = ['High-Level', 'Mid-Level']

# #### Naive Bayes
# Building Naive Bayes model with best performing hyperparameters
nb = GaussianNB(var_smoothing=1e-08)
nb.fit(X_train, y_train)

nb.predict(X_test)


def predict_income(age, maritalstatus, sex, workclass, nativecountry, education):
    rawIn = census.drop(columns=['income'])
    encoded_census = pd.get_dummies(data=rawIn, columns=['workclass', 'education', 'marital-status',
                                                         'sex', 'native-country'])
    encoded = pd.DataFrame([[0] * encoded_census.shape[1]], columns=encoded_census.columns)

    encoded.age[encoded.age == 0] = age
    encoded.get('workclass_' + workclass)[0] = 1
    encoded.get('education_' + education)[0] = 1
    encoded.get('marital-status_' + maritalstatus)[0] = 1
    encoded.get('sex_' + sex)[0] = 1
    encoded.get('native-country_' + nativecountry)[0] = 1

    encoded_input = encoded.drop(columns=['workclass_Private', 'education_HS',
                                          'marital-status_Single', 'sex_Male',
                                          'native-country_United-States'])

    return nb.predict(encoded_input)


def main():
    """ web interface """
    st.set_page_config(layout="wide")
    st.write('# Income Predictor')
    st.markdown(''' 
    Welcome to the App which predicts Income Levels
    '''
                '''
    This application uses supervised learning techniques to classify potential donors for 
    non profits as likely to be mid-level or high-level donors. This  will allow nonprofits 
    to better compete for the attention of high-level donors, many of which can provide 
    tremendous benefits when relationships are cultivated personably, and allow organizations 
    to better allocate their time for fundraising ultimately to help more people. To provide a 
    donor classification, the application will use basic information collected by non profits 
    when enrolling new volunteers and supporters.''')

    age_col, education_col, workclass_col = st.columns(3)
    sex_col, maritalstatus_col, nativecountry_col = st.columns(3)

    # age = st.slider('Age', min_value=17, max_value=80, value=27, step=1)
    with age_col:
        age = age_col.slider('**Age**', min_value=17, max_value=80, value=27, step=1)

    with maritalstatus_col:
        maritalstatus = maritalstatus_col.selectbox(
            '**Marital Status**',
            ('Single', 'Married'))

    with sex_col:
        sex = sex_col.selectbox(
            '**Sex**',
            ('Female', 'Male'))

    workclass_map = {'Private': 'Private', 'Government': 'Government',
                     'Self employed': 'Self-emp', 'No income': 'No-income'}
    with workclass_col:
        workclass = workclass_col.selectbox(
            '**Workclass**',
            ('Private', 'Government', 'Self employed', 'No income'))
        workclass = workclass_map[workclass]

    nativecountry_map = {'United States': 'United-States', 'Non-US': 'Non-US'}
    with nativecountry_col:
        nativecountry = nativecountry_col.selectbox(
                        '**Native Country**',
                        ('United States', 'Non-US'))
        nativecountry = nativecountry_map[nativecountry]

    education_map = {'High School': 'HS', 'Bachelors': 'Bachelors',
                     'Did not finish high school': 'DNF HS', 'Associate': 'Assoc',
                     'Masters': 'Masters', 'Prof-school': 'Prof-school',
                     'Doctorate': 'Doctorate'}

    with education_col:
        education = education_col.selectbox(
            '**Education**',
            ('High School', 'Bachelors', 'Did not finish high school', 'Associate',
             'Masters', 'Prof-school', 'Doctorate'))
        education = education_map[education]

    out_map = {'Mid-Level': 'The predicted income is in the Mid level for the given input fields.',
               'High-Level': 'The predicted income is in the High level for the given input fields.'}
    if st.button('**Submit**'):
        out = predict_income(age, maritalstatus, sex, workclass, nativecountry, education)
        st.markdown(out_map[out[0]])
    st.markdown('''
    The application will provide a classification of "High-Level" for any individual who is 
    likely to be able to contribute a large donation, or Mid-Level" for an individual who is 
    likely to only be able to contribute a smaller contribution.
    Thank you for using our app, and we hope it was helpful''')


if __name__ == '__main__':
    main()
