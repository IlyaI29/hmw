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