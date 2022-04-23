from operator import truediv
from pydoc import cli
from turtle import title
from types import MemberDescriptorType
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '!')

#events

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Doing nothing"))
    print("Beepity Boopity Beep")

@client.event
async def on_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        pass

@client.event
async def on_command_error(ctx, error):
    if isinstance (error, commands.CommandNotFound):
        await ctx.send ("That command doesn't exist.If it is a genuine sugestion please DM personaly me and I will try.")

#commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge (limit=amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply ("Please add a value to purge")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member=None, reason=None):
    if user == None:
        await ctx.reply("Specify a user.")
    else:
        await user.kick(reason=reason)
        await ctx.reply(f"Successfully kicked {user.mention}. Reason: {reason}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member=None, reason=None):
    if user == None:
        await ctx.reply("Specify a user.")
    else:
        await user.ban(reason=reason)
        await ctx.reply(f"Successfully kicked {user.mention}. Reason: {reason}")

@client.command(aliases= ['forgive'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
@commands.has_permissions(read_message_history=True)
async def favortie_song(ctx):
    embed = discord.Embed(title = "This is my creators favorite song", description = f"Click on the url to listen to the favortie song of my cerator", url= "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    await ctx.send(embed = embed)

@client.command()
async def Ariahelp(ctx):
    embed = discord.Embed(title="ARIA commands help", description=f"If you have any problems please contact me through Modmail or DMs. \n \n **Note:**: This is not a public bot. \n \n **User commands** \n !ahelp: Opens this window \n \n !ping: Tell you the latency of your commands. To be used if the bot won't respond to your commands. \n \n !clear: Clear the messages. Default amount: 5.  \n \n **Admin Commands** \n \n !ban: bans user. \n \n !unban: unbans the user. \n \n !kick: kicks the user. "  ,  colour=0x4dff4d)
    await ctx.send(embed = embed)

client.run(os.environ['BOT_TOKEN'])   