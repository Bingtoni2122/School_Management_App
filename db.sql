dbcursor.execute("""CREATE TABLE IF NOT EXISTS Students 
               (sID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
               name CHAR(99) NOT NULL,
               phone CHAR(11) NOT NULL,
               note TEXT NOT NULL,
               doneCourse INT NOT NULL
               ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"""
)
dbcursor.execute("""CREATE TABLE IF NOT EXISTS Courses (
       cId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       sID INT NOT NULL,
       type INT NOT NULL,
       subject CHAR(10) NOT NULL,
       endScore FLOAT NOT NULL,
       teacher CHAR(99) NOT NULL,
       attendances TEXT NOT NULL,
       FOREIGN KEY (sID) REFERENCES Students(sID)
       ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"""
)
dbcursor.execute("""CREATE TABLE IF NOT EXISTS Teachers (
       tId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       tName CHAR(50) NOT NULL,
       tPhone CHAR(12) NOT NULL,
       checkin TEXT NOT NULL,
       checkout TEXT NOT NULL,
       info TEXT NOT NULL,
       ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"""
)
