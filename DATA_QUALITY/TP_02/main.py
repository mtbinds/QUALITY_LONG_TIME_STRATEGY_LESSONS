import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax
from graph import get_plot_from_dataframe

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
mean = []
std = []
minli = []
maxli = []
minyear = []
maxyear = []

def statistics(dataframe):
    for i, month in enumerate(months, start=0):
        print("\n\nStats du mois de " + months[i] + ":\n")
        print("moyenne du mois de " + months[i] + " : " + str(nanmean(dataframe[:, i])))
        print("Écart-type du mois de " + months[i] + " : " + str(nanstd(dataframe[:, i])))
        print("Min du mois de " + months[i] + " : " + str(nanmin(dataframe[:, i])))
        print("Max du mois de " + months[i] + " : " + str(nanmax(dataframe[:, i])))
        mean.append(nanmean(dataframe[:, i]))
        std.append(nanstd(dataframe[:, i]))
        minli.append(nanmin(dataframe[:, i]))
        maxli.append(nanmax(dataframe[:, i]))
    year_climat = dataframe[~isnan(dataframe)]
    minyear.append(nanmin(year_climat))
    maxyear.append(nanmax(year_climat))
    print('\n')
    print("Température minimale de l'année : " + str(minyear[0]))
    print("Température maximale de l'année : " + str(maxyear[0]))
    
def calcul_rolling_mean(dataframe):
    df = pd.DataFrame(dataframe)
    roll = df.rolling(2, win_type='triang').sum()
    print("Rolling mean : " + roll)

if __name__ == '__main__':
    climat = genfromtxt('Data/Climat.csv', delimiter=';', dtype=float, skip_header=True)
    statistics(climat)
    # calcul_rolling_mean(climat)
    get_plot_from_dataframe(months, climat, mean, std, minli, maxli, minyear, maxyear)
    