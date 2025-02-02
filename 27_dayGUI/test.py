import tkinter as tk
window = tk.Tk()
window.title("Celsius to Fahrenheit converter")
window.minsize(width=300, height=300)

def button_click():
    temp = float(input.get())
    res = round(temp * 1.8 + 32, 2)
    my_labelRES.config(text=res)


#LABEL
my_label = tk.Label(text="Temp of Celsius", font=("Arial", 15, "bold"))
my_label.grid(column=0, row=0)

my_labelF = tk.Label(text="Temp of Fahrenheit =", font=("Arial", 15, "bold"))
my_labelF.grid(column=0, row=2)

my_labelRES = tk.Label(text="", font=("Arial", 15, "bold"))
my_labelRES.grid(column=1, row=2)
# Button
button = tk.Button(text="Click here", command=button_click)
button.grid(column=0, row=1)


# Entry
input = tk.Entry(window)
input.grid(column=2, row=0)




























window.mainloop()