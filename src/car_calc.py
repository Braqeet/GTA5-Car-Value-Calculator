import tkinter as tk
from tkinter import messagebox


def calculate_full_value():
    try:
        base_value = float(entry_base_value.get())
        sell_value = float(entry_sell_value.get())

        # Calculate base resale value and upgrade values
        base_resale_value = 0.60 * base_value
        upgrade_resale_value = sell_value - base_resale_value
        full_upgrade_value = upgrade_resale_value / 0.50

        # Calculate full value
        full_value = base_value + full_upgrade_value

        # Display result in the label
        label_result.config(text=f"Full car value (including upgrades): ${full_value:,.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")


# Create the main application window
root = tk.Tk()
root.title("Car Value Calculator")
root.geometry("400x300")

# Labels and input fields for purchase price and sell price
label_base_value = tk.Label(root, text="Enter the purchase price:")
label_base_value.pack(pady=10)

entry_base_value = tk.Entry(root)
entry_base_value.pack(pady=5)

label_sell_value = tk.Label(root, text="Enter the sell price:")
label_sell_value.pack(pady=10)

entry_sell_value = tk.Entry(root)
entry_sell_value.pack(pady=5)

# Button to calculate the full car value
btn_calculate = tk.Button(root, text="Calculate", command=calculate_full_value)
btn_calculate.pack(pady=20)

# Label to display the result
label_result = tk.Label(root, text="")
label_result.pack(pady=20)

# Run the main application loop
root.mainloop()
