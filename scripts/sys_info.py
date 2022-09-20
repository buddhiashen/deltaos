from tkinter import *
import platform



root = Tk()
root.title("DELTA OS - System Information")
root.iconbitmap('icons/stats.ico')
root.geometry("600x200")

info = f"System: {platform.system()}\n \
Username: {platform.node()}\n \
Release: {platform.release()}\n \
Version: {platform.version()}\n \
Machine: {platform.machine()}\n \
Processor: {platform.processor()}\n \
"



my_label = Label(root, text=info, font=("Arial", 14))
my_label.pack(pady=20)

root.resizable(False, False)
root.mainloop()