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
    bounds_data = dataset[(dataset['year released'] >= 2009) & (dataset['year released'] <= 2019)]
    data = bounds_data.groupby("artist").mean()
    b = px.line(data, x='year released', y='dur')
    b.show()


def top_fast_genre(df):
    # top genre vs duration
    # how does the duration of a song relate to the top genre in songs from 2010 to 2019?
    data2 = df.groupby('top genre', as_index=False).mean()
    data2 

    fig1 = px.bar(data2, x='top genre', y='dur', labels={'x':'Genre', 'y':'Duration (sec)'})

    fig1.update_layout(
    title_text='Top Genre from 2010-2019 Mean Duration'
    )

    fig1.show()

    fastest_genres = data2.nlargest(n=10, columns=['dur'])
    fig2 = px.bar(fastest_genres, x='top genre', y='dur', labels={'x':'Genre', 'y':'Duration (sec)'})

    fig2.update_layout(
    title_text='Top Genre from 2010-2019 Mean Duration'
    )

    fig2.show()

    test1 = data2.nlargest(n=10, columns=['dur'])
    print(test1)


def mean_dur_bpm_in_group_type(df):
    avg_dur = df.groupby(['year released', 'artist type'], as_index=False)[('dur','bpm')].mean()
    fig = px.line_polar(avg_dur, r = 'dur', theta ='artist type', color='bpm',symbol="year released", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
    fig.show()


def popular_streamers(df):
    # not printing
    data3 = df.groupby('Artist', as_index=False)['Streams'].max()
    g = data3.nlargest(n=15, columns=['Streams'])
    fig = px.bar(g, x='Artist', y='Streams')
    fig.update_layout(
    title_text='Top Genre from 2010-2019 Mean Duration'
    )

    fig.show()


def funnel_graph(df):
    group_by_artist = df2.groupby(['Artist','Track Name'], sort=False, as_index=False)['Streams'].max()
    # data4 = group_by_artist.groupby(['Track Name'] )['Streams'].max()
    k = group_by_artist.nlargest(n=15, columns=['Streams'])
    # l = k.groupby(['Artist', 'Track Name'])['Streams'].max().nlargest(n=15)
    px.funnel(k, x='Track Name', y='Streams', color='Artist')


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
    
    
def main():
    # read datasets => dataframe
    df1 = pd.read_csv(top_100, on_bad_lines='skip')
    df2 = pd.read_csv(data2, sep='#', header=None)

    # loading_data(df1, df2)
    # load_in_data(df1, df2)
    #plot1(df1)
    top_fast_genre(df1)
    mean_dur_bpm_in_group_type(df1)
    popular_streamers(df2)
    spotify_2010_2019_plot(df1)

if __name__ == '__main__':
    main()