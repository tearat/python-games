from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry('300x500')
root.title('Войти в ситсемус')
root.resizable(0, 0)

def registration():
    text = Label( text='Для входа в ситсемус зарегистрируйся!' )
    text_login = Label( text='Введи логин' )
    reg_login = Entry()
    text_pass = Label( text='Введи порол?' )
    reg_pass = Entry( show='Ы' )
    text_pass_again = Label( text='Введи порол? ещё раз' )
    reg_pass_again = Entry( show='Ы' )
    button_reg = Button( text='рег ми', command=lambda: save_user() )
    button_skip = Button( text='у меня уже есть спс', command=lambda: iHave() )
    
    text.pack()
    text_login.pack()
    reg_login.pack()
    text_pass.pack()
    reg_pass.pack()
    text_pass_again.pack()
    reg_pass_again.pack()
    button_reg.pack()
    button_skip.pack()
    
    def clear_reg():
        text.destroy()
        text_login.destroy()
        reg_login.destroy()
        text_pass.destroy()
        reg_pass.destroy()
        text_pass_again.destroy()
        reg_pass_again.destroy()
        button_reg.destroy()
        button_skip.destroy()
    
    def iHave():
        clear_reg()
        login()
    
    def save_user():
        login_pass_save = {}
        login_pass_save[reg_login.get()] = reg_pass.get()
        f = open( 'login.txt', 'wb' )
        pickle.dump( login_pass_save, f )
        f.close()
        
        clear_reg()
        login()
    
def login():
    text  = Label( text='Теперь ты можеш зайти в ситсемус' )
    text_log = Label( text='Введи наш логин' )
    enter_login = Entry()
    text_pass = Label( text='Введи порол?' )
    enter_pass = Entry( show='Ы' )
    button_ener = Button( text='войнич', command=lambda: checking() )
    
    text.pack()
    text_log.pack()
    enter_login.pack()
    text_pass.pack()
    enter_pass.pack()
    button_ener.pack()
    
    def checking():
        f = open( 'login.txt', 'rb' )
        data = pickle.load( f )
        f.close()
        
        if enter_login.get() in data:
            if enter_pass.get() == data[ enter_login.get() ]:
                messagebox.showinfo( 'scss', 'привет как дела' )
            else:
                messagebox.showerror( 'err', 'ты чё ахуед неверный порол?' )
        else:
            messagebox.showerror( 'err', 'тлогин нет' )

registration()
    
root.mainloop()