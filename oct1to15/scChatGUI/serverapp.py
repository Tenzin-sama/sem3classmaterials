"""for server side"""
import socket
from threading import *
import tkinter
from tkinter import *


class ServerGUI:

    def __init__(self, win):
        global conn, runstate  # shared variable across all modules

        self.win = win
        self.win.title("GUI Chat")
        # Display Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 600, 450
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))
        # Elements

    def createChat(self, chatHeadname):
        pass
        # Button
        self.chatHead = Button(self.win, text=chatHeadname, command=self.gotoChatHead)
        # Label
        self.chatDisplay = Label(self.win)
        # Entry
        self.sendMessage = Entry(self.win)

    def gotoChatHead(self):
        pass


    def sendData(self):
        """funtion to send data to client"""
        global conn, runstate
        while runstate:
            server_message = "Server: " + input()
            if server_message == 'Server: x':
                print("[You have disconnected]")
                print("...please wait...\n")
                runstate = False
            server_data = server_message.encode()
            conn.send(server_data)

    def receiveData(self):
        """function to receive data from client"""
        global conn, runstate
        while runstate:
            client_data = conn.recv(1024)
            client_message = client_data.decode()
            if client_message == "Client: x":  # if client has disconnected
                print("[Client has disconnected]")
                runstate = False
            if runstate:
                print(client_message)


def main():
    """create the window"""
    win = Tk()
    ServerGUI(win)
    win.mainloop()


if __name__ == "__main__":
    main()
