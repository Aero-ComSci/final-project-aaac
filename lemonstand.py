import tkinter as tk

prices = {
    "Small": 2.00,
    "Medium": 3.00,
    "Large": 4.00
}

order = []

def add_to_order(size, ice, grape):
    """Adds an item to the order list."""
    ice_status = "Ice" if ice.get() else "No Ice"
    grape_status = "With 1 Grape" if grape.get() else "No Grape"
    item_price = prices[size] + (0.50 if grape.get() else 0)
    order.append((size, item_price, ice_status, grape_status))
    update_receipt()

def update_receipt():
    """Updates the receipt field."""
    receipt_lines = []
    for item in order:
        line = f"{item[0]} - ${item[1]:.2f} ({item[2]}, {item[3]})"
        receipt_lines.append(line)
    receipt_text.set("\n".join(receipt_lines))

def calculate_total():
    """Calculates and shows the total cost."""
    total = sum(item[1] for item in order)
    total_label.config(text=f"Total: ${total:.2f}")

root = tk.Tk()
root.title("Lemonade Stand")

size_label = tk.Label(root, text="Choose cup size:")
size_label.pack()

size_var = tk.StringVar()
size_var.set("Small")
sizes = ["Small", "Medium", "Large"]
size_menu = tk.OptionMenu(root, size_var, *sizes)
size_menu.pack()

ice_var = tk.BooleanVar()
ice_checkbox = tk.Checkbutton(root, text="Ice", variable=ice_var)
ice_checkbox.pack()

grape_var = tk.BooleanVar()
grape_checkbox = tk.Checkbutton(root, text="Include 1 Grape (+$0.50)", variable=grape_var)
grape_checkbox.pack()

add_button = tk.Button(root, text="Add to Order", command=lambda: add_to_order(size_var.get(), ice_var, grape_var))
add_button.pack()

receipt_text = tk.StringVar()
receipt_label = tk.Label(root, textvariable=receipt_text, relief="sunken", width=40, height=6, anchor="w", justify="left")
receipt_label.pack(pady=10)

total_button = tk.Button(root, text="Show Total", command=calculate_total)
total_button.pack()

total_label = tk.Label(root, text="Total: $0.00")
total_label.pack()

root.mainloop()
