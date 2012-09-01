from googlevoice import Voice
from googlevoice.util import input
import getip
import time
phonenum = '' # Place you phone number here
currentip = getip.getpubip()
while 1:
	temp = getip.getpubip()
	if currentip != temp:	
		voice = Voice()
		voice.login()
		voice.send_sms(phonenum, temp)
		currentip = temp
	time.sleep(7200)	
#text = getip.getpubip()
#Voice = Voice()
#voice.login()
#voice.send_sms(phonenum, text)
