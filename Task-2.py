#Dharmishtha Chandegara
#GUI Calculator using Tkinter

from symtable import Symbol
from tkinter import *
import tkinter as tk 

#Constants
LABEL_CURRENTFONT = ("Arial",40,"bold")
LABEL_TOTALFONT = ("Arial",16)
DEFAULT_FONT = ("Arial",20)
DIGIT_FONT = ("Arial",24,"bold")

OFF_WHITE = "#F8FAFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
LIGHT_BLUE = "#CCEDFF"
WHITE = "#FFFFFF"


#Class Calc
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x700")
        self.window.resizable(0,0)
        self.window.title("Task 2")
     
        self.total = ""
        self.current_input = ""
        
        self.dis_frame = self.create_dis_frame()   
        self.total_label, self.current_label = self.create_dis_label()
     
        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            '.': (4,1), 0: (4,2)
        }

        #For Arithmetic Opeartions
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        self.btn_frame = self.create_btn_frame()
        self.btn_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.btn_frame.rowconfigure(x,weight=1)   #Expands Row
            self.btn_frame.columnconfigure(x,weight=1)   #Expands Column
            
        self.create_operators()
        self.create_btns()
        
        self.create_spe_btn()
        self.bind_keys()
        
        
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.eval())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_exp(digit))
            
        for key in self.operators:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
            
            
    def create_spe_btn(self):
        self.create_clear_btn()
        self.create_equal_btn()
        
        
    #Displaying the Labels
    def create_dis_label(self):
        total_label = tk.Label(self.dis_frame, text=self.total, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,font=LABEL_TOTALFONT) 
        total_label.pack(expand=TRUE, fill="both")
     
        current_label = tk.Label(self.dis_frame, text=self.current_input, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LABEL_CURRENTFONT) 
        current_label.pack(expand=TRUE, fill="both")
        
        return total_label, current_label
    
    
    #Creating Display Frame   
    def create_dis_frame(self):
        frame = tk.Frame(self.window, height=200,bg=LIGHT_GRAY)  
        frame.pack(expand=TRUE, fill="both")
        return frame
    
    
    def add_exp(self, value):
        self.current_input += str(value)
        self.update_label()
      
        
    #Method For display buttons
    def create_btns(self):
        for digit, grid_value in self.digits.items():
            btn = tk.Button(self.btn_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT, borderwidth=0, command= lambda x=digit: self.add_exp(x))
            btn.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
      
      
    def append_operator(self, operator):
        self.current_input += operator
        self.total += self.current_input
        self.current_input = ""
        self.update_total_label()
        self.update_label()  
            
            
    #For Operators
    def create_operators(self):
        i=0
        for operator, symbol in self.operators.items():
            btn = tk.Button(self.btn_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth= 0, command= lambda x=operator: self.append_operator(x)) 
            
            btn.grid(row=i, column=4, sticky=tk.NSEW) 
            i+=1
     
    
    def clear(self):
        self.current_input = ""
        self.total = ""
        
        self.update_label()
        self.update_total_label()
        
               
    def create_clear_btn(self):
            btn = tk.Button(self.btn_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth= 0, command= self.clear) 
            
            btn.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW) 
           
    
    def eval(self):
        self.total += self.current_input
        self.update_total_label()
        
        try: 
            self.current_input = str(eval(self.total))
            self.total = ""
        except Exception as e:
            self.current_input = "Error"
        finally:
            self.update_label()
        
        
    def create_equal_btn(self):
            btn = tk.Button(self.btn_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth= 0, command=self.eval) 
            
            btn.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW) 
       
         
    #Creating Button Frame
    def create_btn_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=TRUE, fill="both")
        return frame
    
       
    def update_total_label(self):
        expression = self.total
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f' {symbol} ')
            
        self.total_label.config(text=expression)
       
         
    def update_label(self):
        self.current_label.config(text=self.current_input[:11])  
         
     
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
