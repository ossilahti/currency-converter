import tkinter as tk
from currency_converter import CurrencyConverter

c = CurrencyConverter()


def to_dollars():
    eur_to_dollars = c.convert(100, 'EUR', 'USD')
    print(eur_to_dollars)


def to_pounds():
    eur_to_pounds = c.convert(100, 'EUR', 'GBP')
    print(eur_to_pounds)


root = tk.Tk()

inputField = tk.Entry(root)
inputField.grid(row=0, column=0, padx=10, pady=10)
inputField.focus_set()

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=1, column=0)

to_usd_button = tk.Button(buttons_frame, text="Convert to USD",
                          background="black",
                          foreground="white", command=to_dollars())
to_usd_button.grid(row=1, column=0, padx=10, pady=10)

to_gbp_button = tk.Button(buttons_frame, text="Convert to GBP",
                          background="black",
                          foreground="white", command=to_pounds())
to_gbp_button.grid(row=1, column=1, padx=10, pady=10)
root.mainloop()





