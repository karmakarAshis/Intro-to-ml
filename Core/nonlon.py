def outer():
    n=1

    def inner():
        global n
        n=2
        print(n)

    inner()
    print(n)

outer()
