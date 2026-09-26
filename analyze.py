"""
COVID-19 Global Impact Analysis
--------------------------------
Data source: Worldometer cumulative COVID-19 totals (public data,
https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/)
for the 14 countries with the highest reported case counts.

This script:
1. Loads and cleans the country-level case/death data.
2. Computes each country's Case Fatality Rate (CFR).
3. Ranks countries by total cases and by CFR.
4. Produces two charts: total cases by country, and CFR by country.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("covid19_country_data.csv")

# 2. Clean + derive metrics
df = df.dropna()
df["case_fatality_rate_pct"] = (df["total_deaths"] / df["total_cases"] * 100).round(2)
df_sorted_cases = df.sort_values("total_cases", ascending=False)
df_sorted_cfr = df.sort_values("case_fatality_rate_pct", ascending=False)

print("Top 5 countries by total cases:")
print(df_sorted_cases[["country", "total_cases"]].head(5).to_string(index=False))

print("\nTop 5 countries by case fatality rate (%):")
print(df_sorted_cfr[["country", "case_fatality_rate_pct"]].head(5).to_string(index=False))

# 3. Chart 1 - Total cases by country
plt.figure(figsize=(9, 5))
plt.barh(df_sorted_cases["country"], df_sorted_cases["total_cases"] / 1e6, color="#1F4E5F")
plt.xlabel("Total confirmed cases (millions)")
plt.title("COVID-19 Total Confirmed Cases by Country")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("cases_by_country.png", dpi=150)
plt.close()

# 4. Chart 2 - Case fatality rate by country
plt.figure(figsize=(9, 5))
plt.barh(df_sorted_cfr["country"], df_sorted_cfr["case_fatality_rate_pct"], color="#8B1E2D")
plt.xlabel("Case Fatality Rate (%)")
plt.title("COVID-19 Case Fatality Rate by Country")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("cfr_by_country.png", dpi=150)
plt.close()

print("\nCharts saved: cases_by_country.png, cfr_by_country.png")
