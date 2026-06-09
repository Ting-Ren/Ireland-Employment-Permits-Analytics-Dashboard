# 🇮🇪 Ireland Employment Permits Analytics Dashboard

An interactive, data-driven Streamlit dashboard designed to analyze and track corporate visa sponsorship trends in Ireland from 2021 through 2026 (current up to May 2026). 

This application consolidates multi-year government data into a unified interface, empowering job hunters and market analysts to bypass fragmented spreadsheets and instantly uncover hiring trajectories.

## 🚀 Key Features

* **🔍 Fuzzy Employer Group Search:** Instantly aggregate and track permit metrics for specific corporate clusters or subsidiaries (e.g., searching "Google" pulls data for *Google Ireland Limited*, *Google Cloud*, etc.) into a unified matrix view.
* **📅 Dynamic Timeframe Filtering:** Slice macro and micro data views instantly across customizable year ranges using inline controls.
* **📈 Trend Line & Volume Matrix Views:** Compare side-by-side annual performance matrices alongside interactive Plotly charts with zero horizontal scrolling.
* **🎯 Column-Isolated Grid Search:** Interrogate raw records via independent dropdown and text inputs to isolate specific data parameters without mixing row parameters.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit (UI & Layout Optimization)
* **Data Engineering:** Pandas (Dynamic Multi-Year Parsing Pipeline & Pivot Transformations)
* **Data Visualization:** Plotly Express (Interactive Data Visualization)

## 📊 Data Source

Data is sourced natively from the Irish government's official monthly releases. 
> 📄 **Data Courtesy of:** [Department of Enterprise, Tourism and Employment (DETE) Statistics](https://enterprise.gov.ie/en/what-we-do/workplace-and-skills/employment-permits/statistics/)

## 🏃‍♂️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
