import pandas as pd
import numpy as np

data = pd.read_csv('./data.csv')
new_data_with_deleted_null = data.dropna()
print(new_data_with_deleted_null)
print(df.fillna(130, inplace = True))

data['date'] = data.to_dateTime(df['date'])

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
    
    df.drop_duplicates(inplace = True)
