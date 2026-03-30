class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'

        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Пример использования и проверка
if __name__ == "__main__":
    # Создаем студентов
    student1 = Student('Ruoy', 'Eman', 'your_gender')
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']

    student2 = Student('John', 'Doe', 'male')
    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Основы программирования']

    # Создаем лекторов
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer1.courses_attached += ['Python', 'Git']

    lecturer2 = Lecturer('Петр', 'Петров')
    lecturer2.courses_attached += ['Python', 'Java']

    # Создаем ревьюеров
    reviewer1 = Reviewer('Сергей', 'Сергеев')
    reviewer1.courses_attached += ['Python', 'Git']

    # Выставляем оценки лекторам (студенты оценивают лекторов)
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 10)
    student1.rate_lecture(lecturer1, 'Git', 8)

    student2.rate_lecture(lecturer2, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Java', 9)

    # Выставляем оценки студентам (ревьюеры оценивают студентов)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Git', 8)

    reviewer1.rate_hw(student2, 'Python', 7)
    reviewer1.rate_hw(student2, 'Java', 8)

    # Проверка __str__ методов
    print("=== Проверка __str__ ===")
    print(reviewer1)
    print()
    print(lecturer1)
    print()
    print(student1)
    print()

    # Проверка сравнения лекторов
    print("=== Сравнение лекторов ===")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
    print()

    # Проверка сравнения студентов
    print("=== Сравнение студентов ===")
    print(f"student1 > student2: {student1 > student2}")
    print(f"student1 < student2: {student1 < student2}")
    print(f"student1 == student2: {student1 == student2}")

    # Задание №4: Полевые испытания

    # Создаем по 2 экземпляра каждого класса
    print("=== Создание экземпляров ===")

    # Студенты
    student1 = Student('Ruoy', 'Eman', 'female')
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']
    student1.grades = {'Python': [9, 10, 8], 'Git': [7, 9]}

    student2 = Student('John', 'Doe', 'male')
    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Основы программирования']
    student2.grades = {'Python': [7, 8, 9], 'Java': [6, 7]}

    # Лекторы
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer1.courses_attached += ['Python', 'Git']
    lecturer1.grades = {'Python': [9, 10, 8], 'Git': [7, 9]}

    lecturer2 = Lecturer('Петр', 'Петров')
    lecturer2.courses_attached += ['Python', 'Java']
    lecturer2.grades = {'Python': [7, 8, 9], 'Java': [6, 7]}

    # Ревьюеры
    reviewer1 = Reviewer('Сергей', 'Сергеев')
    reviewer1.courses_attached += ['Python', 'Git']

    reviewer2 = Reviewer('Анна', 'Антонова')
    reviewer2.courses_attached += ['Python', 'Java']

    print("Создано 2 студента, 2 лектора, 2 ревьюера")
    print()

    # Проверка всех методов
    print("=== Проверка методов ===")

    # Метод rate_hw (ревьюер ставит оценки студенту)
    print("1. rate_hw (ревьюер оценивает студента):")
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Git', 8)
    reviewer2.rate_hw(student2, 'Python', 9)
    reviewer2.rate_hw(student2, 'Java', 7)
    print("Оценки добавлены")
    print()

    # Метод rate_lecture (студент оценивает лектора)
    print("2. rate_lecture (студент оценивает лектора):")
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Git', 8)
    student2.rate_lecture(lecturer2, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Java', 8)
    print("Оценки добавлены")
    print()

    # Метод __str__
    print("3. __str__ метод:")
    print("Студент:")
    print(student1)
    print()
    print("Лектор:")
    print(lecturer1)
    print()
    print("Ревьюер:")
    print(reviewer1)
    print()

    # Методы сравнения
    print("4. Сравнение лекторов:")
    print(f"   lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"   lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print()

    print("5. Сравнение студентов:")
    print(f"   student1 > student2: {student1 > student2}")
    print(f"   student1 < student2: {student1 < student2}")
    print()

    # Функции для подсчета средних оценок
    print("=== Функции подсчета средних оценок ===")


    def average_student_grade(students_list, course):
        """
        Подсчет средней оценки за домашние задания по всем студентам в рамках курса
        """
        all_grades = []
        for student in students_list:
            if course in student.grades:
                all_grades.extend(student.grades[course])

        if not all_grades:
            return 0

        return round(sum(all_grades) / len(all_grades), 1)


    def average_lecturer_grade(lecturers_list, course):
        """
        Подсчет средней оценки за лекции всех лекторов в рамках курса
        """
        all_grades = []
        for lecturer in lecturers_list:
            if course in lecturer.grades:
                all_grades.extend(lecturer.grades[course])

        if not all_grades:
            return 0

        return round(sum(all_grades) / len(all_grades), 1)


    # Проверка функций
    students = [student1, student2]
    lecturers = [lecturer1, lecturer2]

    print(f"Средняя оценка студентов по курсу 'Python': {average_student_grade(students, 'Python')}")
    print(f"Средняя оценка студентов по курсу 'Git': {average_student_grade(students, 'Git')}")
    print(f"Средняя оценка студентов по курсу 'Java': {average_student_grade(students, 'Java')}")
    print()

    print(f"Средняя оценка лекторов по курсу 'Python': {average_lecturer_grade(lecturers, 'Python')}")
    print(f"Средняя оценка лекторов по курсу 'Git': {average_lecturer_grade(lecturers, 'Git')}")
    print(f"Средняя оценка лекторов по курсу 'Java': {average_lecturer_grade(lecturers, 'Java')}")