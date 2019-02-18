import discord
from discord.ext import commands
import asyncio
from itertools import cycle
Token = 'NTMxMDcyMTU1NjQ4MDAwMDAw.DxIwNQ.OPPUQMl_GAHC6s6FqKfpXWfNelc'


client = commands.Bot(command_prefix = ':')
client.remove_command('help')




status = ['for ROUNAK', 'I am learning!', 'with Music!']
async def change_status():
	await client.wait_until_ready()
	msgs = cycle(status)
	while not client.is_closed:
		current_status = next(msgs)
		await client.change_presence(game=discord.Game(name=current_status))
		await asyncio.sleep(3)
	
	
@client.event
async def on_ready():
	
	print('The Musicdroid is ready!!')
	print(client.user.name)
	print(client.user.id)
	
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name='Admin')
	await client.add_roles(member, role)


@client.command()
async def echo(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(output)
	
@client.command(pass_context=True)
async def purge(ctx, amount=1):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say('Purged!')
	
@client.command()
async def owner():
	embed = discord.Embed(
	      title = 'MusicDroid',
	      description = '**My owner is :-**'
	                               '```Rounak```',
	      colour = discord.Colour.red()
	)
	
	embed.set_footer(text='MusicDroid by ROUNAK')
	await client.say(embed=embed)
	
	
	
@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	embed = discord.Embed(
	     colour = discord.Colour.orange()
	     )
	embed.set_author(name='[COMMANDS]')
	embed.add_field(name='ping', value='Returns Pong', inline=True)
	embed.add_field(name='owner', value='Gives my owner name.', inline=True)
	embed.add_field(name='purge <no. of messages to be purged>', value='Deletes the desired no. of Messages')
	await client.say('Check your DMs!!')
	await client.send_message(author, embed=embed)
	
	
	
@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.Disconnect()
    
    
@client.command()
async def send(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
		await client.send_message(client.get_channel("490499003419459586"),  output)
       

    
    
client.loop.create_task(change_status())
client.run(Token)





