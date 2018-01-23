from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("400x400")

score = 0

def q1():
    question = Label(root, text="В чём смысл жизни?")
    answer = Entry()
    button = Button( root, text="Go1", command=lambda: game1() )
#    question.grid(row=0)
    question.grid()
    answer.grid()
    button.grid()
    
    def game1():
        if ( (answer.get().lower() == "нет его") or (answer.get().lower() == "его нет") ):
            global score
            score=score+1
        q2()

def q2():
    question_2 = Label(root, text="Ты чё сука?")
    answer_2 = Entry()
    button_2 = Button( root, text="Go2", command=lambda: game2() )
    question_2.grid()
    answer_2.grid()
    button_2.grid()
    
    def game2():
        if answer_2.get().lower() == "да":
            global score
            score=score+1
            messagebox.showinfo("end", "molodec")
            endgame()
        else:
            messagebox.showerror("errrror", "Hui tam plaval!!!")
            endgame()
    
def endgame():
    if score == 0:
        messagebox.showerror("result", "Debil suka")
    if score == 1:
        messagebox.showerror("result", "Norm")
    if score == 2:
        messagebox.showerror("result", "You win")
    
q1()
    
root.mainloop()