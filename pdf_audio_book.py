import os, time
import pdftotext

from pygame import mixer
from gtts import gTTS
from pydub import AudioSegment

def start(**kwargs):
  text, file, lang, slow = kwargs.values()
  audio = gTTS(text, lang=lang, slow=slow)
  audio.save(file)

  if os.name == 'posix':
    sound = AudioSegment.from_mp3(file)
    old = file
    file = f'{file.split('.')[0]}.ogg'
    sound.export(file, format='ogg')
    os.remove(old)
  
  mixer.init()
  mixer.music.load(file)
  mixer.music.play()

  seconds = 0 
  while  mixer.music.get_busy() == 1:
    time.sleep(0.10)
    seconds += 0.10
  
  mixer.quit()
  os.remove(file)

with open('arg_1.pdf', 'rb') as f:
  pdf = pdftotext.PDF(f)

for page in pdf:
  start(
    text=page,
    file='audio_tmp.mp3',
    lang='pt-br',
    slow='False'
  )
