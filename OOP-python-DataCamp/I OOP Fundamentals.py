"""
In this chapter, you'll learn what object-oriented programming (OOP) is, how it 
differs from procedural-programming, and how it can be applied. You'll then define
your own classes, and learn how to create methods, attributes, and constructors.
************************************************************************************"""
#---------------------------------------------------#
""" type() to find the class attribute 
    dir(x) list all attributes and methods
    help(x) show the documentation for the object """
#---------------------------------------------------#
#Exploring object interface
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)
#---------------------------------------------------#
""" help() or help(x) will show the documentation for the object or class x"""
#---------------------------------------------------#
#Exploring object interface

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
#help(mystery) in console
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)
#---------------------------------------------------#
# Understanding class definition
Class My_Counter:
    
  def set_count(self, n):
    self.count = n
    
mc = My_Counter()
mc.set_count(5)
mc.count += 1
print(mc.count)
#---------------------------------------------------#
#Create your first class 
#explore salary & name
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)
#---------------------------------------------------#
""" SETTER METHOD"""
#Using attributes in class definition ->
#Increase salary of emp by 1500
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)
#---------------------------------------------------#
#give raise method
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount):
        self.salary =  self.salary + amount 

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)
#---------------------------------------------------#
#month salary method
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12
    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
#---------------------------------------------------#
"""__INIT__()"""
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)     
#---------------------------------------------------#
#Add a class constructor
#condition constructor
class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

    # ...Other methods omitted for brevity ...

emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
#---------------------------------------------------#
#Add the hire_date attribute and set it to today's date
class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
#---------------------------------------------------#
#Write a class from scratch
import numpy as np
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y  

    def distance_to_origin(self):
        return np.sqrt((self.x**2)+(self.y**2))

    def reflect(self,axis):
        if axis == "x":
            self.y = - self.y
        elif axis == "y":
            self.x = - self.x
        else:
            print("ValueError: try with 'x' or 'y'")

"""trying outputs:"""
pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
"""
must return :
(-3.0,0.0)
5.0"""
#---------------------------------------------------#
