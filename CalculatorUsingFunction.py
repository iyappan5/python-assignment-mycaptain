def add(a,b):
    print(a+b)
def sum(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
a=int(input("enter a:"))
b=(input("enter b:"))
opr=input("enter opr:")
if opr=="+":
   print(add(a,b))
if opr=="-":
   print(sum(a,b))
if opr=="*":
   print(mul(a,b))
if opr=="/":
   print(div(a/b))
