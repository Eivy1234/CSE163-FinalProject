# Research Question 1
# This file contains the code for the visuals of the plots for the first research Question
# The visuals will be done with plotly and use multiple music streaming datasets
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

top_100 = "/users/eivy/Documents/CSE 163/Group Project /CSE163-FinalProject/Datasets/Spotify/Spotify 2010 - 2019 Top 100.csv"
data2 = "/users/eivy/Documents/CSE 163/Group Project /CSE163-FinalProject/Datasets/Spotify/data 2.csv"


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


def stream_distributions(df2):
    streams_artist = df2.groupby("Artist", as_index=False)["Streams"].mean()
    fig = go.Figure(data=go.Violin(y=streams_artist['Streams'], box_visible=True, line_color='black',
                               meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                               x0='Violin/Box plot of mean artist streams per '))

    fig.update_layout(yaxis_zeroline=False)
    fig.show()


def testing_violin_graph(df2):
    streams_artist = df2.groupby("Artist", as_index=False)["Streams"].mean()
    print('Mean of unique artists streams: ',streams_artist.mean(),
          'Median unique artist streams: ',streams_artist.median(),
          'Max artist streams',streams_artist.max())


def average_duration_per_year(df):
    """
    Method takes a dataframe and filters the music from the years 2010 through 2019. 
    Muisc is grouped by the year it was released ("year released") and then
    and the avaerage of song durations is calcualted for every year. 
    With plotly.express, a line plot is created ro showcase the connection
    between the average song duration in seconds for every year between 2010
    and 2019.
    """
    years_2010 = df['year released'] >= 2010
    years_2019 = df['year released'] <= 2019
    data = df[years_2010 & years_2019]
    mean_dur = data.groupby('year released', as_index=False)['dur'].mean()

    px.line(
        mean_dur, x='year released', y='dur', markers=True, 
        labels={"dur": "Average Song Duaration (seconds)", 
        "year released": "Year"}, title="Average Duration of Songs Over Time")
    px.savefig('laksdjbf', bbox_inches="tight")

    px.show()


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
    df = pd.read_csv(top_100, encoding='latin-1')

    top_fast_genre(df1)
    mean_dur_bpm_in_group_type(df1)
    popular_streamers(df2)
    stream_distributions(df2)
    testing_violin_graph(df2)
    average_duration_per_year(df)
    spotify_2010_2019_plot(df1)

if __name__ == '__main__':
    main()