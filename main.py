import discord
import pyautogui
import os

TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#Code starts
client = discord.Client()

#Discord login
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # CHECK IF BOT IS THE SENDER
    if message.author == client.user:
        return

    # Greeting
    if message.content.startswith('$hello'):  # Verified
        try:
            await message.channel.send('Hi ' + str('<@' + str(message.author.id) + '>') + ' !')
        except:
            await message.channel.send('Hi ' + message.author.name + ' !\nUnknown error occured.')

    #Screenshot Request
    if message.content.startswith('$ss'):
        try :
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\KIIT\PycharmProjects\ssSender\ss\ss.png')
            await message.channel.send(file=discord.File(r'C:\Users\KIIT\PycharmProjects\ssSender\ss\ss.png'))
            try:
                os.remove(r'C:\Users\KIIT\PycharmProjects\ssSender\ss\ss.png')
            except:
                pass
        except :
            await message.channel.send('Hi ' + message.author.name + ' !\nUnknown error occured.')

#Discord request
client.run(TOKEN)
