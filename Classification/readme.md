# Fraud Detection Prediction System

## 📌 Project Overview

This project is a **Machine Learning based Fraud Detection System** that predicts whether a financial transaction is **fraudulent or genuine**.
The model is trained on transaction data and deployed using **Streamlit** to provide an interactive web interface for users to enter transaction details and get predictions.

---

## 🚀 Features

* Predicts **fraudulent vs genuine transactions**
* Interactive **Streamlit web application**
* Uses **Machine Learning classification models**
* Handles **categorical and numerical features using pipelines**
* Includes **data preprocessing and model serialization**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle (for saving the trained model)

---

## 📂 Project Structure

```
Fraud-Detection-Project
│
├── FRAUD.py                  # Streamlit application
├── fraud_detection_pipeline.pkl  # Trained ML pipeline
├── dataset.csv               # Transaction dataset
├── model_training.ipynb      # Model training notebook
└── README.md                 # Project documentation
```

---

## 📊 Dataset Features

The model uses the following transaction attributes:

* `type` – Transaction type (PAYMENT, TRANSFER, CASH_OUT, etc.)
* `amount` – Transaction amount
* `oldbalanceOrg` – Sender's balance before transaction
* `newbalanceOrig` – Sender's balance after transaction
* `oldbalanceDest` – Receiver's balance before transaction
* `newbalanceDest` – Receiver's balance after transaction

Target Variable:

* `isFraud` – Indicates whether the transaction is fraudulent (1) or genuine (0)

---

## ⚙️ Model Pipeline

The project uses a **Scikit-learn Pipeline** that includes:

1. **ColumnTransformer**

   * StandardScaler for numerical features
   * OneHotEncoder for categorical features

2. **Classification Model**

   * Random Forest / Logistic Regression

3. **Pipeline Serialization**

   * Saved using `pickle` for deployment

---



## 🖥 Application Interface

The user needs to enter transaction details:

* Transaction Type
* Amount
* Old Balance (Sender)
* New Balance (Sender)
* Old Balance (Receiver)
* New Balance (Receiver)

After clicking **Predict**, the system displays whether the transaction is:

✅ Genuine Transaction
⚠️ Fraudulent Transaction

---

## 📈 Future Improvements

* Improve model accuracy using **advanced algorithms**
* Handle **class imbalance using SMOTE**
* Deploy using **Streamlit Cloud / AWS / Heroku**
* Add **transaction visualization dashboard**

---

## 👩‍💻 Author

**Aswathi**

---

## 📜 License

This project is open-source and available under the **MIT License**.
