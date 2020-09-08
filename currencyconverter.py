import tkinter as tk
from forex_python.converter import CurrencyRates


def convert():
    input_field = entry.get()
    label1 = tk.Label(root, text=input_field)
    label1.grid()
    print(input_field)


c = CurrencyRates()
root = tk.Tk()
root.title("Currency Converter")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=10, pady=10)

to_usd_button = tk.Button(root, text="Convert to USD", command=convert)
to_usd_button.grid(row=1, column=0, padx=10, pady=10)

to_gbp_button = tk.Button(root, text="Convert to GBP", command=convert)
to_gbp_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()





