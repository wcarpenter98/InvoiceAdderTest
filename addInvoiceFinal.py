import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

class App(tk.Frame):

    def __init__(self, master):
        self.master = master
        lbl1 = tk.Label(self.master, text = "Zach's Invoice Adder")
        lbl1.grid(row = 0, column = 0, columnspan = 3)
        btn1 = tk.Button(self.master, text="CLICK ME TO BROWSE TO THE FILE", command=self.load_file, width=30)
        btn1.grid(row = 2, column = 1)
        self.lbl3 = tk.Label(self.master, text = "INVOICE INFORMATION WILL BE DISPLAYED BELOW")
        self.lbl3.grid(row = 3, column = 1)
        self.text1 = tk.Text(self.master, height = 30, width = 100)
        self.text1.grid(row = 5, column = 1)
        master.title('Superior Lawn Care Invoice Adder 2019')






    def load_file(self):
            fname = askopenfilename(filetypes=(("All files", "*.*"),
                                               ("HTML files", "*.html;*.htm"),
                                               ("Template files", "*.tplate"),
                                               ("Text files", "*.txt")))

            if fname:
                try:

                    file = open(fname, "r")
                    line = file.read()
                    line = line.rstrip()
                    line = line.replace("\n", "")
                    line = line.rstrip()
                    line = line.split()
                    line = ([s.replace('$', '') for s in line]) # remove all the 8s
                    total = sum([int(num) for num in line])
                    string1 = "---------------------------Below--is--6.5% sales tax---------------------------"
                    string2 = "The total without sales tax is " + str(round(total, 2))
                    salesTaxTotal = 0.065 * total
                    string3 = "Sales tax is " + str(round(salesTaxTotal, 2))
                    totalDisplay = total + salesTaxTotal
                    string4 = "Overall total is " + str(round(totalDisplay, 2))
                    string5 = "---------------------------Below--is--7.0% sales tax---------------------------"
                    string6 = "The total without sales tax is " + str(round(total, 2))
                    salesTaxTotal = 0.07 * total
                    string7 = "Sales tax is " + str(round(salesTaxTotal, 2))
                    totalDisplay = total + salesTaxTotal
                    string8 = "Overall total is " + str(round(totalDisplay, 2))
                    string9 = string1 + "\n" + string2 + "\n" + string3 + "\n" + string4 + "\n" + string5 + "\n" + string6 + "\n" + string7 + "\n" + string8 
                    self.text1.delete(1.0, "end")
                    self.text1.insert(1.0, string9) 
                    
                except:                    
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                return


if __name__ == "__main__":

    root = tk.Tk()
    myapp = App(root)
    root.mainloop()



