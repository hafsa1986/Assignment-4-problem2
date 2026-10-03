#Problem 2:  a Python program that creates a Python dictionary 

import json

# Creating a Python dictionary
student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

# Converting dictionary to JSON string
student_json = json.dumps(student)

print(student_json)
