class Student:
    s1 = 0
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Student.s1+=1
    def showcount(self):
        print ("Total students are %d" % Student.s1)
    def showstudent(self):
        print ("ID : ", self.id,  ", Name: ", self.name)




st1 = Student (1,"abc")
st2 = Student (2, "pqr")
st3 = Student (3, "xyz")


st1.showstudent()
st2.showstudent()
st3.showstudent()
print ("Total Students are %d" % Student.s1)

