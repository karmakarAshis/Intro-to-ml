course = ['History', 'Math', 'Physics', 'CompSci']

course2 =['Art', 'Ged']

# course.insert(0, course2)

# course.extend(course2)

# course.remove('Math')

# course.sort()

course_str = ' - '.join(course)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)