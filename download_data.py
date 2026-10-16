import yfinance as yf
import pandas as pd

tickers = [
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "INFY.NS",
    "AXISBANK.NS",
    "M&M.NS",
    ]

prices = yf.download(
    tickers,
    start="2023-07-01",
    end="2026-07-01",
    auto_adjust=True,
    threads=False
)["Close"]

prices.to_excel("VaR project.xlsx")

print(prices.head())
print("\nMissing values:")
print(prices.isna().sum())