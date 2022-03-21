#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:19:04 2022

@author: samantha
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

frase = pd.read_fwf('lerolero.txt').to_string(index=False, na_rep=' ')

# gerar nuvem de palavras
nuvem = WordCloud(
    background_color='black',
    width=1600,
    height=600).generate(frase)

# criar gráfico
fig, ax =plt.subplots( figsize = (10,7))
ax.imshow (nuvem, interpolation = 'bilinear')
ax.set_axis_off()














