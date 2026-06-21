import pandas as pd 
employees = pd.DataFrame({ 
  "Employee":[ 
    "Aman", 
    "Priya", 
    "Rahul", 
    "Sneha", 
    "Ankit", 
    "Riya", 
    "Karan", 
    "Meena"
  ], 
  "Department":[ 
    "IT", 
    "HR", 
    "IT", 
    "HR", 
    "Sales", 
    "Sales", 
    "IT", 
    "HR"
  ], 
  "Salary":[ 
    50000, 
    45000, 
    60000, 
    48000, 
    55000, 
    52000, 
    65000, 
    47000 
  ] 
})
print(employees)

employees.groupby("Department")

#sum
employees.groupby("Department")["Salary"].sum()

#mean()