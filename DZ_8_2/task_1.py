# У вас есть абстракция учитель, вам надо написать класс
# согласно этой абстракции характеристики класса:
# Поля (атрибуты) класса class Teacher:
# имя (name) в примере Иван Петров;
# образование (education) в примере БГПУ;
# опыт работы (experience) в примере 4 года;
# Все атрибуты необходимо сделать защищенными.
# Для данных атрибутов необходимо написать геттеры (для всех)
# а для атрибута опыт работы (experience) также необходим еще и
# сеттер.

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


teacher = Teacher(name="Иван Иванов", education="БГПУ", experience="4")
print()
print(teacher.get_teacher_data())
print()
print(teacher.add_mark("Петр Петров", "5"))
print()
print(teacher.remove_mark("Василий Васильев", "3"))
print()
print(teacher.give_a_consultation("9Б"))
