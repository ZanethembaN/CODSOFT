import tkinter as tk
from colours import *
from math import sqrt, sin, cos, tan, log, radians

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"CALCULATOR")
        self.root.geometry("300x300")


        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=('Helvetica', 16), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'sin', 'cos', 'tan',
            'log', '(', ')', 'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def button_click(self, button):
        current_text = self.entry_var.get()

        if button == "=":
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button == "C":
            self.entry_var.set("")

        elif button == "sqrt":
            self.entry_var.set(sqrt(float(current_text)))

        elif button == "sin":
            self.entry_var.set(sin(radians(float(current_text))))

        elif button == "cos":
            self.entry_var.set(cos(radians(float(current_text))))

        elif button == "tan":
            self.entry_var.set(tan(radians(float(current_text))))

        elif button == "log":
            self.entry_var.set(log(float(current_text)))

        else:
            self.entry_var.set(current_text + button)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
