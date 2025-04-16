
# 🚕 NYC Taxi Trip Data Analysis & Fare Prediction

This project analyzes Yellow Taxi trip data in New York City and builds a **Linear Regression model** to predict taxi fare amounts based on trip features. The dataset comes from the [NYC Taxi & Limousine Commission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

![Cover](A_high-resolution_digital_photograph_captures_Time.png)

---

## 📦 Dataset

- **Source**: NYC TLC Public Trip Data
- **File**: `yellow_tripdata_2024-08.parquet`
- **Size**: Over 1 million rows of taxi trip records
- **Link**: [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## 🔍 Key Steps in the Notebook

1. **Importing Libraries** – pandas, matplotlib, seaborn, scikit-learn, etc.
2. **Loading Data** – Reads Parquet file into DataFrame
3. **Data Cleaning** – Replaces missing values to median for numerical data, replaces missing values to mode for categorical data, removes irrelevant columns (e.g., `extra`,`mta_tax`, `tip_amount`, `tolls_amount`, `improvement_surcharge`, `total_amount`, `congestion_surcharge`)
4. **Feature Engineering** – Adds feature total trip time
5. **Exploratory Data Analysis** – Uses `seaborn` and `matplotlib` for visualizing patterns
6. **Modeling** – Trains a Linear Regression model using `scikit-learn`
7. **Evaluation** – Reports MSE and MAE and R² scores
8. **Model Export** – Saves the trained model with `pickle`

---

## 🛠️ How to Run

1. **Clone the repo** or download the `.ipynb` and `.parquet` file
2. Make sure you have Python installed (3.8+ recommended)

3. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib statsmodels pyarrow
   ```

4. **Run the notebook**:
   Open `Copy_of_Taxi_Dataset.ipynb` in Jupyter Notebook, Google Colab, or VS Code and execute all cells.

---

## 📊 Model Metrics

- **Model**: Linear Regression
- **Target**: `fare_amount`
- **Metrics**:
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
  - R² Score

---

## 📁 Project Structure

```
├── Copy_of_Taxi_Dataset.ipynb
├── yellow_tripdata_2024-08.parquet
├── A_high-resolution_digital_photograph_captures_Time.png
└── README.md
```
