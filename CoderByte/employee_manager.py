class Employee:

    def __init__(self, name : str, salary : int):
        # Check salary is valid 
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.base_salary = salary
        self.bonus = 0

    @property
    def role(self):
        return "Employee"
    
    def get_role(self):
        return self.role
    
    def get_total_compensation(self):
        return self.base_salary + self.bonus

class Manager(Employee):
    def __init__(self, name : str, salary : int, bonus : int = 0):
        # Check bonus is valid 
        if bonus < 0:
            raise ValueError("Bonus cannot be negative")
    
        super().__init__(name, salary)
        self.bonus = bonus
        
    @property
    def role(self):
        return "Manager"


# 1. Base Employee Tests
emp1 = Employee("Alice", 50000)
assert emp1.name == "Alice", "Error: Employee name not set correctly"
assert emp1.base_salary == 50000, "Error: Employee base_salary not set correctly"
assert emp1.get_role() == "Employee", "Error: Employee get_role() failed"
assert emp1.get_total_compensation() == 50000, "Error: Employee get_total_compensation() failed"


# 2. Manager Tests (Inheritance)
mgr1 = Manager("Bob", 80000, 20000)
assert isinstance(mgr1, Employee), "Error: Manager class does not inherit from Employee"
assert mgr1.name == "Bob", "Error: Manager name not set correctly (Check your super() call)"
assert mgr1.base_salary == 80000, "Error: Manager base_salary not set correctly"
assert mgr1.bonus == 20000, "Error: Manager bonus not set correctly"

# 3. Manager Tests (Method Overriding)
assert mgr1.get_role() == "Manager", "Error: Manager get_role() failed to override base method"
assert mgr1.get_total_compensation() == 100000, "Error: Manager get_total_compensation() failed to include bonus"

# 4. Polymorphism & Edge Cases
emp2 = Employee("Charlie", 0)
mgr2 = Manager("Diana", 0, 5000)
staff = [emp2, mgr2]

assert staff[0].get_total_compensation() == 0, "Error: Failed on Employee with 0 salary"
assert staff[1].get_total_compensation() == 5000, "Error: Failed on Manager with 0 base salary but valid bonus"

print("All tests passed! Great job.")