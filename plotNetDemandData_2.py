import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import os

excel_files = [
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


df = pd.DataFrame()

for file in excel_files:
    data = pd.read_excel(file, header=3)
    filename = os.path.basename(file)
    parts = filename.split('-')
    day = parts[2]  # '2'
    year = parts[3].replace('.xlsx', '') 
    full_date_str = f"August {day}, {year}"
    file_date = pd.to_datetime(full_date_str, format='%B %d, %Y')
    data['Date'] = file_date
    df = pd.concat([df, data], ignore_index=True)

df['MW'].replace('NR', np.nan, inplace=True)
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))
df['MW'] = pd.to_numeric(df['MW'], errors='coerce')
font_prop = font_manager.FontProperties(size=14)
fig, ax = plt.subplots(figsize=(14, 8))
dates = sorted(df['Date'].unique()) 
colors = plt.cm.plasma(np.linspace(0, 1, len(dates)))
for i, date in enumerate(dates):
    date_data = df[df['Date'] == date]
    ax.plot(date_data['Datetime'], date_data['MW'], label=f'August {date.day}', color=colors[i])
    ax.scatter(date_data['Datetime'], date_data['MW'], color=colors[i], s=5, label=None)
    for j in range(0, len(date_data), len(date_data) // 5):
        ax.text(date_data['Datetime'].iloc[j], date_data['MW'].iloc[j], 
                f'{date_data["MW"].iloc[j]:.1f}', fontsize=9, color=colors[i])

ax.set_xlabel('Date and Time', fontsize=14, fontproperties=font_prop)
ax.set_ylabel('MW', fontsize=14, fontproperties=font_prop)
ax.set_title('Net Solar Energy Demand for August 2023', fontsize=16, fontproperties=font_prop)
plt.xticks(rotation=45)
ax.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Day of August', title_fontsize=12, fontsize=10, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()

