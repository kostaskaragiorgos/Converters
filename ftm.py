"""
F to M converter
"""
from tkinter import Label, Text, StringVar, Tk, OptionMenu
from tkinter import Button, Menu, END, messagebox as msg
import os
import csv
import pandas as pd
def fixdf(df):
    """ checks if df is empty else drops duplicates"""
    if df.empty:
        msg.showerror("ERROR", "NO CONVERTIONS SAVED")
    else:
        df.drop_duplicates(keep="first", inplace=True)
def showconv():
    """ shows convertions done """
    if not os.path.exists('ft_to_m.csv'):
        msg.showerror("ERROR", "NO FILE TO SHOW")
    else:
        df = pd.read_csv('ft_to_m.csv')
        fixdf(df)
        msg.showinfo("FT TO M", str(df))
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Enter an amount choose from and to lists and press convert button")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "About FT TO M CONVERTER \nVersion 1.0")
class FtToM():
    """ Ft To M Class"""
    def __init__(self, master):
        self.master = master
        self.master.title("FT TO M CONVERTER")
        self.master.geometry("250x150")
        self.master.resizable(False, False)
        if not os.path.exists('ft_to_m.csv'):
            with open('ft_to_m.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['FT', 'M'])
        self.amleb = Label(self.master, text="Amount")
        self.amleb.pack()
        self.textname = Text(self.master, height=1)
        self.textname.pack()
        self.fromleb = Label(self.master, text="From")
        self.fromleb.pack()
        fromlist = list([" ", "FT", "M"])
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
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Clear text field", accelerator='Alt+S', command=self.cleart)
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
        """ clears the text field"""
        self.textname.delete(1.0, END)
    def saveconvertion(self, value):
        with open('ft_to_m.csv', 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([str(float(self.textname.get(1.0, END))), str(value)])
    def mtoftconvertion(self):
        value = float(self.textname.get(1.0, END))/0.3048
        self.saveconvertion(value)
        msg.showinfo("M TO FT", str(float(self.textname.get(1.0, END)))+" M ARE " +str(value)+" FT ")
    def ftmconvertion(self):
        value = float(self.textname.get(1.0, END))*0.3048
        self.saveconvertion(value)
        msg.showinfo("FT TO M", str(float(self.textname.get(1.0, END)))+" FT ARE "+str(value)+" M ")
    def conv(self):
        """ convert button function """
        if  self.varfrom.get() == " ":
            msg.showerror("ERROR", "THIS CONVERTION CAN NOT BE DONE")
        else:
            try:
                if float(self.textname.get(1.0, END)) > 0:
                    if self.varfrom.get() == "FT":
                        self.ftmconvertion()
                    elif  self.varfrom.get() == "M":
                        self.mtoftconvertion()
            except ValueError:
                msg.showerror("Value Error", "Enter a number higher than zero")
        self.cleart()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ the main function """
    root = Tk()
    FtToM(root)
    root.mainloop()
if __name__ == '__main__':
    main()
