import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Task4a_data.csv")

df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['USD - GBP'], label='USD to GBP trend')

plt.title("USD rates to GBP over time")
plt.xlabel('Date')
plt.ylabel('USD to GBP rates')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()