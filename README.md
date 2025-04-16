
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

1. **Clone the Repository** or download the `.ipynb` and `.parquet` file
   Make sure you have Python installed (3.8+ recommended)
   git clone [https://github.com/AnaTupa/nyc-taxi-fare-prediction](https://github.com/AnaTupa/Fare_Prediction_Model)
2. **Create a Virtual Environment**:
   python -m venv venv
   Windows:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate
4. **Install dependencies**:
   pip install -r requirements.txt
5. **Run the App**:
   streamlit run app.py

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
Fare_Prediction_Model/
├── app.py                  # Main Streamlit app
├── fare_model.pkl          # Trained model
├── scaler.pkl              # StandardScaler for preprocessing
├── taxi_zone_lookup.csv    # NYC Taxi zone lookup data
├── taxi.png                # Header image
└── README.md               # Project instructions
```
