import pandas as pd

employees = pd.DataFrame({
  "Employees": [
    "Aman",
    "Priya",
    "Rahul",
    "Sneha",
    "Ankit"
  ],

  "JoiningDate": [
    "2021-05-12", 
    "2020-11-25", 
    "2022-03-18", 
    "2023-01-08", 
    "2019-07-15"
  ],

  "LoginTime": [ 
    "2026-07-01 09:15:30", 
    "2026-07-01 10:45:12", 
    "2026-07-02 08:30:45", 
    "2026-07-03 11:20:10", 
    "2026-07-04 07:55:25" 
  ],

  "JoiningDate": [ 
    "2020-05-15", 
    "2021-11-20", 
    "2019-03-10", 
    "2023-01-08", 
    "2018-09-25" 
  ]
})

print(employees)

print(employees.dtypes)

employees["JoiningDate"] = pd.to_datetime(
  employees["JoiningDate"]
)
print(employees.dtypes)

employees["LoginTime"] = pd.to_datetime(employees["LoginTime"])
print(employees)

employees["Hour"] = employees["LoginTime"].dt.hour
print(employees)

employees["Minute"] = employees["LoginTime"].dt.minute
print(employees)

employees["Second"] = employees["LoginTime"].dt.second
print(employees)

employees["DayName"] = employees["LoginTime"].dt.day_name()
print(employees)

employees["MonthName"] = employees["LoginTime"].dt.month_name()
print(employees)

employees["Weekday"] = employees["LoginTime"].dt.weekday
print(employees)

employees["Start"] = employees["LoginTime"].dt.is_month_start
print(employees)

employees["End"] = employees["LoginTime"].dt.is_month_end
print(employees)

dates = pd.to_datetime([
  "2024-06-01",
  "2025-06-01"
])

dates.is_leap_year

#combining multiple date functions
employees["Year"] = employees["LoginTime"].dt.year 
employees["Month"] = employees["LoginTime"].dt.month 
employees["Day"] = employees["LoginTime"].dt.day 
employees["Hour"] = employees["LoginTime"].dt.hour 
employees["Minute"] = employees["LoginTime"].dt.minute 
employees["DayName"] = employees["LoginTime"].dt.day_name() 
employees["MonthName"] = employees["LoginTime"].dt.month_name()

employees["JoiningDate"] = pd.to_datetime(employees["JoiningDate"])
print(employees)

#current date and time 
today = pd.Timestamp.now()
print(today)

#current date only 
today = pd.Timestamp.today().normalize()
print(today)

#subtract two dates
today = pd.Timestamp.today()
employees["Experience"] = today - employees["JoiningDate"]
print (employees)

#timedelta represt the differnce between two dates or times

#convert timedelta into years
today = pd.Timestamp.today()
employees["ExperienceYears"] = (
  (today - employees["JoiningDate"]).dt.days / 365
)
print(employees)

#add days
employees["ProbationEnd"] = (
  employees["JoiningDate"] + 
  pd.Timedelta(days=90)
)
print(employees)

#add month
employees["OneMonthLater"] = (
  employees["JoiningDate"] +
  pd.DateOffset(months=1)
)
print(employees)

#add years
employees["ProbationEnd"] = (
  employees["JoiningDate"] + 
  pd.Timedelta(days=90)
)
print(employees)

#Add months
employees["OneMonthLater"] = (
  employees["JoiningDate"] +
  
)