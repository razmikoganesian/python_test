import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# load data set

data = pd.read_csv("experience_salary.csv")

X = data[["YerasExperince"]]
Y = data[["Salary"]]

model = LinearRegression()
model.fit(X, Y)

st.title("Salary predictor based on experience")
st.write("Enter your years of experience to predict your salary:  ")

years_input = st.number_input(
    "Years of experience", min_value=0.5, max_value=60.0, step=0.1
)

if years_input:
    print(years_input)

    prediction = model.predict([[years_input]])
    predicted_salary = round(float(prediction[0][0]), 2)

    st.success(f"Estimated salary: ${predicted_salary}")

st.subheader("Regression line")

fig, ax = plt.subplots()
ax.scatter(X, Y, color="blue", label="Actual Data")
ax.plot(X, model.predict(X), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.grid(True)
fig.tight_layout()
st.pyplot(fig)
