import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


# Converts the currencies and concludes the result as a label.
def converter(from_curr, to_curr):
    convert = c.get_rate(from_curr, to_curr)
    input_field = int(entry.get()) * convert
    label = tk.Label(root, text=input_field)
    label.grid(row=3, columnspan=3)


# Is a callback function for the combobox event bind.
def callback_func(event):
    converter(from_currency.get(), to_currency.get())


# Swaps the from currency and to currency's values.
def swap():
    temp = from_currencies.get()
    from_currencies.set(to_currencies.get())
    to_currencies.set(temp)


# ---------------------------------------------------------------------------------


# Initializes the window
c = CurrencyRates()
root = tk.Tk()
root.geometry('250x300')
root.title("Currency Converter")

# Entry/text box
entry = tk.Entry(root, width=33, borderwidth=3)
entry.grid(columnspan=3, padx=10, pady=10)

# Makes the combobox for from currencies
from_currency = tk.StringVar()
from_currencies = ttk.Combobox(root, width=10, textvariable=from_currency, state="readonly")

# Adding combobox drop down list
from_currencies['values'] = ('EUR', 'USD', 'GBP')
from_currencies.grid(column=1, row=1)
from_curr_label = tk.Label(root, text="From: ")
from_curr_label.grid(row=1, column=0)

# Shows EUROs as a default value
from_currencies.current(0)
from_currencies.bind("<<ComboboxSelected>>", callback_func)

# Makes the combobox for to currencies
to_currency = tk.StringVar()
to_currencies = ttk.Combobox(root, width=10, textvariable=to_currency, state="readonly")

# Adding combobox drop down list
to_currencies['values'] = ('EUR', 'USD', 'GBP')
to_currencies.grid(column=1, row=2)
to_curr_label = tk.Label(root, text="To: ")
to_curr_label.grid(row=2, column=0)

# Shows DOLLARs as a default value
to_currencies.current(1)
to_currencies.bind("<<ComboboxSelected>>", callback_func)

swap = tk.Button(root, text="Swap", command=swap)
swap.grid(row=1, column=2)

root.mainloop()
