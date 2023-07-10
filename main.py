import tkinter
import tkinter.messagebox
import customtkinter
import data
import classes

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("Attendance App.py")
        self.geometry(f"{1000}x{700}")

        # configure grid layout (6 x 10)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        
        # create Search entry and button
        self.searchEntry = customtkinter.CTkEntry(self, placeholder_text="Tìm tên học viên")
        self.searchEntry.grid(row=10, column=1, columnspan=5, pady = 20, padx = 10, sticky="nsew")
        
        self.main_button_1 = customtkinter.CTkButton(master=self, command = self.searchEvent, 
                                                     text = "Enter", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=10, column=6, pady = 20, padx = 10, sticky="nsew")
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=10)
        
        # create Add new Students + Courses
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = "Thêm học viên", command=self.add_NewStudent)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.teacherButton = customtkinter.CTkButton(self.sidebar_frame, text = "Điểm danh giáo viên", command=self.attendanceTeacher)
        self.teacherButton.grid(row=2, column=0, padx=20, pady=10)
        # create apperance mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        self.returnData = data.returnData()
        
        
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=1, columnspan = 6, rowspan = 9, pady=(20, 0), padx = 10, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.scrollable_frame_checkboxs = []
        
        # student list interface
        self.indexLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Mã số", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.indexLabel.grid(row=0, column=0,  sticky="nsew")
        self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Họ và tên", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.nameLabel.grid(row=0, column=1,  sticky="nsew")
        self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Số điện thoại", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.phoneLabel.grid(row=0, column=2,  sticky="nsew")
        self.attendanceLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Thông tin", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.attendanceLabel.grid(row=0, column=3, sticky="nsew")
        self.attendanceLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Xóa HV", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.attendanceLabel.grid(row=0, column=4, sticky="nsew")
        # List student
        self.studentList = []
        tuplesStudent = self.returnData.returnStudentsList()
        count = 0
        self.maxsID = 0
        for student in tuplesStudent:
            count+=1
            if (student[0]>self.maxsID):self.maxsID = student[0]
            self.studentList.append(classes.Student(student[0], student[1], student[2], student[3], student[4]))
            # Interface
            self.indexLabel = customtkinter.CTkLabel(self.scrollable_frame, text = str(self.studentList[len(self.studentList)-1].index))
            self.indexLabel.grid(row=count, column=0, sticky="nsew")
            self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame, text = self.studentList[len(self.studentList)-1].name)
            self.nameLabel.grid(row=count, column=1, sticky="nsew")
            self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame, text = self.studentList[len(self.studentList)-1].phone)
            self.phoneLabel.grid(row=count, column=2, sticky="nsew")
            self.viewButton = customtkinter.CTkButton(self.scrollable_frame, text = "View", command=lambda lId=len(self.studentList)-1:self.viewButton_event(lId), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.viewButton.grid(row=count, column=3, sticky="sew")
            self.viewButton = customtkinter.CTkButton(self.scrollable_frame, text = "Delete", command=lambda lId=len(self.studentList) - 1, rcount=count:self.deleteStudent(lId,rcount), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.viewButton.grid(row=count, column=4, sticky="sew")
            
            # Add button + Checkbox
            #self.scrollable_frame_checkboxs.append(self.attendanceCheckbox)
    def deleteStudent(self, lid, rcount):
        sid = self.studentList[lid].index
        if (self.returnData.maindb.delData("students", sid)):
            self.indexLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "")
            self.indexLabel.grid(row=rcount, column=0, sticky="nsew")
            self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "")
            self.nameLabel.grid(row=rcount, column=1, sticky="nsew")
            self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "")
            self.phoneLabel.grid(row=rcount, column=2, sticky="nsew")
            self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "")
            self.nameLabel.grid(row=rcount, column=3, sticky="nsew")
            self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "")
            self.phoneLabel.grid(row=rcount, column=4, sticky="nsew")
        
    def deleteCourse(self, cid, rcount):
        if (self.returnData.maindb.delData("courses", cid)):
            self.viewDetailCourse.cindexLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.cindexLabel.grid(row=rcount, column=0, pady =10, sticky="nsew")
            self.viewDetailCourse.typeLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.typeLabel.grid(row=rcount, column=1, pady =10, sticky="nsew")
            self.viewDetailCourse.subjectLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.subjectLabel.grid(row=rcount, column=2, pady =10, sticky="nsew")
            self.viewDetailCourse.endScoreLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.endScoreLabel.grid(row=rcount, column=3, pady =10, sticky="nsew")
            self.viewDetailCourse.teacherLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.teacherLabel.grid(row=rcount, column=4, pady =10, sticky="nsew")
            self.viewDetailCourse.endScoreLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.endScoreLabel.grid(row=rcount, column=5, pady =10, sticky="nsew")
            self.viewDetailCourse.teacherLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "", font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.teacherLabel.grid(row=rcount, column=6, pady =10, sticky="nsew")
        
    def searchEvent(self):
        if (self.searchEntry.get() != ""):
            results = self.returnData.maindb.searchStudent(self.searchEntry.get())
            count = 0
            self.scrollable_frame.search_frame = customtkinter.CTkScrollableFrame(self)
            self.scrollable_frame.search_frame.grid(row=9, column=1, columnspan = 6, rowspan = 1, pady=(20, 0), padx = 10, sticky="nsew")
            self.scrollable_frame.search_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
            for result in results:
                idcount = 0
                for student in self.studentList:
                    if int(result[0]) == student.index:
                        break
                    idcount+=1
                count+=1
                self.indexLabel = customtkinter.CTkLabel(self.scrollable_frame.search_frame, text = str(self.studentList[idcount].index))
                self.indexLabel.grid(row=count, column=0, sticky="nsew")
                self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame.search_frame, text = self.studentList[idcount].name)
                self.nameLabel.grid(row=count, column=1, sticky="nsew")
                self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame.search_frame, text = self.studentList[idcount].phone)
                self.phoneLabel.grid(row=count, column=2, sticky="nsew")
                self.noteLabel = customtkinter.CTkLabel(self.scrollable_frame.search_frame, text = self.studentList[idcount].note, wraplength=150)
                self.noteLabel.grid(row=count, column=3, sticky="nsew", columnspan = 2)
                self.viewButton = customtkinter.CTkButton(self.scrollable_frame.search_frame, text = "View", command=lambda lId=len(self.studentList)-1:self.viewButton_event(lId), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
                self.viewButton.grid(row=count, column=5, sticky="sew")
                
    def attendanceTeacher(self): 
        self.TeacherAttendance = customtkinter.CTk()
        # configure window
        self.TeacherAttendance.title("Teacher Details")
        self.TeacherAttendance.geometry(f"{900}x{700}")

        # configure grid layout (5x7)
        self.TeacherAttendance.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.TeacherAttendance.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        # configure scorllable frame
        self.TeacherAttendance.scrollable_frame = customtkinter.CTkScrollableFrame(self.TeacherAttendance)
        self.TeacherAttendance.scrollable_frame.grid(row=0, column=0, columnspan = 8, rowspan = 5, pady=(20, 0), sticky="nsew")
        self.TeacherAttendance.scrollable_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        
        self.TeacherAttendance.cindexLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Mã giáo viên", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.cindexLabel.grid(row=0, column=0, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.typeLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Tên giáo viên", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.typeLabel.grid(row=0, column=1, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.subjectLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Phone", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.subjectLabel.grid(row=0, column=2, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.endScoreLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Thông tin", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.endScoreLabel.grid(row=0, column=3, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.endScoreLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Check - in", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.endScoreLabel.grid(row=0, column=4, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.endScoreLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Check - out", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.endScoreLabel.grid(row=0, column=5, sticky="sew", padx = 5, pady= 5)
        self.TeacherAttendance.endScoreLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "Xóa GV", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.TeacherAttendance.endScoreLabel.grid(row=0, column=6, sticky="sew", padx = 5, pady= 5)
        self.teacherList = []
        tuplesTeachers = self.returnData.returnTeachersList()
        count = 0
        self.maxtID = 0
        for teacher in tuplesTeachers:
            count+=1
            if (teacher[0]>self.maxtID):self.maxtID = teacher[0]
            self.teacherList.append(classes.Teacher(teacher[0], teacher[1], teacher[2], teacher[3], teacher[4], teacher[5]))
            # Interface
            self.TeacherAttendance.indexLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = str(self.teacherList[len(self.teacherList)-1].index))
            self.TeacherAttendance.indexLabel.grid(row=count, column=0, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.nameLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = self.teacherList[len(self.teacherList)-1].name)
            self.TeacherAttendance.nameLabel.grid(row=count, column=1, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.phoneLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = self.teacherList[len(self.teacherList)-1].phone)
            self.TeacherAttendance.phoneLabel.grid(row=count, column=2, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "View", command=lambda lId=len(self.teacherList)-1:self.viewTeacherButton_event(lId), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.TeacherAttendance.viewButton.grid(row=count, column=3, sticky="sew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "Check - in", command=lambda lId=len(self.teacherList)-1, iOo = 1:self.attendanceTeacherButton_event(lId,iOo), font=customtkinter.CTkFont(size=15))
            self.TeacherAttendance.viewButton.grid(row=count, column=4, sticky="sew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "Check - out", command=lambda lId=len(self.teacherList)-1, iOo = 0:self.attendanceTeacherButton_event(lId,iOo), font=customtkinter.CTkFont(size=15))
            self.TeacherAttendance.viewButton.grid(row=count, column=5, sticky="sew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "Delete", command=lambda tId=self.teacherList[len(self.teacherList)-1].index, rcount = count:self.deleteTeacher(tId, rcount), font=customtkinter.CTkFont(size=15))
            self.TeacherAttendance.viewButton.grid(row=count, column=6, sticky="sew", padx = 5, pady= 5)        
            
        self.TeacherAttendance.addTeacherButton = customtkinter.CTkButton(self.TeacherAttendance, text = "Thêm giáo viên", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50, command = self.add_NewTeacher)
        self.TeacherAttendance.addTeacherButton.grid(row = 5, column = 5, sticky="sew", columnspan = 2, padx = 5, pady= 5)
        self.TeacherAttendance.mainloop()
    
    def deleteTeacher(self, tid, rcount):
        if (self.returnData.delData("teachers", tid)):
            self.TeacherAttendance.indexLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.indexLabel.grid(row=rcount, column=0, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.nameLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.nameLabel.grid(row=rcount, column=1, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.phoneLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.phoneLabel.grid(row=rcount, column=2, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.indexLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.indexLabel.grid(row=rcount, column=3, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.nameLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.nameLabel.grid(row=rcount, column=4, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.phoneLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.phoneLabel.grid(row=rcount, column=5, sticky="nsew", padx = 5, pady= 5)
            self.TeacherAttendance.phoneLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = "")
            self.TeacherAttendance.phoneLabel.grid(row=rcount, column=6, sticky="nsew", padx = 5, pady= 5)
    
    def viewTeacherButton_event(self, lId:int):
        self.teacherView = customtkinter.CTk()
        # configure window
        self.teacherView.title("Attendance Teacher")
        self.teacherView.geometry(f"{500}x{500}")

        # configure grid layout (6 x 10)
        self.teacherView.grid_columnconfigure((0, 1, 2), weight=1)
        self.teacherView.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.teacherView.scrollable_frame = customtkinter.CTkScrollableFrame(self.teacherView)
        self.teacherView.scrollable_frame.grid(row=0, column=0, columnspan = 3, rowspan = 3, pady=(20, 0), padx = 10, sticky="nsew")
        self.teacherView.scrollable_frame.grid_columnconfigure((0,1), weight=1)
        self.teacherView.checkinLabel = customtkinter.CTkLabel(self.teacherView.scrollable_frame, text = "Check-in")
        self.teacherView.checkinLabel.grid(column = 0, row = 0, pady = 5)
        self.teacherView.checkoutLabel = customtkinter.CTkLabel(self.teacherView.scrollable_frame, text = "Check-out")
        self.teacherView.checkoutLabel.grid(column = 1, row = 0, pady = 5)
        #attendance
        # configure scorllable frame
        tuplesAttend = self.returnData.returnAllAttenOfTeacher(self.teacherList[lId].index)
        count = 0
        countrow = 1
        for attends in tuplesAttend:
            print(attends)
            for att in attends:
                attenList = att.split(";")
                print(attenList[0])
                count+=1
                countrow = 0
                for attend in attenList:                    
                    #print(attend)
                    countrow+=1
                    if (count % 2 != 0):
                        self.teacherView.attendLabel = customtkinter.CTkLabel(self.teacherView.scrollable_frame, text = attend)
                        self.teacherView.attendLabel.grid(column = 0, row = countrow, pady = 5)
                    else:
                        self.teacherView.attendLabel = customtkinter.CTkLabel(self.teacherView.scrollable_frame, text = attend)
                        self.teacherView.attendLabel.grid(column = 1, row = countrow, pady = 5)
        
        self.teacherView.tnote = customtkinter.CTkTextbox(self.teacherView)
        self.teacherView.tnote.insert("0.0", self.teacherList[lId].note)
        self.teacherView.tnote.grid(row=3, column=0, rowspan = 2, columnspan = 3, pady=(10, 0), padx = 10, sticky="nsew")
        
        # Change note
        self.teacherView.changeNote = customtkinter.CTkButton(self.teacherView, text = "Lưu ghi chú", command=lambda lId = lId:self.changeTeacherNote_event(lId), font=customtkinter.CTkFont(size=15), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.teacherView.changeNote.grid(row=5, column=2, sticky="ne", pady = 10, padx = 5)
        
        
        self.teacherView.mainloop()
    
    def changeTeacherNote_event(self, lId: int):
        tId = self.teacherList[lId].index
        self.returnData.maindb.changeTeacherNote(tId, self.teacherView.tnote.get("0.0", "end"))
        self.teacherList[lId].note = self.teacherView.tnote.get("0.0", "end")

        pass
    
    def attendanceTeacherButton_event(self, lId: int, iOo: int):
        try: 
            if (iOo):
                time = self.teacherList[lId].teacherNewAttendance(self.returnData, 1)
                tkinter.messagebox.showinfo(message = time)
                return()
            else:
                time = self.teacherList[lId].teacherNewAttendance(self.returnData, 0)
                tkinter.messagebox.showinfo(message = time)
                return()        
        except Exception as error:
            print(error) 
            tkinter.messagebox.showinfo(message = "Điểm danh không thành công.")
        #print(time)
    
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def attendanceButton_event(self, cId: int, lId):
        time = ""
        try: 
            for course in self.studentList[lId].courses:
                if course.index == cId:
                    time = course.newAttendance(self.returnData)
                    print(time)
                    tkinter.messagebox.showinfo(message = time)
                    return()        
        except Exception as error:
            print(error); 
            tkinter.messagebox.showinfo(message = "Điểm danh không thành công.")
        #print(time)

    def addCourseButton_event(self, lId: int):
        try:
            sId = self.studentList[lId].index
            itype = int(self.typeEntry.get())
            coursesCount = self.returnData.returnTotalofCourse()
            if (lId > 0 or lId < len(self.studentList)):
                self.studentList[lId].addCourse(coursesCount, itype, self.teacherEntry.get(), self.subjectEntry.get())
                self.returnData.maindb.addCourseData(sId, self.typeEntry.get(), self.subjectEntry.get(), 0, self.teacherEntry.get(), "")
                self.addCourse.destroy()
            else:
                warning = customtkinter.CTkLabel(self.addCourse, text = "Nhập sai thông tin", fg_color= "Red")
                warning.grid(row = 2, column = 1, columnspan = 3, sticky = "sew")
                return
        except Exception as error:
            print(error)
            warning = customtkinter.CTkLabel(self.addCourse, text = "Nhập sai thông tin", fg_color= "Red")
            warning.grid(row = 2, column = 1, columnspan = 3, sticky = "sew")
            
            return
        
    def courseButton_event(self, lid: int):
        sid = self.studentList[lid].index
        self.addCourse = customtkinter.CTk()
        
        #configure window
        self.addCourse.title("Add New Course")
        self.addCourse.geometry(f"{500}x{200}")
        
        #configure grid layout (3x5)
        self.addCourse.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.addCourse.grid_rowconfigure((0,1,2,3), weight=1)
        
        # Define
        sId = tkinter.StringVar()
        teacher = tkinter.StringVar()
        type = tkinter.StringVar()
        subject = tkinter.StringVar()
        
        # Entry
        self.teacherEntry = customtkinter.CTkEntry(self.addCourse, placeholder_text="Nhập tên giáo viên")
        self.teacherEntry.grid(row=0, column=0, columnspan=5, sticky="sew")
        self.typeEntry = customtkinter.CTkComboBox(self.addCourse, values=["Chọn khóa học", "24", "48"], variable = type)
        self.typeEntry.grid(row=1, column=0, pady = 20, columnspan=2, sticky="sew")
        self.subjectEntry = customtkinter.CTkComboBox(self.addCourse, values=["Chọn môn học", "Piano", "Guitar", "Organ", "Art"], variable = subject)
        self.subjectEntry.grid(row=1, column=3, pady = 20, columnspan=2,  sticky="sew")
        
        # Enter Button
        addCourseButton = customtkinter.CTkButton(self.addCourse, text = "Enter", 
                                                  command = lambda sId = sid:self.addCourseButton_event(lid))
        addCourseButton.grid(row = 3, column = 1, columnspan = 3, pady = 20, sticky = "sew")
        
        self.addCourse.mainloop()
    
    def changeEndScore_event(self, sId:int):
        try:
            cid = int(self.viewDetailCourse.cidesEntry.get())
            endScore = float(self.viewDetailCourse.endscoreEntry.get())
            self.returnData.maindb.changeEndScoreCourse(cid, endScore)
            tuplesCourse = self.returnData.returnCourseOfStudent(sId)
            count = 0
            for course in tuplesCourse:
                count+=1 
                if (cid == course[0]):
                    break
            self.viewDetailCourse.endScoreLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(endScore), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.endScoreLabel.grid(row=count, column=3, pady = 10, sticky="nsew")
        except:
            return
    
    def changeNote_event(self, sId: int):
        self.returnData.maindb.changeNote(sId, self.viewDetailCourse.snote.get("0.0", "end"))
                
    def viewButton_event(self, lId: int):
        sId = self.studentList[lId].index
        self.viewDetailCourse = customtkinter.CTk()
        # configure window
        self.viewDetailCourse.title("Course Detail")
        self.viewDetailCourse.geometry(f"{800}x{700}")

        # configure grid layout (5x7)
        self.viewDetailCourse.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6,7), weight=1)
        self.viewDetailCourse.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        
        # configure scorllable frame
        self.viewDetailCourse.scrollable_frame_course = customtkinter.CTkScrollableFrame(self.viewDetailCourse)
        self.viewDetailCourse.scrollable_frame_course.grid(row=0, column=0, columnspan = 8, rowspan = 4, pady=(20, 0), sticky="nsew")
        self.viewDetailCourse.scrollable_frame_course.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.viewDetailCourse.scrollable_frame_course_checkboxs = []
        
        self.viewDetailCourse.cindexLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Mã khóa học", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.cindexLabel.grid(row=0, column=0, sticky="sew")
        self.viewDetailCourse.typeLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Khóa học", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.typeLabel.grid(row=0, column=1, sticky="sew")
        self.viewDetailCourse.subjectLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Môn học", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.subjectLabel.grid(row=0, column=2, sticky="sew")
        self.viewDetailCourse.endScoreLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Điểm cuối khóa", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.endScoreLabel.grid(row=0, column=3, sticky="sew")
        self.viewDetailCourse.teacherLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Giáo viên", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.teacherLabel.grid(row=0, column=4, sticky="sew")
        self.viewDetailCourse.attendanceLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Điểm danh", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.attendanceLabel.grid(row=0, column=5, sticky="sew")
        self.viewDetailCourse.attendanceLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = "Xóa khóa học", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.viewDetailCourse.attendanceLabel.grid(row=0, column=6, sticky="sew")
        
        self.attendanceList = []
        tuplesCourse = self.returnData.returnCourseOfStudent(sId)
        count = 0
        cidList = ["Chọn khóa học"]
        for course in tuplesCourse:
            count+=1
            cidList.append(str(course[0]))
            self.studentList[lId].courses.append(classes.Course(course[0], course[1], course[2], course[3], course[4], course[5],course[6]))
            self.viewDetailCourse.cindexLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(course[0]), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.cindexLabel.grid(row=count, column=0, pady =10, sticky="nsew")
            self.viewDetailCourse.typeLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(course[2]), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.typeLabel.grid(row=count, column=1, pady =10, sticky="nsew")
            self.viewDetailCourse.subjectLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(course[3]), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.subjectLabel.grid(row=count, column=2, pady =10, sticky="nsew")
            self.viewDetailCourse.endScoreLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(course[4]), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.endScoreLabel.grid(row=count, column=3, pady =10, sticky="nsew")
            self.viewDetailCourse.teacherLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_course, text = str(course[5]), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.teacherLabel.grid(row=count, column=4, pady =10, sticky="nsew")
            self.viewDetailCourse.attendanceButton = customtkinter.CTkButton(self.viewDetailCourse.scrollable_frame_course, text = "Điểm danh", command=lambda cId=int(course[0]), lId=lId:self.attendanceButton_event(cId, lId), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.attendanceButton.grid(row=count, column=5, pady =10, sticky="sew")
            self.viewDetailCourse.attendanceButton = customtkinter.CTkButton(self.viewDetailCourse.scrollable_frame_course, text = "Delete", command=lambda cid=int(course[0]), rcount = count:self.deleteCourse(cid, rcount), font=customtkinter.CTkFont(size=15))
            self.viewDetailCourse.attendanceButton.grid(row=count, column=6, pady =10, sticky="sew")
        
        self.viewDetailCourse.addCourse = customtkinter.CTkButton(self.viewDetailCourse, text = "Thêm khóa học", command=lambda lid = lId: self.courseButton_event(lid), font=customtkinter.CTkFont(size=15), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.viewDetailCourse.addCourse.grid(row=4, column=0, sticky="new", pady = 20)
        
        # change endscore
        self.viewDetailCourse.cidesEntry = customtkinter.CTkComboBox(self.viewDetailCourse, values = cidList, variable = "Chọn khóa học")
        self.viewDetailCourse.cidesEntry.grid(row = 4, column = 2, sticky="new", pady = 20)
        self.viewDetailCourse.endscoreEntry = customtkinter.CTkEntry(self.viewDetailCourse, placeholder_text="Nhập điểm cuối khóa")
        self.viewDetailCourse.endscoreEntry.grid(row = 4, column = 4, sticky="new", pady = 20)
        self.viewDetailCourse.changeScore = customtkinter.CTkButton(self.viewDetailCourse, text = "Lưu điểm", command=lambda sId = sId:self.changeScore_event(sId), font=customtkinter.CTkFont(size=15), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.viewDetailCourse.changeScore.grid(row=4, column=5, sticky="ne", pady = 20)
        
        #self.viewDetailCourse.labelNote = customtkinter.CTkLabel(master=self.viewDetailCourse, text="Ghi chú: " + self.studentList[sId-1].note, wraplength=100, justify = "left", font = ("Arial", 21))
        #self.viewDetailCourse.labelNote.grid(row=5, column=0, rowspan = 2, columnspan = 3, pady=(10, 0), padx = 10, sticky="nsew")
        
        self.viewDetailCourse.snote = customtkinter.CTkTextbox(self.viewDetailCourse)
        self.viewDetailCourse.snote.insert("0.0", self.studentList[lId].note)
        self.viewDetailCourse.snote.grid(row=5, column=0, rowspan = 2, columnspan = 3, pady=(10, 0), padx = 10, sticky="nsew")

        # change note
        self.viewDetailCourse.changeNote = customtkinter.CTkButton(self.viewDetailCourse, text = "Lưu ghi chú", command=lambda sId = sId:self.changeNote_event(sId), font=customtkinter.CTkFont(size=15), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.viewDetailCourse.changeNote.grid(row=7, column=2, sticky="ne", pady = 10)
        
        #attendance
        # configure scorllable frame
        self.viewDetailCourse.scrollable_frame_attendance = customtkinter.CTkScrollableFrame(self.viewDetailCourse)
        self.viewDetailCourse.scrollable_frame_attendance.grid(row=4, column=4, columnspan = 4, rowspan = 4, pady=(10, 0), sticky="nsew")
        self.viewDetailCourse.scrollable_frame_attendance.grid_columnconfigure((0), weight=1)
        
        tuplesAttend = self.returnData.returnAllAttenOfStudent(sId)
        count = 0
        for attends in tuplesAttend:
            print(attends)
            for att in attends:
                if (isinstance(att, int)): 
                    count+=1
                    self.viewDetailCourse.attendLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_attendance, text = "Mã khóa học: " + str(att))
                    self.viewDetailCourse.attendLabel.grid(row = count, pady = 5)
                else:
                    attenList = att.split(";")
                    print(attenList[0])
                    for attend in attenList:
                        if (attend!=""):
                            count+=1
                            #print(attend)
                            self.viewDetailCourse.attendLabel = customtkinter.CTkLabel(self.viewDetailCourse.scrollable_frame_attendance, text = attend)
                            self.viewDetailCourse.attendLabel.grid(row = count, pady = 5)
        self.viewDetailCourse.mainloop()

    def newStudent_button_event(self):
        if (self.newStudentnameEntry.get() != "" and self.newStudentphoneEntry.get() != ""):
            self.studentList.append(classes.Student(self.maxsID+1, self.newStudentnameEntry.get(), 
                                                    self.newStudentphoneEntry.get(), self.newStudentnoteEntry.get(), 0))
            self.returnData.maindb.addStudentData(self.newStudentnameEntry.get(), 
                                                  self.newStudentphoneEntry.get(), self.newStudentnoteEntry.get(), 0)
            # add new student to interface
            self.indexLabel = customtkinter.CTkLabel(self.scrollable_frame, text = str(self.studentList[len(self.studentList)-1].index))
            self.indexLabel.grid(row=len(self.studentList)-1, column=0, sticky="nsew")
            self.nameLabel = customtkinter.CTkLabel(self.scrollable_frame, text = self.studentList[len(self.studentList)-1].name)
            self.nameLabel.grid(row=len(self.studentList)-1, column=1, sticky="nsew")
            self.phoneLabel = customtkinter.CTkLabel(self.scrollable_frame, text = self.studentList[len(self.studentList)-1].phone)
            self.phoneLabel.grid(row=len(self.studentList)-1, column=2, sticky="nsew")
    
            self.viewButton = customtkinter.CTkButton(self.scrollable_frame, text = "View", command=lambda lId=len(self.studentList)-1:self.viewButton_event(lId), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.viewButton.grid(row=len(self.studentList)-1, column=3, sticky="nsew")
            self.viewButton = customtkinter.CTkButton(self.scrollable_frame, text = "Delete", command=lambda lId=len(self.studentList) - 1, rcount=len(self.studentList)-1:self.deleteStudent(lId,rcount), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.viewButton.grid(row=len(self.studentList)-1, column=4, sticky="sew")
            self.maxsID += 1
            self.addNewStudent.destroy()
        else:
            self.addNewStudent.label_noti = customtkinter.CTkLabel(self.addNewStudent, text="Vui lòng nhập đầy đủ thông tin")
            self.addNewStudent.label_noti.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="snew", columnspan = 2)
            
    def add_NewStudent(self):
        self.addNewStudent = customtkinter.CTk()
        self.addNewStudent.title("Add New Student")
        self.addNewStudent.geometry(f"{400}x{300}")
        self.addNewStudent.grid_columnconfigure((0,1,2,3),weight=1)
        self.addNewStudent.grid_rowconfigure((0,1,2,3,4), weight=1)
        
        self.addNewStudent.label = customtkinter.CTkLabel(self.addNewStudent, text = "Thêm học viên mới", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.addNewStudent.label.grid(row=0, column=1, pady = 20, sticky="sew")
        
        self.newStudentnameEntry = customtkinter.CTkEntry(self.addNewStudent, placeholder_text="Nhập tên học viên")
        self.newStudentnameEntry.grid(row=1, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.newStudentphoneEntry = customtkinter.CTkEntry(self.addNewStudent, placeholder_text="Nhập số điện thoại phụ huynh")
        self.newStudentphoneEntry.grid(row=2, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.newStudentnoteEntry = customtkinter.CTkEntry(self.addNewStudent, placeholder_text="Nhập ghi chú")
        self.newStudentnoteEntry.grid(row=3, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.addNewStudent.quit = customtkinter.CTkButton(self.addNewStudent, command=self.newStudent_button_event, text = "Thêm học viên", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.addNewStudent.quit.grid(row=4, column=2, padx=(10, 20), pady=(20, 20), sticky="nsew")
        
        self.addNewStudent.mainloop()

    def newTeacher_button_event(self):
        if (self.newTeachernameEntry.get() != "" and self.newTeacherphoneEntry.get() != ""):
            self.teacherList.append(classes.Teacher(self.maxtID+1, self.newTeachernameEntry.get(), 
                                                    self.newTeacherphoneEntry.get(), "", "", self.newTeachernoteEntry.get()))
            self.returnData.maindb.addTeacherData(self.newTeachernameEntry.get(), 
                                                  self.newTeacherphoneEntry.get(), self.newTeachernoteEntry.get())
            # add new student to interface
            self.TeacherAttendance.indexLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = str(self.teacherList[len(self.teacherList)-1].index))
            self.TeacherAttendance.indexLabel.grid(row=len(self.teacherList)-1, column=0, sticky="nsew")
            self.TeacherAttendance.nameLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = self.teacherList[len(self.teacherList)-1].name)
            self.TeacherAttendance.nameLabel.grid(row=len(self.teacherList)-1, column=1, sticky="nsew")
            self.TeacherAttendance.phoneLabel = customtkinter.CTkLabel(self.TeacherAttendance.scrollable_frame, text = self.teacherList[len(self.teacherList)-1].phone)
            self.TeacherAttendance.phoneLabel.grid(row=len(self.teacherList)-1, column=2, sticky="nsew")
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "View", command=lambda tId=len(self.teacherList):self.viewTeacherButton_event(tId), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=50)
            self.TeacherAttendance.viewButton.grid(row=len(self.teacherList)-1, column=3, sticky="sew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "Check - in", command=lambda tId=self.teacherList[len(self.teacherList)-1].index, iOo = 1:self.attendanceTeacherButton_event(tId,iOo), font=customtkinter.CTkFont(size=15))
            self.TeacherAttendance.viewButton.grid(row=len(self.teacherList)-1, column=4, sticky="sew", padx = 5, pady= 5)
            self.TeacherAttendance.viewButton = customtkinter.CTkButton(self.TeacherAttendance.scrollable_frame, text = "Check - out", command=lambda tId=self.teacherList[len(self.teacherList)-1].index, iOo = 0:self.attendanceTeacherButton_event(tId,iOo), font=customtkinter.CTkFont(size=15))
            self.TeacherAttendance.viewButton.grid(row=len(self.teacherList)-1, column=5, sticky="sew", padx = 5, pady= 5)
            self.maxtID += 1
            self.addNewTeacher.destroy()
        else:
            self.addNewTeacher.label_noti = customtkinter.CTkLabel(self.addNewTeacher, text="Vui lòng nhập đầy đủ thông tin")
            self.addNewTeacher.label_noti.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="snew", columnspan = 2)
    
    def add_NewTeacher(self):
        self.addNewTeacher = customtkinter.CTk()
        self.addNewTeacher.title("Add New Teacher")
        self.addNewTeacher.geometry(f"{400}x{300}")
        self.addNewTeacher.grid_columnconfigure((0,1,2,3),weight=1)
        self.addNewTeacher.grid_rowconfigure((0,1,2,3,4), weight=1)
        
        self.addNewTeacher.label = customtkinter.CTkLabel(self.addNewTeacher, text = "Thêm giáo viên mới", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.addNewTeacher.label.grid(row=0, column=1, pady = 20, sticky="sew")
        
        self.newTeachernameEntry = customtkinter.CTkEntry(self.addNewTeacher, placeholder_text="Nhập tên giáo viên")
        self.newTeachernameEntry.grid(row=1, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.newTeacherphoneEntry = customtkinter.CTkEntry(self.addNewTeacher, placeholder_text="Nhập số điện giáo viên")
        self.newTeacherphoneEntry.grid(row=2, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.newTeachernoteEntry = customtkinter.CTkEntry(self.addNewTeacher, placeholder_text="Nhập ghi chú")
        self.newTeachernoteEntry.grid(row=3, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="nsew")
        
        self.addNewTeacher.quit = customtkinter.CTkButton(self.addNewTeacher, command=self.newTeacher_button_event, text = "Thêm giáo viên", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.addNewTeacher.quit.grid(row=4, column=2, padx=(10, 20), pady=(20, 20), sticky="nsew")
        
        self.addNewTeacher.mainloop()

if __name__ == "__main__":
    app = mainWindow()
    app.mainloop()
    
        
        