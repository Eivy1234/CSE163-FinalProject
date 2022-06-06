# Research Question 1
# This file contains the code for the visuals of the plots for the first research Question
# The visuals will be done with plotly and use multiple music streaming datasets
import numpy as np
# import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

top_100 = "/users/eivy/Documents/CSE 163/Group Project /CSE163-FinalProject/Datasets/Spotify/Spotify 2010 - 2019 Top 100.csv"
data2 = "/users/eivy/Documents/CSE 163/Group Project /CSE163-FinalProject/Datasets/Spotify/data 2.csv"

"""
with open(top_100, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
"""

def load_in_data(csv_file1, csv_file2):

    # data = pd.read_csv(csv_file1)
    # data2 = pd.read_csv(csv_file2)
    merged = csv_file2.merge(csv_file1, left_on="CTIDFP00",
                              right_on="", how='left')
    print(merged)

    return merged


def loading_data(data1, data2):
    print(data2)

def plot1(dataset):
    a = dataset.head()
    b = px.line(a, x='title', y='dur')

def testing(number):
    double = number * 2
    print(double)
    return double

def repeatByNum(word, num):
    for i in range(1, num + 1):
        print(word)

def spotify_2010_2019_plot(df):
    """
    Filters music from years 2010 to 2019 from spotify, then it groups them
    by year based on the most popular genre of that year. Then, it plots the
    filtered data into a scatter plot, so the connection between the year and
    genre can be easily noticible. This is done by taking the dataframe as a
    parameter.
    """
    years_2010 = df['year released'] >= 2010
    years_2019 = df['year released'] <= 2019
    data = df[years_2010 & years_2019]
    top_genre = data.groupby('year released')['top genre'].max()
    
    sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
    sns.relplot(data=top_genre, color='purple')

    plt.xticks(rotation=45)
    plt.title("Most Popular Genre of each year in Spotify from 2010 to 2019")
    plt.xlabel('Year')
    plt.ylabel('Genre')
    plt.savefig('Spotify_Most_Popular_Genre_2010_to_2019', bbox_inches="tight")
    plt.show()
    
    
#this is just a comment
def main():
    df1 = pd.read_csv(top_100, on_bad_lines='skip')
    df2 = pd.read_csv(data2, sep='#', header=None)
    # loading_data(df1, df2)
    # load_in_data(df1, df2)
    plot1(df1)
    a = df1.head()
    px.line(a, x='title', y='dur')
    spotify_2010_2019_plot(df1)
    # testing(69)
    # repeatByNum("j", 5)
    # repeatByNum("ahhh", 5)

if __name__ == '__main__':
    main()