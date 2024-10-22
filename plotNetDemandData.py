import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# Updated list of Excel files for August 2023, located inside the 'digitizedData' folder
excelFiles = [
    './digitizedData/data33kVsubStation-August-1-2023.xlsx',
    './digitizedData/data33kVsubStation-August-2-2023.xlsx',
    './digitizedData/data33kVsubStation-August-3-2023.xlsx',
    './digitizedData/data33kVsubStation-August-4-2023.xlsx',
    './digitizedData/data33kVsubStation-August-5-2023.xlsx',
    './digitizedData/data33kVsubStation-August-6-2023.xlsx',
    './digitizedData/data33kVsubStation-August-7-2023.xlsx',
    './digitizedData/data33kVsubStation-August-8-2023.xlsx',
    './digitizedData/data33kVsubStation-August-9-2023.xlsx',
    './digitizedData/data33kVsubStation-August-10-2023.xlsx',
    './digitizedData/data33kVsubStation-August-11-2023.xlsx',
    './digitizedData/data33kVsubStation-August-12-2023.xlsx',
    './digitizedData/data33kVsubStation-August-13-2023.xlsx',
    './digitizedData/data33kVsubStation-August-14-2023.xlsx',
    './digitizedData/data33kVsubStation-August-15-2023.xlsx',
    './digitizedData/data33kVsubStation-August-16-2023.xlsx',
    './digitizedData/data33kVsubStation-August-17-2023.xlsx',
    './digitizedData/data33kVsubStation-August-18-2023.xlsx',
    './digitizedData/data33kVsubStation-August-19-2023.xlsx',
    './digitizedData/data33kVsubStation-August-20-2023.xlsx',
    './digitizedData/data33kVsubStation-August-21-2023.xlsx',
    './digitizedData/data33kVsubStation-August-22-2023.xlsx',
    './digitizedData/data33kVsubStation-August-23-2023.xlsx',
    './digitizedData/data33kVsubStation-August-24-2023.xlsx',
    './digitizedData/data33kVsubStation-August-25-2023.xlsx',
    './digitizedData/data33kVsubStation-August-26-2023.xlsx',
    './digitizedData/data33kVsubStation-August-27-2023.xlsx',
    './digitizedData/data33kVsubStation-August-28-2023.xlsx',
    './digitizedData/data33kVsubStation-August-29-2023.xlsx',
    './digitizedData/data33kVsubStation-August-30-2023.xlsx',
    './digitizedData/data33kVsubStation-August-31-2023.xlsx'
]


# Initialize an empt

df = pd.DataFrame()

for file in excelFiles:
    data = pd.read_excel(file,header=3)
    df = pd.concat([df,data])


#NRinds = df_netDemand[df_netDemand.MW=='NR'].index
df_netDemand =  df
df_netDemand['MW'].replace('NR',np.nan,inplace=True)

font_prop = font_manager.FontProperties(size=20)
f,ax = plt.subplots(figsize=(10,6))

ax.plot(df_netDemand['Time'],df_netDemand['MW'],label='net demand', color = 'k')
ax.set_ylabel('MW', color='r', fontproperties=font_prop)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
plt.legend(prop={'size':12})
plt.show()
