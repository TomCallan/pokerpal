from copyreg import constructor
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        self.constructor=[]
        self.clicked=[]
        
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GButton_185=tk.Button(root)
        self.GButton_185["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_185["font"] = ft
        self.GButton_185["fg"] = "#000000"
        self.GButton_185["justify"] = "center"
        self.GButton_185["text"] = "ACE"
        self.GButton_185.place(x=460,y=340,width=100,height=40)
        self.GButton_185["command"] = self.Button_185_command

        self.GButton_441=tk.Button(root)
        self.GButton_441["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_441["font"] = ft
        self.GButton_441["fg"] = "#000000"
        self.GButton_441["justify"] = "center"
        self.GButton_441["text"] = "2"
        self.GButton_441.place(x=40,y=160,width=100,height=40)
        self.GButton_441["command"] = self.Button_441_command

        self.GButton_945=tk.Button(root)
        self.GButton_945["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_945["font"] = ft
        self.GButton_945["fg"] = "#000000"
        self.GButton_945["justify"] = "center"
        self.GButton_945["text"] = "3"
        self.GButton_945.place(x=40,y=250,width=100,height=40)
        self.GButton_945["command"] = self.Button_945_command

        self.GButton_41=tk.Button(root)
        self.GButton_41["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_41["font"] = ft
        self.GButton_41["fg"] = "#000000"
        self.GButton_41["justify"] = "center"
        self.GButton_41["text"] = "4"
        self.GButton_41.place(x=40,y=340,width=100,height=40)
        self.GButton_41["command"] = self.Button_41_command

        self.GButton_689=tk.Button(root)
        self.GButton_689["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_689["font"] = ft
        self.GButton_689["fg"] = "#000000"
        self.GButton_689["justify"] = "center"
        self.GButton_689["text"] = "5"
        self.GButton_689.place(x=180,y=160,width=100,height=40)
        self.GButton_689["command"] = self.Button_689_command

        self.GButton_332=tk.Button(root)
        self.GButton_332["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_332["font"] = ft
        self.GButton_332["fg"] = "#000000"
        self.GButton_332["justify"] = "center"
        self.GButton_332["text"] = "6"
        self.GButton_332.place(x=180,y=250,width=100,height=40)
        self.GButton_332["command"] = self.Button_332_command

        self.GButton_609=tk.Button(root)
        self.GButton_609["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_609["font"] = ft
        self.GButton_609["fg"] = "#000000"
        self.GButton_609["justify"] = "center"
        self.GButton_609["text"] = "7"
        self.GButton_609.place(x=180,y=340,width=100,height=40)
        self.GButton_609["command"] = self.Button_609_command

        self.GButton_878=tk.Button(root)
        self.GButton_878["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_878["font"] = ft
        self.GButton_878["fg"] = "#000000"
        self.GButton_878["justify"] = "center"
        self.GButton_878["text"] = "8"
        self.GButton_878.place(x=310,y=160,width=100,height=40)
        self.GButton_878["command"] = self.Button_878_command

        self.GButton_257=tk.Button(root)
        self.GButton_257["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_257["font"] = ft
        self.GButton_257["fg"] = "#000000"
        self.GButton_257["justify"] = "center"
        self.GButton_257["text"] = "9"
        self.GButton_257.place(x=310,y=250,width=100,height=40)
        self.GButton_257["command"] = self.Button_257_command

        self.GButton_328=tk.Button(root)
        self.GButton_328["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_328["font"] = ft
        self.GButton_328["fg"] = "#000000"
        self.GButton_328["justify"] = "center"
        self.GButton_328["text"] = "10"
        self.GButton_328.place(x=310,y=340,width=100,height=40)
        self.GButton_328["command"] = self.Button_328_command

        self.GButton_815=tk.Button(root)
        self.GButton_815["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_815["font"] = ft
        self.GButton_815["fg"] = "#000000"
        self.GButton_815["justify"] = "center"
        self.GButton_815["text"] = "JACK"
        self.GButton_815.place(x=460,y=160,width=100,height=40)
        self.GButton_815["command"] = self.Button_815_command

        self.GButton_502=tk.Button(root)
        self.GButton_502["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_502["font"] = ft
        self.GButton_502["fg"] = "#000000"
        self.GButton_502["justify"] = "center"
        self.GButton_502["text"] = "QUEEN"
        self.GButton_502.place(x=460,y=220,width=100,height=40)
        self.GButton_502["command"] = self.Button_502_command

        self.GButton_149=tk.Button(root)
        self.GButton_149["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_149["font"] = ft
        self.GButton_149["fg"] = "#000000"
        self.GButton_149["justify"] = "center"
        self.GButton_149["text"] = "KING"
        self.GButton_149.place(x=460,y=280,width=100,height=40)
        self.GButton_149["command"] = self.Button_149_command

        self.GButton_229=tk.Button(root)
        self.GButton_229["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.GButton_229["font"] = ft
        self.GButton_229["fg"] = "#000000"
        self.GButton_229["justify"] = "center"
        self.GButton_229["text"] = "♠"
        self.GButton_229.place(x=40,y=30,width=100,height=75)
        self.GButton_229["command"] = self.Button_229_command

        self.GButton_162=tk.Button(root)
        self.GButton_162["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.GButton_162["font"] = ft
        self.GButton_162["fg"] = "#000000"
        self.GButton_162["justify"] = "center"
        self.GButton_162["text"] = "♥"
        self.GButton_162.place(x=180,y=30,width=100,height=75)
        self.GButton_162["command"] = self.Button_162_command

        self.GButton_580=tk.Button(root)
        self.GButton_580["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.GButton_580["font"] = ft
        self.GButton_580["fg"] = "#000000"
        self.GButton_580["justify"] = "center"
        self.GButton_580["text"] = "♦"
        self.GButton_580.place(x=320,y=30,width=100,height=75)
        self.GButton_580["command"] = self.Button_580_command

        self.GButton_87=tk.Button(root)
        self.GButton_87["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.GButton_87["font"] = ft
        self.GButton_87["fg"] = "#000000"
        self.GButton_87["justify"] = "center"
        self.GButton_87["text"] = "♣"
        self.GButton_87.place(x=460,y=30,width=100,height=75)
        self.GButton_87["command"] = self.Button_87_command

    def Button_185_command(self):
        self.GButton_185.configure(bg="red")
        self.clicked.append(self.GButton_185)
        self.check(185)

    def Button_441_command(self):
        self.GButton_441.configure(bg="red")
        self.clicked.append(self.GButton_441)
        self.check(441)


    def Button_945_command(self):
        self.GButton_945.configure(bg="red")
        self.clicked.append(self.GButton_945)
        self.check(945)


    def Button_41_command(self):
        self.GButton_41.configure(bg="red")
        self.clicked.append(self.GButton_41)
        self.check(41)


    def Button_689_command(self):
        self.GButton_689.configure(bg="red")
        self.clicked.append(self.GButton_689)
        self.check(689)


    def Button_332_command(self):
        self.GButton_332.configure(bg="red")
        self.clicked.append(self.GButton_332)
        self.check(332)


    def Button_609_command(self):
        self.GButton_609.configure(bg="red")
        self.clicked.append(self.GButton_609)
        self.check(609)


    def Button_878_command(self):
        self.GButton_878.configure(bg="red")
        self.clicked.append(self.GButton_878)
        self.check(878)


    def Button_257_command(self):
        self.GButton_257.configure(bg="red")
        self.clicked.append(self.GButton_257)
        self.check(257)


    def Button_328_command(self):
        self.GButton_328.configure(bg="red")
        self.clicked.append(self.GButton_328)
        self.check(328)


    def Button_815_command(self):
        self.GButton_815.configure(bg="red")
        self.clicked.append(self.GButton_815)
        self.check(815)


    def Button_502_command(self):
        self.GButton_502.configure(bg="red")
        self.clicked.append(self.GButton_502)
        self.check(502)


    def Button_149_command(self):
        self.GButton_149.configure(bg="red")
        self.clicked.append(self.GButton_149)
        self.check(149)


    def Button_229_command(self):
        self.GButton_229.configure(bg="red")
        self.clicked.append(self.GButton_229)
        self.check(229)


    def Button_162_command(self):
        self.GButton_162.configure(bg="red")
        self.clicked.append(self.GButton_162)
        self.check(162)


    def Button_580_command(self):
        self.GButton_580.configure(bg="red")
        self.clicked.append(self.GButton_580)
        self.check(580)


    def Button_87_command(self):
        self.GButton_87.configure(bg="red")
        self.clicked.append(self.GButton_87)
        self.check(87)

    def check(self, x):
        self.deck = {
            229:'s', 
            162:'h', 
            580:'d', 
            87:'c',
            441:'2',
            945:'3',
            41 :'4',
            689:'5',
            332:'6',
            609:'7',
            878:'8',
            257:'9',
            328:'10',
            815:'j',
            502:'q',
            149:'k',
            185:'a',
        }

        d1 = {
        'a':2,
        '2':3,
        '3':4,
        '4':5,
        '5':6,
        '6':7,
        '7':8,
        '8':9,
        '9':10,
        '10':11,
        'j':12,
        'q':13,
        'k':14,
        }

        d2 = {
            's':1,
            'h':2,
            'c':3,
            'd':4,
        }

        if len(self.constructor) == 0:
            self.constructor.append(self.deck[x])
        elif len(self.constructor) == 1:
            if self.deck[x] in d2:
                self.constructor.insert(0, self.deck[x])
            else:
                self.constructor.insert(1, self.deck[x])
        if len(self.constructor) == 2:
            print(self.constructor)
            for i in self.clicked:
                i.configure(bg="#efefef")
            self.clicked = []
            self.constructor = []

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
