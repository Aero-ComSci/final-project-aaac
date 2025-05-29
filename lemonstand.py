import tkinter as tk

# Pricing dictionary
prices = {
    "Small": 2.00,
    "Medium": 3.00,
    "Large": 4.00
}

order = []

def add_to_order(size, no_ice):
    """Adds an item to the order list."""
    ice_status = "No Ice" if no_ice.get() else "With Ice"
    order.append((size, prices[size], ice_status))
    update_receipt()

def update_receipt():
    """Updates the receipt field."""
    receipt_text.set("\n".join([f"{item[0]} - ${item[1]:.2f} ({item[2]})" for item in order]))

def calculate_total():
    """Calculates and shows the total cost."""
    total = sum(item[1] for item in order)
    total_label.config(text=f"Total: ${total:.2f}")

# Create main window
root = tk.Tk()
root.title("Lemonade Stand")

# Cup size selection
size_label = tk.Label(root, text="Choose cup size:")
size_label.pack()

size_var = tk.StringVar()
size_var.set("Small")  # Default selection
sizes = ["Small", "Medium", "Large"]
size_menu = tk.OptionMenu(root, size_var, *sizes)
size_menu.pack()

# No ice option
no_ice_var = tk.BooleanVar()
no_ice_checkbox = tk.Checkbutton(root, text="No Ice", variable=no_ice_var)
no_ice_checkbox.pack()

# Add to order button
add_button = tk.Button(root, text="Add to Order", command=lambda: add_to_order(size_var.get(), no_ice_var))
add_button.pack()

# Receipt field
receipt_text = tk.StringVar()
receipt_label = tk.Label(root, textvariable=receipt_text, relief="sunken", width=40, height=6, anchor="w", justify="left")
receipt_label.pack(pady=10)

# Total button
total_button = tk.Button(root, text="Show Total", command=calculate_total)
total_button.pack()

# Total label
total_label = tk.Label(root, text="Total: $0.00")
total_label.pack()

# Run application
root.mainloop()
