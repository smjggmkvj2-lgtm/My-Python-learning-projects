import sqlite3
class ExamTracker:
    def __init__(self):
        self.conn = sqlite3.connect('exams.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS exams (
                id INTEGER PRIMARY KEY,
                subject TEXT,
                date TEXT,
                done INTEGER
            )
        ''')
        self.conn.commit()
    def add_exam(self, subject, date):
        self.c.execute('INSERT INTO exams (subject, date) VALUES (?, ?)', (subject, date))
        self.conn.commit()
    def show_exam(self):
        self.c.execute('SELECT * FROM exams')
        exams = self.c.fetchall()
        if len(exams) == 0:
            print("There is no exams done right now")
            return
        else:
            for exam in exams:
                status = "✅ Done" if exam[3] == 1 else "❌ Not done"
                print(f"Id: {exam[0]} | Subject: {exam[1]} | Date: {exam[2]} | {status}")
    def mark_exam_done(self, subject):
        self.c.execute('SELECT * FROM exams')
        exams = self.c.fetchall()
        if len(exams) == 0:
            print("There is no exams done right now")
            return
        else:
            self.c.execute('UPDATE exams SET done = 1 WHERE subject = ?', (subject,))
            self.conn.commit()
            print(f"{subject} marked as done ✅")
tracker = ExamTracker()


while True:
    choice = input("1 - Add Exam, 2 - Show Exam, 3 - Mark Exam Done, 4 - Exit: ")
    if choice == "1":
        subject = input("Enter an Subject you want to add: ").strip().lower()
        date = input("Enter the date when did you wrote it: ")
        tracker.add_exam(subject, date)
    elif choice == "2":
        tracker.show_exam()
    elif choice == "3":
        subject = input("Enter the subject you want to mark as done: ").strip().lower()
        tracker.mark_exam_done(subject)
    elif choice == "4":
        print("Bye, thanks for using the exam tracker!")
        break
    else:
        print("Wrong choice")