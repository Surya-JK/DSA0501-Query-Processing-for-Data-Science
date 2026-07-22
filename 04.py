import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('alphabet_stock_data.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

# Filter dates
start_date = '2020-04-01'
end_date = '2020-05-01'
filtered_df = df.loc[start_date:end_date]

plt.figure(figsize=(10, 5))
plt.plot(filtered_df.index, filtered_df['Close'], label='Close Price', color='blue')
plt.title('Alphabet Inc. Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()