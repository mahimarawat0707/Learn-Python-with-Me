import pandas as pd

employees = pd.read_csv("employees.csv")

print(employees.head())

print(employees.info())

print(employees.describe())

print(employees.isnull().sum())

employees = employees.drop_duplicates()

employees["Salary"] = employees["Salary"].fillna(
  employees["Salary"].mean()
)

print(employees.isnull().sum())

high_salary =[employees["Salary"]<500000]
print(high_salary)

print(
  employees[employees["City"]=="Chandigarh"]
)

print(
  employees[employees["Department"]=="IT"]
)

#Sorting
print(employees.sort_values(
  by="Salary",
  ascending= True
))

print(employees.sort_values(by="Age"))

#add new column 
employees["Tax"] = employees["Salary"]*0.10

employees["Net Salary"] = employees["Salary"] - employees["Tax"]

#Group by
summary = employees.groupby("Department")["Salary"].mean()

#unique
print(employees["Department"].unique())
print(employees["Age"].unique())

#nlargest() return the rows with the largest value
top3 = employees.nlargest(3, "Salary")
print(top3)

topage= employees.nlargest(1, "Age")
print(topage)

#nsmallest() return the rows with smallest value
lowest = employees.nsmallest(3, "Salary")
print(lowest)

#loc Select rows and columns by their labels or using conditions
print(employees.loc[2])
print(employees.loc[2, "Salary"])
print(employees.loc[1:3])

print(
  employees.loc[employees["Salary"]>55000]
)

print(
  employees.loc[:, ["Name", "Salary"]]
)

#idxmax Returns the index of the maximum value
print(employees["Salary"].idxmax())

print(
  employees.loc[
    employees["Salary"].idxmax()
  ]
)

#idxmin() returns the index of the minimum value
print(
  employees.loc[
    employees["Salary"].idxmin()
    ]
)

#plot()
import matplotlib.pyplot as plt
employees["Salary"].plot()
plt.show()

employees.plot(
  x="Name",
  y="Salary",
  kind="bar"
)
plt.show()

employees["Department"].value_counts().plot(
  kind="pie",
  autopct="%1.1f%%"
)
plt.show()

employees["Salary"].plot(
  kind="hist",
  bins=5
)
plt.show()

# employees.plot(
#   x="Age",
#   y="Salary",
#   kind="Scatter"
# )
# plt.show()

employee = pd.DataFrame({
  "Department": ["IT", "IT", "HR", "HR", "Finance"],
  "Gender": ["Male", "Female", "Male", "Female", "Female"],
  "Salary": [50000, 60000,45000,50000,70000]
})
print(employee)

pivot= pd.pivot_table(
  employee,
  values="Salary",
  index="Department",
  aggfunc="mean"
)
print(pivot)

#wide format
sales = pd.DataFrame({
  "Employee": ["Aman", "Priya"],
  "January": [1000,2000],
  "February": [1100, 1300],
  "March": [1050, 1250]
})
print(sales)

#melt() convert wide format data into long format data 
melted = pd.melt(
  sales,
  id_vars= "Employee",
  var_name="Month",
  value_name="Sales"
)
print(melted)

#merge() combine two DataFrames based on a common column
employees = pd.DataFrame({
  "EmployeeID": [1,2,3],
  "Name": ["Aman", "Priya", "Rahul"]
})

departments = pd.DataFrame({
  "EmployeesID": [1,2,3],
  "Department": ["IT", "HR", "Finance"]
})

merged = pd.merge(
  employees,
  departments,
  on="EmployeesID"
)
print(merged)

#DIFFERENT TYPE OF MERGE 
#Inner Join (Default) Return only matching records
pd.merge(employees, departments, on="EmployeeID", how="left")

#left join keeps all rows from the left dataframe
pd.merge(employees, departments, on="EmployeesID", how="left")

#right join keeps all rows from the right DatFrame
pd.merge(employees, departments, on="EmployeeID", how="right")

#full outer join keeps all rows from both dataframes
pd.merge(employees, departments, on="EmployeeID", how="outer")