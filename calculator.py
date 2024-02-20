import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.current_number = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(root, textvariable=self.result_var, bg='pink',font=("Arial",18), bd=5, relief="ridge", width=15, anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2,bg='gray', command=lambda btn=button: self.button_click(btn)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        if button == 'C':
            self.current_number = ""
            self.result_var.set("0")
        elif button == '=':
            try:
                result = str(eval(self.current_number))
                self.result_var.set(result)
                self.current_number = result
            except:
                self.result_var.set("Error")
                self.current_number = ""
        else:
            if self.result_var.get() == "Error":
                self.result_var.set("0")
                self.current_number = ""
            self.current_number += button
            self.result_var.set(self.current_number)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
