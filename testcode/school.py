class Classroom(object):
    def __init__(self,room_num="",students=[]):
        self.students = students
        self.room_num = room_num
    def get_JSON_dict(self):
        d = vars(self)
#        print d
        student_list = []
        for student in self.students:
#           print student
            student_list.append(vars(student))
        d['students'] = student_list
#       print d
        return d


class Student(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
