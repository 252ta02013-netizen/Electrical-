import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("students.csv")

# Expected columns:
# study_hours, attendance, previous_marks, final_marks

X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks"
    ]
]

y = data["final_marks"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Test model
prediction = model.predict(X_test)

error = mean_absolute_error(
    y_test,
    prediction
)

print("Mean Absolute Error:", error)

# Predict new student's marks

study_hours = float(
    input("Study hours per day: ")
)

attendance = float(
    input("Attendance percentage: ")
)

previous_marks = float(
    input("Previous marks: ")
)

student = [[
    study_hours,
    attendance,
    previous_marks
]]

predicted_marks = model.predict(student)

print(
    "Predicted Final Marks:",
    round(predicted_marks[0], 2)
)
