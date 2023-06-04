import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
import os
import numpy as np

label_list = ['10-4','10-5','10-6','Control']

path = "C:\\Users\\Modern\\Desktop\\Бельская\\МТТ_AMB_19-Aug-22_3.21.42_PM.csv"

data_df = pd.read_csv(path,skiprows=4,header=None, sep='\t')

data_np = data_df[2].to_numpy()

data_reshape = np.reshape(data_np,(12,8))
data_rotate = np.rot90(data_reshape)

np.savetxt("C:\\Users\\Modern\\Desktop\\Бельская\\AMB.csv", data_rotate, delimiter=",")