import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set

data = pd.read_csv("experience_salary.csv")

X = data[["YerasExperince"]]
Y = data[["Salary"]]

model = LinearRegression()
model.fit(X, Y)

data["PredictedSalary"] = model.predict(X)

print("Model Coefficient (slope):", round(float(model.coef_[0][0]), 2))
print("Model Intercept (base salary):", round(float(model.intercept_[0]), 2))

plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, data["PredictedSalary"], color="red", label="Regression line")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.grid(True)
plt.tight_layout()
plt.show()
