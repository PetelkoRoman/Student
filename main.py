# Класс студентов
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_enrolled = set()
        self.homework_grades = {}  # Словарь для хранения оценок за задания: ключ - название курса, значение - список оценок

    def enroll_in_course(self, course_name):
        self.courses_enrolled.add(course_name)

    def add_homework_grade(self, course_name, grade):
        if course_name in self.courses_enrolled:
            if course_name not in self.homework_grades:
                self.homework_grades[course_name] = []
            self.homework_grades[course_name].append(grade)
        else:
            raise ValueError(f"Ошибка! Студент не зачислен на курс '{course_name}'.")

    def average_homework_grade(self, course_name=None):
        """ Рассчитывает средний балл по домашним заданиям. """
        if course_name is None:
            all_grades = sum([grades for grades_list in self.homework_grades.values() for grades in grades_list])
            total_count = sum(len(grades) for grades in self.homework_grades.values())
            return round(all_grades / total_count, 2) if total_count > 0 else 0
        elif course_name in self.homework_grades and len(self.homework_grades[course_name]) > 0:
            return round(sum(self.homework_grades[course_name]) / len(self.homework_grades[course_name]), 2)
        else:
            return 0

    def info(self):
        return f"{self.name} {self.surname}, курсы: {', '.join(self.courses_enrolled)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Список курсов, к которым прикреплён преподаватель

    def add_course(self, course_name):
        if course_name not in self.courses_attached:
            self.courses_attached.append(course_name)

    def remove_course(self, course_name):
        if course_name in self.courses_attached:
            self.courses_attached.remove(course_name)

    def info(self):
        return f"{self.name} {self.surname}, закрепленные курсы: {', '.join(self.courses_attached)}"


# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок: ключ - название курса, значение - список оценок

    def add_grade(self, course_name, grade):
        if course_name in self.courses_attached:
            if course_name not in self.grades:
                self.grades[course_name] = []
            self.grades[course_name].append(grade)
        else:
            raise ValueError(f"Ошибка! Курс '{course_name}' не закреплен за данным лектором.")

    def average_grade(self, course_name=None):
        """ Возвращает среднюю оценку по курсу или общую среднюю оценку по всем курсам. Если указан конкретный курс, возвращает среднее значение по этому курсу, иначе рассчитывает общее среднее по всем курсам. """
        if course_name is None:
            all_grades = sum([grades for grades_list in self.grades.values() for grades in grades_list])
            total_count = sum(len(grades) for grades in self.grades.values())
            return round(all_grades / total_count, 2) if total_count > 0 else 0
        elif course_name in self.grades and len(self.grades[course_name]) > 0:
            return round(sum(self.grades[course_name]) / len(self.grades[course_name]), 2)
        else:
            return 0


# Класс эксперта-проверяющего
class Reviewer(Mentor):
    def give_homework_grade(self, student, course_name, grade):
        """ Эксперт выставляет оценку студенту за выполненное домашнее задание. """
        if course_name in self.courses_attached:
            student.add_homework_grade(course_name, grade)
        else:
            raise ValueError(f"Ошибка! Эксперт не закреплен за курсом '{course_name}'.")




# Демонстрация работы классов
if __name__ == "__main__":
    mentor = Mentor("Иван", "Иванов")
    lecturer = Lecturer("Андрей", "Андреев")
    reviewer = Reviewer("Ольга", "Олиферова")

    # Закрепляем курсы за преподавателями
    mentor.add_course('Python')
    mentor.add_course('JavaScript')
    lecturer.add_course('Python')
    lecturer.add_course('Алгоритмы и структуры данных')
    reviewer.add_course('Python')
    reviewer.add_course('Алгоритмы и структуры данных')

    # Создаем студентов
    student1 = Student("Елена", "Петрова")
    student2 = Student("Дмитрий", "Кузнецов")

    # Записываем студентов на курсы
    student1.enroll_in_course('Python')
    student2.enroll_in_course('Алгоритмы и структуры данных')

    # Ставим оценки студентам за домашние задания
    try:
        reviewer.give_homework_grade(student1, 'Python', 9)
        reviewer.give_homework_grade(student2, 'Алгоритмы и структуры данных', 8)
    except ValueError as e:
        print(e)

    # Проверяем полученные оценки
    print(f"Средний балл Елены Петровой по курсу 'Python': {student1.average_homework_grade('Python')}")
    print(f"Средний общий балл Дмитрия Кузнецова: {student2.average_homework_grade()}")