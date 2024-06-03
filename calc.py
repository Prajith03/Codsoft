import tkinter as tk

root = tk.Tk()
root.title('Arithmetic Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)

ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=4, padx=10, pady=10, sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')

class ArithmeticCalculator:
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except Exception:
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg="red", width=6, height=2,
                                highlightbackground='#ADD8E6', highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='n' +
                       's'+'e' + 'w', padx=10, pady=10)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

btn_CE = tk.Button(root, text='CLEAR', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg="#000000",
                  highlightbackground='#ADD8E6', highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_add.grid(row=1, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sub.grid(row=2, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_mul.grid(row=3, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_div.grid(row=4, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

if __name__ == '__main__':
    sc_app = ArithmeticCalculator()
    root.mainloop()
