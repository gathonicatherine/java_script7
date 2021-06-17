class Car:
    name="BMW"
    def __init__(self,make,model,color,price):
       self.make=make
       self.model=model
       self.color=color
       self.price=price
      
    def move(self):
        return f"Hello your car make is {self.make} and the model is {self.model} in {self.color} which costs {self.price}" 