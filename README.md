#  Advanced Dashboard with Matplotlib

A visually rich, professional-level static dashboard built using **Matplotlib**, **Seaborn**, and **Pandas**. This project demonstrates how to combine multiple chart types into a single dashboard layout and render it as a high-quality `.png` image for reporting and analysis.

---

##  Overview

This project uses Python’s Matplotlib `GridSpec` layout to display multiple data visualizations—line plot, bar chart, pie chart, and scatter plot—all in one structured layout. It is ideal for static reporting, analytics presentations, and building your portfolio as a data analyst or Python developer.

---

##  Dashboard Preview

> Output: `Dashboard_With_Matplotlib.png`

![Dashboard Output](<img width="1800" height="2000" alt="Dashboard_With_Matplotlib" src="https://github.com/user-attachments/assets/3814f7e2-68fa-4709-885d-6182d9abf805" />
)

---

##  Project Structure

dashboard_with_matplotlib/
├── data.csv # Input dataset
├── dashboard.py # Python script to create and save dashboard
├── Dashboard_With_Matplotlib.png # Output dashboard image (auto-generated)
└── README.md # Project documentation


---

## 📂 Dataset Format (data.csv)

This project expects a basic CSV format with the following sample structure. You can replace this with your own relevant dataset and modify the plotting logic accordingly:

```csv
Year,Sales,Profit,Region,Category
2018,120,30,North,Tech
2019,150,45,South,Office
2020,180,60,East,Furniture
2021,200,70,West,Tech
2022,210,90,North,Furniture
```
You can use any dataset, just make sure the columns match your visualization requirements in dashboard.py.

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/dvanhu/Dashboard-with-Matplotlib.git
cd Dashboard-with-Matplotlib
```

2. **Install Required Packages**

```bash
pip install matplotlib pandas seaborn
```

3. **Run the Dashboard Script**

```bash
python dashboard.py
```

The output will be saved as `Dashboard_With_Matplotlib.png` in the same directory.

## **Tech Stack**

| Technology   | Purpose                          |
|--------------|----------------------------------|
| Python 3.x   | Main programming language        |
| Pandas       | CSV data handling                |
| Matplotlib   | Core charting & layout framework |
| Seaborn      | Chart styling & enhancement      |

## **What You'll Learn**

- Using GridSpec to organize multiple subplots  
- Loading and preprocessing CSV data using pandas  
- Enhancing chart readability with seaborn  
- Exporting static charts as `.png` for offline use  
- Styling charts using custom color palettes, titles, and legends  

## **Sample Visualizations**

- **Line Plot**: Sales trend over years  
- **Bar Chart**: Profit by region  
- **Pie Chart**: Category distribution  
- **Scatter Plot**: Correlation between sales and profit  

All visualizations are customized for better clarity and are arranged in a clean dashboard layout.


