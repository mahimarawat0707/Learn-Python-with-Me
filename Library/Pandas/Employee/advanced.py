import pandas as pd 
employees = pd.DataFrame({ 
  "Name": [ 
    "aman", 
    "PRIYA", 
    "Rahul123", 
    "Sneha", 
    "Ankit" 
    ], 
    "Email": [ 
      "aman@gmail.com", 
      "priya@yahoo.com", 
      "rahul123@gmail.com", 
      "sneha@hotmail.com", 
      "ankit@gmail.com" 
      ], 
      "Phone": [ 
        "9876543210", 
        "9876501234", 
        "9123456789", 
        "9876123456", 
        "9988776655" 
        ] 
})
print(employees)

#str.startswith() checks whether each string starts with a given character or word
print(employees["Email"].str.startswith("aman"))

#str.endswith() checks whether a string ends with certain text
print(employees["Email"].str.endswith("gmail.com"))

#str.extract() extracts specific information from text using Regular Expressions
print(employees["Email"].str.extract(r'@(.*)'))

#str.findall() return every occurrence matching a regex pattern
codes = pd.Series([
  "EMP101",
  "EMP205",
  "ABC500"
])
print(codes.str.findall(r'\d+'))

#str.count() counts how many times a pattern appears
print(employees["Email"].str.count("a"))

#str.slice() extracts part of a string using positions
print(employees["Phone"].str.slice(0,4))

#str.capitalize() capitalizes only the first letter
print(employees["Name"].str.capitalize())

#str.swapcase() converts uppercase letters to lowercase and lowercase letters to uppercase
print(employees["Name"].str.swapcase())

#str.isalpha() checks whether every character is a letter
print(employees["Name"].str.isalpha())

#str.isnumeric() checks whether the string contains only numbers
print(employees["Phone"].str.isnumeric())

#str.isalnum() checks whether the string contains only letters and number
print(employees["Name"].str.isalnum())

#regex with str.contains() find gmail users
print(employees[
  employees["Email"].str.contains("gmail")
])

print(employees[
  employees["Email"].str.contains(r"\.com$")
])

print(employees[ 
  employees["Email"].str.contains(r"\d")
])

#regex with str.replace()
employees["Name"] = employees["Name"].str.replace(
  r"\d",
  "",
  regex = True
)
