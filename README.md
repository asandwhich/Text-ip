Text-ip
=======

Python script that uses py-google-voice to send an sms containing your ip address

You will need to put the destination phone number where the comment indicates in ipsend.py and your account information in a pygooglevoice file. Run ipsend.py to start the script, and it will check the ip address every two hours.

Requirements:
A usable google voice account and the ability to send sms with said account.
A functioning install of the pygooglevoice library, found at the link below.
An internet connection and an install of either python 2.6 or 2.7.

Google Voice python bindings: http://code.google.com/p/pygooglevoice/
