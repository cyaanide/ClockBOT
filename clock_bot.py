#If you want to use this code you will need to do follow these steps:
#1.Download discord.py (pip3 install discord.py)
#2.Upload these custom emojis to a server (discord bots already have nitros, so make a test server and upload these emojis on that serve then you can use the bot anywhere.)
#  The link to the emojis: https://ibb.co/R64MPMX https://ibb.co/DrKqy8M https://ibb.co/ZTWJZC7
#3.After you are done uploading the emojis, type out  the emojis with a '\' in front of them, like '\:notimeEmoji', you will get the emoji name and id (for ex <:nothing:715844013093159002>). note down the enoji id's in their long form. Yes include the < and >.
#4.Replace every instance of '<:nothing:715844013093159002>' in the code below with your emoji id for the plain black emoji, same goes for '<:915:715786860118409256>' for the 9:15 emote and '<:notime:715787229095657563>' with the emote id of noTime emote.
#5.Make your own bot at discord.com , generate a bot token and paste it in bot.run("") at the end.
#6.Make the bot join your server and copy the id of the channel you want the live clock in, paste it in line 62.
#7.You are good to go. run the script (dont forget to save it) by typing 'python3 clock_bot.py' in terminal open in the code folder.


import discord	
from discord.ext import commands
from datetime import datetime
import asyncio

digit_0 = {1:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock930:", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 5:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock9:"}
digit_1 = {1:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 2:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:"}
digit_2 = {1:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock930:", 2:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock9:", 5:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 6:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 7:":clock3:<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>"}
digit_3 = {1:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock930:", 2:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock9:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock9:"}
digit_4 = {1:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock930:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:"}
digit_5 = {1:":clock330:<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 4:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock930:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock9:"}
digit_6 = {1:":clock330:<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>", 4:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock930:", 5:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock9:"}
digit_7 = {1:"<:915:715786860118409256><:915:715786860118409256><:915:715786860118409256>:clock930:", 2:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:"}
digit_8 = {1:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock930:", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock9:", 5:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock9:"}
digit_9 = {1:":clock330:<:915:715786860118409256><:915:715786860118409256>:clock930:", 2:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 3:":clock6:<:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 4:":clock3:<:915:715786860118409256><:915:715786860118409256>:clock930:", 5:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 6:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:", 7:"<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>:clock6:"}
one_blank_line = {1:"<:nothing:715844013093159002>", 2:"<:nothing:715844013093159002>", 3:"<:nothing:715844013093159002>", 4:"<:nothing:715844013093159002>", 5:"<:nothing:715844013093159002>", 6:"<:nothing:715844013093159002>", 7:"<:nothing:715844013093159002>"}
two_blank_line = {1:"<:nothing:715844013093159002><:nothing:715844013093159002>", 2:"<:nothing:715844013093159002><:nothing:715844013093159002>", 3:"<:nothing:715844013093159002><:nothing:715844013093159002>", 4:"<:nothing:715844013093159002><:nothing:715844013093159002>", 5:"<:nothing:715844013093159002><:nothing:715844013093159002>", 6:"<:nothing:715844013093159002><:nothing:715844013093159002>", 7:"<:nothing:715844013093159002><:nothing:715844013093159002>"}
two_dots = {1:"<:nothing:715844013093159002>", 2:"<:notime:715787229095657563>", 3:"<:nothing:715844013093159002>", 4:"<:nothing:715844013093159002>", 5:"<:nothing:715844013093159002>", 6:"<:notime:715787229095657563>", 7:"<:nothing:715844013093159002>"}
dispach_int_dict = {0:digit_0, 1:digit_1, 2:digit_2, 3:digit_3, 4:digit_4, 5:digit_5, 6:digit_6, 7:digit_7, 8:digit_8, 9:digit_9}
blank_emoji_line = "<:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002><:nothing:715844013093159002>"
blank_emoji_double_line = blank_emoji_line + "\n" + blank_emoji_line
def clock():
	time_now = datetime.now()
	string_time = time_now.strftime("%H:%M")
	hour_first = int(string_time[:1])
	hour_second = int(string_time[1:2])
	minute_first = int(string_time[3:4])
	minute_second = int(string_time[4:])
	dispach_time = {1:hour_first, 3:hour_second, 7:minute_first, 8:minute_second}

	output_string = ""

	for line in range(1,8):
		for place in range(10):
			if(place in [2,4,6,8]):
				output_string += one_blank_line[line]
			if(place in [1,3,7,8]):
				digit = dispach_time[place]
				output_string += dispach_int_dict[digit][line]
			if(place == 5):
				output_string += two_dots[line]
		output_string += "\n"
	output_string += blank_emoji_line
	return output_string

bot = commands.Bot(command_prefix= "clock.", description= "Bot made by Cyan1de#8794 to annoy rude")


@bot.event
async def on_ready():
	print("bot running")
	bot.main_channel = bot.get_channel()
	await bot.main_channel.send(blank_emoji_double_line)
	await asyncio.sleep(2)
	bot.message_1 = await bot.main_channel.send("Ready! message 1")
	await asyncio.sleep(2)
	bot.message_2 = await bot.main_channel.send("Ready! message 2")
	await asyncio.sleep(2)
	bot.message_3 = await bot.main_channel.send("Ready! message 3")
	await asyncio.sleep(2)
	bot.message_4 = await bot.main_channel.send("Ready! message 4")
	await main_event()


def find_nth(str_input, n, character):
	times_found = 0 
	for i in range(len(str_input)):
		if(str_input[i] == character):
			if(times_found == n):
				return i
			else:
				times_found += 1
	return None

async def main_event():
	clock_string = clock()
	second_line_break_position = find_nth(clock_string, 1, '\n')
	fourth_line_break_position = find_nth(clock_string, 3, '\n')
	sixth_line_break_position = find_nth(clock_string, 5, '\n')
	print(fourth_line_break_position)
	clock_string_first_half = clock_string[:second_line_break_position+1]
	clock_string_second_half = clock_string[second_line_break_position+1:fourth_line_break_position+1]
	clock_string_third_half = clock_string[fourth_line_break_position+1:sixth_line_break_position+1]
	clock_string_fourth_half = clock_string[sixth_line_break_position+1:]

	await bot.message_1.edit(content = clock_string_first_half)
	await bot.message_2.edit(content = clock_string_second_half)
	await bot.message_3.edit(content = clock_string_third_half)
	await bot.message_4.edit(content = clock_string_fourth_half)
	await asyncio.sleep(60)
	await main_event()

bot.run("")