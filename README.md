# 🛒 Retail Demand Forecasting – Capstone Project

## Overview
This project was created as part of my final capstone for the Code Institute’s *Data Analytics with AI* programme.  
The goal was to work with a large, real-world dataset to explore, clean, analyse, and visualise retail sales data in a meaningful way.  

I used **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit** to go from raw data to an interactive dashboard that allows users to explore sales performance across different stores and product categories.  
The project shows how data analytics can be used to uncover sales trends, identify seasonality, and help businesses make informed decisions.

---

## Dataset
The data comes from [Kaggle – Store Sales: Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting).  
It contains around **3 million rows** covering daily sales from 2013 to 2017 across multiple stores and product families.

**Files used:**
- `train.csv` – main file with daily sales for each store and product family  
- `stores.csv` – details about each store  
- `transactions.csv` – store-level transactions data  
- `holidays_events.csv` – national holidays and events  
- `oil.csv` – oil prices used as an external factor  

**Key columns:**
- `date` – date of sale  
- `store_nbr` – store number  
- `family` – product family (category)  
- `sales` – sales amount  
- `onpromotion` – number of items on promotion  

---

## Tools and Libraries
| Purpose | Tools Used |
|----------|-------------|
| Data analysis | Python, Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit |
| Development | Jupyter Notebook, VS Code, Git, GitHub |

---

## Project Process

### 1. Data Loading and Inspection
I started by loading the `train.csv` file in Jupyter Notebook.  
I checked its structure, data types, and size using commands such as `df.info()` and `df.describe()`.  
This gave me a clear understanding of what the data looked like before cleaning.

### 2. Data Cleaning
The next step was preparing the data for analysis:
- Converted the `date` column to a proper datetime format.  
- Sorted the data by store, family, and date.  
- Checked for missing values and replaced them with zeros.  
- Saved the cleaned file to `/data/processed/train_clean.csv`.

The raw data was quite large, so I made sure only processed versions were included in the repository for easier management.

### 3. Exploratory Data Analysis (EDA)
I then explored sales patterns and behaviour over time.  
Some of the things I looked at include:
- Overall sales trends across the years.  
- Which product families performed best.  
- How sales varied by store.  
- The relationship between promotions and sales.  

I used **Matplotlib** and **Seaborn** to create line charts, bar charts, and box plots.  
For example:

```python
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['sales'])
plt.title("Daily Sales Over Time")

This helped identify clear weekly and seasonal trends, with visible spikes around holidays.

### 4. Feature Engineering
To capture longer-term trends, I created lag features and moving averages:
- **Lag features** showed previous sales behaviour.  
- **Rolling averages** smoothed out short-term fluctuations.  

These new features were saved in `/data/processed/train_features.csv` for later use.

---

### 5. Findings and Insights
From the analysis, I found:
- Sales followed strong weekly and seasonal cycles.  
- Families such as **GROCERY I**, **BEVERAGES**, and **BREAD/BAKERY** consistently had higher sales.  
- Promotions increased sales, but their impact varied by store and product.  
- **December** had clear spikes due to holiday periods.  

These findings highlighted how promotions and seasonality drive retail demand, helping inform stock planning and marketing decisions.

---

## Streamlit Dashboard
After completing the notebook, I built a simple **Streamlit** dashboard to make the findings more interactive and accessible.

**File:** `dashboard/app.py`

**Key Features:**
- Dropdown filters for **Store** and **Product Family**  
- Line chart showing daily sales trends  
- Bar chart displaying top-performing families  
- Box plot comparing weekly sales behaviour  
- Monthly summary of total sales  

This allows anyone to explore the dataset visually without needing to use Jupyter Notebook.

**To run the dashboard:**
```bash
cd dashboard
streamlit run app.py