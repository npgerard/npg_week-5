import plotly.express as px
import pandas as pd

# update/add code below ...

import numpy as np


def survival_demographics():
    '''Returns dataset of survivability grouped by class/gender/age_group'''
    df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

    # define the age bins; 
    bins = [0,13,20,60, np.inf]
    labels = ['Child','Teen','Adult','Senior']

    # create the new field age_group according to the pre-defined cut bins and labels
    df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # create a new field to sum survivors
    df['survived_numeric'] = df['Survived'].astype(int)

    # summarize number of passengers and survivors by class, sex, and age group
    df_summary = df.groupby(['Pclass','Sex','age_group'], observed=True).agg(
        n_passengers=('age_group','size'),
        n_survivors=('survived_numeric','sum')
    )


    # calculate the survivability row by row
    df_summary['survival_rate'] = df_summary['n_survivors'] / df_summary['n_passengers']

    

    #return the dataframe
    return df_summary.reset_index()

def visualize_demographic():
    '''returns plotly figure to answer the question if women and children were truly prioritized'''

    # get the initital dataset to work with
    df_prelim = survival_demographics()
    df_prelim = df_prelim.reset_index()

    # categorize each record as either 'Women and Children' or 'Other'
    df_prelim['priority_category'] = np.where(
        (df_prelim['Sex'] == 'female') | (df_prelim['age_group'].isin(['Child', 'Teen'])),
        'Women and Children',
        'Other'
    )

    # summarize the new 
    df_summary = df_prelim.groupby('priority_category').agg(
        n_passengers=('n_passengers','sum'),
        n_survivors=('n_survivors','sum')
        )

    df_summary['survival_rate'] = df_summary['n_survivors'] / df_summary['n_passengers']

    df_summary = df_summary.reset_index()

    fig = px.bar(
        df_summary, 
        x='priority_category',
        y='survival_rate',
        text=df_summary['survival_rate'].apply(lambda x: f"{x:.1%}"),
        labels={'priority_category': 'Group', 'survival_rate': 'Survival Rate'},
        title='Survival Rate by Priority Category'
    )

    # Format y-axis as percentages
    fig.update_yaxes(tickformat=".1%")

    # Show the value labels on top of bars
    fig.update_traces(textposition='outside')
    return fig


def family_groups():
    '''Returns a table of min/mean/max fare by family size'''

    #get the initial dataset
    df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

    #add the family_size parameter
    df['family_size'] = df['SibSp']+df['Parch']+1

    #create the summary table to return
    df_summary = df.groupby(['family_size', 'Pclass']).agg(
        #n_passengers=('family_size','sum'),
        avg_fare=('Fare','mean'),
        min_fare=('Fare', 'min'),
        max_fare=('Fare', 'max')
        )
    
    return df_summary

def last_names():
    '''assigned function to return last names and counts of passengers with that last name'''
    #get the initial dataset
    df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

    return df['Name'].str.extract(r'^([^,]+)')[0].value_counts()


def visualize_families():
    '''provides scatterplot of average cost of ticket per family size for 3rd class passengers'''

    #get the dataset and reset the index so we can use it as a regular dataframe.
    df = family_groups().reset_index()
    df_pclass3 = df[df["Pclass"] == 3]

    fig = px.scatter(
        df_pclass3,
        x="family_size",
        y="avg_fare",
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Fare"
        },
        #always give a title! And always give context to inclusion/exclusion of data
        title="Family Size vs Average Fare (Pclass = 3)"
    )

    return fig

