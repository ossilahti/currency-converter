import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


def convert_dollars():
    convert_usd = c.get_rate('EUR', 'USD')
    input_field = int(entry.get()) * convert_usd
    label1 = tk.Label(root, text=input_field)
    label1.grid(row=2, column=1)


def convert_pounds():
    convert_gbp = c.get_rate('EUR', 'GBP')
    input_field = int(entry.get()) * convert_gbp
    label2 = tk.Label(root, text=input_field)
    label2.grid(row=2, column=2)


def callback_func(event):
    print("This is supposed to print values")
    if n.get() == 'EUR' and n1.get() == 'USD':
        convert_usd = c.get_rate('EUR', 'USD')
        input_field = int(entry.get()) * convert_usd
        label1 = tk.Label(root, text=input_field)
        label1.grid(row=2, column=1)
    if n.get() == 'EUR' and n1.get() == 'GBP':
        convert_gbp = c.get_rate('EUR', 'GBP')
        input_field = int(entry.get()) * convert_gbp
        label2 = tk.Label(root, text=input_field)
        label2.grid(row=2, column=2)


c = CurrencyRates()
root = tk.Tk()
root.geometry('250x300')
root.title("Currency Converter")

entry = tk.Entry(root, width=33, borderwidth=3)
entry.grid(columnspan=3, padx=10, pady=10)

to_usd_button = tk.Button(root, text="Convert to USD", command=convert_dollars)
to_usd_button.grid(row=1, column=1, padx=10, pady=10)

to_gbp_button = tk.Button(root, text="Convert to GBP", command=convert_pounds)
to_gbp_button.grid(row=1, column=2, padx=10, pady=10)


n = tk.StringVar()
from_currencies = ttk.Combobox(root, width=10, textvariable=n)

# Adding combobox drop down list
from_currencies['values'] = ('EUR', 'USD', 'GBP')
from_currencies.grid(column=1, row=15)

# Shows EUROs as a default value
from_currencies.current(0)
from_currencies.bind("<<ComboboxSelected>>", callback_func)


n1 = tk.StringVar()
to_currencies = ttk.Combobox(root, width=10, textvariable=n1)

# Adding combobox drop down list
to_currencies['values'] = ('EUR', 'USD', 'GBP')
to_currencies.grid(column=2, row=15)

# Shows DOLLARs as a default value
to_currencies.current(1)
to_currencies.bind("<<ComboboxSelected>>", callback_func)


root.mainloop()





