import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


# Converts the currencies and concludes the result as a label.
def converter(from_curr, to_curr):
    convert = c.get_rate(from_curr, to_curr)
    input_field = int(entry.get()) * convert
    label = tk.Label(root, text=input_field, font=("Georgia", 15))
    label.grid(row=4, column=1)
    label2 = tk.Label(root, text=to_curr, font=("Georgia", 15))
    label2.grid(row=4, column=2)


# Is a callback function for the button 'Convert'.
def callback():
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
root.geometry('300x300')
root.title("Currency Converter")

# A label to the top of the window
banner_label = tk.Label(root, text="Currency Converter 1.0", font=("Georgia", 15), fg="green", padx=10, pady=10)
banner_label.grid(row=0, columnspan=3)

# Entry/text box
entry = tk.Entry(root, width=13)
entry.grid(row=3, column=1, padx=10, pady=10)

# Makes the combobox for from currencies
from_currency = tk.StringVar()
from_currencies = ttk.Combobox(root, width=10, textvariable=from_currency, state="readonly")

# Adding combobox drop down list
from_currencies['values'] = ('EUR', 'USD', 'GBP')
from_currencies.grid(column=1, row=1)
from_curr_label = tk.Label(root, text="From: ", padx=10, font=("Arial", 10))
from_curr_label.grid(row=1, column=0)

# Shows EUROs as a default value
from_currencies.current(0)

# Makes the combobox for to currencies
to_currency = tk.StringVar()
to_currencies = ttk.Combobox(root, width=10, textvariable=to_currency, state="readonly")

# Adding combobox drop down list
to_currencies['values'] = ('EUR', 'USD', 'GBP')
to_currencies.grid(column=1, row=2)
to_curr_label = tk.Label(root, text="To: ", padx=10, font=("Arial", 10))
to_curr_label.grid(row=2, column=0)

# Shows DOLLARs as a default value
to_currencies.current(1)

# Makes the 'Swap' -button
swap = tk.Button(root, text="Swap", command=swap, width=7, font=("Arial", 9))
swap.grid(row=2, column=2)

# Makes the 'Convert' -button
convert_button = tk.Button(root, text="Convert", command=callback, width=7, font=("Arial", 9))
convert_button.grid(row=3, column=2)

root.mainloop()
