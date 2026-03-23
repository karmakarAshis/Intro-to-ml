def hello_func(greeting, name='basic'):
    return "{},  {} Function".format(greeting, name)

# print(hello_func('Hi'))

course =['Math', 'physics']
info = {'name': "Ashis", 'age': 25}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info(course, info)
student_info(*course, **info)

