import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])

# Clean data
t_per = df["value"].quantile(0.025)
b_per = df["value"].quantile(0.975)
df = df.loc[(df["value"] > t_per) & (df["value"] < b_per)]

df_copy = df.copy()
df_copy.loc[:, "month"] = df.index.month
df_copy.loc[:, "year"] = df.index.year

months = {
        1: "January", 
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }


def set_month(month_no):
    for i in range(1, 13):
        if month_no == i:
            month_no = months[i]
            return month_no


months_2 = [months[i][:3] for i in range(1, 13)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.plot(df.index, df.values, color="red")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_copy.groupby(["month", "year"], as_index=False).mean()
    df_bar["month"] = df_bar["month"].apply(set_month)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax = sns.barplot(data=df_bar, x="year", y="value", hue="month", palette="Set1")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(title="Months", loc="upper left")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    sns.boxplot(data=df_box, x="month", y="value", ax=ax[1])
    ax[1].set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")
    ax[1].set_xticklabels(months_2)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
