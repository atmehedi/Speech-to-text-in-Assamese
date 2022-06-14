from Tkinter import * 
running = False
root = Tk()
def start_motor(event):
    global running
    running = True
    print("starting recording...")

def stop_motor(event):
    global running
    print("stopping recording...")
    running = False

button = Button(root, text ="forward")
button.pack(side=LEFT)
button.bind('<ButtonPress-1>',start_motor)
button.bind('<ButtonRelease-1>',stop_motor)
root.mainloop()