
import matplotlib.pyplot as plt

labels = [
    "Historical 95%", "Parametric 95%", "Historical 99%", "Parametric 99%"
]

expected = [5.0, 5.0, 1.0, 1.0]
actual = [7.35, 5.92, 1.84, 1.84]

x = range(len(labels))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    [i - width / 2 for i in x],
    expected,
    width,
    label="Expected breach rate"
)

plt.bar(
    [i + width / 2 for i in x],
    actual,
    width,
    label="Actual breach rate"
)

plt.xticks(list(x), labels)
plt.ylabel("Breach rate (%)")
plt.title("VaR Backtesting: Expected vs Actual Breach Rates")
plt.legend()
plt.tight_layout()
plt.savefig("backtesting_breach_rates.png", dpi=300)
plt.show()