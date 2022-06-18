import pyttsx3 as tts
import wikipedia as wik


cbtBot = tts.init()  # this sets up the bot, name is cbtBot lol

# okay here we go

volume = cbtBot.getProperty('volume')
cbtBot.setProperty('volume', 1.0)  # set and get the volume

voices = cbtBot.getProperty('voices')
cbtBot.setProperty('voices', voices[0].id) # get and set the voice, it is a female voice

cbt = "Cock and ball torture"  # get wiki name
result = wik.summary(cbt, sentences = 3)  # read the wiki and get sentences

cbtBot.save_to_file(result, "cbtewe.mp3")  # istg if this dont work
cbtBot.runAndWait() # run!
