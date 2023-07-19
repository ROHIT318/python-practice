from oop import Employee

class IA_employee(Employee):
    def __init__(self, name: str, skill: str, has_bike="False", project_code=None):
        super().__init__(name, skill, has_bike)
        
        self.project_code = project_code
        
    def display_project(self):
        print(f"{self.name} is deployed on project {self.project_code}")
            

iaEmp1 = IA_employee("Rohit Sharma", "Power Automate", project_code=410002841)
iaEmp1.display_project()
# iaEmp1.display_details()
##print(IA_employee.all_instances)
