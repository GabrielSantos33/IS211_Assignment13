INSERT INTO student (student_id, student_first_name, student_last_name) VALUES (1,"John","Smith") ;
INSERT INTO quizzes (quiz_id, quiz_subject, quiz_question_amount, quiz_date) VALUES (1, "Python Basics", 5, "February, 5th, 2015")
INSERT INTO score(score_id, score_total, student_id, quiz_id) VALUES (1,100,1,1)
SELECT score.student_id, student.student_first_name FROM score INNER JOIN student ON  score.student_id = student.student_id WHERE score.student_id = 1