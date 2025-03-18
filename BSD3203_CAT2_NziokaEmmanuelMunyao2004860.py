# BSD 3203 CAT 2 FOR 20/04860 NZIOKA EMMANUEL MUNYAO(PYTHON)
# The code of this CAT, below, was written and edited on Notepad++ v8.7.8 64 bit and tested and run on Google Colab
# All the steps are highlighted and labelled correctly
# The machine used for this CAT  supports displaying date and time in the long format however, 
#  Python code was used to display the current date and time for every question heading. The Machine name is Emmanuel-Rogger(Emmanuel Nzioka).
# In case of any problems, the author of this script can be reached through +254791971305 or 2004860@students.ac.ke
                            # Section B: Python Programming (20 Marks)
                            # Question 4: Data Manipulation with Pandas (6 Marks)
import datetime
# Get current date and time
current_datetime = datetime.datetime.now()
# Print results
print("Current Date and Time:", current_datetime)
import pandas as pd
# Create employee_data dataframe
employee_data = pd.DataFrame({
    "Name": ["John Doe", "Jane Smith", "Mike Brown", "Anna White", "Emma Davis"],
    "Department": ["HR", "IT", "Sales", "IT", "Sales"],
    "Salary": [55000, 75000, 48000, 82000, 61000],
    "Hire_Date": pd.to_datetime(["2020-06-15", "2018-03-22", "2019-10-10", "2021-01-05", "2017-07-19"])
})
# Save dataset to CSV
employee_data.to_csv("employee_data.csv", index=False)
# Load dataset from CSV
employee_data = pd.read_csv("employee_data.csv")
# Display only Name and Salary columns
print(employee_data[["Name", "Salary"]])
# Filter records where Salary is above 60000
print(employee_data[employee_data["Salary"] > 60000])
# Group data by Department and calculate the average salary per department
department_salary = employee_data.groupby("Department")["Salary"].mean().reset_index()
# Save to CSV
department_salary.to_csv("department_salary.csv", index=False)
                                        # Question 5: Data Visualization with Matplotlib / Seaborn (6 Marks)
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
# Get current date and time
current_datetime = datetime.datetime.now()
# Print results
print("Current Date and Time:", current_datetime)
# Histogram of Salary distribution
plt.figure(figsize=(8,5))
sns.histplot(employee_data["Salary"], bins=5, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
# Boxplot showing Salary by Department
plt.figure(figsize=(8,5))
sns.boxplot(x="Department", y="Salary", data=employee_data)
plt.title("Salary by Department")
plt.show()
                                            # Question 6: Machine Learning - Linear Regression (8 Marks)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
# Get current date and time
current_datetime = datetime.datetime.now()
# Print results
print("Current Date and Time:", current_datetime)
# Create house_prices dataframe
house_prices = pd.DataFrame({
    "Square_Feet": [1500, 1800, 2400, 3000, 1200],
    "Bedrooms": [3, 4, 4, 5, 2],
    "Price": [300000, 350000, 450000, 600000, 250000]
})
# Save dataset to CSV
house_prices.to_csv("house_prices.csv", index=False)
# Load dataset from CSV
house_prices = pd.read_csv("house_prices.csv")
# Define features and target variable
X = house_prices[["Square_Feet", "Bedrooms"]]
y = house_prices["Price"]
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Display model coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
# Predict the price of a house with 2000 square feet and 3 bedrooms
predicted_price = model.predict([[2000, 3]])
print("Predicted price for a 2000 sq ft, 3-bedroom house:", predicted_price[0])