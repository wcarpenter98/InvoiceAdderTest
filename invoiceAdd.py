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
        self.lbl3 = tk.Label(self.master, text = "INVOICE INFORMATION")
        self.lbl3.grid(row = 3, column = 1)
        
        
        self.text1 = tk.Text(self.master, height = 1, width = 100)
        self.text1.grid(row = 5, column = 1)

        self.text2 = tk.Text(self.master, height = 1, width = 100)
        self.text2.grid(row = 6, column = 1)

        self.text3 = tk.Text(self.master, height = 1, width = 100)
        self.text3.grid(row = 7, column = 1)

        self.text4 = tk.Text(self.master, height = 1, width = 100)
        self.text4.grid(row = 8, column = 1)

        self.text5 = tk.Text(self.master, height = 1, width = 100)
        self.text5.grid(row = 9, column = 1)

        self.text6 = tk.Text(self.master, height = 1, width = 100)
        self.text6.grid(row = 10, column = 1)

        self.text7 = tk.Text(self.master, height = 1, width = 100)
        self.text7.grid(row = 11, column = 1)

        self.text8 = tk.Text(self.master, height = 1, width = 100)
        self.text8.grid(row = 12, column = 1)


    def add_numbers(self):

        x = self.entry1.get()
        y = self.entry2.get()

        if x != "" and y != "":
            sumxy = int(x) + int(y)

            self.lbl3.config(text = "Sum = {}".format(sumxy))

            self.entry3.delete(0, "end")
            self.entry3.insert(0, sumxy)

            self.text1.delete(1.0, "end")
            self.text1.insert(1.0, sumxy)

            messagebox.showinfo("Sum of {} and {}".format(x,y), 
                                "Sum of {} and {} = {}".format(x, y, sumxy))


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
                    
                    self.text1.delete(1.0, "end")
                    self.text1.insert(1.0, string1)       
                    self.text2.delete(1.0, "end")
                    self.text2.insert(1.0, string2) 




                    salesTaxTotal = 0.065 * total

                    string3 = "Sales tax is " + str(round(salesTaxTotal, 2))

                    totalDisplay = total + salesTaxTotal
                    string4 = "Overall total is " + str(round(totalDisplay, 2))

                    self.text3.delete(1.0, "end")
                    self.text3.insert(1.0, string3)       
                    self.text4.delete(1.0, "end")
                    self.text4.insert(1.0, string4) 

                          

                    string5 = "---------------------------Below--is--7.0% sales tax---------------------------"

                    string6 = "The total without sales tax is " + str(round(total, 2))


                    salesTaxTotal = 0.07 * total

                    string7 = "Sales tax is " + str(round(salesTaxTotal, 2))

                    totalDisplay = total + salesTaxTotal
                    string8 = "Overall total is " + str(round(totalDisplay, 2))

                    self.text5.delete(1.0, "end")
                    self.text5.insert(1.0, string5)       
                    self.text6.delete(1.0, "end")
                    self.text6.insert(1.0, string6) 

                    self.text7.delete(1.0, "end")
                    self.text7.insert(1.0, string7)       
                    self.text8.delete(1.0, "end")
                    self.text8.insert(1.0, string8) 



                    
                except:                    
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                return


if __name__ == "__main__":

    root = tk.Tk()
    myapp = App(root)
    root.mainloop()



