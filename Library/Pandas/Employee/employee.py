import pandas as pd

employees = pd.DataFrame({
  "Name": ["Aman", "PRIYA", "rahul", "Ankit", "Sneha"],
  "Email": [
    "aman@gmail.com",
    "PRIYA@gmail.com",
    "rahul@gmail.com",
    "AnKiT@gmail.com",
    "sneha@gmail.com",
  ],
  "City": [
    "New Delhi",
    "Mumbai",
    "chandigarh",
    "Jaipur",
    "pune"
  ]
})
print(employees)

#str.lower() convert every charater in a string to lowercase
employees["Email"] = employees["Email"].str.lower()
print(employees["Email"])

#str.upper() convert every character to uppercase
employees["City"] = employees["City"].str.upper()
print(employees["City"])

#str.title() capitalized the first letter of every word
employees["City"] = employees["City"].str.title()
print(employees["City"])

#str.strip() remove spaces from the beginning and end of a string
employees["Name"] = employees["Name"].str.strip()
print(employees["Name"]) #str.lstrip() remove spaces only from the left   str.rstrip() removes spaces only from the right

#str.replace() repace one string with another
employees["Email"] = employees["Email"].str.replace(
  "gmail",
  "outlook"
)
print(employees["Email"])

#str.contains() checks whether a string contains a particular word or pattern
gmail_users = employees[
  employees["Email"].str.contains("gmail")
]
print(gmail_users)

employees["Email"].str.contains(
  "gmail",
  case=False
)

#splits a string into multiple parts using a separator
employees["Email"].str.split("@")

employees["Username"] = employees[
  "Email"
  ].str.split("@").str[0]

#str.len() return the length of each string
employees["Name Length"] = employees["Name"].str.len()
print(employees)

#chaining multiple string functions
stat = employees["Name"] = (
  employees["Name"]
  .str.strip()
  .str.title()
)
employees["Email"] = (
  employees["Email"]
  .str.strip()
  .str.lower()
)
print(stat)