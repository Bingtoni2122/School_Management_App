import mysql.connector
from mysql.connector import errorcode
import datetime

class Database():
    def __init__(self, base: mysql.connector.connection.MySQLConnection):
        self.db = base
        self.dbcursor = self.db.cursor()
        self.dbcursor.execute("SHOW TABLES")
        for tb in self.dbcursor:
            print(tb)
            
    def closeDB(self):
        self.db.close()

    def addStudentData(self, name: str, phone: str, note: str, doneCourse: int):
        sqlFormula = """INSERT INTO Students (name, phone, note, doneCourse)
                                    VALUES (%s, %s, %s, %s)"""
        newStudent = (name, phone, note, doneCourse)
        self.dbcursor.execute(sqlFormula, newStudent)
        self.db.commit()
    
    def addCourseData(self, sId: int, type: int, subject: str, endScore: float, teacher: str, attendances: str):
        sqlFormula = """INSERT INTO courses (sID, type, subject, endScore, teacher, attendances)
                                    VALUES (%s, %s, %s, %s, %s, %s)"""
        newStudent = (sId, type, subject, endScore, teacher, attendances)
        self.dbcursor.execute(sqlFormula, newStudent)
        self.db.commit()
    
    def delData(self, tablename: str, index: int):
        try: 
            if (tablename == "students"):
                sqlFormula = """DELETE FROM courses WHERE sid = %s"""
                condition = (index,)
                self.dbcursor.execute(sqlFormula, condition)
                sqlFormula = """DELETE FROM students WHERE sid = %s"""
                condition = (index,)
                self.dbcursor.execute(sqlFormula, condition)
                self.db.commit()
                return True
            elif (tablename == "teachers"):
                sqlFormula = """DELETE FROM teachers WHERE tid = %s"""
                condition = (index,)
                self.dbcursor.execute(sqlFormula, condition)
                self.db.commit()
                return True
            elif (tablename == "courses"):
                sqlFormula = """DELETE FROM courses WHERE cid = %s"""
                condition = (index,)
                self.dbcursor.execute(sqlFormula, condition)
                self.db.commit()
                return True
        except Exception as error:
            print(error)
            return False
            
    
    def changeEndScoreCourse(self, cId: int, newscore: float):
        sqlFormula = """UPDATE Courses SET endScore = %s WHERE cID = %s"""
        newContent = (newscore, cId)
        self.dbcursor.execute(sqlFormula, newContent)
        self.db.commit()
    
    def changeNote(self, sId: int, newnote: str):
        sqlFormula = """UPDATE Students SET note = %s WHERE sID = %s"""
        newContent = (newnote, sId)
        self.dbcursor.execute(sqlFormula, newContent)
        self.db.commit()
    def changeTeacherNote(self, tId: int, newnote: str):
        sqlFormula = """UPDATE Teachers SET info = %s WHERE tID = %s"""
        newContent = (newnote, tId)
        self.dbcursor.execute(sqlFormula, newContent)
        self.db.commit()
        
    def getAllStudents(self):
        sqlFormula = """SELECT * from Students"""
        self.dbcursor.execute(sqlFormula)
        return(self.dbcursor.fetchall())
        
    def getSudent(self, sId: int):
        sqlFormula = """SELECT * from Students WHERE sID = %s"""
        studentIndex = (sId,)
        self.dbcursor.execute(sqlFormula, studentIndex)
        return(self.dbcursor.fetchall())
    
    def searchStudent(self, keyword: str):
        try:
            sqlFormula = """SELECT DISTINCT* from Students WHERE sID = %s
                            OR name = %s OR phone = %s"""
            ikeyword = int(keyword)
            studentIndex = (ikeyword, keyword, keyword)
            self.dbcursor.execute(sqlFormula, studentIndex)
            return(self.dbcursor.fetchall())
        except:
            sqlFormula = """SELECT DISTINCT* from Students WHERE
                            name = %s OR phone = %s"""
            studentIndex = (keyword, keyword)
            self.dbcursor.execute(sqlFormula, studentIndex)
            return(self.dbcursor.fetchall())
    
    def getCourseOfStudent(self, sId: int):
        sqlFormula = """SELECT * from Courses WHERE sId = %s"""
        studentIndex = (sId,)
        self.dbcursor.execute(sqlFormula, studentIndex)
        return(self.dbcursor.fetchall())
    
    def addAttendances(self, cId: int, newAttendance: str):
        #sqlFormula = """SElECT attendances FROM Courses WHERE cId = %s"""
        #courseIndex = (cId,)
        #self.dbcursor.execute(sqlFormula,courseIndex)
        #result = str(self.dbcursor.fetchone()[0])
        #if (result!=""):
        #    result += ";" + newAttendance
        #else: result = newAttendance
        attendances = (newAttendance, cId)
        sqlFormula = """UPDATE Courses SET attendances = %s WHERE cId = %s"""
        self.dbcursor.execute(sqlFormula, attendances)
        self.db.commit()
    
    def addEmptyAttendance(self, tId: int, attendance: str):
        attendances = (attendance, tId)
        sqlFormula = """UPDATE Teachers SET checkout = %s WHERE tId = %s"""
        self.dbcursor.execute(sqlFormula, attendances)
        self.db.commit()
        
    def addTeacherAttendances(self, tId: int, updateAtten: str, newAttendance: str, checkinAttendance: str, checkoutAttendance: str, inOrout: bool):
        if (inOrout):
            if (updateAtten != ""): attendances = (updateAtten + ";" + newAttendance, tId)
            else: attendances = (updateAtten + newAttendance, tId)
            print("Checkin " + checkinAttendance)
            print("Checkout " + newAttendance)
            if (checkinAttendance != ""):
                checkin = datetime.datetime.strptime(checkinAttendance, '%d/%m/%Y %H:%M:%S')
                new = datetime.datetime.strptime(newAttendance, '%d/%m/%Y %H:%M:%S')
                if (new.date() == checkin.date()):
                    return(3)
            sqlFormula = """UPDATE Teachers SET checkin = %s WHERE tId = %s"""
            self.dbcursor.execute(sqlFormula, attendances)
            self.db.commit()           
            return(1)
        elif (not inOrout): 
            try:
                if (updateAtten != "" and checkoutAttendance != ""): attendances = (updateAtten + ";" + newAttendance, tId)
                else: attendances = (updateAtten + newAttendance, tId)
                checkout = datetime.datetime.strptime(newAttendance, '%d/%m/%Y %H:%M:%S')
                print("Checkin " + checkinAttendance)
                print("Checkout " + checkoutAttendance)
                print("New Attendance " + newAttendance)
                flag = 1
                if (checkinAttendance == ""): 
                    return(2)
                else: checkin = datetime.datetime.strptime(checkinAttendance, '%d/%m/%Y %H:%M:%S')
                if (checkoutAttendance != ""):
                    old = datetime.datetime.strptime(checkoutAttendance, '%d/%m/%Y %H:%M:%S')
                    if (checkout.date() == old.date()):
                        return(4)
                
                if (checkin.date() < checkout.date()): return(2)
                elif (checkin.date() != checkout.date()):
                    return(0)
                
                sqlFormula = """UPDATE Teachers SET checkout = %s WHERE tId = %s"""
                self.dbcursor.execute(sqlFormula, attendances)
                self.db.commit()
                return(flag)
            except Exception as error:
                print(error)
                 
    def addTeacherData(self, name: str, phone: str, note: str):
        sqlFormula = """INSERT INTO Teachers (tname, tphone, checkin, checkout, info)
                                    VALUES (%s, %s, %s, %s, %s)"""
        newTeacher = (name, phone, "", "", note)
        self.dbcursor.execute(sqlFormula, newTeacher)
        self.db.commit()
    def getAllTeachers(self):
        sqlFormula = """SELECT * from Teachers"""
        self.dbcursor.execute(sqlFormula)
        return(self.dbcursor.fetchall())
    def getAttendOfStudent(self, sid):
        sqlFormula = """select cid,attendances from Courses where sid = %s"""
        sId = (sid,)
        self.dbcursor.execute(sqlFormula, sId)
        return(self.dbcursor.fetchall())
    def getAttendOfTeacher(self, tid):
        sqlFormula = """select checkin,checkout from Teachers where tid = %s"""
        tId = (tid,)
        self.dbcursor.execute(sqlFormula, tId)
        return(self.dbcursor.fetchall())
class returnData():
    def __init__(self):
        check = False
        db = mysql.connector.connection.MySQLConnection
        self.maindb = mysql.connector.connection.MySQLConnection
        try:
            config = {
                'user': '<database_username>',
                'password': '<database_password>',
                'host': '127.0.0.1',
                'database': 'attendanceappdb',
                'raise_on_warnings': True,
            }  
            db = mysql.connector.connect(**config, auth_plugin='mysql_native_password')
            dbcursor = db.cursor()
            check = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        if (check):
            self.maindb = Database(db)
            db.close
            #self.maindb.addStudentData("Nguyễn B", "0903348779", "Học sinh thứ 2", 0)
            #self.maindb.addCourseData(2, 48, "Art", 0, "Cô giáo 5", "")
            #newdb.addAttendances(1, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            #newdb.changeEndScoreCourse(1, 8.9)
    
    def returnStudentsList(self):
        tuplesStudent = self.maindb.getAllStudents()
        return tuplesStudent
    def returnTeachersList(self):
        tuplesTeacher = self.maindb.getAllTeachers()
        return tuplesTeacher

    def returnCourseOfStudent(self, sId: int):
        tuplesCourse = self.maindb.getCourseOfStudent(sId)
        return tuplesCourse
    
    def returnTotalofCourse(self):
        self.maindb.dbcursor.execute("SELECT COUNT(*) FROM COURSES")
        result=self.maindb.dbcursor.fetchone()
        return(int(result[0]))
    
    def returnAllAttenOfStudent(self, sid: int):
        tuplesStudent = self.maindb.getAttendOfStudent(sid)
        return tuplesStudent
    def returnAllAttenOfTeacher(self, tid: int):
        tuplesStudent = self.maindb.getAttendOfTeacher(tid)
        return tuplesStudent
    
    def delData(self, tablename: str, index: int):
        return self.maindb.delData(tablename, index)