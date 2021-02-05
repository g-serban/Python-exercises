def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a   # just give me whatever a is and pause the fct until the next part
        temp = a # temporary var, that is going to hold whatever a is
        a = b  # and now we modify a to it's new value
        b = temp + b  # and now we need the old a to calculate b


for x in fib(1000):
    print(x)



# generator vs a list

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a 
        a = b
        b = temp + b
    return result

# print(fib2(1000))