## try, except , else and finally
try:
    x=10/0
except ZeroDivisionError:
    print("10/0 is impossible")
else:
    print("no error")

## other example
try:
    a=6
    a.lower()
except AttributeError:
    print("int value doesnt have lower() method")
else:
    print("no error")