import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax
from graph_error import get_plot_from_dataframe
import math

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
   
def clean_data(dataframe):
    avg_month = nanmean(dataframe, axis=0)
    for i, avg_month in enumerate(avg_month, start=0):
        for j in range(len(dataframe)):
            if math.isnan(dataframe[j][i]):
                if j < 28:
                    dataframe[j][i] = round(avg_month)
            else:
                if 0 < j < 30:
                    if verif_data(dataframe[j - 1][i], dataframe[j][i], dataframe[j + 1][i]):
                        dataframe[j][i] = round(avg_month)
    np.savetxt("./Data/Climat_cleaned.csv", dataframe, delimiter=";")

def verif_data(prev, data, next):
    moyenne = (prev + next) / 2
    if data > (moyenne + 7) or data < (moyenne - 7):
        return True
    return False

    np.savetxt("./Data/Climat_cleaned.csv", dataframe, delimiter=";")	

def calcul_rolling_mean(dataframe):
    df = pd.DataFrame(dataframe)
    roll = df.rolling(2, win_type='triang').sum()
    print("Rolling mean : " + roll)

if __name__ == '__main__':
    climat = genfromtxt('./Data/Climat-Erreur.csv', delimiter=';', dtype=float, skip_header=True)
    statistics(climat)
    cleaned_climat = clean_data(climat)
    # calcul_rolling_mean(climat)
    get_plot_from_dataframe(months, cleaned_climat, mean, std, minli, maxli, minyear, maxyear)
    