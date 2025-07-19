# Dashboard with Matplotlib

# 📚 Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import cycler

# For Jupyter users: enable inline plotting (omit if running as .py file)
# %matplotlib inline

# 📊 Data Reading & Analysis

# Define countries and their regions
country_codes = ['JPN', 'NGA', 'PAK', 'CHN', 'USA', 'IND', 'CAN', 'GHA', 'KEN', 'BGD']
country_groups = {
    'JPN': 'Asia', 'PAK': 'South Asia', 'IND': 'South Asia', 'CHN': 'Asia',
    'USA': 'North America', 'NGA': 'Africa', 'CAN': 'North America',
    'GHA': 'Africa', 'KEN': 'Africa', 'BGD': 'South Asia'
}

# Load the CSV
df = pd.read_csv('countries_data.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Aggregate yearly stats per country
df_line = df.groupby(['year', 'country'])[
    ['Exports', 'GDP Per Capita (USD)', 'co2 emissions', 'Access to electricity']
].mean().reset_index()

# Compute region-level aggregates
df2 = df.set_index('country')
region = df2.groupby(country_groups).mean().reset_index()

# Styling for visual appeal
colors = cycler('color', [
    '#EE6666', '#3cbd2d', '#47f5ec', '#EECC55', '#d42fad',
    '#cc74f7', '#809185', '#f5a802', '#e502f5', '#402633'
])
plt.rc('axes', facecolor='white', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

# Create GridSpec layout
fig = plt.figure(figsize=(18, 20), facecolor='#f9f5fa')
grid = plt.GridSpec(6, 4, wspace=0.6, hspace=0.9)
fig.suptitle(
    'Dashboard Showing Different Indicators for Countries (2012–2020)',
    fontsize=20, fontweight='bold', color='#9003a8'
)
fig.text(0.35, 0.95, 'This dashboard is made with Matplotlib GridSpec Function.', fontsize=15)

# Define subplot axes
ax12 = fig.add_subplot(grid[0, :])
ax13 = fig.add_subplot(grid[1, :])
ax21 = fig.add_subplot(grid[2, 0])
ax22 = fig.add_subplot(grid[2, 1])
ax31 = fig.add_subplot(grid[2, 2])
ax32 = fig.add_subplot(grid[2, 3])
ax41 = fig.add_subplot(grid[3, :])
ax51 = fig.add_subplot(grid[4:, :])

# 1️⃣ GDP per Capita over time
for c in country_codes:
    d = df[df['country'] == c]
    ax12.plot(d['year'], d['GDP Per Capita (USD)'], label=c)
ax12.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax12.set_title("GDP Per Capita of Countries since 2012")
ax12.set_xlabel("Year")
ax12.set_ylabel("GDP Per Capita")
ax12.set(facecolor='#f9f5fa')

# 2️⃣ Access to electricity over time
for c in country_codes:
    d = df[df['country'] == c]
    ax13.plot(d['year'], d['Access to electricity'], label=c)
ax13.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax13.set_title("Access to Electricity of Countries since 2012")
ax13.set_xlabel("Year")
ax13.set_ylabel("Access to Electricity (%)")
ax13.set(facecolor='#f9f5fa')

# 3️⃣ Pie charts by region
location = region['country']
ax21.pie(region['Energy use per capita'], labels=location)
ax21.set_title("Energy Use per Capita by Region")
ax22.pie(region['co2 emissions'], labels=location)
ax22.set_title("CO₂ Emissions by Region")
ax31.pie(region['Inflation'], labels=location)
ax31.set_title("Inflation by Region")
ax32.pie(region['Access to electricity'], labels=location)
ax32.set_title("Access to Electricity by Region")

# 4️⃣ Scatter: Inflation trends
sns.scatterplot(
    ax=ax41, x='year', y='Inflation', hue='country',
    size='Inflation', sizes=(20, 200), data=df
)
ax41.legend(loc='center left', prop={'size': 10}, ncol=2, bbox_to_anchor=(1, 0.5))
ax41.set_title("Inflation in Countries since 2012")
ax41.set_xlabel("Year")
ax41.set(facecolor='#f9f5fa')

# 5️⃣ Bar: GDP Annual Growth
sns.barplot(
    ax=ax51, x='year', y='GDP Growth(Annual)',
    hue='country', data=df
)
ax51.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax51.set_title("GDP Annual Growth in Countries since 2012")
ax51.set_xlabel("Year")
ax51.set(facecolor='#f9f5fa')
ax51.annotate(
    'Witness the negative GDP\n growth in 2020 (COVID)',
    xy=(9, -1), xytext=(7, -3),
    arrowprops=dict(facecolor='green', shrink=0.05)
)
ax51.annotate(
    'Only negative growth for Nigeria',
    xy=(5, -1), xytext=(3, -3),
    arrowprops=dict(facecolor='red', shrink=0.05)
)

# 6️⃣ Annotations
plt.text(7, 60, 'USA has the highest GDP Per Capita throughout', fontsize=9, color='r')
plt.text(7, 48, 'The rise of Bangladesh in electricity access is impressive!', fontsize=9, color='b')
plt.text(7, 22, 'Inflation has been highest in Africa throughout', fontsize=9, color='#08000a')

# ✅ Save dashboard image
fig.savefig('Dashboard_With_Matplotlib.png', facecolor=fig.get_facecolor(), transparent=True)
print("🚀 Saved 'Dashboard_With_Matplotlib.png'")
