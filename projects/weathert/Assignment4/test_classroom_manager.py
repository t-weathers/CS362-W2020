from unittest import TestCase
import testUtility
import random
import classroom_manager

class testClassroomManager(TestCase):

    def set_upStudent(self):
        StudentTest = Student(93456,"john", "smith")
        StudentTest2 = Student(00000,"mary","jo")
        StudentTest3 = Student(01010,"benny","beaver")
        
    def testStudentProperties(self):
        set_upStudent()
        assert(type(StudentTest.id) == int)
        assert(type(StudentTest.first_name) == str)
        assert(type(StudentTest.last_name) == str)
        assert(type(StudentTest.assignments) == type([]))

    def testStudentConstructor(self):
        set_upStudent()
        assert(StudentTest.id == 93456)
        assert(StudentTest.first_name == "john")
        assert(StudentTest.last_name == "smith")
        assert(StudentTest.assignments.size() == 0)

        assert(StudentTest2.id == 00000)
        assert(StudentTest2.first_name == "mary")
        assert(StudentTest2.last_name == "jo")
        assert(StudentTest2.assignments.size() == 0)

        assert(StudentTest.id == 01010)
        assert(StudentTest.first_name == "benny")
        assert(StudentTest.last_name == "beaver")
        assert(StudentTest.assignments.size() == 0)

    def testStudentGetFullName(self):
        set_upStudent()
        assert(StudentTest.get_full_name() == "john smith")
        assert(StudentTest2.get_full_name() == "mary jo")
        assert(StudentTest3.get_full_name() == "benny beaver")

    def testStudentGetAssignments(self):
        set_upStudent()
        set_upAssignment()
        
        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)
        StudentTest.submit_assignment(AsgnTest3)

        test = [AsgnTest,AsgnTest2,AsgnTest3]

        assert(StudentTest.get_assignments().size() == test.size())
        assert(StudentTest.get_assignments()[0] == test[0])
        assert(StudentTest.get_assignments()[1] == test[1])
        assert(StudentTest.get_assignments()[2] == test[2])
        assert(StudentTest2.get_assignments() == [])


    def testStudentGetAssignment(self):
        set_upStudent()
        set_upAssignment()

        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)

        assert((StudentTest.get_assignment("asgn1")).max_score == 30.00)
        assert((StudentTest.get_assignment("asgn1")).name == "asgn1")

        assert((StudentTest.get_assignment("asgn2")).max_score == 50.00)
        assert((StudentTest.get_assignment("asgn2")).name == "asgn2")

    def testStudentGetAverage(self):

        set_upStudent()
        set_upAssignment()

        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)

        StudentTest.testStudentGetAssignment("asgn1").assign_grade(30.00)   #30/30
        StudentTest.testStudentGetAssignment("asgn2").assign_grade(45.00) #45/50

        assert(StudentTest.get_average() == 0.9375)


        StudentTest2.submit_assignment(AsgnTest)
        StudentTest2.submit_assignment(AsgnTest2)

        StudentTest2.testStudentGetAssignment("asgn1").assign_grade(10.00)   #10/30
        StudentTest2.testStudentGetAssignment("asgn2").assign_grade(00.00) #45/50

        assert(StudentTest2.get_average() == 0.125)


    def testStudentSubmit(self):
        set_upStudent()
        set_upAssignment()

        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)

        assert(StudentTest.assignments[0].name == "asgn1")
        assert(StudentTest.assignments[0].max_score == 30.00)

        assert(StudentTest.assignments[1].name == "asgn2")
        assert(StudentTest.assignments[1].max_score == 50.00)
    
    def testStudentRemoveAsgn(self):
        set_upStudent()
        set_upAssignment()

        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)

        assert(StudentTest.assignments[0].name == "asgn1")
        assert(StudentTest.assignments[0].max_score == 30.00)
        assert(StudentTest.assignments.size() == 2)

        StudentTest.remove_assignment("asgn1")
        
        assert(StudentTest.assignments[0].name != "asgn1")
        assert(StudentTest.assignments[0].max_score != 30.00)
        assert(StudentTest.assignments[0].name -= "asgn2")
        assert(StudentTest.assignments[0].max_score == 50.00)
        assert(StudentTest.assignments.size() == 1)


    def set_upAssignment(self):
        AsgnTest = Assignment("asgn1",30.00)
        AsgnTest2 = Assignment("asgn2",50.00)
        AsgnTest3 = Assignment("asgn3",70.00)

    def testAsgnProperties(self):
        set_upAssignment()
        assert(type(AsgnTest.name) == str)
        assert(type(AsgnTest.grade) == float)
        assert(type(AsgnTest.max_score) == float)


    def testAsgnConstructor(self):
        set_upAssignment()
        assert(AsgnTest.name == "asgn1")
        assert(AsgnTest.max_score == 30.00)
        assert(AsgnTest.grade == -1)

        assert(AsgnTest2.name == "asgn2")
        assert(AsgnTest2.max_score == 50.00)
        assert(AsgnTest2.grade == -1)

        assert(AsgnTest3.name == "asgn3")
        assert(AsgnTest3.max_score == 70.00)
        assert(AsgnTest3.grade == -1)


    def testAsgnAssignGrade(self):
        set_upStudent()
        set_upAssignment()

        StudentTest.submit_assignment(AsgnTest)
        StudentTest.submit_assignment(AsgnTest2)

        assert(StudentTest.assignments[0].grade == -1)
        assert(StudentTest.assignments[1].grade == -1)

        StudentTest.testStudentGetAssignment("asgn1").assign_grade(30.00)   #30/30
        StudentTest.testStudentGetAssignment("asgn2").assign_grade(45.00) #45/50

        assert(StudentTest.assignments[0].grade == 30.00)
        assert(StudentTest.assignments[1].grade == 45.00)


