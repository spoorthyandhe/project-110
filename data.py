from pandas.io.pytables import AppendableFrameTable
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data],["readig_time"],show_hist=False)
fig.show()
print("population mean:- ",statistics.mean(data))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Mean of sampling distribution :-",statistics.mean(mean_list) )

setup()    