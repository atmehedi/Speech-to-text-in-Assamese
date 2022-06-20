# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv

# freq = 16000
# duration = 2
# recording = sd.rec(int(duration * freq),
# 				samplerate=freq, channels=1)

# sd.wait()

# write("koa1.wav", freq, recording)
from tkinter import *
from tkinter.ttk import Progressbar
import time
from traceback import print_last


def step():
	pb.stop()
	for i  in range(100):
		ws.update_idletasks()
		pb['value'] +=1
		txt['text']=pb['value'],'%'
		print(i)
		if i%20==0:
			time.sleep(1)

ws = Tk()
ws.title('T.O.D.S.A')
ws.geometry('600x300')
ws.config(bg='#345')


pb = Progressbar(
    ws,
    orient = HORIZONTAL,
    length = 100,
    mode = 'determinate'
    )

pb.place(x=40, y=20)

txt = Label(
    ws,
    text = '0%',
    bg = '#345',
    fg = '#fff'

)

txt.place(x=150 ,y=20 )

Button(
    ws,
    text='Start',
    command=step
).place(x=40, y=50)

ws.mainloop()