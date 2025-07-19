import pandas as pd

# Заміни на свій шлях до файлу
file_path = 'data/ZA7888_v1-0-0.dta'

df = pd.read_stata(file_path, convert_categoricals=False)

print(df.head())

# Зберегти як CSV
df.to_csv('data/output.csv', index=False)
