# 🛒 Retail Demand Forecasting – Capstone Project

## Overview
This project was developed as part of my final capstone for the Code Institute’s *Data Analytics with AI* programme.  
The aim was to explore and analyse a large real-world dataset to understand retail sales performance, trends, and seasonality.  

Using **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**, I processed raw sales data and created an interactive dashboard that helps visualise store and product performance.  
The project demonstrates how data analysis can reveal useful business insights and support better decision-making.

🌐 **Live Dashboard:** [Check it out on Heroku](https://retail-demand-forecasting-3c6fb0a301e9.herokuapp.com/)

This project is now live and fully deployed using Heroku.  
It runs my Streamlit dashboard with a smaller sample of the dataset so it loads faster online.

---

## Dataset
The dataset is from [Kaggle – Store Sales: Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting).  
It contains around **3 million rows** of daily sales from 2013 to 2017 across multiple stores and product families.

**Files included:**
- `train.csv` – main file with daily sales for each store and product family  
- `stores.csv` – store information  
- `transactions.csv` – number of transactions per store  
- `holidays_events.csv` – holidays and special events  
- `oil.csv` – oil prices used as an external factor  

**Key columns:**
- `date` – date of sale  
- `store_nbr` – store number  
- `family` – product category  
- `sales` – total daily sales  
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

### Step 1 – Loading and Exploring the Data
I began by loading the `train.csv` file into Jupyter Notebook to understand its structure and contents.  
Basic commands such as `df.info()` and `df.describe()` helped identify column types, missing data, and overall dataset size.

---

### Step 2 – Data Cleaning
Before analysis, I cleaned and prepared the dataset:
- Converted the `date` column to a datetime format  
- Sorted by store, family, and date  
- Replaced missing values with zeros  
- Saved a clean version to `/data/processed/train_clean.csv`  

This made the data ready for analysis and ensured consistency across all files.

---

### Step 3 – Exploratory Data Analysis (EDA)
I explored sales trends and relationships between different variables.  
The main areas I looked at were:
- Overall sales performance over time  
- Product families with the highest sales  
- Store-level differences  
- The effect of promotions on sales  

I used **Matplotlib** and **Seaborn** to create visuals such as line charts, bar charts, and box plots.  

```python
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['sales'])
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

```

This revealed clear weekly patterns and seasonal spikes, especially around holidays.

⸻

### Step 4 – Feature Engineering

To capture longer-term trends, I created new features:

 	•	Extra columns showing sales from previous days (to capture short-term trends)
	•	Moving averages to highlight overall patterns

These were saved in /data/processed/train_features.csv and used later in the dashboard.

⸻

### Step 5 – Key Findings

From the analysis, I found that:

    •	Sales followed consistent weekly and seasonal cycles
	•	Families like GROCERY, BEVERAGES, and BREAD/BAKERY were top performers
	•	Promotions had a positive effect, though it varied by product and store
	•	Sales consistently spiked in December due to holiday demand

These insights help highlight how seasonality and promotions influence customer buying behaviour.

⸻

Streamlit Dashboard

After completing the analysis, I built an interactive dashboard using Streamlit to make the findings easier to explore.

File: dashboard/app.py

Main features:

    •	Dropdown filters for Store and Product Family
	•	Line chart of daily sales trends
	•	Bar chart for top-performing families
	•	Box plot showing weekly sales patterns
	•	Monthly summary of total sales

    

This dashboard allows users to interact with the data and visualise trends without using Jupyter.

To run the dashboard:

```bash
cd dashboard
streamlit run app.py
```

### Ethical Considerations

    •	The dataset contains no personal or sensitive information
	•	All data is aggregated by store and used for educational purposes
	•	Original Kaggle files are excluded from version control for good data-handling practice


⸻

### Reproducibility

To reproduce this project:

```bash

# 1. Clone the repository
git clone https://github.com/Elmifarah1/retail-demand-forecasting.git

# 2. Set up a virtual environment
cd retail-demand-forecasting
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the notebook
jupyter lab

# 5. Launch the dashboard
cd dashboard
streamlit run app.py
```
### Reflection

This project allowed me to put my data analysis skills into practice and work through a full end-to-end workflow — from collecting and cleaning data, all the way to building a working dashboard. I Improved in: 
	
    •	Ceaning and managing large datasets
    •	Analysing data using Pandas
	•	Visualising insights with Matplotlib and Seaborn
	•	Creating an interactive dashboard with Streamlit
	•	Using Git and GitHub for version control

This project also taught me the importance of planning, version control, and breaking tasks into smaller steps.  
If I had more time, I’d add simple forecasting models to predict future sales and compare them to the real results.  
Overall, this project gave me the confidence to handle data from start to finish and present it in a way that makes sense to both technical and non-technical audiences.

⸻

### Credits
	•	Dataset: Kaggle – Store Sales: Time Series Forecasting
	•	Created by: Elmi Farah - Code Institute – Data Analytics with AI Capstone Project (2025)