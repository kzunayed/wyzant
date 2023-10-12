import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['AAPL', 'IBM', 'MSFT', 'GOOG']
all_data = {}
for ticker in tickers:
    all_data[ticker] = yf.download(ticker)
print(all_data['AAPL'].tail())

price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
print(price.head())
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

price.plot.line()
plt.title('Stock Prices')
plt.show()

price['AAPL'].plot.line()
plt.title('AAPL Stock Prices')
plt.show()

returns = price.pct_change()
print(returns.tail())

cov_matrix = returns.cov()
print('Covariance between MSFT and IBM:')
print(cov_matrix.loc['MSFT', 'IBM'])

corr_matrix = returns.corr()
print('Correlation between MSFT and IBM:')
print(corr_matrix.loc['MSFT', 'IBM'])
