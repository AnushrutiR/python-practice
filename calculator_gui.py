import tkinter as tk
window=tk.Tk()
window.title("Calculator")
window.geometry("300x400")
display=tk.Entry(window,font="Arial 20",justify="right")
display.grid(row=0,column=0,columnspan=4,sticky="nsew")
def click(value):
    if value == 'C':
        display.delete(0, tk.END)
    elif value == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, value)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button, font="Arial 15", width=5, height=2, command=lambda b=button: click(b))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
window.mainloop()
