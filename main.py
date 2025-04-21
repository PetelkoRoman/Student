class Student:
    def __init__(self, first_name, last_name, courses=None):
        """ Конструктор студента. :param first_name: Имя студента :param last_name: Фамилия студента :param courses: Список курсов, на которых студент записан """
        self.first_name = first_name
        self.last_name = last_name
        self.courses = [] if courses is None else courses

    def enroll_course(self, course):
        """ Записать студента на новый курс. :param course: Название нового курса """
        if course not in self.courses:
            self.courses.append(course)

    def drop_course(self, course):
        """ Отменить запись студента на курс. :param course: Название курса """
        if course in self.courses:
            self.courses.remove(course)

    def show_courses(self):
        """ Вернуть строку с перечисленными курсами студента. """
        return ", ".join(self.courses)


class Mentor:
    def __init__(self, first_name, last_name, courses=None):
        """ Конструктор преподавателя. :param first_name: Имя преподавателя :param last_name: Фамилия преподавателя :param courses: Курсы, которые ведёт преподаватель """
        self.first_name = first_name
        self.last_name = last_name
        self.courses = [] if courses is None else courses

    def assign_course(self, course):
        """ Назначить преподавателя на курс. :param course: Курс, на который назначается преподаватель """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """ Удалить курс из списка курсов преподавателя. :param course: Курс, который удаляется """
        if course in self.courses:
            self.courses.remove(course)


class Lecturer(Mentor):
    def lecture_on_course(self, course):
        """ Проводить лекцию по заданному курсу. :param course: Название курса """
        if course in self.courses:
            return f"{self.first_name} {self.last_name} провёл лекцию по курсу '{course}'."
        else:
            return f"{self.first_name} {self.last_name} не ведёт указанный курс."


class Reviewer(Mentor):
    def evaluate_hw(self, student_first_name, student_last_name, course, grade):
        """ Проверить домашнее задание студента и поставить оценку. :param student_first_name: Имя студента :param student_last_name: Фамилия студента :param course: Курс, по которому выполняется оценка :param grade: Оценка (строкой или числом) """
        if course in self.courses:
            return f"Преподаватель {self.first_name} {self.last_name} оценил домашнее задание студента {student_first_name} {student_last_name} по курсу '{course}'. Оценка: {grade}"
        else:
            return f"Курсом '{course}' занимается другой преподаватель."

# Тестирование классов
if __name__ == "__main__":
    # Создание объектов
    student1 = Student(first_name="Иван", last_name="Иванов")
    mentor1 = Mentor(first_name="Сергей", last_name="Семёнов")
    lecturer1 = Lecturer(first_name="Александр", last_name="Александрович")
    reviewer1 = Reviewer(first_name="Марина", last_name="Дмитриевна")

    # Присваивание курсов преподавателям
    lecturer1.assign_course("Программирование")
    reviewer1.assign_course("Алгоритмы и структуры данных")

    # Запись студента на курсы
    student1.enroll_course("Программирование")
    student1.enroll_course("Алгоритмы и структуры данных")

    # Выполнение действий
    print(lecturer1.lecture_on_course("Программирование"))
    print(reviewer1.evaluate_hw("Иван", "Иванов", "Алгоритмы и структуры данных", "Отлично!"))