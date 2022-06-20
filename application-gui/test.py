import wave
import contextlib
import glob as glob
from pydub import AudioSegment
from pydub.silence import split_on_silence
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