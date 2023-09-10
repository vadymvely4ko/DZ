ex=input("Enter expression:")
try:
    exec("r="+ex)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Expression error")
else:
    print(r)