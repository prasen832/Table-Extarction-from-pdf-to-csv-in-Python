import tabula
import pandas as pd


# We have already downloded the pdf
# Now, convert the table on page no 54 into a csv file using tabula.

# Note: Keep our pdf in current directory.

tabula.convert_into('Walmart.pdf', 'Walmart.csv', pages=56)


# Open and view the table in Pandas Dataframe

df = pd.read_csv('Walmart.csv')


# Delete unnecessary columns

del df['Unnamed: 1']
del df['Unnamed: 3']
del df['Unnamed: 5']


# Rename th first column and replace all the '-' with 0 for further calculations. 

df = df.rename(columns={'(Amounts in millions, except per share data)':'Title'})
df = df.replace(df.iloc[13][1], 0)


# Replace NaN with 0 to make further calculations easy.

df.fillna(0, inplace=True)


# Use ReGex to remove ',','(' and ')' symbols from all columns.

# Convert all columns data type from object to float to make further analysis easy.

df['2021'] = df['2021'].replace(',', '', regex=True)
df['2021'] = df['2021'].replace('\(', '', regex=True)
df['2021'] = df['2021'].replace('\)', '', regex=True)
df['2021'] = df['2021'].astype(float)

df['2022'] = df['2022'].replace(',', '', regex=True)
df['2022'] = df['2022'].replace('\(', '', regex=True)
df['2022'] = df['2022'].replace('\)', '', regex=True)
df['2022'] = df['2022'].astype(float)

df['2023'] = df['2023'].replace(',', '', regex=True)
df['2023'] = df['2023'].replace('\(', '', regex=True)
df['2023'] = df['2023'].replace('\)', '', regex=True)
df['2023'] = df['2023'].astype(float)



# Save this dataframe as csv file to local sy
df.to_csv('Walmart_54.csv')


# Save this dataframe as pdf to local system

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colWidths=[0.7,0.1,0.1,0.1])
table.auto_set_font_size(False)
table.set_fontsize(7)
plt.savefig('Walmart_54.pdf', format='pdf')


# This csv file is now ready for further analysis.




