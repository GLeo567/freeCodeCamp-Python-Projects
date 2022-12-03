import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level", color="y")

    # Create first line of best fit
    to_2050 = pd.Series(range(1880, 2051))
    slope, inter, r, p, se = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.plot(to_2050, inter + slope*to_2050, label="First line of best fit")

    # Create second line of best fit
    df_rec = df.loc[df["Year"] >= 2000]
    rec_to_2050 = pd.Series(range(2000, 2051))
    slope2, inter2, r2, p2, se2 = linregress(x=df_rec["Year"], y=df_rec["CSIRO Adjusted Sea Level"])
    plt.plot(rec_to_2050, inter2 + slope2*rec_to_2050, label="Second line of best fit")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()