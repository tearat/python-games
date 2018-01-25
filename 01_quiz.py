from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("400x400")

score = 0
pairs = {
    "В чём смысл жизни?": "его нет",
    "Ты чё самый умный?": "да"
}
questions = list(pairs.keys())
answers = list(pairs.values())

def next_question(stage):
    question = Label(root, text=questions[stage])
    answer = Entry()
    button = Button( root, text="Ответить", command=lambda: choose() )
    question.grid()
    answer.grid()
    button.grid()
    
    def choose():
        global stage
        if answer.get().lower() == answers[stage]:
            global score
            score+=1
            
        stage+=1
        if stage!=len(questions):
            next_question(stage)
        else:
            endgame()

def endgame():
    if score == 0:
        messagebox.showerror("Результат игры", "Ты дебил")
    if score == 1:
        messagebox.showerror("Результат игры", "Норм")
    if score == 2:
        messagebox.showerror("Результат игры", "А ты умён")
    
stage = 0
next_question(stage)
    
root.mainloop()