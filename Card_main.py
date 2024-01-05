class Employers:
    lst_employers = []

    def __init__(self, name, born_year, job, payment, start_year):
        self.name = name
        self.born_year = born_year
        self.job = job
        self.payment = payment
        self.start_year = start_year
        Employers.lst_employers.append(self)

    def show_all_employers(self):
        print(f'Найдено {len(self.lst_employers)} сотрудников')
        all_objects = Employers.lst_employers
        for obj in all_objects:
            print(f'''
            
            Имя: {obj.name}
            Возраст: {2023 - obj.born_year}
            Должность: {obj.job}
            Зарплата: {obj.payment}
            Лет в компании: {2023 - obj.start_year}
            
            ''')

    def show_info(self):
        print(f'''
        
            Имя: {self.name}
            Возраст: {2023 - self.born_year}
            Должность: {self.job}
            Зарплата: {self.payment}
            Лет в компании: {2023 - self.start_year}
            
        ''')


e1 = Employers('Гена', 2000, 'Админ', 20334, 2022)
e2 = Employers('аля', 1993, 'Админ2', 20334, 2012)

e1.show_info()
e1.show_all_employers()
