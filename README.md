# Sales Analytics & Prediction System

A data analytics project analyzing sales and predicting profitability with SQL, Python (Pandas, scikit-learn, Streamlit). Features SQL reports, visualizations, a 94% accurate Logistic Regression model, and an interactive Streamlit app.

| SQLite, Pandas, Streamlit

## Setup
1. Clone: `git clone https://github.com/your-username/sales-analytics`
2. Install: `pip install -r requirements.txt`
3. Run:
   - `python db_loader.py`
   - `python reporting.py`
   - `python visualization.py`
   - `streamlit run ml_app.py`

## Outputs
- Reports: `Sales_Analytics_Report.pdf`
- Charts: PNG files in root folder


## Extended Description
Extended Description
The Sales Analytics & Prediction System is a comprehensive data analytics project designed to extract actionable insights from sales data and predict profitability. Leveraging a robust tech stack, the project showcases proficiency in data processing, visualization, predictive modeling, and user interface development, making it a strong demonstration of end-to-end data analytics capabilities.
Project Objectives

Analyze Sales Data: Aggregate and report sales, profit, and order metrics across multiple dimensions (region, category, month, quarter, year).
Visualize Trends: Create intuitive charts to highlight performance patterns for stakeholders.
Predict Profitability: Build a machine learning model to forecast whether a sale will be profitable or result in a loss.
Enable User Interaction: Develop a web-based interface for real-time predictions, simulating client-facing tools.

Key Features

SQL-Based Reporting: Queries extract insights from a SQLite database, generating Excel reports for:

Total sales by region.
Top 10 customers by revenue.
Average profit by product category.
Sales, profit, and orders by month, quarter, and year.


Data Visualizations: Professional charts created with Seaborn and Matplotlib:

Bar chart for regional sales.
Line chart for monthly sales trends.
Bar charts for quarterly and yearly sales.


Machine Learning Model: A Logistic Regression model (94% accuracy) predicts profit/loss using features like Sales, Quantity, and Discount.
Streamlit Web App: An interactive interface allows users to input sales data and receive instant profit/loss predictions.
Documentation: A detailed Word report and PowerPoint presentation summarize the project, including code, outputs, and insights.

Technical Details

Dataset: Superstore Sales Dataset (Kaggle), with columns like Order Date, Sales, Profit, Quantity, Discount, Region, and Category.
Technologies:

SQLite: For efficient data storage and querying.
Python: Pandas for data processing, scikit-learn for machine learning, Seaborn/Matplotlib for visualizations.
Streamlit: For building the interactive web app.


Workflow:

Load CSV data into SQLite (db_loader.py).
Generate Excel reports with SQL queries (reporting.py).
Create visualizations (visualization.py).
Deploy a web app with a pre-trained ML model (ml_app.py).



Outputs

Excel Reports: sales_by_region.xlsx, top_customers.xlsx, avg_profit_category.xlsx, monthly_sales.xlsx, quarterly_sales.xlsx, yearly_sales.xlsx.
Charts: High-resolution PNGs (chart_sales_by_region.png, chart_monthly_sales.png, chart_quarterly_sales.png, chart_yearly_sales.png).
Web App: Streamlit app for real-time predictions (screenshot: streamlit_app.png).
Documentation: Sales_Analytics_Report.pdf and Sales_Analytics_Presentation.pptx.

Why This Project?
This project demonstrates a full spectrum of data analytics skills:

Data Analysis: SQL queries for multi-level insights.
Visualization: Clear, professional charts for stakeholder communication.
Machine Learning: Accurate predictive modeling with real-world applicability.
User Interface: Client-friendly app for interactive data exploration.
Documentation: Professional deliverables for technical and non-technical audiences.

Explore the code, run the app, or view the report to see the project in action!
View Report | Run the App | View Presentation

## Technologies
- SQLite, Pandas, scikit-learn, Streamlit, Seaborn, Matplotlib
