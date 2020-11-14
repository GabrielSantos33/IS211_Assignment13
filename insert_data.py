import sqlite3
conn = sqlite3.connect('hw13.db')
con = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXIST student(student_id INT PRIMARY KEY NOT NULL,student_first_name TEXT NOT NULL,student_last_name TEXT NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXIST quizzes(quiz_id INT PRIMARY KEY NOT NULL,quiz_subject TEXT NOT NULL,quiz_question_amount INT NOT NULL,quiz_date DATE)')
    c.execute('CREATE TABLE IF NOT EXIST score(score_id INT PRIMARY KEY NOT NULL,score_total INT NOT NULL,student_id INT,quiz_id INT)')
    
    
def insert_data():
    c.execute('INSERT INTO student (student_id, student_first_name, student_last_name) VALUES (1,"John","Smith")')
    c.execute('INSERT INTO quizzes (quiz_id, quiz_subject, quiz_question_amount, quiz_date) VALUES (1, "Python Basics", 5, "February, 5th, 2015")')
    c.execute('INSERT INTO score(score_id, score_total, student_id, quiz_id) VALUES (1,100,1,1) SELECT score.student_id, student.student_first_name FROM score INNER JOIN student ON  score.student_id = student.student_id WHERE score.student_id = 1)')



