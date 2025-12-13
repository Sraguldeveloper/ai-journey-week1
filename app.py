from typing import List

# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "cherry":
#         break
# print("Loop has ended.")

# for i in range(1,11,2):
#     print(i)

# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1
# print("While loop has ended.")


# def greet_name(name):
#     print(f"Hello,{name}!")
# greet_name("Alice")

def add_number(a,b)->int:
    return a+b
# print(add_number(19,29))

#Create Grade calculator

# 1. Define the List of Scores
student_scores = [85, 92, 78, 95, 88, 70]
# print("--- Score Analysis ---")

# # 2. Use a Loop to Print Individual Scores
# print("Individual Scores:")
# for score in student_scores:
#     print(f"- {score}")
# print("----------------------")


# 3. Function to Calculate the Sum
def calculate_sum(scores_list):
    """Calculates the sum of all scores in a list."""
    total = 0
    # Use a loop to add up all scores
    for score in scores_list:
        total += score # This is shorthand for: total = total + score
    return total


# 4. Function to Calculate the Average
def calculate_average(scores_list):
    """Calculates the average score."""
    
    # Call the sum function we just defined
    total_sum = calculate_sum(scores_list)
    
    # Get the number of items in the list (the count of students)
    count = len(scores_list)
    
    # Check to prevent division by zero if the list is empty
    if count == 0:
        return 0
    
    average = total_sum / count
    return average


# 5. Execute the Functions and Print Results

# Get the results by calling the functions
total_score = calculate_sum(student_scores)
average_score = calculate_average(student_scores)

# Print the final output
# print(f"Total points earned: {total_score}")
# print(f"Number of students: {len(student_scores)}")
# print(f"The average score is: {average_score:.2f}") # .2f formats the float to 2 decimal places

# print("--- Analysis Complete ---")


# person = {
#     "name":"Alex",
#     "age":30,
#     "city":"London",
#     "occupation":["Developer","Tutor"]
# }
# for key,value in person.items():
#     print(f"{key}:{value}")
# fileName = "myData"
# try:
#     with open(fileName,'r')as file:
#         content = file.read()

#         print("---File content")
#         print(content)
# except FileNotFoundError:
#     print(f"{fileName} is not present")
#     with open(fileName,"w") as file:
#         content = file.write("workingAswesome")

# class Dog:
#     species = "Canis familiaris"
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed = breed
#         self.is_sitting = False
#     def bark(self):
#         print(f"{self.name} say:Woof! Woof!")
#     def sit(self):
#         self.is_sitting = True
#         print(f"{self.name} is now sitting")
# fido = Dog("Fido","Golden Retriever")
# buddy = Dog("Buddy","Labrador")

# fido.bark()
# fido.sit()


# import math
# radius = 5
# area = math.pi*radius**2
# print(f"{area}Area fo the circle")

# from random import randint
# luck_number = randint(1,10)
# print(f"Your lucky number:{luck_number}")

# from  data_processor.reader import load_data
# from data_processor import cleaner

# data = load_data("input.csv")
# import calculator as cal

# addOperation = cal.Calculator(10,30)
# print(addOperation.add())

# print(type(3))
# print(type(30.43))
# print(type("Hello"))
# print(type([1,2,3]))
# print(type((1,2)))
# print(type({ "name":"Alice", "age":25}))
# print(type({1,2,3}))
# print(type(True))
# print(type(None))
# print(type(lambda x: x + 1))
# print(type(3+4j))

# radius = 9
# area = 3.14*radius**2
# print(int(area))

# def factorial(n: int) -> int:
#     """Calculate the factorial of a number."""
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

def sumOfElement(num:int)->int:
    total = 0
    finalResult=0
    for i in range(1,num+1):
        total+=i
        finalResult+=total
    return finalResult

def OddOrEven(n:int)->str:
    if(n%2==0): return "even"
    else: return "odd"
# print(OddOrEven(4))

def swapTwoNumber(a:int,b:int)->int:
    a,b=b,a
    return a,b
# print(swapTwoNumber(10,30))

def sumOfdigit(lst:List[int])->int:
    return sum(lst)
# print(sumOfdigit([12,304,23]))

def greatestOfThreeNumber(a:int,b:int,c:int)->int:
    if a>b and a>c:return a
    elif b>a and b>c: return b
    else: return b
# print(greatestOfThreeNumber(29,403,2))

def convertToUpperCase(string:str)->str:
    return string.upper();
# print(convertToUpperCase("mark"))