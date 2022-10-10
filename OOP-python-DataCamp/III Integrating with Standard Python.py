"""
//// operator & method  ////         
      ==    __eq__()        2 objects of a class are compared using ==, (self and other), returns Boolean
      !=    __ne__()        
      >=    __ge__()
      <=    __le__()
      >     __gt__()
      <     __lt__() """
#----------------------------------------------------------------------------------#
class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self,number,balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
#----------------------------------------------------------------------------------#
#Checking class equality
class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and \
        (type (self) == type(other) )

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)
#----------------------------------------------------------------------------------#
""" <- when comparing a child object to a parent object
    Python always calls the child's __eq__() method ."""
#----------------------------------------------------------------------------------#
#String formatting review
my_num = 5
my_str = "Hello"

#f = ...
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str) 
print(f)
# my_num is 5, and my_str is "Hello".
#----------------------------------------------------------------------------------#
""" <- you use \"  \"  to scape quotation mark function & just for them to appear as decoration ."""
#----------------------------------------------------------------------------------#
"""Add the __str__() method to Employee that satisfies the following:

      - If emp is an Employee object with name "Amar Howard" and salary of 40000, then print(emp) outputs"""
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
        output = """
        Employee name:{name}
        Employee salary:{salary}
        """.format(name = self.name, salary = self.salary)
        return output

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
"""  output:
            Employee name:Amar Howard
            Employee salary:30000
            
            Employee name:Carolyn Ramirez
            Employee salary:35000"""
#----------------------------------------------------------------------------------#
# __repr__() String representation of objects
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        
        return "Employee(\"{name}\", {salary})".format(name = self.name, salary = self.salary)


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))
"""output:
Employee("Amar Howard", 30000)
Employee("Carolyn Ramirez", 35000)"""
#----------------------------------------------------------------------------------#
""" <- <- You should always define at least one of the string 
representation methods for your object to make sure that 
the person using your class can get important information about the object easily."""
#----------------------------------------------------------------------------------#
#Catching exceptions
# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
        try : 
            return 1/x[ind]
        except ZeroDivisionError :
            print("Cannot divide by zero!")
        except IndexError:
            print("Index out of range!")
a = [5,6,0,7]

# Works okay. returns 1/6, or 0.166666
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))
#----------------------------------------------------------------------------------#
#Catching exceptions 2 : 3/3
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    try:  
      self.salary += amount

    except amount > Employee.MAX_BONUS:
          print("The bonus amount is too high!")  
        
    except self.salary + amount <  Employee.MIN_SALARY:
          print("The salary after bonus is too low!")
#----------------------------------------------------------------------------------#
""" <- except block for a parent exception will catch child exceptions.

 <-   better to include an except block for a child exception before the block for a 
      parent exception, otherwise the child exceptions will be always be caught in the
      parent block, and the except block for the child will never be executed."""
#----------------------------------------------------------------------------------#
