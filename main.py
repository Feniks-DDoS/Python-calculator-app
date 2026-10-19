import tkinter as tk
root = tk.Tk()

display = tk.Entry(root, width=20, font=("Arial", 30) ,bg="white", state="readonly" ,justify="right", fg="black", bd=3)
display.grid(row=0, column=0, columnspan=4, sticky="we")


def state_normal():
    display.config(state="normal")

def state_readonly():
    display.config(state="readonly")

def main():
    root.title("Calculator")
    root.resizable(False, False)
    home_icon = tk.PhotoImage(file="Icon/calculator.png")
    root.iconphoto(False, home_icon)

    root.geometry("350x450+400+400")
    root.config(bg="white")

    digits_array = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "C", "="]
    operators_array = ["+", "-", "*", "/"]

    for i in range(4):
        for j in range(3): 
            btn_clear = digits_array[j + 3 * i]
            btn_calculate = digits_array[j + 3 * i]
            if btn_clear == "C":
                btn_clear = tk.Button(root, text="C", width=6, height=4, activebackground="navy", font=("Arial", 15),command=clear_display)
                btn_clear.grid(row=i + 1, column=j, sticky="nsew")
            elif btn_calculate == "=":
                btn_calculate = tk.Button(root, text="=", width=6, height=4, activebackground="navy", font=("Arial", 15), command=calculate)
                btn_calculate.grid(row=i + 1, column=j, sticky="nsew")
            else:
                tk.Button(root, text=digits_array[j + 3 * i], width=6, height=4, font=("Arial", 15), activebackground="navy",
                      command=lambda value=digits_array[j + 3 * i]: insert_value(value)
                      ).grid(row=i + 1, column=j, sticky="nsew")
           

    for i in range(4):
        tk.Button(root, text=operators_array[i], width=6, height=4, bg="navy", fg="white", font=("Arial", 15),
                  command=lambda value=operators_array[i]: insert_value(value)
                  ).grid(row=i + 1, column=3, sticky="nsew")

    for j in range(4):
        root.grid_columnconfigure(j, minsize=60, weight=1)

    for i in range(5):
        root.grid_rowconfigure(i, minsize=60, weight=1)

    root.mainloop()

def clear_display():
    state_normal()

    display.delete(0, tk.END)

    state_readonly()


def calculate():
    expression = display.get()

    try:
        result = eval(expression)
    except:
        result = "Error"

    state_normal()

    display.delete(0, tk.END)
    display.insert(tk.END, result)

    state_readonly()


def insert_value(value):
    current = display.get() 
    
    if current == "0" and value.isdigit():
        
        state_normal()

        display.delete(0, tk.END)      
        display.insert(tk.END, value) 

        state_readonly()
        return
    
    if value == "0" and current == "0":
        return
    
    state_normal()

    display.insert(tk.END, value)
    
    state_readonly()


if __name__ == "__main__":
    main()