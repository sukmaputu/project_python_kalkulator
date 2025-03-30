from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Kalkulator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        
        # Entry untuk tampilan angka
        Entry(
            master, 
            width=17, 
            bg='#fff', 
            font=('Arial Bold', 28), 
            textvariable=self.equation, 
            justify='right'
        ).place(x=0, y=0)

        # Tombol angka dan operasi
        buttons = [
            ('7', 30, 100), ('8', 100, 100), ('9', 170, 100), ('/', 240, 100),
            ('4', 30, 170), ('5', 100, 170), ('6', 170, 170), ('*', 240, 170),
            ('1', 30, 240), ('2', 100, 240), ('3', 170, 240), ('-', 240, 240),
            ('C', 30, 310), ('0', 100, 310), ('=', 170, 310), ('+', 240, 310),
        ]
        
        for (text, x, y) in buttons:
            Button(
                master, 
                text=text, 
                width=5, 
                height=2, 
                font=('Arial', 18), 
                bg='#fff', 
                command=lambda t=text: self.show(t) if t not in ('C', '=') else (
                    self.clear() if t == 'C' else self.solve()
                )
            ).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

# Menjalankan aplikasi
root = Tk()
calculator = Calculator(root)
root.mainloop()
