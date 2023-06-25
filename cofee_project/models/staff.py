from cofee_project.models.menu_item import MenuItem


class StaffInterface:
    def Order(self, menu_item: MenuItem, amount: int):
        pass


class Staff(StaffInterface):
    def __init__(self, Role: str, Salary: float, Age: int, Name: str):
        self.Role = Role
        self.Salary = Salary
        self.Age = Age
        self.Name = Name

    def Order(self, menu_item: MenuItem, amount: int):
        print("opk")
