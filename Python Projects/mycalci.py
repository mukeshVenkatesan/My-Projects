from tkinter import *
cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
def btn_click(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btn_clear():
    global operator
    operator=""
    text_input.set("")
def btn_equals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)

txt_disp=Entry(cal,font=("arial",20,'bold'),textvariable=text_input,bd=30,
               insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)
btn7=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='7',command=lambda :btn_click(7)).grid(row=1,column=0)
btn8=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='8',command=lambda :btn_click(8)).grid(row=1,column=1)
btn9=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='9',command=lambda :btn_click(9)).grid(row=1,column=2)
btn_plus=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='+',command=lambda :btn_click("+")).grid(row=1,column=3)

btn4=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='4',command=lambda :btn_click(4)).grid(row=2,column=0)
btn5=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='5',command=lambda :btn_click(5)).grid(row=2,column=1)
btn6=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='6',command=lambda :btn_click(6)).grid(row=2,column=2)
btn_minus=Button(cal,padx=18,pady=16,bd=10,bg='black',fg='powder blue',font=('arial',20,'bold'),text='-',command=lambda:btn_click('-')).grid(row=2,column=3)

btn1=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='1',command=lambda :btn_click(1)).grid(row=3,column=0)
btn2=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='2',command=lambda :btn_click(2)).grid(row=3,column=1)
btn3=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='3',command=lambda :btn_click(3)).grid(row=3,column=2)
btn_div=Button(cal,padx=18,pady=16,bd=10,bg='black',fg='powder blue',font=('arial',20,'bold'),text='/',command=lambda:btn_click('/')).grid(row=3,column=3)

btn0=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='0',command=lambda :btn_click(0)).grid(row=4,column=0)
btn_clr=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='c',command=btn_clear).grid(row=4,column=1)
btnmultiply=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='*',command=lambda :btn_click('*')).grid(row=4,column=2)
btnequal=Button(cal,padx=18,pady=16,bd=8,bg='black',fg='powder blue',font=('arial',20,'bold'),text='=',command=btn_equals).grid(row=4,column=3)
cal.mainloop()