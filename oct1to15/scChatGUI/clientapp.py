"""for client side. Part of scChatGUI. Tenzin, CS19B"""
import socket
from tkinter import *
from threading import Thread

global runstate


class ClientGUI:
    global runstate

    def __init__(self, win):
        global runstate  # shared variable across all modules
        runstate = True  # to dictate whether to continue running or stop

        self.win = win
        self.win.title("GUI Chat (Client)")
        self.win.config(background="#5a8a26")
        # Display Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 600, 450
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))
        self.win.resizable(False, False)

        self.user = "Client 1"
        self.chatMessage = "<You have joined the chat>"
        self.newSelfMessage = ""
        self.conn, self.threadRec = None, None

        # Frames (1-ChatHistory, 2-EntryBOx, 3-SendButton)
        self.chatFrame1 = Frame(self.win, bg="#385723", bd=1)
        self.chatFrame1.place(x=120, y=10, width=470, height=385)

        self.chatFrame2 = Frame(self.win, bg="#385723", bd=1)
        self.chatFrame2.place(x=120, y=405, width=402, height=34)

        self.chatFrame3 = Frame(self.win, bg="#253917", bd=1)
        self.chatFrame3.place(x=531, y=405, width=58, height=34)

        # Show current user
        self.chatFrame4 = Frame(self.win, bg="#385723", bd=1)
        self.chatFrame4.place(x=10, y=395, width=100, height=44)
        self.chatFrame41 = Frame(self.chatFrame4, bg="#c5e0b4")
        self.chatFrame41.place(x=0, y=0, width=98, height=42)
        self.userIdentity1 = Label(self.chatFrame41, text="Connected as", bg="#c5e0b4")
        self.userIdentity1.config(font=("Calibri", 9, "bold"), fg="#253917")
        self.userIdentity1.place(x=0, y=0, width=98, height=17)
        self.userIdentity2 = Label(self.chatFrame41, text=self.user, bg="#c5e0b4", font=("Calibri", 16, "bold"))
        self.userIdentity2.config(font=("Calibri", 16, "bold"), fg="#253917")
        self.userIdentity2.place(x=0, y=15, width=98, height=25)

        # Elements to show those users currently connected
        self.inChatText = f"In chat:\n\n{self.user} (You)"
        self.chatFrame5 = Frame(self.win, bg="#385723", bd=1)
        self.chatFrame5.place(x=10, y=10, width=100, height=84)
        self.inChat = Label(self.chatFrame5, text=self.inChatText, bg="#c5e0b4", anchor="nw")
        self.inChat.config(font=("Calibri", 12, "bold"), fg="#253917", bg="#c5e0b4", justify='left')
        self.inChat.place(x=0, y=0, width=98, height=82)

        # Elements for ChatLogs, EntryBox, and SendButton
        self.chatDisplay = Label(self.chatFrame1, text=self.chatMessage, anchor='nw')
        self.chatDisplay.config(font=("Calibri", 13), fg="#253917", bg="#c5e0b4", justify='left')
        self.chatDisplay.place(x=0, y=0, width=468, height=383)

        self.chatEntry = Entry(self.chatFrame2, relief="flat", font=("Calibri", 13))
        self.chatEntry.bind("<Return>", lambda event: self.hitEnter())
        self.chatEntry.place(x=0, y=0, width=400, height=32)
        self.chatEntry.focus()

        self.chatSendButton = Button(self.chatFrame3, text="Send", relief='flat', command=self.hitEnter)
        self.chatSendButton.config(bg="#385723", fg="White", font=("Calibri", 13, "bold"))
        self.chatSendButton.place(x=0, y=0, width=56, height=32)

        # socket
        self.createConnection()

    def createConnection(self):
        """to create a connection with client"""
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (internet ver 4, socket TCP/IP)
            self.conn.connect(('127.0.0.1', 8082))  # ((IP address, post))
            print("Connection Established\n")  # if connected to server
            self.showInChat("\nServer")

            self.threadRec = Thread(target=self.receiveData)
            self.threadRec.start()

            server_message = "<A Client has connected>\n"
            data = server_message.encode()
            self.conn.send(data)
        except ConnectionRefusedError:
            self.showError("\n<Cannot connect to server>\n<Restart after server is on>")

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
            server_message = self.user + ": " + self.chatEntry.get()
            server_data = server_message.encode()
            self.conn.send(server_data)
        except ConnectionResetError:
            self.showError("<Connection lost>")
            self.newSelfMessage = "You: " + self.chatEntry.get() + " (not sent)"

    def receiveData(self):
        """function to receive data from client and pass to updateChat()"""
        global runstate
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
                    self.newSelfMessage = "\n<Server has disconnected>"
                    self.showInChat("")
                    self.updateChat()
                except RuntimeError:
                    print()


def main():
    """create the window"""
    win = Tk()
    ClientGUI(win)
    win.mainloop()


if __name__ == "__main__":
    main()
