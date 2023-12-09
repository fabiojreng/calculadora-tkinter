import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")
        self.resizable(False, False)
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entrada para exibir os números e resultados
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 18), bd=10, relief=tk.GROOVE, justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Botões
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Erro")
        else:
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
