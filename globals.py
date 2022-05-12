import os
import pandas as pd
import pickle
import numpy as np
import scipy as sp
import scipy.signal as sig
import seaborn as sns
import matplotlib
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy.stats import wilcoxon, ttest_rel


fs = 16

fmts = ['svg','pdf']
#fmts = []

columnwidth = 3.5 # in
pagewidth = 8.5 - 0.680 - 0.564 # in; weird numbers from IEEEtran.cls

preamble = r'\input{'+os.getcwd()+r'/macros}'
preamble = ''
matplotlib.rcParams['text.latex.preamble'] = preamble

font = { 'fontsize': fs, 'fontname': 'sans-serif', 'fontweight':'normal' }

rc={'axes.labelsize': fs, 'font.size': fs, 'legend.fontsize': fs, 
            'axes.titlesize': fs,'xtick.labelsize': fs, 'ytick.labelsize': fs,
                'text.usetex':True,'pdf.fonttype':42}

mpl.rcParams.update(rc)

sns.set(rc=rc)
#sns.palplot(sns.color_palette("Paired_r",9))
sns.set_palette('Paired_r',9)
sns.set_style("white")

palette = sns.color_palette()

colors = dict(M='#6600CC',
              F='#000000',
              B='#FFFFFF',
              H='#009900',
              r='#FDB119',
              u='#009900',
              d='#FD6E19',
              #y='#0033FF',  #or 6600CC which is darker and I prefer 
              y='#6600CC',  #or 6600CC which is darker and I prefer 
              N='#0000CC',
              D='#CC0000',
              first5='#B1B1B1',
              last5='#999999')
              # D = dominant = right; N = nondominant = left

colors['right'] = colors['D']
colors['left']  = colors['N']

