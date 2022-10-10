"""   - Polymorphism : using unified interface to operate on objects or different clases 
*****************************************************************************************************"""
# Polymorphic methods
# identify the output
class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()
"""output : 
Parent talking!
Child talking!
Talkative Child talking!
Parent talking!"""
#-------------------------------------------------------------------------#
# 2.a
# Define a Rectangle class
class Rectangle():
    def __init__(self,h, w):
        self.h = h
        self.w= w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self,w,w)
""" <- Square constructor that accepts one parameter w, and sets both
the h and w attributes to the value of w."""
#-------------------------------------------------------------------------#
# 2.b
""" <- in the console or the script pane, create a Square object with side length 4. Then try assigning 7 to the h attribute.
What went wrong with these classes

# option 3 :
The 4x4 Square object would no longer be a square if we assign 7 to h."""
#-------------------------------------------------------------------------#
# 2.c
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

# Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
# Define set_w to set w          
    def set_w(self,w):
      self.w = w
      
#set both attributes to w      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 
e
# Define set_h to set w to h attribute
    def set_h(self, h):
      self.h = h
      self.w = h

# Define set_w to set h wo w attribute    
    def set_w(self,w):
      self.w= w
      self.h= w 
#-------------------------------------------------------------------------#
# 2.d
""" <- How does using these setter methods violate Liskov Substitution principle?
option 2 : 

Each of the setter methods of Square change both h and w attributes, while 
setter methods of Rectangle change only one attribute at a time, so the Square 
objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant."""
#-------------------------------------------------------------------------#
"""*************************************************************************
Restricting access methods: 
   - naming conventions: 
        - start with single '_' --> "internal" , not part of public API
      > helper method that checks attr validation,  if you see an attribute with one leading underscore in someone's class - 
        don't use it! The dev trusts you with this responsibility.
        - start with couble '__' -> "private" (psudo attributes), to prevent name clashes in inherited classes
      > version attr of class & shouldnt be passed to child classes
        - __name__
      > runs whenever obj is printed
   >  Only used for built-in methods (__init__(), __repr__()) 
   - use @property to customize access:
   - Overriding __getattr__(), __Setattr__():
****************************************************************************"""
# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30  #internal attribute 
    _MAX_MONTHS = 12 #internal attribute 
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
    """map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator."""        
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):

        return self.month <= BetterDate._MAX_MONTHS and self.day <= BetterDate._MAX_DAYS

bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())
"""*************************************************************************
@Property:
     *      _salary -> "protected" attribute
     $      @property               #returns the data
            def salary(self):
               return self._salary
     $      @salary_setter          #implements validations & sets the attr(if don't add this it'd be read-only, add getter)
            def salary(self,)
     # access property : emp.salary
     # call setter : emp.salary = 6.000
****************************************************************************"""
# a
# Create a Customer class
class Customer:
    def __init__(self,name,new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError
        else :
            self._balance = new_bal #protected attr
#-------------------------------------------------------------------------#
# b
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  
    
    # Add a decorated balance() method returning _balance
    @property
    def balance(self):
        return self._balance 
#-------------------------------------------------------------------------#
# c
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance
     
    # Add a setter balance() method
    @balance.setter
    def balance(self, new_balance):
        # Validate the parameter value
        if new_balance < 0 :
            raise ValueError
        else:
            self._balance = new_balance
        
        # Print "Setter method is called"
        print("Setter method is called")
#-------------------------------------------------------------------------#
# d
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)
#-------------------------------------------------------------------------#
#Read-only properties
#a
import pandas as pd
from datetime import datetime

# LoggedDF class definition from Chapter 2
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self.created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]})

# Assign a new value to ldf's created_at attribute and print
ldf.created_at = '2035-07-13'
print(ldf.created_at)
#-------------------------------------------------------------------------#
#b
import pandas as pd
from datetime import datetime

# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    # Add a read-only property: _created_at
    @property  
    def created_at(self):
        return self._created_at 

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 
