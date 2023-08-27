import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
import os


def conversion(path, label_list):
    data_df = pd.read_excel(path,skiprows=24,header=None)

    data_df.drop(labels=[0,1,14], axis=1, inplace=True)
    data_df.drop(labels=[6], axis=0, inplace=True)
    print(data_df)
    labels = data_df.columns

    result_labels = {label_list[0]:[],label_list[1]:[],label_list[2]:[],'Control':[]}
    results = pd.DataFrame(result_labels)


    
    results[label_list[0]] =  pd.concat([data_df[3],data_df[4]],ignore_index=True)
    results[label_list[1]] =  pd.concat([data_df[5],data_df[6],data_df[7]],ignore_index=True)
    results[label_list[2]] =  pd.concat([data_df[8],data_df[9],data_df[10]],ignore_index=True)
    results[label_list[3]] =  pd.concat([data_df[11],data_df[12]],ignore_index=True)


    file_name_ext = os.path.basename(path)
    folder_path = os.path.dirname(path)
    file_name,extention = file_name_ext.split(".") 

    # Check if folder /Image exists, if no - create one
    if os.path.isdir(folder_path + '/Converted'):
        print('Image folder already exists')
    else:
        os.mkdir(folder_path + '/Converted')

    save_path = folder_path + '/Converted/' + file_name + '.csv'
    results.to_csv(save_path,index=False)

root = tk.Tk()
paths = fd.askopenfilenames(parent=root, title='Open files')


label_list = ['10-4','10-5','10-6','Control']

for path in paths:
    print(path)
    conversion(path,label_list)