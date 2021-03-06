"""
lbs to kg converter
"""
from tkinter import Tk, Button, Label, Text, StringVar, OptionMenu, Menu, END
from tkinter import messagebox as msg
import csv
import os 
import pandas as pd
def showconv():
    """ shows the convertions done """
    if not os.path.exists('lbs_to_kg.csv'):
        msg.showerror("ERROR", "NO FILE TO SHOW")
    else:
        df = pd.read_csv('lbs_to_kg.csv')
        if df.empty:
            msg.showerror("ERROR", "NO CONVERTIONS SAVED")
        else:
            df.drop_duplicates(keep="first", inplace=True)
            msg.showinfo("LBS TO KG", str(df))
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Enter an amount and choose from the from and to lists and press the convert button")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "About LBS TO KG CONVERTER \nVersion 1.0")
class lbs_to_kg():
    def __init__(self, master):
        """ lbs to kg class """
        self.master = master
        self.master.title("LBS TO KG CONVERTER")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        if not os.path.exists('lbs_to_kg.csv'):
            with open('lbs_to_kg.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['LBS', 'KG'])
        self.amleb = Label(self.master, text="Amount")
        self.amleb.pack()
        self.textname = Text(self.master, height=1)
        self.textname.pack()
        self.fromleb = Label(self.master, text="From")
        self.fromleb.pack()
        fromlist = list([" ", "KG", "LBS"])
        self.varfrom = StringVar(master)
        self.varfrom.set(fromlist[0])
        self.popupfrommenu = OptionMenu(self.master, self.varfrom, *fromlist)
        self.popupfrommenu.pack()
        self.convb = Button(self.master, text="Convert", command=self.conv)
        self.convb.pack()
        # menu 
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Convert", accelerator='Ctrl+T', command=self.conv)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu (self.menu, tearoff=0)
        self.edit_menu.add_command(label="Clear text field", accelerator='Alt + S', command=self.cleart)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Convertions", accelerator='Ctrl+S', command=showconv)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Alt-s>', lambda event: self.cleart())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-s>', lambda event: showconv())
        self.master.bind('<Control-t>', lambda event: self.conv())
    def cleart(self):
        """ clears text field """
        self.textname.delete(1.0, END)
    def save_convertion(self,value):
        with open('lbs_to_kg.csv', 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([str(float(self.textname.get(1.0, END))), str(value)])
    def libs_to_kg_convertion(self):
        value = float(self.textname.get(1.0, END))*0.45359237
        self.save_convertion(value)
        msg.showinfo("LBS TO KG", str(float(self.textname.get(1.0, END)))+" LBS ARE "+str(value)+" KG ")
    def kg_to_libs_convertion(self):
        value = float(self.textname.get(1.0, END))*2.20462
        self.save_convertion(value)
        msg.showinfo("KG TO LBS", str(float(self.textname.get(1.0, END)))+" KG ARE " +str(value)+" LBS ")
    def conv(self):
        """ convertion fuction """ 
        try:
            if float(self.textname.get(1.0, END)) > 0:
                if self.varfrom.get() == "LBS":
                    self.libs_to_kg_convertion()
                elif  self.varfrom.get() == "KG":
                    self.kg_to_libs_convertion()
                else:
                    msg.showerror("ERROR", "THIS CONVERTION CAN NOT BE DONE")
        except ValueError:
            msg.showerror("Value Error", "Enter a number higher than zero")
        self.cleart()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    lbs_to_kg(root)
    root.mainloop()
if __name__ == '__main__':
    main()
