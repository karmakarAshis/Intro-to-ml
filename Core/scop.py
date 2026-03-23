def square(value):
    new_val = value ** 2
    return new_val


a = square(3)

#      LEGB
# local , enclosing, global, built in 

x = 'Gobal x'

def test():
    global x
    x='local x'
    # print(y)
    print(x)



test()
print(x)