class Student:
    school="AkiraChix"
    def __init__(self,name,age,school):
        self.name = name
        self.age= age
        self.school= school
        # adding attributes in an argument 
        
    def speak(self):
        return f"Hello my name is {self.name} and i am {self.age} years old. I love {self.school}"    
        #adding methods to the attributes we gave above 

        