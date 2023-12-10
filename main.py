import tkinter as tk


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")
        self.resizable(True, True)
        self.maxsize(400, 500)
        self.minsize(250, 300)
        self.bind("<Key>", self.on_key_press)
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(
            self,
            textvariable=self.result_var,
            font=("Arial", 18),
            bd=10,
            relief=tk.GROOVE,
            justify="right",
        )
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
        ]

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i + 1, weight=1)

        row_val, col_val = 1, 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col):
        bg_color = "orange" if text in ["/", "*", "-", "+", "="] else None
        button = tk.Button(
            self,
            text=text,
            padx=20,
            pady=20,
            font=("Arial", 14),
            command=lambda t=text: self.on_button_click(t),
            bg=bg_color,
        )
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Erro")
        else:
            self.result_var.set(current_text + button)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in ["/", "*", "-", "+", "=", "."]:
            self.on_button_click(key)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
