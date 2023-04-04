import tkinter as tk
import socket

# create the main window
root = tk.Tk()
root.title("Networking App")
root.geometry("300x150")

# create a label widget
label = tk.Label(root, text="Enter a URL:")
label.pack(pady=10)

# create an entry widget
entry = tk.Entry(root)
entry.pack()

# create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# create a button to look up the IP address
def lookup_ip():
    try:
        url = entry.get()
        ip_address = socket.gethostbyname(url)
        result_label.config(text=f"The IP address of {url} is {ip_address}")
    except socket.gaierror:
        result_label.config(text="Invalid URL")

# create a button to clear the result
def clear_result():
    result_label.config(text="")

# create a button to exit the app
def exit_app():
    root.destroy()

# create a button to look up the IP address
lookup_button = tk.Button(root, text="Lookup", command=lookup_ip)
lookup_button.pack(side=tk.LEFT, padx=10)

# create a button to clear the result
clear_button = tk.Button(root, text="Clear", command=clear_result)
clear_button.pack(side=tk.LEFT)

# create a button to exit the app
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=10)

# run the main event loop
root.mainloop()
