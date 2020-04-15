
import tkinter as tk
# Declarando los recursos que se van a utilizar en el programa
def suma():
    ans.set("suma= " + str(float(nu1.get())+ float(nu2.get())))
def resta():
    ans.set("resta= " + str(float(nu1.get())- float(nu2.get())))
def multiplicacion():
    ans.set("multiplicacion= " + str(float(nu1.get()) * float(nu2.get())))
def division():
    ans.set("division= " + str(float(nu1.get())/ float(nu2.get())))
def limpiar():
    ans.set("")
    nu1.set("")
    nu2.set("")

root = tk.Tk()

root.geometry('250x200')
root.title('Calculadora')
root.configure(bg="#61d4b3")

nu1 = tk.StringVar()
tk.Entry(root, textvariable=nu1 ).place(x=0,y=0)
nu2 = tk.StringVar()
tk.Entry(root, textvariable=nu2 ).place(x=130,y=0)
ans=tk.StringVar()
tk.Entry(root, textvariable=ans).place(x=60,y=145)

tk.Button(root, text='Sumar', bd=0, command=suma,bg="#fdd365",padx=42,pady=5).place(x=0, y=25)
tk.Button(root, text='Resta', bd=0, command=resta,bg="#fdd365",padx=42,pady=5).place(x=130, y=25)
tk.Button(root, text='Multiplicar', bd=0, command=multiplicacion,bg="#fdd365",padx=30,pady=5).place(x=0, y=65)
tk.Button(root, text='Dividir', bd=0, command=division,bg="#fdd365",padx=42,pady=5).place(x=130, y=65)
tk.Button(root, text='limpiar', bd=0, command=limpiar,bg="#fb8d62",padx=110,pady=5).place(x=0, y=105)
tk.Button(root, text='Salir', bd=0, command=root.destroy,padx=50,pady=4, bg="#009688").place(x=60, y=169)
root.mainloop()