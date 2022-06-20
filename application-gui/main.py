import os
import vlc
from playsound import playsound
import mysql.connector
import speech_recognition as sr
from gtts import gTTS
flag1 = 0
from tkinter import *
from tkinter import font
from tkinter.font import Font
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import os
from sys import byteorder
from array import array
from struct import pack
from tokenize import String
import pyaudio
import wave
import warnings
from tensorflow import keras
from lables import all_label
from sklearn.preprocessing import LabelEncoder
import librosa as librosa
import IPython.display as ipd
import numpy as np
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
import wave
import contextlib
import glob as glob
warnings.filterwarnings("ignore")

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
model = keras.models.load_model('cnn-assamese.h5')

root = Tk()
root.title("T.O.D.S.A")
root.geometry("800x500")
root.configure(background="black")
photo = PhotoImage(file = "./gifs/1124.png")
root.iconphoto(False, photo)

fontText = Font(size = 20, weight = "bold")
text1 = Label(root,text="মই আপোনাক কেনেকৈ সহায় কৰিব পাৰো ?",font=fontText,fg="yellow",background="black",anchor=CENTER,justify=CENTER,wraplength=600)
text1.pack(pady=50)


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        
        self.image = Image.open("./gifs/1124.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
       

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
    
    def change_pic(labelname):
 	 
      photo1 = ImageTk.PhotoImage(Image.open("b.png"))
      labelname.configure(image=photo1)
      print ("updated")

def test1():
        global flag1 
        global text1  
        text1.config(text="Listening.......")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
        )
        cursor = mydb.cursor()
# if cursor.execute("CREATE DATABASE todsa") :
#     print("Database created !")
        cursor.execute("use todsabase")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS dialogues (id bigint(11) AUTO_INCREMENT primary key,questions VARCHAR(1000), "
            "ans VARCHAR(1000))")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak anything...")
            audio = r.listen(source)

            try:
                text1.config(text="working on it...")
                text = r.recognize_google(audio)
                print("you said :", format(text))
                myText = format(text)
                language = 'en'
                cursor.execute("SELECT * FROM `dialogues` WHERE questions ='{}'".format(myText))

                sql = myresult = cursor.fetchall()
                x = myText.find("Open Chrome")
                t = myText.find("open Chrome")
                y = myText.find("open Google Chrome")
                z = myText.find("search")
                p = myText.find("who is")
                o = myText.find("what is")
                if p!=-1 or o!=-1:
                    if p!=-1 :
                        pParam = myText.split("who is",1)[1]
                        PUrl = 'https://duckduckgo.com/html/?q='+pParam
                        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",}
                        page = requests.get(PUrl, headers=headers).text
                        soup1 = BeautifulSoup(page, 'html.parser').find("a",class_="result__snippet")
                        print(soup1.text)
                        myText = soup1.text
                        text1.config(text=myText)
                        #print(pParam)
                    else :
                        pParam = myText.split("what is",1)[1]
                        PUrl = 'https://duckduckgo.com/html/?q='+pParam
                        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",}
                        page = requests.get(PUrl, headers=headers).text
                        soup1 = BeautifulSoup(page, 'html.parser').find("a",class_="result__snippet")
                        print(soup1.text)
                        myText = soup1.text
                        text1.config(text=myText)
                else :
                    if x!=-1 or y!=-1 or t!=-1 and z!=-1:
                        sParam = myText.split("search",1)[1]
                        d = sParam.strip()
                        s = d.replace(' ','+')
                        link = "https://www.google.com/search?q="
                        search = "start chrome "+link+s
                        print(search)
                        #os.system(search)
                        os.system(search)
                        myText = "opening google chrome and searching "+s
                        text1.config(text=myText)
                        flag1 = 1
                

                    if flag1 !=1 :    
                        if x !=-1 or y!=-1 or t!=-1 and z==-1:
                            #os.system("google-chrome")
                            os.system("start chrome")
                            myText = "opening google chrome."
                            text1.config(text=myText)
                        elif not sql:
                            com0 = "play music"
                            com1 = "open YouTube"
                            pdf = myText.find('download a PDF')
                            
                            if myText==com0 :
                                myText = "Playing music on youtube"
                                text1.config(text=myText)
                                music = "start chrome "+"https://www.youtube.com/watch?v=Mxgkx8A4rTw"
                                os.system(music)
                            elif myText==com1 :
                                myText = "Opening Youtube.com"
                                text1.config(text=myText)
                                os.system("start chrome https://www.youtube.com/")
                            elif pdf!=-1 :
                                myText = "Downloading pdf  for you"
                                pfile = "start chrome "+"http://uru.ac.in/uruonlinelibrary/Cyber_Security/Cryptography_and_Network_Security.pdf"
                                os.system(pfile)
                                text1.config(text=myText)
                            else :
                                myText = "Sorry I don't Understand !you said "+text
                                text1.config(text=myText)
                        else:
                            for x in myresult:
                                print(''.join(x[1]))
                                if ''.join(x[1]) == myText:
                                    myText = ''.join(x[2])
                                    print(x)
                                    text1.config(text=myText)
                                else:
                                    myText = "Sorry I didn't get the point .you said "+text
                                    text1.config(text=myText)
                myobj = gTTS(text=myText, lang=language, slow=False)
                myobj.save("voice.mp3")
                #os.system("mpg321 voice.mp3")
                #os.system("start voice.mp3")
                #playsound('voice.mp3')
                p = vlc.MediaPlayer("voice.mp3")
                p.play()

            except Exception as e:
                print("error = ", e)
                ErText = "Sorry I didn't get the point .you said "+text
                text1.config(text=ErText)
                myobj = gTTS(text=ErText, lang=language, slow=False)
                myobj.save("voice.mp3")
                p = vlc.MediaPlayer("voice.mp3")
                p.play()
               # os.system("start voice.mp3")
                #playsound('voice.mp3')
                #playsound.close
               # os.remove("voice.mp3")
def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD
def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r


def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i) > THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data


def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    silence = [0] * int(seconds * RATE)
    r = array('h', silence)
    r.extend(snd_data)
    r.extend(silence)
    return r


def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r


def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


def segmentation():

    # reading from audio mp3 file
    filename = "file.wav"
    sound = AudioSegment.from_wav(filename)
    # spliting audio files
    audio_chunks = split_on_silence(
        sound, min_silence_len=70, silence_thresh=-40)
    # loop is used to iterate over the output list
    for i, chunk in enumerate(audio_chunks):
        output_file = "./temp/audio_{0}.wav".format(i)
        print("Exporting file", output_file)
        chunk.export(output_file, format="wav")

def prepareAudio(audio_in_file: String):

    audio_out_file = "out_sine.wav"
    one_sec_segment = AudioSegment.silent(duration=1000)
    song = AudioSegment.from_wav(audio_in_file)
    final_song = one_sec_segment + song
    final_song.export(audio_out_file, format="wav")

    with contextlib.closing(wave.open(audio_out_file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
       # print(duration)
    # print(song.duration_seconds)
    time2 = (2-duration)*1000
    #print("time2 : ", time2)
    one_sec_segment = AudioSegment.silent(duration=time2)
    song = AudioSegment.from_wav(audio_in_file)
    final_song = one_sec_segment + song
    counter = 0
    filename = "./coocked/final{}.wav"
    while os.path.isfile(filename.format(counter)):
        counter += 1
    filename = filename.format(counter)
    final_song.export(filename, format="wav")
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(duration)

def predict(audio):
    prob = model.predict(audio.reshape(1, 8000, 1))
    index = np.argmax(prob[0])
    return index


def speech2text(filename):

    le = LabelEncoder()
    y = le.fit_transform(all_label)
    classes = list(le.classes_)

    samples, sample_rate = librosa.load(
        filename, sr=16000)

    #samples ,sample_rat = librosa.load('ki1.wav',sr = 16000)
    samples = librosa.resample(samples, sample_rate, 8000)
    ipd.Audio(samples, rate=8000)

    return classes[predict(samples)]
def assam():
    text = []
    str = " "
    print("Please speak words one by one...") 
    text1.config(text="শব্দ হুনী আছো")
    record_to_file('file.wav')
    segmentation()
    text1.config(text="হ্মমা কৰিব |আকৌ চেস্টা কৰক |")
    for filename in glob.glob('./temp/*.wav'):
        with contextlib.closing(wave.open(filename, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration>0.30:
                prepareAudio(filename)
        os.remove(filename)
    for filename in glob.glob('./coocked/*.wav'):
    #fname = filename.replace("./temp\\","")
        with contextlib.closing(wave.open(filename, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
        # print(duration)
            if duration>1.0:
                t = (duration-1)*1000
                print(duration)
                print(filename)
                # pydub does things in milliseconds
                newAudio = AudioSegment.from_wav(filename)
                newAudio = newAudio[:-t]
                newAudio.export(filename, format="wav")
    for filename in glob.glob('./coocked/*.wav'):
       text.append(speech2text(filename))
       os.remove(filename)
        

    
    text1.config(text=str.join(text))
    print("process Complete")
    
              
boldFont = Font(size = 10, weight = "bold")
button1 = Button(root, text="কোৱা",height=2,background="black",fg="red",font=boldFont,command=assam)
button1.pack(side=BOTTOM,expand=True,fill=BOTH)
e = Example(root)
e.pack(fill=BOTH, expand=YES)

root.mainloop()