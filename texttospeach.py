from gtts import gTTS
from playsound import playsound
import os
mytest = 'Uday kamina ke sath sath chutiya bhi hai!'
language='en'
myobj = gTTS(text=mytest,lang=language,slow=False,tld='com')
myobj.save("welcome.mp3")
#os.system("mpg321 welcome.mp3")
playsound("welcome.mp3")
