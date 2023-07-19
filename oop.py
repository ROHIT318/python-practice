##import pandas as pd

# Declaring a class
class Employee:
    # class attribute or shared variable
    scientific_name = "Homo Sapien Sapiens"
    
    # To list all the instances of an object created
    all_instances = []
    
    # creating constructor
    # name and skill to be str type always
    def __init__(self, name: str, skill: str, has_bike="False"):
        # Do validation using assert
        assert type(name) == str, "Name should be string"
        
        # creating attributes
        self.name = name
        self.skill = skill
        self.bike = has_bike
        
        # Store all instances in a list
        Employee.all_instances.append(self)
        
    # creating methods
    def skills_with_name(self):
        return self.skill + " " + self.name
        
    def display_details(self):
        print(self.name + ", " + self.skill + ", " + self.bike)
        
    # Magic method to represent the object (maybe)
    def __repr__(self):
        return f"{self.name}-{self.skill}-{self.bike} from class {self.__class__.__name__}"
        
    # Class method to operate on class itself rather than instance; decorator
    # @classmethod
    # class create_instance(cls):
    #     pass

    # Creating read only attributes using "decorator"
##    @property
##    def 

# Creating an instance 
emp1 = Employee("Rohit Sharma", "Power Automate")
emp1.has_masters = True
emp1.name = "New Name"
emp1.display_details()
# print(emp1.has_masters)

emp2 = Employee("Rahul Sharma", "MR", "True")
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














# Timestamp: getter, setter
