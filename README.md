# ss-sender
Job : Sends the screenshot of the host PC to the discord server on which the screenshot is requested.
Read this full document to make it for yourself without any coding skills.

**Used Items = {"Language" : "Python 3.7",**
**"Library" : "pyautogui",**
**"API" : "Discord Python API"}**



**FAQs you must read before running this for your needs:**

Q.	What is the use of this Bot?

	This bot is a tool which is used by people to keep a check on their kids/sibilings,
	who might bluff you if you go near them and see computer screen,
	without disturbing them.
	Sorry peeps!

Q.	Can this bot be used for cheating?
	
	Yes, it can be used to cheat, but it's like a tool which can be used for either an purpose or demonic same as nuclear power.

Q.	What are the requirements ?
	
	Not much but it requires :
		1. A normal computer
		2. Internet connection

Q.	Do I need coding skills to make this?
	
	Not if you read this document till the end, but you should have even better skill of copy-pasting text.

Q.	How bot works?

	Bot takes a second to do this. However, it might be slow bacause of your internet connectivity.
		1. Bot takes on the screenshot of the device screen on which it is running it's code.
		2. Bot saves the screenshot on your device.
		3. Bot sends this image to the person who requested for this screenshot.
		4. Bot deletes the image from local device.
	Bot only works while the code is running. Discord is not necessesary to be installed in the device in which code is running.

Q. How to make this bot?

	Follow the shortest procedures to make this bot given below.

**Important :**

	1.	You'll have to run the "bot code" on the same device of which you want screenshot.
	2.	You can skip some steps, if you have done it in the past.


**Steps :**

	1. Make discord server and let bot in it.
		-	Watch this till 5:50 : https://www.youtube.com/watch?v=SPTfmiYiuok
		-	Follow all the steps.
		-	Give bot name as you wish.
		-	Copy the generated TOKEN and keep it with you.
		
	2. Install Python 3.0
		-	Watch and follow this whole video : https://www.youtube.com/watch?v=Wys0OaCGvMk
		-	Remember the step of opening new file in IDLE and running it.
		
	3. Install dependencies.
		-	Click on windows start button on left bottom corner of the screen.
		-	Type command prompt in the search bar and open the black coloured icon.
		-	Paste "pip install pyautogui" as the black colour screen opens and let the installation happen.
			-	It would just take a minute or two.
		
	4. Copy paste token and location
		-	Open IDLE by searching in search from windows start button.
		-	Create a new file.
		-	Copy and paste my code from here: https://github.com/vgauravkumar/ss-sender/blob/main/main.py
		-	In fifth line i.e. TOKEN = 'xx..xx', instead of xx...xx, paste your TOKEN inside the colon.
		-	Make a folder anywhere on your windows and copy the folder path after getting into that folder.
			- How? : https://www.youtube.com/watch?v=xnuwJGNtsv8
		-	Add /ss.png after the path by simply pasting anywhere and typing /ss.png and copying whole line again.
		-	At line 33,34 and 36, paste this path by erasing mine.
		
	5. Run code (F5).

That's it. Now you can test it on your discord server by typing $ss or let any other person to press to give this command and see your screen's image.

You can close the code file window if you want, but do not close the output window(It shall be displaying "Logged in as xyz").

To stop the bot simply press Ctrl+C in the output window or close the output window and killing the process.

This bot is not made for the purpose of taking away privacy from anyone in any form.
