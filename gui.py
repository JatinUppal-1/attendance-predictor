import tkinter as tk
from tkinter import messagebox
from utils.attendance import calculate_attendance

def get_result():
    try:
        # Get data from the boxes and convert to int
        c = int(entry_conducted.get())
        a = int(entry_attended.get())
        m = int(entry_miss.get())
        
        res = calculate_attendance(c, a, m)
        res = int(res)
        
        # Display the result
        label_result.config(text=f"Predicted Attendance: {res}%", fg="blue")
        
        # Show alert based on percentage
        if res < 75:
            messagebox.showwarning("Status", "DETAIN: Attendance below 75%!")
        elif 75 <= res < 80:
            messagebox.showinfo("Status", "Warning: Likely to be detained.")
        else:
            messagebox.showinfo("Status", "Safe: You are good to go!")
            
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers only!")

# --- Setup the Window ---
root = tk.Tk()
root.title("CEC Attendance Predictor")
root.geometry("400x300")

# --- UI Elements ---
tk.Label(root, text="Classes Conducted:").pack(pady=5)
entry_conducted = tk.Entry(root)
entry_conducted.pack()

tk.Label(root, text="Classes Attended:").pack(pady=5)
entry_attended = tk.Entry(root)
entry_attended.pack()

tk.Label(root, text="Planned Misses:").pack(pady=5)
entry_miss = tk.Entry(root)
entry_miss.pack()

tk.Button(root, text="Calculate Status", command=get_result, bg="green").pack(pady=20)

label_result = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
label_result.pack()

root.mainloop()