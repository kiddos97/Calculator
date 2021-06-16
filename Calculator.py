#We will be creating a GUI calculator with Python using the Tkinter module
#Creator : Osaro Imarhiagbe
# Python code will have the following functions
# Add/Subtraction
# Multiplication/Divison


#imorting everything from the tkinter module
from tkinter import *
#globally declare the expression variable
#access among all the fucntions
exp = ""
#function to update expression (number) in the test entry box
def num_input(num, equation):
    #delcaring the global expression
    global exp
    #concatentaion of string
    exp = exp + str(num)
    #update expression by using set method
    equation.set(exp)
#Function to evaluate the final expression
#function to clear contents of the entry box
def clear (equation):
    global exp
    exp = ""
    #setting empty string in the input field
    equation.set("")
def finalexp(equation):
    # Try and except statement is used
    # to handle errors like zero division error etc.

    try:
        global exp

        #eval function evlauate the expression
        #str function converts the result into a string
        total = str(eval(exp))
        equation.set(total)
        #initialize the expression via empty string
        exp = ""
             #if error is genterated handle by the except block
    except:

     equation.set(" error ")
     exp = ""

#function to clear contents of the entry box


#Driver Code for the GUI
if __name__ == '__main__':
    #create the gui window
    calwindow = Tk()

    #set the background color of the gui window
    calwindow.configure(bg = 'black' )
    #set the title of the gui window
    calwindow.title("Calculator")
    #set the configuration of the gui window
    calwindow.geometry("265x150")

    #StringVar is the variable class
    #we create and instance of this class
    equation = StringVar()

    #create the test entry box for expression
    entry_box = Entry(calwindow, textvariable = equation)

    #grid method is used to place widgets at perspective
    #positions in table like structure
    entry_box.grid(columnspan = 4, ipadx = 70)

    equation.set('')


    #Create buttons for the calculator and
    #put them at specific positioins on the window
    #when the button is clicked the following
    # command from the button will take place

    button7 = Button(calwindow, text = '7', fg = 'white', bg = 'black',
                     command = lambda: num_input(7,equation), height = 1, width = 7)
    button7.grid(row = 2, column = 0)
    button8 = Button(calwindow, text = '8', fg= 'white',bg = 'black',
                     command = lambda: num_input(8,equation), height = 1, width = 7)
    button8.grid(row = 2, column = 1)
    button9 = Button(calwindow, text = '9', fg = 'white', bg = 'black',
                     command = lambda: num_input(9, equation), height = 1, width = 7)
    button9.grid(row = 2, column = 2)
    button4 = Button(calwindow, text = '4', fg = 'white', bg = 'black',
                     command = lambda:  num_input(4,equation), height = 1, width = 7)
    button4.grid(row = 3, column = 0)
    button5 = Button(calwindow, text = '5', fg = 'white', bg = 'black',
                     command = lambda: num_input(5,equation), height = 1, width = 7)
    button5.grid(row = 3, column = 1)
    button6 = Button(calwindow, text = '6',fg = 'white',bg ='black',
                     command = lambda: num_input(6,equation), height = 1, width = 7)
    button6.grid(row = 3, column = 2)
    button1 = Button(calwindow,text = '1',fg = 'white',bg = 'black',
                     command = lambda: num_input(1,equation), height = 1, width = 7)
    button1.grid(row = 4,column = 0)
    button2 = Button(calwindow, text = '2',fg = 'white',bg = 'black',
                     command = lambda: num_input(2,equation), height = 1, width = 7)
    button2.grid(row = 4,column = 1)
    button3 = Button(calwindow,text = '3', fg = 'white',bg = 'black',
                     command = lambda: num_input(3,equation),height = 1, width = 7)
    button3.grid(row = 4, column = 2)
    button0 = Button(calwindow,text = '0',fg = 'white',bg = 'black',
                     command = lambda: num_input(0,equation),height = 1, width = 7)
    button0.grid(row = 5, column = 1)
    plus = Button(calwindow, text = '+',fg = 'white',bg = 'black',
                  command = lambda: num_input("+",equation), height = 1, width = 7)
    plus.grid( row = 2, column = 3)
    minus = Button(calwindow, text = '-',fg = 'white',bg = 'black',
                   command = lambda: num_input("-",equation), height = 1, width = 7)
    minus.grid(row = 3, column = 3)
    multi = Button(calwindow, text = '*',fg = 'white',bg = 'black',
                   command = lambda: num_input("*",equation), height = 1, width = 7)
    multi.grid(row = 4, column = 3)
    divid = Button(calwindow, text = '/',fg = 'white',bg = 'black',
                   command = lambda: num_input("/",equation), height = 1, width = 7)
    divid.grid(row = 5, column = 3)
    decimal = Button(calwindow,text = '.',fg = 'white',bg = 'black',
                     command = lambda: num_input(".",equation), height = 1, width =7)
    decimal.grid(row = 5, column = 2)
    equal = Button(calwindow, text = '=',fg = 'white',bg = 'black',\
                   command = lambda: finalexp(equation), height = 1, width = 7)
    equal.grid(row = 6, column = 3)
    clear = Button(calwindow, text='clear', fg='white', bg='black',
                   command=lambda: clear(equation), height=1, width=7)
    clear.grid(row=5, column=0)
    #calling calwindow main
if  __name__ == '__main__':
    calwindow.mainloop()