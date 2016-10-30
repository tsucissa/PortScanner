import socket
from tkinter import *
from tkinter import messagebox
#Above are the imported statements for the gui interface

class CissaPortScanner:
    def __init__(self):
        gui = Tk() #Creation of the GUI
        self.srvr = Entry(gui, textvariable='target')
        self.srvr.grid(row=0, column=1, sticky=E)
        self.srvr.setvar(name='target', value='127.0.0.1')
        #The above statements creates the first textbooks and sets a predefined value
        lbl = Label(gui, text='Target Address:')
        lbl.grid(row=0, column=0, sticky=W)
        lblstrt = Label(gui, text='Starting Port:')
        lblstrt.grid(row=2, column=0, sticky=W)
        self.start = Spinbox(gui, from_=1, to=10, value=1)
        self.start.grid(row=2, column=1, sticky=W)
        lblend = Label(gui, text='Ending Port:')
        lblend.grid(row=3, column=0, sticky=W)
        self.end = Spinbox(gui, from_=1, to=10, value=10)
        self.end.grid(row=3, column=1, sticky=W)
        btn = Button(gui, text='Begin Port Scan ', command=self.scan) #creation of the Button
        btn.grid(row=4, column=1, sticky=E)
        self.txt = Text(gui, width=50, height=20, wrap=WORD)
        self.txt.grid(row=5, column=0, sticky=W)
        self.txt.insert(0.0, ' Press Button to begin scan. \n ')
        gui.resizable(width=False, height=False) #Window is not resizable
        gui.title('Cissa Port Scanner')
        self.txt.insert(0.0, 'Open Ports will appear after the Scan Completes!\n\nPort Scanner by: TSU CISSA. ')
        gui.mainloop() #GUI is executed !

    #The Port Scanner Function
    def pscan(self, port):
        try:
            target = self.srvr.get()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            return True
        except:
            return False

    #The Scan function
    def scan(self):
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, ('Scanning ' + self.srvr.get() + ' ... \n'))

        #The beginning of PSresult.txt
        port_file = open("PSresult.txt", "w")
        port_file.write("\n##Scanned " + self.srvr.get() + ': ##\n')
        #Beginning of the for loop:
        for port in range(int(self.start.get()), int(self.end.get()) + 1):
            if self.pscan(port):
                msg = "Port " + str(port) + ' Is open \n'
                self.txt.insert(float(port) + 1, msg)
                port_file.write(msg)

            else:
                self.txt.insert(float(port) + 1, 'Port ' + str(port) + ' is closed! \n')
                msg = "Port " + str(port) + ' Is closed \n'
                port_file.write(msg)
        port_file.close()

        messagebox.showinfo(title='Cissa Port Scanner', message='Your Scan is finished. Happy Hacking :)')


pscan = CissaPortScanner()
