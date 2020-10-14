"""for server side. Part of scChatGUI. Tenzin, CS19B"""
import socket
from tkinter import *
from threading import Thread

global loopstate, runstate


class ServerGUI:

    def __init__(self, win):
        """initializing"""
        global runstate  # shared variable across all modules
        self.user = "Server"  # current user

        self.win = win
        self.win.title("GUI Chat (Server)")
        self.win.config(background="#507bc8")
        # Display Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 600, 450
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))
        self.win.resizable(False, False)

        # some variables defined
        self.chatMessage = "<You joined the chat>"
        self.newSelfMessage = ""
        self.conn, self.threadRec = None, None

        runstate = True  # to dictate whether to continue running or stop

        # Frames for (1-ChatLogs, 2-EntryBox, 3-SendButton)
        self.chatFrame1 = Frame(self.win, bg="#203864", bd=1)
        self.chatFrame1.place(x=120, y=10, width=470, height=385)

        self.chatFrame2 = Frame(self.win, bg="#203864", bd=1)
        self.chatFrame2.place(x=120, y=405, width=402, height=34)

        self.chatFrame3 = Frame(self.win, bg="#203864", bd=1)
        self.chatFrame3.place(x=531, y=405, width=58, height=34)

        # Elements for showing current user
        self.chatFrame4 = Frame(self.win, bg="#203864", bd=1)
        self.chatFrame4.place(x=10, y=395, width=100, height=44)

        self.chatFrame41 = Frame(self.chatFrame4, bg="#dae3f3")
        self.chatFrame41.place(x=0, y=0, width=98, height=42)

        self.userIdentity1 = Label(self.chatFrame41, text="Connected as", bg="#dae3f3")
        self.userIdentity1.config(font=("Calibri", 9, "bold"), fg="#203864")
        self.userIdentity1.place(x=0, y=0, width=98, height=17)

        self.userIdentity2 = Label(self.chatFrame41, text=self.user, bg="#dae3f3")
        self.userIdentity2.config(font=("Calibri", 16, "bold"), fg="#203864")
        self.userIdentity2.place(x=0, y=15, width=98, height=25)

        # Elements for showing currently connected users
        self.inChatText = "In chat:\n\nServer (You)"
        self.chatFrame5 = Frame(self.win, bg="#203864", bd=1)
        self.chatFrame5.place(x=10, y=10, width=100, height=84)
        self.inChat = Label(self.chatFrame5, text=self.inChatText, bg="#dae3f3", anchor="nw")
        self.inChat.config(font=("Calibri", 12, "bold"), fg="#203864", bg="#dae3f3", justify='left')
        self.inChat.place(x=0, y=0, width=98, height=82)

        # ChatLogs, EntryBox and SendButton
        self.chatDisplay = Label(self.chatFrame1, text=self.chatMessage, anchor='nw')
        self.chatDisplay.config(font=("Calibri", 13), bg="#dae3f3", justify='left')
        self.chatDisplay.place(x=0, y=0, width=468, height=383)

        self.chatEntry = Entry(self.chatFrame2, relief="flat", font=("Calibri", 13))
        self.chatEntry.bind("<Return>", lambda event: self.hitEnter())
        self.chatEntry.place(x=0, y=0, width=400, height=32)
        self.chatEntry.focus()

        self.chatSendButton = Button(self.chatFrame3, text="Send", relief='flat', command=self.hitEnter)
        self.chatSendButton.config(bg="#203864", fg="White", font=("Calibri", 13, "bold"))
        self.chatSendButton.place(x=0, y=0, width=56, height=32)

        self.createConnection()

    def createConnection(self):
        """to create a connection with client"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 8082))  # ((IP address, post))
        server_socket.listen()  # continuously listens to requests on binded (address,port)
        print("Log: Waiting for connection...")
        self.conn, address = server_socket.accept()
        print("Log: Connection established")
        self.showInChat("\nClient 1")

        self.threadRec = Thread(target=self.receiveData)
        self.threadRec.start()

        server_message = "<You have connected with Server>\n"
        data = server_message.encode()
        self.conn.send(data)

    def showInChat(self, anotheruser=""):
        """show who are in chat/ in connection"""
        self.inChatText = f"In chat:\n\n{self.user} (You)" + anotheruser
        self.inChat.config(text=self.inChatText)

    def updateChat(self):
        """to update chat logs"""
        self.chatMessage += "\n" + self.newSelfMessage
        self.chatDisplay.config(text=self.chatMessage)

    def hitEnter(self):
        """called when clicking on [Send] or hitting [Enter] from Entry"""
        if self.chatEntry.get() != "":
            self.newSelfMessage = "You: " + self.chatEntry.get()
            self.sendData()
            self.updateChat()
            self.chatEntry.delete(0, "end")

    def showError(self, errmsg):
        """pass through error message to chat"""
        self.newSelfMessage = errmsg
        self.updateChat()

    def sendData(self):
        """funtion to send data to client"""
        global runstate
        try:
            server_message = "Server: " + self.chatEntry.get()
            server_data = server_message.encode()
            self.conn.send(server_data)
        except ConnectionResetError:
            self.newSelfMessage = "You: " + self.chatEntry.get() + " (not sent)"

    def receiveData(self):
        """function to receive data from client and pass to updateChat()"""
        global loopstate, runstate
        while runstate:
            try:
                client_data = self.conn.recv(1024)
                client_message = client_data.decode()
                if runstate:
                    self.newSelfMessage = client_message
                    self.updateChat()
            except ConnectionResetError:
                runstate = False
                try:
                    self.newSelfMessage = "\n<Client has disconnected>"
                    self.showInChat()
                    self.updateChat()
                except RuntimeError:
                    print()


def main():
    """create the window"""
    global loopstate
    loopstate = True
    win = Tk()
    ServerGUI(win)
    win.mainloop()


if __name__ == "__main__":
    main()
