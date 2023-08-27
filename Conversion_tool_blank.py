import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
import os
import numpy as np


def conversion(path, label_list):
    data_df = pd.read_excel(path,skiprows=23,header=None)
    data_df.drop(columns=[0,1,14], axis=1, inplace=True)

    result_labels = {label_list[0]:[],label_list[1]:[],label_list[2]:[],'Control':[]}
    results = pd.DataFrame(result_labels)

    #Concat 3 column
    i = 2
    for label in label_list:
        results[label] = pd.concat([data_df[i],data_df[i+1],data_df[i+2]],ignore_index=True)
        i = i+3

    file_name_ext = os.path.basename(path)
    folder_path = os.path.dirname(path)
    file_name,extention = file_name_ext.split(".") 

    results["Blanks"] = np.nan
    results.loc[0, "Blanks"] = results.loc[0, "10-4"]
    results.loc[1, "Blanks"] = results.loc[23, "10-4"]
    results.loc[2, "Blanks"] = results.loc[0, "Control"]
    results.loc[3, "Blanks"] = results.loc[23, "Control"]

    results.loc[0, "10-4"] = np.nan
    results.loc[23, "10-4"] = np.nan
    results.loc[0, "Control"] = np.nan
    results.loc[23, "10-4"] = np.nan


    print(results)

    # Check if folder /Converted exists, if no - create one
#     if os.path.isdir(folder_path + '/Converted'):
#         print('Folder already exists')
#     else:
#         os.mkdir(folder_path + '/Converted')

#     save_path = folder_path + '/Converted/' + file_name + '.csv'
#     results.to_csv(save_path,index=False)

root = tk.Tk()
paths = fd.askopenfilenames(parent=root, title='Open files')

label_list = ['10-4','10-5','10-6','Control']

for path in paths:
    conversion(path,label_list)