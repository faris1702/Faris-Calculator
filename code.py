import tkinter as tk

root = tk.Tk()
root.title("Faris Calculator")
root.geometry("400x400")
photo = tk.PhotoImage(file = "cal_icon.png")
root.iconphoto(False, photo)

class Calculator:
    def __init__(self, master):
        self.master = master

        #add entry field
        self.entry = tk.Entry(master, width=30,font = ("Arial",14))
        self.entry.grid(row = 0, column = 0, columnspan=4)

        self.addButton("1", 1, 0)
        self.addButton("2", 1, 1)
        self.addButton("3", 1, 2)
        self.addButton("+", 1, 3)

        self.addButton("4", 2, 0)
        self.addButton("5", 2, 1)
        self.addButton("6", 2, 2)
        self.addButton("-", 2, 3)

        self.addButton("7", 3, 0)
        self.addButton("8", 3, 1)
        self.addButton("9", 3, 2)
        self.addButton("*", 3, 3)

        self.addButton("=", 4, 0)
        self.addButton("0", 4, 1)
        self.addButton(".", 4, 2)
        self.addButton("/", 4, 3)    

        self.addButton("(", 5, 0)
        self.addButton(")", 5, 1)
        self.addButton("C", 5, 2)
        self.addButton("CE", 5, 3)    

    def addButton(self, txt, row, col):
        if txt in ["=", "+", "/", "-", "*"]:
            b = tk.Button(self.master, text = txt, width = 5, height = 2, font = ("Arial",14), fg = "black", bg = "orange", command=lambda: self.button_press(txt))
        elif txt == "C" or txt == "CE":
            b = tk.Button(self.master, text = txt, width = 5, height = 2, font = ("Arial",14), fg = "black", bg = "red", command=lambda: self.button_press(txt))
        else:
            b = tk.Button(self.master, text = txt, width = 5, height = 2, font = ("Arial",14), command=lambda: self.button_press(txt))
        b.grid(row = row, column= col, padx= 2, pady = 2)

    def button_press(self, txt):
        if txt == "=":
            try:
                ans = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, ans)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "ERROR")

        elif txt == "C":
            self.entry.delete(0, tk.END)
        
        elif txt == "CE":
            self.entry.delete(len(self.entry.get())-1, tk.END)

        else:
            self.entry.insert(len(self.entry.get()), txt)




c = Calculator(root)
root.mainloop() # type: ignore