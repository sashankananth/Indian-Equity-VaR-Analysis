# VaR and Expected Shortfall Analysis of an Indian Equity Portfolio

## Overview

This project evaluates the market risk of a hypothetical ₹10 lakh Indian equity portfolio comprising HDFC Bank, ICICI Bank, Infosys, Axis Bank, and Mahindra & Mahindra.

Using historical market data from July 2023 to June 2026, I calculated Value at Risk (VaR) and Expected Shortfall (ES), compared alternative estimation methods, and evaluated their performance through out-of-sample backtesting.

## Methods and Tools

**Risk analysis**
- Historical Simulation and Parametric (Variance-Covariance) VaR at 95% and 99% confidence levels.
- Historical and Parametric Expected Shortfall.
- Return distribution analysis using a histogram, skewness, and excess kurtosis.
- Rolling 250-day out-of-sample backtesting.
- Kupiec Proportion of Failures test to assess observed VaR breach frequencies.

**Tools:** Microsoft Excel, Python, Pandas, yfinance, and Matplotlib.

## Project Files

- `download_data.py` — Downloads historical stock-price data.
- `plot_distribution.py` — Generates the portfolio returns chart.
- `plot_backtesting.py` — Generates the backtesting comparison chart.
- `VaR project.xlsx` — Excel workbook containing the data and analysis.
- `VaR project.docx` — Detailed methodology, results, and interpretation.
- `returns_histogram.png` — Distribution of daily portfolio returns.
- `backtesting_breach_rates.png` — Expected versus actual breach rates.

## Data Sources and Limitations

**Sources:** [Trendlyne holdings snapshot — insert exact URL]([https://www.trendlyne.com/](https://trendlyne.com/portfolio/superstar-shareholders/54044/latest/vanguard-fund/)) and [Yahoo Finance](https://finance.yahoo.com/).

The portfolio weights are normalised from the disclosed holdings percentages of five selected stocks associated with Vanguard; this is not a reconstruction of any individual Vanguard fund. Portfolio weights are held constant for the historical return analysis. VaR and ES are historical estimates and do not guarantee future outcomes.

## Reproducing the Project

Python dependencies: `yfinance`, `pandas`, `openpyxl`, and `matplotlib`.

Install them with:

```bash
pip install yfinance pandas openpyxl matplotlib
```

Run the data-download script with:

```bash
python download_data.py
```

Run the chart script with:

```bash
python plot_backtesting.py
```

The main financial calculations and Kupiec test are documented in the Excel workbook; the Python scripts handle data retrieval and visualisation.

---

*This project was developed for educational purposes and does not constitute investment advice.*
