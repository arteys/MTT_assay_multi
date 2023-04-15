import pandas as pd

path = "D:\Минин\BNTM-349.xlsx"

data_df = pd.read_excel(path,skiprows=23,header=None)
data_df.drop(columns=[0,1,14], axis=1, inplace=True)


label_list = ['10-4','10-5','10-6','Control']

result_labels = {label_list[0]:[],label_list[1]:[],label_list[2]:[],'Control':[]}
results = pd.DataFrame(result_labels)

print(data_df)

i = 2
for label in label_list:
    results[label] = pd.concat([data_df[i],data_df[i+1],data_df[i+2]],ignore_index=True)
    i = i+3

print(results)