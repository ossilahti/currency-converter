import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


def converter(from_curr, to_curr):
    convert = c.get_rate(from_curr, to_curr)
    input_field = int(entry.get()) * convert
    label = tk.Label(root, text=input_field)
    label.grid(row=2, column=1)


def callback_func(event):
    converter(from_currency.get(), to_currency.get())


c = CurrencyRates()
root = tk.Tk()
root.geometry('250x300')
root.title("Currency Converter")

entry = tk.Entry(root, width=33, borderwidth=3)
entry.grid(columnspan=3, padx=10, pady=10)

from_currency = tk.StringVar()
from_currencies = ttk.Combobox(root, width=10, textvariable=from_currency)

# Adding combobox drop down list
from_currencies['values'] = ('EUR', 'USD', 'GBP')
from_currencies.grid(column=1, row=15)

# Shows EUROs as a default value
from_currencies.current(0)
from_currencies.bind("<<ComboboxSelected>>", callback_func)

to_currency = tk.StringVar()
to_currencies = ttk.Combobox(root, width=10, textvariable=to_currency)

# Adding combobox drop down list
to_currencies['values'] = ('EUR', 'USD', 'GBP')
to_currencies.grid(column=2, row=15)

# Shows DOLLARs as a default value
to_currencies.current(1)
to_currencies.bind("<<ComboboxSelected>>", callback_func)


root.mainloop()





