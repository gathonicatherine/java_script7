# Given this list of students containing age and name, 
#  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"},
#   {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}],
#    write a function that greets each student and tells them the year they were born. 
#    e.g Hello Eunice, you were born in the year 2002.


class Person:
    person="details"
    def __init__(self,name,year):
        self.name=name
        self.year=year        
    def greetings(self):
        return f"Hello {self.name} you were born in {self.year}" 


# Given list x = [100,110,120,130,140,150], use list comprehension 
# to create another list containing each number in the list multiplied by 
list_x=[100,110,120,130,140,150]
for a in list_x:
    print(a*5)

    # Write a function named divisible_by_seven that; 
    # using the range function and a for loop returns a list 
    # containing all the numbers between 100 and 200 that are divisible by 7.
class Divisible:
    def __init__(self,divisible_by_seven):
        self.divisible_by_seven=divisible_by_seven
    def numbers(self):
        for numbers in self.divisible_by_seven:
            range in ("100..200")
            print(range*7)



# Create a Class Rectangle with the following Attributes and Methods
# Attributes: The class has attributes width and length that represent the two sides of a rectangle 
# Methods:
#  Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
# Add a method named perimeter which returns the perimeter (P) of the rectangle using the formula P=2(length+width)

class Rectangle:
    def __init__(self,width,length): 
        self.width=width
        self.length=length
    def area(self):
        return f"A ={self.width}*{self.length}" 
    def perimeter(self):
        return f"P=2{self.length}+{self.width}"
        


           



