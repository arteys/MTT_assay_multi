import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
import os
import numpy as np

label_list = ['10-4','10-5','10-6','Control']

path = "C:\\Users\\Modern\\Desktop\\Бельская\\BNPGA-418.xlsx"

data_df = pd.read_excel(path,skiprows=2,header=None)


data_np = data_df[3].to_numpy()


data_reshape = np.reshape(data_np,(12,8))
data_rotate = np.rot90(data_reshape)

print(data_rotate)

np.savetxt("C:\\Users\\Modern\\Desktop\\Бельская\\BNPGA-418.csv", data_rotate, delimiter=",")