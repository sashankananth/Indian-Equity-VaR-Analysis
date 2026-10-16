import pandas as pd
import matplotlib.pyplot as plt

returns =pd.read_excel(
     "VaR project.xlsx",
      sheet_name="Returns",
      header=3)

portfolio_returns = returns["Portfolio Return"].dropna()

plt.figure(figsize=(10, 6))
plt.hist(portfolio_returns, bins=50)

plt.title("Distribution of Daily Portfolio Returns")
plt.xlabel("Daily Portfolio Return")
plt.ylabel("Frequency")

plt.show()