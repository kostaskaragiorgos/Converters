from tkinter import *
from tkinter import messagebox as msg

import csv
import os 
import pandas as pd

class lbs_to_kg():
    def __init__(self,master):
        self.master = master
        self.master.title("LBS TO KG CONVERTER")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        
        if os.path.exists('lbs_to_kg.csv') == False:
            with open('lbs_to_kg.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['LBS','KG'])
        
        self.amleb = Label(self.master,text = "Amount")
        self.amleb.pack()
        
        self.textname = Text(self.master,height = 1 )
        self.textname.pack()
        
        self.fromleb = Label(self.master,text = "From")
        self.fromleb.pack()
        
        fromlist = list([" ", "KG", "LBS"])
        self.varfrom = StringVar(master)
        self.varfrom.set(fromlist[0])
        self.popupfrommenu = OptionMenu(self.master,self.varfrom,*fromlist)
        self.popupfrommenu.pack()
        
        self.toleb = Label(self.master,text = "To")
        self.toleb.pack()
        
        tolist = list([" ", "KG", "LBS"])
        self.varto = StringVar(master)
        self.varto.set(fromlist[0])
        self.popuptomenu = OptionMenu(self.master,self.varto,*tolist)
        self.popuptomenu.pack()
        
        self.convb = Button(self.master,text = "Convert", command = self.conv)
        self.convb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Convert",accelerator = 'Ctrl+T',command = self.conv)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.show_menu = Menu(self.menu,tearoff = 0)
        self.show_menu.add_command(label = "Show Convertions",accelerator = 'Ctrl+S',command = self.showconv)
        self.menu.add_cascade(label = "Show",menu = self.show_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-s>',lambda event:self.showconv())
        self.master.bind('<Control-t>',lambda event:self.conv())
        
    def showconv(self):
        df = pd.read_csv('lbs_to_kg.csv')
        msg.showinfo("LBS TO KG", str(df))
    
    def conv(self):
        corf = 0
        if self.varfrom.get() == " " or self.varto.get() == " " or self.varfrom.get() == self.varto.get():
            msg.showerror("ERROR","THIS CONVERTION CAN NOT BE DONE")
        else:
            try:
                if float(self.textname.get(1.0,END)) > 0:
                    corf = 1
                else:
                    msg.showerror("Value Error", "Enter a number higher than zero")
                    self.textname.delete(0,END)
            except:
                msg.showerror("Value Error", "Enter a number higher than zero")
                self.textname.delete(1.0,END)
        if corf == 1:
            if self.varfrom.get() == "LBS":
                value = float(self.textname.get(1.0,END))*0.45359237
                with open('lbs_to_kg.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(float(self.textname.get(1.0,END))),str(value)])

                msg.showinfo("LBS TO KG", str(float(self.textname.get(1.0,END)))+" LBS ARE "+str(value)+" KG ")
                
            elif self.varfrom.get() == "KG":
                value = float(self.textname.get(1.0,END))*2.20462
                with open('lbs_to_kg.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(value),str(float(self.textname.get(1.0,END)))])

                msg.showinfo("KG TO LBS",str(float(self.textname.get(1.0,END)))+" KG ARE " +str(value)+" LBS ")
               
           
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help","Enter an amount and choose from the from and to lists and press the convert button")
    
    def aboutmenu(self):
        msg.showinfo("About","About LBS TO KG CONVERTER \nVersion 1.0")

def main():
    root=Tk()
    ltk = lbs_to_kg(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
