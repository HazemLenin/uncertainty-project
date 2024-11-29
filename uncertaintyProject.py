import tkinter as tk
from tkinter import ttk, messagebox

# Global variables
alternatives = []
root = tk.Tk()
root.title("Decision Making Under Uncertainty")
root.geometry("800x600")

# Create main sections
input_section = ttk.LabelFrame(root, text="Add New Alternative")
input_section.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

results_section = ttk.LabelFrame(root, text="Analysis")
results_section.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

# Make window responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

def add_alternative():
    name = name_entry.get().strip()
    values_text = values_entry.get().strip()
    
    if not name or not values_text:
        messagebox.showwarning("Missing Data", "Please enter both name and values!")
        return
    
    try:
        values = [float(x.strip()) for x in values_text.split(',')]
        alternatives.append({
            'name': name,
            'values': values
        })
        
        # Update display
        alternatives_display.delete(1.0, 'end')
        for alt in alternatives:
            alternatives_display.insert('end', f"{alt['name']}: {alt['values']}\n")
        
        # Clear inputs
        name_entry.delete(0, 'end')
        values_entry.delete(0, 'end')
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers separated by commas")

def check_data():
    if not alternatives:
        messagebox.showwarning("No Data", "Please add some alternatives first!")
        return False
    return True

def calculate_maximax():
    if not check_data():
        return
    
    # Find best alternative and its maximum value
    best_value = float('-inf')
    best_alt = None
    
    for alt in alternatives:
        max_value = max(alt['values'])
        if max_value > best_value:
            best_value = max_value
            best_alt = alt['name']
    
    result_var.set(f"Maximax Result: {best_value:.2f}\nBest Alternative: {best_alt}")

def calculate_maximin():
    if not check_data():
        return
    
    # Find best alternative and its minimum value
    best_value = float('-inf')
    best_alt = None
    
    for alt in alternatives:
        min_value = min(alt['values'])
        if min_value > best_value:
            best_value = min_value
            best_alt = alt['name']
    
    result_var.set(f"Maximin Result: {best_value:.2f}\nBest Alternative: {best_alt}")

def get_alpha():
    dialog = tk.Toplevel(root)
    dialog.title("Hurwicz Alpha")
    dialog.geometry("300x150")
    dialog.transient(root)
    dialog.grab_set()
    
    alpha_var = tk.StringVar()
    result = {'alpha': None}
    
    def validate_and_close():
        try:
            alpha = float(alpha_var.get())
            if 0 <= alpha <= 1:
                result['alpha'] = alpha
                dialog.destroy()
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a number between 0 and 1")
    
    ttk.Label(dialog, text="Enter optimism coefficient (α)\nBetween 0 and 1:", justify='center').pack(pady=10)
    entry = ttk.Entry(dialog, textvariable=alpha_var)
    entry.pack(pady=5)
    entry.focus()
    ttk.Button(dialog, text="OK", command=validate_and_close).pack(pady=10)
    
    dialog.wait_window()
    return result['alpha']

def calculate_hurwicz():
    if not check_data():
        return
    
    alpha = get_alpha()
    if alpha is None:
        return
    
    # Find best alternative using Hurwicz criterion
    best_value = float('-inf')
    best_alt = None
    
    for alt in alternatives:
        hurwicz_value = max(alt['values']) * alpha + min(alt['values']) * (1-alpha)
        if hurwicz_value > best_value:
            best_value = hurwicz_value
            best_alt = alt['name']
    
    result_var.set(f"Hurwicz Result (α={alpha:.2f}): {best_value:.2f}\nBest Alternative: {best_alt}")

def calculate_laplace():
    if not check_data():
        return
    
    # Find best alternative using average value
    best_value = float('-inf')
    best_alt = None
    
    for alt in alternatives:
        avg_value = sum(alt['values'])/len(alt['values'])
        if avg_value > best_value:
            best_value = avg_value
            best_alt = alt['name']
    
    result_var.set(f"Laplace Result: {best_value:.2f}\nBest Alternative: {best_alt}")

# Create input widgets
name_frame = ttk.Frame(input_section)
name_frame.pack(fill='x', pady=5)

ttk.Label(name_frame, text="Name:").pack(side='left')
name_entry = ttk.Entry(name_frame)
name_entry.pack(side='left', padx=5, fill='x', expand=True)

values_frame = ttk.Frame(input_section)
values_frame.pack(fill='x', pady=5)

ttk.Label(values_frame, text="Values:").pack(side='left')
values_entry = ttk.Entry(values_frame)
values_entry.pack(side='left', padx=5, fill='x', expand=True)

ttk.Label(input_section, 
         text="Enter comma-separated numbers (e.g., 10, 20, 30)",
         font=('Arial', 8, 'italic')).pack(pady=(0, 10))

ttk.Button(input_section, text="Add Alternative", command=add_alternative).pack(pady=5)

alternatives_display = tk.Text(input_section, height=12, width=40, font=('Consolas', 10))
alternatives_display.pack(pady=10, padx=5, fill='both', expand=True)

# Create results widgets
methods_frame = ttk.LabelFrame(results_section, text="Choose Method")
methods_frame.pack(fill='x', padx=5, pady=5)

# Create calculation buttons
maximax_btn = ttk.Button(methods_frame, text="Maximax", command=calculate_maximax, width=20)
maximax_btn.grid(row=0, column=0, padx=5, pady=5)

maximin_btn = ttk.Button(methods_frame, text="Maximin", command=calculate_maximin, width=20)
maximin_btn.grid(row=0, column=1, padx=5, pady=5)

hurwicz_btn = ttk.Button(methods_frame, text="Hurwicz", command=calculate_hurwicz, width=20)
hurwicz_btn.grid(row=1, column=0, padx=5, pady=5)

laplace_btn = ttk.Button(methods_frame, text="Laplace", command=calculate_laplace, width=20)
laplace_btn.grid(row=1, column=1, padx=5, pady=5)

# Results display
results_display = ttk.LabelFrame(results_section, text="Results")
results_display.pack(fill='both', expand=True, padx=5, pady=10)

result_var = tk.StringVar(value="Results will appear here")
result_label = ttk.Label(results_display, textvariable=result_var, font=('Arial', 12))
result_label.pack(pady=20)

# Start the application
if __name__ == "__main__":
    root.mainloop()
    
