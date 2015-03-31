import json

'''
f = open("car.json")
car = json.load(f)
print car
#print type(car)
#print car.keys()
f.close()
'''

'''
f = open('car.json')
car = json.load(f) 
f.close()
car['mycars']['color'] = "red"
f = open("car.json","w")
json.dump(car,f,indent=2)
f.close()

print json.dumps(car,indent=2)
'''

from school import *
student1 = Student(name="Jackie",grade="1")
student2 = Student(name="Alfredo",grade="1")
first_grade = Classroom(students=[student1,student2],room_num="B214")
#print vars(student1)
#print vars(student2)
#first_grade.get_JSON_dict()
print "\n"
print json.dumps(first_grade.get_JSON_dict(),indent=2)

