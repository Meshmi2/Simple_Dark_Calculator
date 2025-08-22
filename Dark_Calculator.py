import tkinter as tk
import random

class CalcolatriceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calcolatrice Tema Scuro")
        master.geometry("320x320")
        master.resizable(False, False)
        master.configure(bg="#222222")
        self.display = tk.Entry(master, width=20, font=("Arial", 18), borderwidth=2, relief="groove", bg="#333333", fg="#FFFFFF")
        self.display.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        self.dark_colors = [
            "#2D2D2D", "#3C3F41", "#23272E", "#282C34",
            "#1A1A1A", "#212121", "#343434", "#44475A",
            "#373737", "#2E3440", "#242424", "#22223B",
            "#1B1B1B", "#2C2C2C", "#292929", "#383838"
        ]

        self.button_widgets = []
        for idx, (text, row, col) in enumerate(self.buttons):
            btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14),
                            bg=self.dark_colors[idx], fg="#FFFFFF",
                            command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.button_widgets.append(btn)

    def recolor_buttons(self):
        for btn in self.button_widgets:
            btn.configure(bg=random.choice(self.dark_colors))

    def on_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
            self.recolor_buttons()
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalcolatriceGUI(root)
    root.mainloop()