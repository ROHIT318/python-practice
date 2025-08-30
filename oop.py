#import csv
import pandas as pd

# Declaring a class
class Employee:
    # class attribute or shared variable
    scientific_name = "Homo Sapien Sapiens"
    ## To list all the instances of an object created
    all_employees = []
    
    # creating constructor, name and skill to be str type always
    def __init__(self, name: str, skill: str, has_bike="False") -> None:
        # Do validation using assert
        assert type(name) == str, "Name should be string"
        assert type(skill) == str, "Skill should be string"
        
        # creating instance attributes and assigning value to them
        self.name = name
        self.skill = skill
        self.bike = has_bike
        
        # Store all instances in a list
        Employee.all_employees.append(self)
        
    # creating methods
    def skills_with_name(self):
        return self.skill + " " + self.name
    def display_details(self):
        print(self.name + ", " + self.skill + ", " + self.bike)
        
    # Magic method to represent the object. Mainly used by developer for logging purpose. Something that can be used to recreate the object.
    def __repr__(self):
        return "Employee(name='{self.name}', skill='{self.skill}', has_bike={self.has_bike})"

    # Magic method to also represent the object. Mainly used to be shown to user.
    def __str__(self):
        return f"{self.name}-{self.skill}-{self.bike} from class {self.__class__.__name__} by str"

    # Get data from csv, not passing any arguement cause this is supposed to read and create objects
    # No access to instance level attributes, can access or modify class-level attributes
    # Can be invoked usng class name or instance name, can be used as constructor 
    @classmethod
    def get_csv_data(cls):
        df = pd.read_csv('data.csv')
        for index, emp in df.iterrows():
            Employee(emp['name'], emp['skill'], str(emp['bike']))

    @classmethod
    def change_scientific_name(cls):
        cls.scientific_name = 'Homo Sapiens'
        print(cls.scientific_name)

    # Methods that are not dependent on a secific class or instance
    # Can not modify instance or class attributes
    # No arguement required to be passed
    @staticmethod
    def display_skill(arg):
        print(arg)

    @staticmethod
    def company_detail():
        print('PwC India is a 150 year old company')


##    def instance_method(self):
##        Employee.all_employees.append(self)
    
# Inheritance: It is the ability of a chiled class to inherit from another class. Increase code reusability by inheriting both attributes and methods.
class ChildEmployee(Employee):
    # Constructor of child class
    def __init__(self, name, skill, hobbies: list, has_bike="False"):
        # Calling parent class constructor using super keyword 
        super().__init__(name, skill, has_bike)
        ## Can also be called using parent class name
        # Employee.__init__(name, skill, has_bike)
        self.hobbies = hobbies
    
    # Magic method to represent the object
    def __repr__(self):
        return "ChildEmployee(name='{self.name}', skill='{self.skill}', hobbies='{self.hobbies}', has_bike={self.has_bike})"
    
    # Special method
    def __call__(self):
        print("Special method called using instance name only.")

    def __add__(self, childEmployee):
        return self.name + ' ' + childEmployee.name
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Getter method
    # @property
    # def has_bike_status(self):
    #     # return self.has_bike
    #     return f'Status of bike for {self.name} using getter method is {self.has_bike}'

    # # Setter method
    # @has_bike_status.setter
    # def has_bike_setter(self, status: str):
    #     self.has_bike = status
    
    
childEmp = ChildEmployee("Rohit", "C++", ['None', 'No Personal Life'], has_bike=False)
print(childEmp) # __repr__ or __str__ called
print(childEmp()) # special __call__ method called
# print(childEmp.has_bike_status)
# print(childEmp.has_bike)

childEmp_new = ChildEmployee("Amit", "C++", ['None', 'No Personal Life'], has_bike=False)
print(childEmp + childEmp_new) # Method overwriting to add two objects name in one go using __add__     .

# # Both true
# print(isinstance(childEmp, Employee))
# print(isinstance(childEmp, ChildEmployee))

# # True, False
# print(issubclass(ChildEmployee, Employee))
# print(issubclass(Employee, ChildEmployee))

# Employee.get_csv_data()

# Employee.company_detail() # PwC India is a 150 year old company
# Employee.change_scientific_name() # Homo Sapiens

# # Creating an instance 
# emp1 = Employee("Rohit Sharma", "Power Automate")
# emp1.has_masters = True
# emp1.name = "New Name"
# ##emp1.instance_method()
# print(Employee.all_employees)
# print(Employee.display_skill("Driving"))
# # emp1.display_details()
# # print(emp1.has_masters)

# emp2 = Employee("Rahul Sharma", "MR", "True")
# emp2.display_details()
# print(emp2.skills_with_name())

# Invoking assertion error
# emp3 = employee(10)
# emp3.display_details()

# Accessing class attributes
# print(emp1.scientific_name)
# print(emp2.scientific_name)

# Shpw details of both class and object attribute
# print(employee.__dict__)
# print(emp1.__dict__)

# Set value of class attribute
# emp1.scientific_name = "Human Being"
# print(emp1.scientific_name)

# emp1.name = "Rohit Sharma"
# emp1.skill = "Power Automate"
# res1 = emp1.skills_with_name(emp1.skill, emp1.name)
# print(type(res1))
# print(res1)


# emp3 = Employee("Rahul Sharma", "Self Employed")
# emp4 = Employee("Ronit Sharma", "Bussiness")
# emp5 = Employee("Amit Sharma", "Government Job")

# print(Employee.all_instances)
# print(Employee.all_instances[0].name)

# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data')
# print(df)
