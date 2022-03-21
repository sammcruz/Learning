#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:28:03 2022

@author: samantha
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# definir tema
sns.set_theme(style = 'whitegrid')
sns.set_palette("pastel")

# Dados
Base_Dados = sns.load_dataset('tips')
Base_Dados.head()

Base_Dados.rename( columns={
    'total_bill' : 'Total conta',
    'tip' : 'Gorjeta',
    'sex' : 'Sexo',
    'smoker' : 'Fumante',
    'day' : 'Dia da semana',
    'time' : 'Periodo',
    'size' : 'Pessoas na mesa'
    }, inplace = True)

# Relplot -> Visualizing statistical relationships
sns.relplot( x='Total conta', y = 'Gorjeta', data=Base_Dados )
sns.relplot( x='Total conta', y = 'Gorjeta', data=Base_Dados, hue = 'Sexo' )
sns.relplot( x='Total conta', y = 'Gorjeta', data=Base_Dados, kind = 'line' )
sns.relplot( x='Total conta', y = 'Gorjeta', data=Base_Dados, kind = 'line', hue='Fumante' )

# Histograma -> Visualizing distributions of data
sns.histplot(data=Base_Dados, x = 'Total conta', binwidth=1)
sns.histplot(data=Base_Dados, x = 'Total conta', hue='Fumante', bins=12)
sns.displot(Base_Dados, x = 'Total conta', binwidth=3)

# Grafico de barras
sns.barplot(data=Base_Dados, x='Sexo', y='Total conta', hue='Fumante')

# Pairplot
sns.pairplot(Base_Dados)
sns.pairplot(Base_Dados, hue='Sexo')
sns.pairplot(Base_Dados, kind='kde')

# boxplot
sns.boxplot(data=Base_Dados, x='Dia da semana', y='Total conta')
sns.boxplot(data=Base_Dados, x='Dia da semana', y='Total conta', hue = 'Sexo')

'''
################  GRÁFICOS EXEMPLOS DA DOCUMENTAÇÃO
'''

# Trivariate histogram with two categorical variables
import seaborn as sns
sns.set_theme(style="dark")

diamonds = sns.load_dataset("diamonds")
sns.displot(
    data=diamonds, x="price", y="color", col="clarity",
    log_scale=(True, False), col_wrap=4, height=4, aspect=.7,
)

# Plotting on a large number of facets
sns.set_theme(style="ticks")

# Create a dataset with many short random walks
rs = np.random.RandomState(4)
pos = rs.randint(-1, 2, (20, 5)).cumsum(axis=1)
pos -= pos[:, 0, np.newaxis]
step = np.tile(range(5), 20)
walk = np.repeat(range(20), 5)
df = pd.DataFrame(np.c_[pos.flat, step, walk],
                  columns=["position", "step", "walk"])

# Initialize a grid of plots with an Axes for each walk
grid = sns.FacetGrid(df, col="walk", hue="walk", palette="tab20c",
                     col_wrap=4, height=1.5)

# Draw a horizontal line to show the starting point
grid.refline(y=0, linestyle=":")

# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "step", "position", marker="o")

# Adjust the tick positions and labels
grid.set(xticks=np.arange(5), yticks=[-3, 3],
         xlim=(-.5, 4.5), ylim=(-3.5, 3.5))

# Adjust the arrangement of the plots
grid.fig.tight_layout(w_pad=1)

# Hexbin plot with marginal distributions

sns.set_theme(style="ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)

sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")

# Plotting model residuals
sns.set_theme(style="whitegrid")

# Make an example dataset with y ~ x
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

# Plot the residuals after fitting a linear model
sns.residplot(x=x, y=y, lowess=True, color="g")

# Dot plot with several variables

sns.set_theme(style="whitegrid")

# Load the dataset
crashes = sns.load_dataset("car_crashes")

# Make the PairGrid
g = sns.PairGrid(crashes.sort_values("total", ascending=False),
                 x_vars=crashes.columns[:-3], y_vars=["abbrev"],
                 height=10, aspect=.25)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size=10, orient="h", jitter=False,
      palette="flare_r", linewidth=1, edgecolor="w")

# Use the same x axis limits on all columns and add better labels
g.set(xlim=(0, 25), xlabel="Crashes", ylabel="")

# Use semantically meaningful titles for the columns
titles = ["Total crashes", "Speeding crashes", "Alcohol crashes",
          "Not distracted crashes", "No previous crashes"]

for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left=True, bottom=True)

# Grouped violinplots with split violins
sns.set_theme(style="whitegrid")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker",
               split=True, inner="quart", linewidth=1,
               palette={"Yes": "b", "No": ".85"})
sns.despine(left=True)



# Scatterplot heatmap

sns.set_theme(style="whitegrid")

# Load the brain networks dataset, select subset, and collapse the multi-index
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
used_columns = (df.columns
                  .get_level_values("network")
                  .astype(int)
                  .isin(used_networks))
df = df.loc[:, used_columns]

df.columns = df.columns.map("-".join)

# Compute a correlation matrix and convert to long-form
corr_mat = df.corr().stack().reset_index(name="correlation")

# Draw each cell as a scatter point with varying size and color
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# Tweak the figure to finalize
g.set(xlabel="", ylabel="", aspect="equal")
g.despine(left=True, bottom=True)
g.ax.margins(.02)
for label in g.ax.get_xticklabels():
    label.set_rotation(90)
for artist in g.legend.legendHandles:
    artist.set_edgecolor(".7")


