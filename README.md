# 🇮🇪 Ireland Employment Permits Analytics Dashboard

An interactive, data-driven analytics platform designed to aggregate and track corporate visa sponsorship trends in Ireland from 2021 through 2026 (current up to May 2026). 

You can do Employer Search for past sponsorship, which can be a reference when you are on the job-hunting in Ireland. By consolidating fragmented monthly government spreadsheets into a unified multi-year interface, this application empowers job hunters to evaluate historical company behavior and target sponsors.

## 🔗 Live Application Access

The dashboard is fully deployed and accessible 24/7 in the cloud. No installation required:
👉 **[Launch Live Ireland Employment Permits Dashboard](https://ireland-employment-permits-analytics-dashboard-ting-ren.streamlit.app/)**

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

## 🤖 AI Declaration

This software application was co-created using a prompt-driven AI development workflow:
* **Product Management & Architecture:** Entirely scoped, defined, and architecturally guided by the repository owner to address localised user-experience gaps in official job-market data reporting.
* **Engineering & Optimization:** Code construction, algorithmic design for the dynamic multi-year spreadsheet parser, edge-case debugging (e.g., JSON matrix parsing bugs), and frontend layout tuning were executed via conversational collaboration with Gemini (Google AI).

## 📊 Data Source

Data is sourced natively from the Irish government's official monthly structural releases. 
> 📄 **Data Courtesy of:** [Department of Enterprise, Tourism and Employment (DETE) Statistics](https://enterprise.gov.ie/en/what-we-do/workplace-and-skills/employment-permits/statistics/)
