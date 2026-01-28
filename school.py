class School():

    def __init__(self,name,foundation_year):
        self.students = []
        self.teachers = {}
        self.name=name
        self.foundation_year = foundation_year
        

   

    def add_new_student(self,student_name,student_class):
        student_record = {"name": student_name, "class" : student_class}
        self.students.append(student_record)

    def add_new_teacher(self,teacher_name,branch):
        self.teachers[teacher_name] = branch

    def view_student_list(self):
        for record in self.students:
            print(record["name"] , "-" , record["class"])

    def view_teacher_list(self):
        for name, branch in self.teachers.items():
            print(name, "-", branch)

        
       

okul = School("ozel", 2001)

okul.add_new_student("Ahmet", 4)

okul.view_student_list()

okul.add_new_teacher("Ayse", "Matematik")


okul.view_teacher_list()
