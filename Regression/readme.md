# Employee Salary Analysis

## 📌 Project Overview

This project performs **data analysis and salary prediction** using an employee dataset.
The goal is to analyze employee information such as **department, experience, leaves, and overtime hours** and use **Machine Learning** to predict employee salary.

The analysis and model development are implemented in a **Jupyter Notebook**.

---

## 📂 Project Structure

```
Salary-Analysis-Project
│
├── Employees.xlsx           # Employee dataset
├── Salary analysis.ipynb    # Jupyter notebook containing analysis and model
├── salary_model.pkl         # Saved machine learning model (pickle file)
└── README.md                # Project documentation
```

---

## 📊 Dataset Description

The dataset contains employee information including:

| Column         | Description                 |
| -------------- | --------------------------- |
| No             | Employee ID                 |
| First Name     | Employee first name         |
| Last Name      | Employee last name          |
| Gender         | Employee gender             |
| Start Date     | Date the employee joined    |
| Years          | Years of experience         |
| Department     | Employee department         |
| Country        | Employee location           |
| Center         | Work center                 |
| Monthly Salary | Employee monthly salary     |
| Annual Salary  | Employee yearly salary      |
| Job Rate       | Performance or job rating   |
| Sick Leaves    | Number of sick leaves taken |
| Unpaid Leaves  | Number of unpaid leaves     |
| Overtime Hours | Extra working hours         |

---

## 🛠 Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook
* Pickle

---

## ⚙️ Machine Learning Model

The project uses **Linear Regression** to predict salary based on employee features.

Steps included:

1. Data loading using **Pandas**
2. Data preprocessing
3. Train-test split
4. Model training using **Linear Regression**
5. Model evaluation using **Mean Absolute Error**
6. Saving the trained model using **pickle**

---

## ▶️ How to Run the Project

### 1️⃣ Install required libraries

```
pip install pandas matplotlib scikit-learn
```

### 2️⃣ Open the notebook

```
jupyter notebook
```

### 3️⃣ Run the notebook

Open:

```
Salary analysis.ipynb
```

Run all cells to perform the analysis and train the model.

---

## 📈 Project Workflow

1. Load the employee dataset
2. Explore and visualize employee data
3. Select important features for prediction
4. Train the Linear Regression model
5. Evaluate model performance
6. Save the trained model

---

## 📊 Output

The model predicts **employee salary based on different features** and evaluates prediction accuracy using **Mean Absolute Error (MAE).**

---

## 👩‍💻 Author

**Aswathi**

---

## 📜 License

This project is open-source and available for learning and educational purposes.
