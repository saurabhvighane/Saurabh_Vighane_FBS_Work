# 4. Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.

from tkinter import *
from tkinter import messagebox

questions = [
    {
        "question": "Which language is used for Python GUI?",
        "options": ["Tkinter", "MySQL", "HTML", "NumPy"],
        "answer": "Tkinter",
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "def", "function", "create"],
        "answer": "def",
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Dictionary",
    },
]

current_question = 0
score = 0


def show_question():

    question_data = questions[current_question]

    question_label.config(text=question_data["question"])

    selected_option.set(None)

    option1.config(text=question_data["options"][0], value=question_data["options"][0])


    option2.config(text=question_data["options"][1], value=question_data["options"][1])

    option3.config(text=question_data["options"][2], value=question_data["options"][2])

    option4.config(text=question_data["options"][3], value=question_data["options"][3])


def check_answer():

    global current_question
    global score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning("Warning", "Please select an answer")
        return

    correct_answer = questions[current_question]["answer"]

    if selected == correct_answer:
        messagebox.showinfo("Correct", "Your answer is correct!")
        score += 1
    else:
        messagebox.showerror(
            "Wrong", f"Wrong answer!\nCorrect answer is: {correct_answer}"
        )

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()


def show_result():

    messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{len(questions)}")

    root.destroy()


root = Tk()

root.title("Quiz Game")
root.geometry("500x400")


Label(root, text="Python Quiz Game", font=("Arial", 18, "bold")).pack(pady=20)


question_label = Label(root, text="", font=("Arial", 14), wraplength=450)

question_label.pack(pady=20)


selected_option = StringVar()


option1 = Radiobutton(root, variable=selected_option, value="", font=("Arial", 12))

option1.pack(anchor="w", padx=50)


option2 = Radiobutton(root, variable=selected_option, value="", font=("Arial", 12))

option2.pack(anchor="w", padx=50)


option3 = Radiobutton(root, variable=selected_option, value="", font=("Arial", 12))

option3.pack(anchor="w", padx=50)


option4 = Radiobutton(root, variable=selected_option, value="", font=("Arial", 12))

option4.pack(anchor="w", padx=50)


Button(root, text="Next", command=check_answer, font=("Arial", 12)).pack(pady=25)


show_question()

root.mainloop()
