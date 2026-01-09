def person():
    age=int(input("Enter your age: "))
    if age<18:
        print("You are a minor.")
    elif age<60 and age >=18:
            print("You are an adult.")
    else:
            print("You are a senior citizen.")
            
            
            
            
def CheckEvenOdd():
    num=int(input("Enter a number: "))
    if num%2==0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.") 
            
def main():
    person()
    CheckEvenOdd()      
if __name__=="__main__":
    main()