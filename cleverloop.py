from cleverbot import Cleverbot
from time import sleep
cb = Cleverbot('cleverloop')
iask = (cb.ask("hi"))

while True:
       print(iask)
       iask = (cb.ask(iask))
       sleep(1)
