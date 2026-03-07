import numpy as np
import pandas as pd

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
temperature = np.array([33,44,22,43,23,55,23])

df = pd.DataFrame({
    'days': days,
    'temperature': temperature,
})

print(df['temperature'].mean())
print(df['temperature'])
print(df['temperature'].min())
print(df['temperature'].max())
print(df['temperature']+33)