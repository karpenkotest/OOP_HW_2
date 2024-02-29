class EmailAlreadyExists(Exception):
    pass


class Employee:
    def __init__(self, name: str, salary_per_day: int, email: str) -> None:
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = self.save_email(email)

    def work(self) -> str:
        return 'I come to the office'

    def save_email(self, email: str) -> str:
        result = self.validate_email(email)
        if result:
            self.email = email
            with open('emails.csv', 'a') as f:
                f.write(email + ' ')
                return self.email

    def validate_email(self, email: str) -> None:
        try:
            with open('emails.csv', 'r') as f:
                content = f.read()
                word_array = content.split()
                if email in word_array:
                    raise EmailAlreadyExists
                return True
        except EmailAlreadyExists:
            return False

    def dict_my(self) -> dict:
        dict_my1 = {self.name: self.salary_per_day}
        return dict_my1

    def check_salary(self, days: int):
        salary = self.salary_per_day * days
        return salary


class Recruiter(Employee):
    def __init__(self, name: str, salary_per_day: int, email: str) -> None:
        super().__init__(name, salary_per_day, email)

    def __str__(self) -> str:
        return f'Recruiter: {self.name}'

    def work(self) -> str:
        return super().work() + f' and start to hiring'


class Developer(Employee):
    def __init__(self, name: str, salary_per_day: int, tech_stack: list, email: str):
        super().__init__(name, salary_per_day, email)
        self.tech_stack = tech_stack

    def work(self) -> str:
        return super().work() + f' and start to coding'

    def __str__(self) -> str:
        tech_stack_humanized = ', '.join(self.tech_stack)
        return f'Developer: {self.name}, {self.salary_per_day}, {tech_stack_humanized}, {self.email}'

    def compare_tech_stack(self, other) -> None:
        self_skills = set(self.tech_stack)
        other_skills = set(other.tech_stack)
        if len(self_skills) > len(other_skills):
            print(f'{self.name} has more skills')
        elif len(self_skills) < len(other_skills):
            print(f'{other.name} has more skills')
        else:
            print(f'Developers have the same number of skills')

    def adding_devs(self, other):
        name = self.name + ' ' + other.name
        added_skills = list(set(self.tech_stack + other.tech_stack))
        bigger_salary = max(self.salary_per_day, other.salary_per_day)
        email = 'some@email.com'
        return Developer(name, bigger_salary, added_skills, email)


developer1 = Developer('Yulia', 200, ['GO', 'C', 'Python'], 'yulia@gmail.com')
developer2 = Developer('Nika', 180, ['Java', 'C'], 'nika000@folia.com')
recruiter1 = Recruiter('Roman', 50, '19roma@gmail.com')

dict_common = developer1.dict_my() | developer2.dict_my() | recruiter1.dict_my()

print(developer1.work())
print(developer2.work())
print(recruiter1.work())
print(developer1)
print(developer2)
print(recruiter1)

employee_with_max_salary = max(dict_common, key=dict_common.get)
max_salary = max(dict_common.values())

print(f'The biggest salary in this company is {max_salary}')
print(f'{employee_with_max_salary} has the biggest salary.')

days = 10
print(f'Salary of {developer1.name} for {days} days is {developer1.check_salary(days)}')
print(f'Salary of {developer2.name} for {days} days is {developer2.check_salary(days)}')
print(f'Salary of {recruiter1.name} for {days} days is {recruiter1.check_salary(days)}')

developer1.compare_tech_stack(developer2)
developer3 = developer1.adding_devs(developer2)
print(developer3)
