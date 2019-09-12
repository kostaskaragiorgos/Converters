from tkinter import *
from tkinter import messagebox as msg

import csv
import os 

class ft_to_m():
    def __init__(self,master):
        self.master = master
        self.master.title("FT TO M CONVERTER")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        
        if os.path.exists('ft_to_m.csv') == False:
            with open('ft_to_m.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['FT','M'])
                f.close()
        
        self.amleb = Label(self.master,text = "Amount")
        self.amleb.pack()
        
        self.textname = Text(self.master,height = 1 )
        self.textname.pack()
        
        self.fromleb = Label(self.master,text = "From")
        self.fromleb.pack()
        
        fromlist = list([" ", "FT", "M"])
        self.varfrom = StringVar(master)
        self.varfrom.set(fromlist[0])
        self.popupfrommenu = OptionMenu(self.master,self.varfrom,*fromlist)
        self.popupfrommenu.pack()
        
        self.toleb = Label(self.master,text = "To")
        self.toleb.pack()
        
        tolist = list([" ", "FT", "M"])
        self.varto = StringVar(master)
        self.varto.set(fromlist[0])
        self.popuptomenu = OptionMenu(self.master,self.varto,*tolist)
        self.popuptomenu.pack()
        
        self.convb = Button(self.master,text = "Convert", command = self.conv)
        self.convb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
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
    
    def conv(self):
       pass
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        msg.showinfo("About","About FT TO M CONVERTER \nVersion 1.0")

def main():
    root=Tk()
    ftm = ft_to_m(root)
    root.mainloop()
    
if __name__=='__main__':
    main()