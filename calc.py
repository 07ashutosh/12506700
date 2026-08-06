def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x/y
if __name__ == "__main__":
    print("Select operation:")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("enter choice 1-4: ")
    
    