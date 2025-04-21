class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

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
        self.grades = {}

    def add_grade(self, course_name, grade):
        if course_name in self.courses_attached:
            if course_name not in self.grades:
                self.grades[course_name] = []
            self.grades[course_name].append(grade)
        else:
            raise ValueError(f"Ошибка! Курс '{course_name}' не закреплен за данным лектором.")

    def average_grade(self, course_name=None):
        if course_name is None:
            all_grades = sum([grade for grades_list in self.grades.values() for grade in grades_list])
            total_count = sum(len(grades) for grades in self.grades.values())
            return round(all_grades / total_count, 2) if total_count > 0 else 0
        elif course_name in self.grades and len(self.grades[course_name]) > 0:
            return round(sum(self.grades[course_name]) / len(self.grades[course_name]), 2)
        else:
            return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()


# Класс экспертов-проверяющих
class Reviewer(Mentor):
    def give_homework_grade(self, student, course_name, grade):
        if course_name in self.courses_attached:
            student.add_homework_grade(course_name, grade)
        else:
            raise ValueError(f"Ошибка! Эксперт не закреплен за курсом '{course_name}'.")

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}"


# Класс студентов
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_enrolled = set()
        self.finished_courses = set()
        self.homework_grades = {}

    def enroll_in_course(self, course_name):
        self.courses_enrolled.add(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_enrolled:
            self.courses_enrolled.remove(course_name)
            self.finished_courses.add(course_name)

    def add_homework_grade(self, course_name, grade):
        if course_name in self.courses_enrolled or course_name in self.finished_courses:
            if course_name not in self.homework_grades:
                self.homework_grades[course_name] = []
            self.homework_grades[course_name].append(grade)
        else:
            raise ValueError(f"Ошибка! Студент не зачислен на курс '{course_name}'.")

    def average_homework_grade(self, course_name=None):
        if course_name is None:
            all_grades = sum([grade for grades_list in self.homework_grades.values() for grade in grades_list])
            total_count = sum(len(grades) for grades in self.homework_grades.values())
            return round(all_grades / total_count, 2) if total_count > 0 else 0
        elif course_name in self.homework_grades and len(self.homework_grades[course_name]) > 0:
            return round(sum(self.homework_grades[course_name]) / len(self.homework_grades[course_name]), 2)
        else:
            return 0

    def __str__(self):
        current_courses = ', '.join(sorted(self.courses_enrolled))
        finished_courses = ', '.join(sorted(self.finished_courses))
        avg_grade = self.average_homework_grade()
        return (
            f"Имя: {self.name}, Фамилия: {self.surname},\n"
            f"Средняя оценка за домашние задания: {avg_grade}\n"
            f"Курсы в процессе изучения: {current_courses}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        return self.average_homework_grade() < other.average_homework_grade()

    def __le__(self, other):
        return self.average_homework_grade() <= other.average_homework_grade()

    def __gt__(self, other):
        return self.average_homework_grade() > other.average_homework_grade()

    def __ge__(self, other):
        return self.average_homework_grade() >= other.average_homework_grade()

    def __eq__(self, other):
        return self.average_homework_grade() == other.average_homework_grade()

    def __ne__(self, other):
        return self.average_homework_grade() != other.average_homework_grade()


# Демонстрация работы классов
if __name__ == "__main__":
    mentor = Mentor("Иван", "Иванов")
    lecturer = Lecturer("Андрей", "Андреев")
    reviewer = Reviewer("Ольга", "Петрова")

    # Назначили Андрея Андреева ответственным за курс "Python"
    lecturer.add_course('Python')

    # Ольга Петрова проверяет задания по курсу "Python"
    reviewer.add_course('Python')

    # Создание студентов
    student1 = Student("Максим", "Сергеевич")
    student2 = Student("Светлана", "Федорова")

    # Максим Сергеевич записывается на курс "Python"
    student1.enroll_in_course('Python')

    # Светлана Федорова тоже записалась на курс "Python"
    student2.enroll_in_course('Python')

    # Ольга Петрова ставит оценку студенту Максиму Сергеевичу за работу по курсу "Python"
    try:
        reviewer.give_homework_grade(student1, 'Python', 8)
        reviewer.give_homework_grade(student2, 'Python', 9)
    except ValueError as e:
        print(e)

    # Андрей Андреев получает оценку за лекцию по курсу "Python"
    lecturer.add_grade('Python', 9.5)

    # Вывести информацию обо всех участниках проекта
    print(reviewer)
    print(lecturer)
    print(student1)
    print(student2)

    # Сравнить двух студентов по оценкам
    if student1 > student2:
        print(f"{student1.name} лучше справляется с домашними заданиями!")
    else:
        print(f"{student2.name} лучше справляется с домашними заданиями!")

    # Сравнить двух лекторов по средним оценкам
    lecturer2 = Lecturer("Михаил", "Николаевич")
    lecturer2.add_course('Python')
    lecturer2.add_grade('Python', 9.0)
    if lecturer > lecturer2:
        print(f"{lecturer.name} читает лучшие лекции!")
    else:
        print(f"{lecturer2.name} читает лучшие лекции!")