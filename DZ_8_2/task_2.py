# Написать класс наследник DisciplineTeacher, его классом
# родителем (базовым классом) будет класс Teacher, ему
# необходимо добавить 2 новых атрибута.
# discipline - предмет его надо перенести из класса Teacher;
# job_title - должность (например завуч, директор, учитель
# старших классов).
# Все атрибуты необходимо сделать защищенными.
# Для данных атрибутов необходимо написать геттеры (для всех)
# а для атрибута job_title также необходим еще и сеттер.
# Далее необходимо адаптировать методы класса родителя а
# именно:
# get_teacher_data
# add_mark
# remove_mark
# give_a_consultation

class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    @property
    def name(self):
        return self.__name

    @property
    def education(self):
        return self.__education

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, years):
        if years < 0:
            raise ValueError("Опыт не может быть отрицательным.")
        self.__experience = years

    def get_teacher_data(self):
        return f"Имя: {self.__name},\nОбразование: {self.__education}\nОпыт работы: {self.__experience} года"

    def add_mark(self, student_name, mark):
        return f"{self.__name} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        return f"{self.__name} удалил оценку {mark} студенту {student_name}"

    def give_a_consultation(self, class_name):
        return f"{self.__name} провел консультацию в классе {class_name}"


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def discipline(self):
        return self.__discipline

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, title):
        self.__job_title = title

    def get_teacher_data(self):
        data = super().get_teacher_data()
        return f"{data}\nПредмет: {self.__discipline}\nДолжность: {self.__job_title}"

    def add_mark(self, student_name, mark):
        return f"{self.__job_title} {self.name} по предмету {self.__discipline} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        return f"{self.__job_title} {self.name} по предмету {self.__discipline} удалил оценку {mark} студенту {student_name}"

    def give_a_consultation(self, class_name):
        return f"{self.__job_title} {self.name} провел консультацию по предмету {self.__discipline} в {class_name} классе"


teacher = DisciplineTeacher(name="Иван Иванов", education="БГПУ", experience=4, discipline="Химия",
                            job_title="Директор")
print()
print(teacher.get_teacher_data())
print()
print(teacher.add_mark("Петр Петров", 5))
print()
print(teacher.remove_mark("Василий Васильев", 3))
print()
print(teacher.give_a_consultation("9Б"))
