import numpy as np
import pandas as pd

numpy_arr_1 = np.array([8,9,10])
numpy_arr_2 = np.array([[8,9,10], [11,12,13], [14,15,16]])

print('-------------------')
print(pd.DataFrame(numpy_arr_1))
print('-------------------')
print(pd.DataFrame(numpy_arr_2))
print(pd.DataFrame(numpy_arr_2, index = ['row1', 'row-2', 'row-3'], columns = ['col-1', 'col-2', 'col-3']))

states = ['California', 'Texas', 'New York']
populations = [39538223, 29145505, 20201249]
data = {'State': states, 'Population': populations}
df = pd.DataFrame(data)
print(df)

numpy_arr_1 = np.array([8,9,10])
new_s = pd.Series(numpy_arr_1, index = ['a', 'b', 'c'])
print(new_s * 10)
print(new_s > 8)
print(new_s[new_s > 8])
print(new_s[(new_s > 8) & (new_s < 10)])


print('-------------------')
countryData = {
    'population': [888, 999, 393, 3939],
    'weather': ['warm','cold', 'warm','cold']
}
countryPandas = pd.DataFrame(countryData, index=['Herat', 'kabul', 'mazar', 'badghis'])
print(countryPandas)
print('----------------')
print(countryPandas.loc['Herat'])
print(countryPandas.loc['Herat': 'mazar', 'population'])
print('----------------')
print(countryPandas.iloc[-1])
print(countryPandas.iloc[1: 3])
print('----------------')
print(countryPandas['population'])