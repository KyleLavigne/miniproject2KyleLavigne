### INF601 - Advanced Programming in Python
### Kyle Lavigne
### Mini Project 2
from tokenize import group

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

# Initial Setup
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

path = "./data/Popular_Spotify_Songs.csv"

songs = pd.read_csv(path, encoding="latin1")

################################################################################
# Question 1: How many songs are in each key?

key = songs[['key']].value_counts()

a = key["A"]
a1 = key["A#"]
b = key["B"]
d = key["C#"]
e = key["D"]
c1 = key["C#"]
d = key["D"]
d1 = key["D#"]
e = key["E"]
f = key["F"]
f1 = key["F#"]
g = key["G"]
g1 = key["G#"]

keys = ['A', 'A#', 'B', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#' ]
values = [a, a1, b, c1, d, d1, e, f, f1, g, g1]

plt.bar(keys, values, edgecolor='black', color=['g','m'])
plt.title('Number of Songs in Each Key')
plt.xlabel('Key')
plt.ylabel('Number of Songs')
plt.savefig("charts/key_amount.png", dpi=300)
print('Saving key_amount.png')

################################################################################
# Question 2: What was the most popular key by streams?

popular_key = songs[['key', 'streams']].groupby('key').mean()

col = "streams" if "streams" in popular_key.columns else popular_key.select_dtypes("number").columns[0]

x = popular_key.index.astype(str)
h = popular_key[col].to_numpy()

plt.bar(x, h, edgecolor='black', color=['g','m'])
plt.title('Average Streams by Key')
plt.xlabel('Key')
plt.ylabel('Average Streams')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/avg_key_streams.png", dpi=300)
print('Saving avg_key_streams.png')

################################################################################
#Question 3: What keys were the most popular in each month of the year?

df = songs.dropna(subset=["released_month", "key"]).copy()

# total streams per month/key
grouped = df.groupby(["released_month", "key"])["streams"].sum().reset_index()

# pick the winning key for each month
best_key = grouped.groupby("released_month")["streams"].idxmax()
winners = grouped.loc[best_key].sort_values("released_month")

# build color map (1 color per key)
unique_keys = winners["key"].unique()
palette = plt.cm.tab20(np.linspace(0, 1, len(unique_keys)))   # any colormap you like
color_map = dict(zip(unique_keys, palette))

# plot
months = winners["released_month"].astype(int)
totals = winners["streams"].to_numpy()
keys = winners["key"]

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(months, totals,
       color=[color_map[k] for k in keys],
       edgecolor="black")

ax.set_title("Most Popular Key by Month (total streams)")
ax.set_xlabel("Release Month")
ax.set_ylabel("Total Streams")
ax.set_xticks(months)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, pos: f"{int(v):,}"))

# annotate each bar with its key
for m, t, k in zip(months, totals, keys):
    ax.text(m, t, k, ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("charts/popular_key.png", dpi=300)
print('Saving popular_key.png')

################################################################################

print('All Done')
# (5/5 points) Initial comments with your name, class and project at the top of your .py file. Done
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as: Done
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data. Done
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

