def addNumbers(val_a,val_b):
    try:
        a=int(val_a)
        b=int(val_b)
        sum1=a+b 
        return str(sum1)
    except:
        return "enter Valid Inputs"

val1,val2=input().split()
print(addNumbers(val1,val2))