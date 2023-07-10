import tkinter
import tkinter.messagebox
import customtkinter
import datetime
import data

class Course():
    def __init__(self, indexx: int, studentIndexx:int, typee: int, subjectt: str, endScoree: float, teacherr: str, attendancess: str):
        if (studentIndexx > 0):
            self.studentIndex = studentIndexx
        if (typee == 24 or typee == 48): 
            self.type = typee
        else: del self
        if (subjectt == "Piano" or subjectt == "Guitar" or 
            subjectt == "Art" or subjectt == "Organ"):
            self.subject = subjectt
        else: del self
        self.index = indexx
        if (endScoree != 0): self.endScore = endScoree
        else: self.endScore = 0
        self.teacher = teacherr
        self.attendanceCount = 0
        if (attendancess != ""): self.attendances = attendancess
        else: self.attendances = ""
    
    #Teacher
    def changeTeacher(self, newTeacher: str):
        self.teacher = newTeacher
    
    #Score
    def changeScore(self, scoree:float):
        self.endScore = scoree

    def getTotalAttandancesOfCoure(self):
        return (len(self.attendances.split(";")) - 1)
    #Attendance
    def newAttendance(self, returndb: data.returnData):
        self.attendanceCount = self.getTotalAttandancesOfCoure()
        if (self.attendanceCount == self.type):
            return("Khóa học này đã kết thúc vào lúc " + self.endCourse())
        elif (self.attendanceCount < self.type):
            self.attendanceCount+=1
            print(1)
            dt_string = (datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
            self.attendances = self.attendances + ";" + dt_string
            returndb.maindb.addAttendances(self.index, self.attendances)
            return("Đã điểm danh buổi " + str(self.attendanceCount) + ": " + dt_string)
        return("Lỗi điểm danh");
    
    #End Course
    def endCourse(self):
        self.endTime = (datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        return self.endTime
        
class Student():
    def __init__(self, indexx: int, namee: str, phonee: str, notee: str, doneCoursee: int):
        self.index = indexx
        self.name = namee
        self.note = notee
        self.phone = phonee
        if (doneCoursee != 0): self.doneCourse = doneCoursee
        else: self.doneCourse = 0
        self.courses = []
    #course
    def addCourse(self, cindex: int, typee: int, teacherr: str, subjectt: str):        
        course = Course(cindex, self.index, typee, subjectt, 0, teacherr, "")
        self.courses.append(course)
    def delCourse(self, course: Course):
        del self.courses[course.index]
        del course 
    def getTotalCourses(self):
        return len(self.courses)
    
    #note
    def changeNote(self, notee: str):
        self.note = notee
        
class Teacher():
    def __init__(self, indexx: int, namee: str, phonee: str, checkinn:str, checkoutt:str, notee: str):
        self.index = indexx
        self.name = namee
        self.note = notee
        self.phone = phonee
        if (checkinn != ""): self.checkin = checkinn
        else: self.checkin = ""  
        if (checkoutt != ""): self.checkout = checkoutt
        else: self.checkout = ""  
    #note
    def changeNote(self, notee: str):
        self.note = notee
    def getAllAttendanceOfTeacher(self, iOo: bool):
        if (iOo):
            return (self.checkin.split(";")) 
        else: return self.checkout.split(";")
    def getTotalAttandancesOfTeacher(self, iOo: bool):
        if (iOo):
            return (len(self.checkin.split(";")) - 1)
        else: return (len(self.checkout.split(";")) - 1)
    #Attendance
    def teacherNewAttendance(self, returndb: data.returnData, iOo: bool):
        print(self.checkin, self.checkout)
        checkinatten = self.checkin.split(";")
        checkoutatten = self.checkout.split(";")
        while (len(checkinatten) > len(checkoutatten)):
            print(len(checkinatten),len(checkoutatten))
            self.checkout+=";"
            returndb.maindb.addEmptyAttendance(self.index, self.checkout)
            checkoutatten = self.checkout.split(";")
            
        dt_string = (datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        if (iOo):
            check = returndb.maindb.addTeacherAttendances(self.index, self.checkin, dt_string, checkinatten[len(checkinatten)-1], checkoutatten[len(checkoutatten)-1], 1)
            
            if (check == 1): 
                if (self.checkin==""): self.checkin = dt_string
                else: self.checkin = self.checkin + ";" + dt_string
                return("Đã check - in lúc " + dt_string)
            elif (check == 0): return("Đã quá hạn check - out")
            elif (check == 2): return("Bạn chưa check - in")
            elif (check == 3): return("Bạn đã check - in rồi")
            elif (check == 4): return("Bạn đã check - out rồi")
            else: return("Đã xảy ra lỗi")
        else:
            check = returndb.maindb.addTeacherAttendances(self.index, self.checkout, dt_string, checkinatten[len(checkinatten)-1], checkoutatten[len(checkoutatten)-1], 0)
            print("Check: ", check)
            #return("Test")
            if (check == 1): 
                if (self.checkout==""): self.checkout = dt_string
                else: self.checkout = self.checkout + ";" + dt_string
                return("Đã check - out lúc " + dt_string)
            elif (check == 0): return("Đã quá hạn check - out")
            elif (check == 2): return("Bạn chưa check - in")
            elif (check == 3): return("Bạn đã check - in rồi")
            elif (check == 4): return("Bạn đã check - out rồi")
            else: return("Đã xảy ra lỗi")
        