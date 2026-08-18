import sqlite3
from datetime import datetime


class ExamTracker:
    def __init__(self):
        self.conn = sqlite3.connect('exams.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS exams (
                id INTEGER PRIMARY KEY,
                subject TEXT,
                date TEXT,
                done INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
    def add_exam(self, subject, date):
        self.c.execute('INSERT INTO exams (subject, date, done) VALUES (?, ?, ?)', (subject, date, 0))
        self.conn.commit()
    def show_exam(self):
        self.c.execute('SELECT * FROM exams')
        exams = self.c.fetchall()
        if not exams:
            print("There are no exams right now.")
            return
        else:
            for exam in exams:
                status = "✅ Done" if exam[3] == 1 else "❌ Not done"
                print(f"Id: {exam[0]} | Subject: {exam[1]} | Date: {exam[2]} | {status}")
    def delete_exam(self, exam_id):
        self.c.execute('DELETE FROM exams WHERE id = ?', (exam_id,))
        self.conn.commit()
        print(f"Exam with ID {exam_id} deleted successfully.")
    def edit_exam(self, exam_id, new_subject=None, new_date=None):
        if new_subject:
            self.c.execute('UPDATE exams SET subject = ? WHERE id = ?', (new_subject, exam_id))
        if new_date:
            self.c.execute('UPDATE exams SET date = ? WHERE id = ?', (new_date, exam_id))
        self.conn.commit()
        print(f"Exam with ID {exam_id} updated successfully.")
    def mark_exam_done(self, exam_id):
        self.c.execute('UPDATE exams SET done = 1 WHERE id = ?', (exam_id,))
        self.conn.commit()
        print(f"Exam with ID {exam_id} marked as done ✅")
    def unmark_exam_done(self, exam_id):
        self.c.execute('UPDATE exams SET done = 0 WHERE id = ?', (exam_id,))
        self.conn.commit()
        print(f"Exam with ID {exam_id} marked as not done ❌")
    def get_exam_by_id(self, exam_id):
        self.c.execute('SELECT * FROM exams WHERE id = ?', (exam_id,))
        exam = self.c.fetchone()
        return exam
    def close(self):
        self.conn.close()


def main():
    tracker = ExamTracker()

    while True:
        choice = input("1 - Add Exam, 2 - Show Exam, 3 - Delete Exam, 4 - Edit Exam, 5 - Mark Exam Done, 6 - Unmark Exam Done, 7 - Exit: ")
        if choice == "1":
            while True:
                subject = input("Enter the subject: ").strip().lower()
                if subject:
                    break
                print("Subject cannot be empty.")
            while True:
                date = input("Enter the exam date (DD.MM.YYYY): ")
                try:
                    datetime.strptime(date, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please use DD.MM.YYYY.")
            tracker.add_exam(subject, date)
            print("Exam added successfully.")
        elif choice == "2":
            tracker.show_exam()
        elif choice == "3":
            while True:
                try:
                    exam_id = int(input("Enter the ID of the exam you want to delete: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid exam ID.")
            exam = tracker.get_exam_by_id(exam_id)
            if exam:
                tracker.delete_exam(exam_id)
            else:
                print("Exam not found.")
        elif choice == "4":
            while True:
                try:
                    exam_id = int(input("Enter the ID of the exam you want to edit: "))
                except ValueError:
                    print("Invalid input. Please enter a valid exam ID.")
                    continue
                exam = tracker.get_exam_by_id(exam_id)
                if exam:
                    new_subject = input("Enter the new subject (leave blank to keep current): ").strip().lower()
                    while True:
                        new_date = input("Enter the new date (leave blank to keep current): ")
                        if new_date == "":
                            new_date = None
                            break
                        try:
                            datetime.strptime(new_date, "%d.%m.%Y")
                            break
                        except ValueError:
                            print("Invalid date format. Please use DD.MM.YYYY.")
                    if not new_subject and new_date is None:
                        print("No changes made.")
                        break
                    tracker.edit_exam(exam_id, new_subject if new_subject else None, new_date if new_date else None)
                    break
                else:
                    print("Exam not found.")
                    break   

        elif choice == "5":
            while True:
                try:
                    exam_id = int(input("Enter the ID of the exam you want to mark as done: "))
                except ValueError:
                    print("Invalid input. Please enter a valid exam ID.")
                    continue
                exam = tracker.get_exam_by_id(exam_id)
                if exam:
                    tracker.mark_exam_done(exam_id)
                    break
                else:
                    print("Exam not found.")
                    break
        elif choice == "6":
            while True:
                try:
                    exam_id = int(input("Enter the ID of the exam you want to unmark as done: "))
                except ValueError:
                    print("Invalid input. Please enter a valid exam ID.")
                    continue
                exam = tracker.get_exam_by_id(exam_id)
                if exam:
                    tracker.unmark_exam_done(exam_id)
                    break
                else:
                    print("Exam not found.")
                    break
        elif choice == "7":
            print("Bye, thanks for using the exam tracker!")
            tracker.close()
            break
        else:
            print("Wrong choice")
if __name__ == "__main__":
    main()