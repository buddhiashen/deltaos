from cgi import test
from os import cpu_count
from re import L
from tkinter import *
from turtle import title
import psutil
import time


window = Tk()
window.geometry("600x500")
window.title("CPU | RAM | DISK Info - DELTA OS")
window.iconbitmap('icons/stats.ico')

# function to display cpu information
def show_cpu_info():
    cpu_usage = psutil.cpu_percent()
    time.sleep(0.5)
    
    num_of_cpu = psutil.cpu_count()
    
    cpu_frequency = psutil.cpu_freq(percpu=True)
    
    mem = psutil.virtual_memory().percent
    
    disk_use = psutil.disk_usage('/')
    
    total = disk_use.total / (1024.0 ** 3)
    used = disk_use.used / (1024.0 ** 3)
    free = disk_use.free / (1024.0 ** 3)


    #print('{} %' .format(cpu_usage))
    cpu_label.config(text='{} %'.format(cpu_usage))
    cpu_label.after(200,show_cpu_info)
    
    no_of_cpu_label.config(text='{}'.format(num_of_cpu))
    
    cpu_freq_label.config(text='{}'.format(cpu_frequency))
    
    mem_label.config(text='{} %'.format(mem))
    
    disk_use_label.config(text='{:.2f} GB'.format(total))
    disk_used_label.config(text='{:.2f} GB'.format(used))
    disk_free_label.config(text='{:.2f} GB'.format(free))


    
    
    
    
    
# cpu title
cpu_title = Label(window, text='CPU Usage :\n(% Utilization) ', font='Arial 11', fg='#0D1117')
cpu_title.place(x=20, y=45)

# label to show percent of cpu
cpu_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 16', width=15)
cpu_label.place(x=128, y=50)
    
    
num_of_cpu_title = Label(window, text='Number of :\nlogical CPUs', font='Arial 11', fg='#0D1117')
num_of_cpu_title.place(x=20, y=115)
    
no_of_cpu_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 16', width=15)
no_of_cpu_label.place(x=128, y=110)    
    
    
cpu_freq_title = Label(window, text='CPU frequency : ', font='Arial 11', fg='#0D1117')
cpu_freq_title.place(x=20, y=180)    

cpu_freq_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 12', width=38)
cpu_freq_label.place(x=138, y=180)
    

mem_title = Label(window, text='System memory : \nusage', font='Arial 11', fg='#0D1117')
mem_title.place(x=20, y=225)
    
mem_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 14', width=15)
mem_label.place(x=145, y=225)


disk_use_title = Label(window, text='Total Disk\nSpace: (GB)', font='Arial 11', fg='#0D1117')
disk_use_title.place(x=20, y=290)

disk_use_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 14', width=15)
disk_use_label.place(x=138, y=289)


disk_use_title = Label(window, text='Used Disk\nSpace: (GB)', font='Arial 11', fg='#0D1117')
disk_use_title.place(x=20, y=350)

disk_used_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 14', width=15)
disk_used_label.place(x=138, y=351)


disk_free_title = Label(window, text='Free Disk\nSpace: (GB)', font='Arial 11', fg='#0D1117')
disk_free_title.place(x=20, y=415)

disk_free_label = Label(window, bg='#e0e0e0', fg='#000000', font='Arial 14', width=15)
disk_free_label.place(x=138, y=415)


    
if __name__ == '__main__':
    show_cpu_info()
    window.mainloop()