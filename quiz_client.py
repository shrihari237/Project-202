import socket
from threading import Thread
from tkinter import *




class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title = "Login"
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300,bg="cyan")

        self.pls = Label(self.login,font="Helvetica 14 bold",justify=CENTER,text="Please login to continue!",fg ="Black",bg="lightcyan")
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)

        self.name_label  = Label(self.login,font="Helvetica 14 bold",text="Enter your username:",fg ="Black",bg="lightcyan")
        self.name_label.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entry_name = Entry(self.login,font="Helvetica 14 bold",text="")
        self.entry_name.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.4)
        self.entry_name.focus()

        self.button = Button(self.login,
                             font="Helvetica 14 bold",
                             text="CONTINUE",
                             command=lambda : self.goahead(self.entry_name.get()))
    

        self.Window.mainloop()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')

                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass

            except:
                print('An error occured')
                client.close()
                break     

    def goahead(self,name):
        self.login.destroy()
        self.name = name

        rcv = Thread(target=self.receive)
        rcv.start()
g= GUI()


# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))



# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()
        
