'''
Создание модулей HR-системы для управления сотрудниками

Цель: Разработать систему для управления данными сотрудников с использованием
 классов Employee, HR, и HRRegistry. Задача — построить структуру, которая позволяет
 хранить, обрабатывать и отображать информацию о сотрудниках.
 '''
import json    #extra task

class Employee:
    '''
    Класс для представления сотрудника с основными полями и методами
    '''

    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self) -> str:
        '''
        Возвращает информацию о сотруднике в виде строки.
        '''
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}"

    def promote(self, new_position: str):
        '''
        Обновляет должность сотрудника.
        '''
        self.position = new_position

    def increase_salary(self, amount: float):
        '''
        Увеличивает зарплату сотрудника на указанную сумму.
        '''
        if amount > 0:
            self.salary += amount
        else:
            print("Сумма увеличения зарплаты должна быть положительной.")

    def to_dict(self) -> dict:    #extra task
        '''
        Преобразует объект Employee в словарь для удобного экспорта.
        '''
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }

# Пример использования класса
# if __name__ == "__main__":
#     emp = Employee(id=1, name="Alice Smith", position="Developer", salary=50000)
#     # print(emp.get_info())
#     emp.promote("Senior Developer")
#     emp.increase_salary(5000)

class HR:
    '''
    Класс HR представляет отдел кадров, который может выполнять действия над объектами Employee
    '''
    def __init__(self):
        self.employees = []

    def hire(self, employee: Employee): 
        '''
        Принимает объект сотрудника и сохраняет его в списке сотрудников
        '''
        if employee not in self.employees:
            self.employees.append(employee)

    def terminate(self, employee_id: int): 
        '''
        Удаляет сотрудника из списка по его ID.
        '''
        for i in self.employees:
            if i == employee_id:
                self.employees.remove(i)

    def get_employee(self, employee_id: int) -> Employee: 
        '''
        Возвращает объект сотрудника по ID
        '''
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

#Пример использования:
# if __name__ == "__main__":
#     hr = HR()
#     emp = Employee(id=2, name="Bob Brown", position="Manager", salary=70000)
#     hr.hire(emp)
#     hr.terminate(2)
    

class HRRegistry:
    '''
    Класс HRRegistry выступает как реестр сотрудников и предоставляет интерфейс 
для управления списком всех сотрудников.
    '''
    def __init__(self):
        self.hr_registries = []

    def add_hr(self,hr: HR): 
        '''
        Добавляет HR в реестр.
        '''
        if hr not in self.hr_registries:
            self.hr_registries.append(hr)
    
    def find_employee_by_name(self, name: str) -> Employee: 
        '''
        Ищет сотрудника по имени среди всех HR-отделов и возвращает объект Employee, если найден.
        '''
        for hr in self.hr_registries:
            for employee in hr.employees:
                if employee.name == name:
                    return employee
        return None
    
    def list_all_employees(self): 
        '''
        Выводит информацию о всех сотрудниках во всех отделах.
        '''
        for hr in self.hr_registries:
            for employee in hr.employees:
                print(employee.get_info())

    def generate_employee_report(self, filename: str = "employees_report.json"):    #extra task
        '''
        Генерирует отчет обо всех сотрудниках и сохраняет его в формате JSON.
        '''
        report = []
        for hr in self.hr_registries:
            for employee in hr.employees:
                report.append(employee.to_dict())
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=3)
        
        print(f"Отчет о сотрудниках сохранен в '{filename}'.")

#Пример использования:
# if __name__ == "__main__":
#     emp = Employee(id=1, name="Alice Smith", position="Developer", salary=50000)
#     #print(emp.get_info())
#     emp.promote("Senior Developer")
#     emp.increase_salary(5000)

if __name__ == "__main__":    #extra task
    registry = HRRegistry()
    hr1 = HR()
    hr2 = HR()
    
    emp1 = Employee(id=1, name="Alice Smith", position="Developer", salary=50000)
    emp2 = Employee(id=2, name="Bob Brown", position="Manager", salary=70000)
    
    hr1.hire(emp1)
    hr2.hire(emp2)
    
    registry.add_hr(hr1)
    registry.add_hr(hr2)
    
    print("Все сотрудники:")
    registry.list_all_employees()
    
    # print("\nПоиск сотрудника по имени 'Alice Smith':")
    # found_employee = registry.find_employee_by_name("Alice Smith")
    # if found_employee:
    #     print(found_employee.get_info())
    # else:
    #     print("Сотрудник не найден.")

    registry.generate_employee_report("employees_report.json")

