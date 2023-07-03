file_path = "./archive.ics.uci.edu_ml_machine-learning-databases_00616_Tetuan City power consumption.csv"

import pandas as pd

df = pd.read_csv(file_path)

# tugas a
print(df[['Temperature', 'Humidity', 'Zone 1 Power Consumption']].head(5))

# tugas b
print(df[['Temperature', 'Humidity', 'Zone 1 Power Consumption']].head(5).var())

# tugas b
print(df[['Temperature', 'Humidity', 'Zone 1 Power Consumption']].head(5).corr())