import tkinter as tk
from forex_python.converter import CurrencyRates
from tkinter import messagebox

# Initialize currency converter
c = CurrencyRates()

# Function to perform conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from.get().upper()
        to_currency = entry_to.get().upper()
        result = c.convert(from_currency, to_currency, amount)
        label_result.config(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From Currency (e.g., USD):").grid(row=1, column=0, padx=10, pady=10)
entry_from = tk.Entry(root)
entry_from.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="To Currency (e.g., EUR):").grid(row=2, column=0, padx=10, pady=10)
entry_to = tk.Entry(root)
entry_to.grid(row=2, column=1, padx=10, pady=10)

btn_convert = tk.Button(root, text="Convert", command=convert_currency)
btn_convert.grid(row=3, column=0, columnspan=2, pady=20)

label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
