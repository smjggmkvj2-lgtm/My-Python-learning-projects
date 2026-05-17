class Exam:
    def __init__(self, subject, date, done=False):
        self.subject = subject
        self.date = date
        self.done = done
class ExamTracker:
    def __init__(self):
        self.exams = []
    def add_exam(self, subject, date):
        new_exam = Exam(subject, date,)
        self.exams.append(new_exam)
    def show_exam(self):
        if len(self.exams) == 0:
            print("There is no exams done right now")
            return
        else:
            for exam in self.exams:
                status = "✅ Done" if exam.done else "❌ Not done"
                print(f"Subject: {exam.subject} | Date: {exam.date} | {status}")
    def mark_exam_done(self, subject):
        if len(self.exams) == 0:
            print("There is no exams done right now")
            return
        for exam in self.exams:
            if exam.subject == subject:
                exam.done = True
                print(f"{exam.subject} marked as done ✅")
                return
        print("Subject was not found")
    def save_to_file(self):
        with open("Exams.txt" , "w") as file:
            for exam in self.exams:
                file.write(f"{exam.subject}\n")
                file.write(f"{exam.date}\n")
                file.write(f"{exam.done}\n")
                file.write(f"---\n")
    def load_from_file(self):
        try:
            with open ("Exams.txt" , "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    subject = lines[i].strip()
                    date = lines[i+1].strip()
                    done = lines[i+2].strip() == "True"
                    i += 4
                    self.add_exam(subject, date)
                    self.exams[-1].done = done
        except FileNotFoundError:
            pass
tracker = ExamTracker()
tracker.load_from_file()

while True:
    choice = input("1 - Add Exam, 2 - Show Exam, 3 - Mark Exam Done, 4 - Exit: ")
    if choice == "1":
        subject = input("Enter an Subject you want to add: ").strip().lower()
        date = input("Enter the date when did you wrote it: ")
        tracker.add_exam(subject, date)
    elif choice == "2":
        tracker.show_exam()
    elif choice == "3":
        if len(tracker.exams) == 0:
            print("There is no exams done right now")
        else:
            subject = input("Enter an Subject you want to mark as done: ").strip().lower()
            tracker.mark_exam_done(subject)
    elif choice == "4":
        print("Bye")
        tracker.save_to_file()
        break
    else:
        print("Wrong Choice")