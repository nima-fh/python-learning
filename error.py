# try:
#     x=int(input("X:"))
#     y=int(input("X:"))
#     print(x/y)
# except Exception as er:
#     print(er.__class__.__name__)
def div(x,y,z):
    try:
            s=x+y
            print(s/z)  
    except ZeroDivisionError:
        print("do not enter 0 value on z")
    except Exception as er:
        print(er.__class__.__name__)
        
div(1,0,0)
