import tkinter as tk
from forex_python.converter import CurrencyRates


def convert_dollars():
    convert_usd = c.get_rate('EUR', 'USD')
    input_field = int(entry.get()) * convert_usd
    label1 = tk.Label(root, text=input_field)
    label1.grid(row=2, column=0)


def convert_pounds():
    convert_gbp = c.get_rate('EUR', 'GBP')
    input_field = int(entry.get()) * convert_gbp
    label1 = tk.Label(root, text=input_field)
    label1.grid(row=2, column=1)


c = CurrencyRates()
root = tk.Tk()
root.title("Currency Converter")

entry = tk.Entry(root, width=33)
entry.grid(columnspan=2, padx=10, pady=10)

to_usd_button = tk.Button(root, text="Convert to USD", command=convert_dollars)
to_usd_button.grid(row=1, column=0, padx=10, pady=10)

to_gbp_button = tk.Button(root, text="Convert to GBP", command=convert_pounds)
to_gbp_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()





