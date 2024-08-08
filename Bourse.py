import yfinance as yf

# Descargar datos históricos de una acción
data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
