import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line 1: all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    plt.plot(years, res.intercept + res.slope * years, 'r')

    # Line 2: from year 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g')

    # Labels
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
