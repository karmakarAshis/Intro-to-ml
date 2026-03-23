student ={
    'name': "Ashis",
    'age' : 25,
    'course': ['Math', 'comppSci']

}

# print(student['course'])

print(student.get('as')) #return a none

print(student.get('as', 'not found')) #return 'not found'  