### INF601 - Advanced Programming in Python
### Kyle Lavigne
### Mini Project 2


#Imports
import pandas as pd
import matplotlib.pyplot as plt


#Initial Setup
path = "./data/Popular_Spotify_Songs.csv"

songs = pd.read_csv(path, encoding="latin1")

################################################################################
#Question 1: How many songs are in each key?

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
plt.show()

################################################################################
#Question 2: What was the most popular key by streams?

popular_key = songs[['key', 'streams']].groupby('key').mean()

col = "streams" if "streams" in popular_key.columns else popular_key.select_dtypes("number").columns[0]

x = popular_key.index.astype(str)        # bar labels
h = popular_key[col].to_numpy()          # bar heights

plt.bar(x, h, edgecolor='black', color=['g','m'])  # list will cycle if shorter than bars
plt.title('Average Streams by Key')
plt.xlabel('Key')
plt.ylabel('Average Streams')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

################################################################################
#Question 3: What keys were the most popular in each month of the year?


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

