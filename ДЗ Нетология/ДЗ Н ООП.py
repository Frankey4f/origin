def avg_grade_in_course():
    avg_grade = []
    grades = [j for i in Student_1.grades for j in Student_2.grades]
    avg_grade = round((sum(grades) / len(grades)))
    return avg_grade

def avg_grade_lect():
    av_grade = []
    grades = [j for i in Lecturer_1.lect_grades for j in Lecturer_2.lect_grades]
    av_grade = round((sum(grades) / len(grades)))
    return av_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached, lect_grades):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lect_grades = {courses_attached: lect_grades}
        self.av_grade = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n{self.av_grade}'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лектор не идентифицирован'
        if self.av_grade > other.av_grade:
            return f'Средний балл {self.name} {self.surname} выше чем {other.name} {other.surname}'
        elif self.av_grade < other.av_grade:
            return f'Средний балл {other.name} {other.surname} ниже чем {self.name} {self.surname}'
        else:
            return f'Средние баллы {self.name} {self.surname} и {other.name} {other.surname} равны!'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade = {}

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_to_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: \
{", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Студент не идентифицирован'
        if self.av_grade < other.av_grade:
            return f'Средний балл {self.name} {self.surname} ниже чем {other.name} {other.surname}'
        elif self.av_grade < other.av_grade:
            return f'Средний балл {other.name} {other.surname} выше чем {self.name} {self.surname}'
        else:
            return f'Средние баллы {self.name} {self.surname} и {other.name} {other.surname} равны!'


Student_1 = Student('Ruoy', 'Eman', 'female')
Student_1.finished_courses += ['GIT']
Student_1.courses_in_progress += ['Python']
Student_1.grades = [9, 9]
Student_1.add_courses('Java')
Student_1.rate_to_lect(Lecturer, 'GIT', 9)
Student_2 = Student('Harry', 'Potter', 'male')
Student_2.finished_courses += ['GIT']
Student_2.courses_in_progress += ['Python']
Student_2.grades = [10, 10]
Student_2.add_courses('Python')
Student_2.rate_to_lect(Lecturer, 'Python', 10)

Lecturer_1 = Lecturer('Some', 'Buddy', 'Python', '9.9')
Lecturer_1.courses_attached += ['Python']
Lecturer_1.lect_grades['Python'] = [10]
Lecturer_2 = Lecturer('Some', 'Buddy', 'Python', '9.9')
Lecturer_2.courses_attached += ['GIT']
Lecturer_2.lect_grades['GIT'] = [9]

Reviewer_1 = Reviewer('Some', 'Buddy')
Reviewer_1.rate_hw(Student_1, 'Python', 9)
Reviewer_2 = Reviewer('Some', 'Buddy')
Reviewer_2.rate_hw(Student_2, 'GIT', 8)

best_student = Student('Kristina', 'Makarovna', 'female')
best_student.av_grade = avg_grade_in_course()
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

best_student.rate_to_lect(Lecturer_1, 'Python', 10)
best_student.rate_to_lect(Lecturer_1, 'Python', 9)
best_student.rate_to_lect(Lecturer_1, 'GIT', 9)
best_student.rate_to_lect(Lecturer_1,'GIT', 10)

second_student = Student('Onotole', 'Vasserman', 'male')
second_student.av_grade = avg_grade_in_course()
second_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['GIT']
second_student.finished_courses += ['Введение в программирование']

second_student.rate_to_lect(Lecturer_2, 'Python', 9)
second_student.rate_to_lect(Lecturer_2, 'Python', 10)
second_student.rate_to_lect(Lecturer_2, 'GIT', 10)
second_student.rate_to_lect(Lecturer_2, 'GIT', 9)

students = [best_student, second_student]

print(best_student < second_student)
print(Lecturer_1 > Lecturer_2)
print(best_student)
