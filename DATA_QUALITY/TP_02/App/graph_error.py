import mplcursors
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from matplotlib.widgets import Button
import numpy as np
from numpy import genfromtxt, isnan, nanstd, nanmean, nanmin, nanmax, searchsorted, arange, array, append

class Cursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([1],[0], marker="o", color="crimson", zorder=3) 
        self.x = x
        self.y = y
        self.txt = ax.text(0, 0, '')

    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        indx = searchsorted(self.x, [x])[0]
        x = self.x[indx]
        y = self.y[indx-1]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text(f'jour {x}, {y}°C')
        self.txt.set_color("crimson")
        self.txt.set_position((x+1,y+1))
        self.ax.figure.canvas.draw()

def get_plot_from_dataframe(months, climat, mean, std, minli, maxli, minyear, maxyear):    
    year_array = array([])
    for i, month in enumerate(months, start=0):
        year_array = append(year_array, climat[:, i])
    year_array = year_array[~isnan(year_array)]

    month = 0
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    title = plt.title(f"Température du mois de {months[month]} \n")    
    suptitle = plt.suptitle("\n\nMoyenne: " + str(round(mean[month], 2)) + ", écart-type: " + str(
        round(std[month], 2)) + " min: " + str(round(minli[month], 2)) + " max: " + str(
        round(maxli[month], 2)), fontsize=10)
    plt.xlabel('Jours')
    plt.ylabel('Température')
    
    plt.axis([1, 31, nanmin(year_array)-5, nanmax(year_array)+5])
    plt.grid(True)
    plot, = plt.plot(range(1, 32, 1), climat[:, month], "b:o", lw=2)

    class Index:
        ind = 0

        def __init__(self, cursor):
            self.cursor = cursor

        def next(self, event):
            if self.ind < 11:
                self.ind += 1
                title.set_text(f"Température du mois de {months[self.ind]} \n ")
                suptitle = plt.suptitle("\n\nMoyenne: " + str(round(mean[self.ind], 2)) + ", écart-type: " + str(
                    round(std[self.ind], 2)) + " min: " + str(round(minli[self.ind], 2)) + " max: " + str(
                    round(maxli[self.ind], 2)), fontsize=10)
                plot.set_ydata(climat[:, self.ind])
                self.cursor.x = arange(len(climat[:, self.ind]))
                self.cursor.y = climat[:, self.ind]
                plt.draw()
            elif self.ind == 11:
                self.ind += 1
                title.set_text(f"Température sur l'année \n ")
                suptitle = plt.suptitle("\n\nmin: " + str(minyear[0]) + " max: " + str(maxyear[0]), fontsize=10)
                x = [x for x in arange(365) if x%30==0 ]
                ax.set_xlim(right=365)
                ax.set_xticks(x)   
                ax.set_xticklabels(x)
                plot.set_xdata(range(0, len(year_array), 1))
                plot.set_ydata(year_array)
                self.cursor.x = arange(1, 366)
                self.cursor.y = year_array
                plt.draw()

        def prev(self, event):
            if self.ind > 0:
                self.ind -= 1
                title.set_text(f"Température du mois de {months[self.ind]} \n ")
                suptitle = plt.suptitle("\n\nMoyenne: " + str(round(mean[self.ind], 2)) + ", écart-type: " + str(
                    round(std[self.ind], 2)) + " min: " + str(round(minli[self.ind], 2)) + " max: " + str(
                    round(maxli[self.ind], 2)), fontsize=10)
                plot.set_ydata(climat[:, self.ind])
                self.cursor.x = arange(len(climat[:, self.ind]))
                self.cursor.y = climat[:, self.ind]
                if self.ind == 11:
                    x = [x for x in arange(31) if x%5==0 ]
                    ax.set_xlim(right=32)
                    ax.set_xticks(x)
                    ax.set_xticklabels(x)
                    plot.set_xdata(range(1, 32, 1))
                plt.draw()

    days = arange(0, 31)
    celsius_degree = climat[days, 0]
    cursor = Cursor(ax, days, celsius_degree)
    plt.connect('motion_notify_event', cursor.mouse_move)

    callback = Index(cursor)
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)

    plt.show()