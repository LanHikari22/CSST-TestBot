import sys
import discord
from discord.ext import commands


DEBUG = True
def dbg(str, file=None, active=True):
    """just a wrapper function to distinguish a DEBUG print from an actual print."""
    try:
        if DEBUG and active:
            if file is None:
                import sys
                print(str, file=sys.stderr)
            else:
                print(str, file=file)
    except: pass


if __name__ == '__main__':
    dbg("Welcome to __main__.py")
    bot = commands.Bot(command_prefix='?', description="You are the reason why I still -- oops this is a song")
    commands = [] # list of BotCMD objects that are available to this bot
    msgHistory = []

async def botmsg(string):
    """Just a simple abstraction that assumes global variables channel and bot"""
    msgHistory.append(await bot.send_message(destination=channel, content=string))

async def execute(message):
    """executes command passed in argv"""

    # obtain user
    user = message.author
    user = str(user)[:-5]

    # obtain argv
    msg = message.content[message.content.index('>')+2:] # remove '<id> '
    argv = msg.split(' ')

    if argv[0] == 'help':
        await botmsg("Hi %s! I'm QBot.cplx! Here's how to use me:\n* help\n* add <number> <number>\n* gg\n* del" % user)
    elif argv[0] == 'add':
        if len(argv) < 2: return await botmsg("I don't know what I'm supposed to add...")
        if not (argv[1].isnumeric() and argv[2].isnumeric()):
            await botmsg("Are you... Are you really adding numbers?")
        await botmsg("Um. I think I can do this... Let's see...\n%s plus %s equals %s, I think??" %
                     (int(argv[1]), int(argv[2]), int(argv[1]) + int(argv[2])))
    elif argv[0] == 'del':
        await botmsg("Error: This is currently unsupported. Give me more premissions if you really want it done.")
        if msgHistory:
            bot.delete_message(msgHistory.pop())
    elif msg == "gg":
        await botmsg("gg %s!" % user)

@bot.event
async def on_ready():
    global server, channel, member # I am sorry. How do you create async methods???

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # gets server and channel we're interacting in....
    for s in bot.servers:
        server = s
    for c in server.channels:
        if c.name == "bot_testing":
            channel = c

    member = server.get_member(user_id=bot.user.id)
    # await bot.change_nickname(member,nickname='QuarkBot') # i'm sorry, you can't
    await bot.change_presence(game=discord.Game(name="QBot.cplx"))


@bot.event
async def on_message(message):
    dbg("<on_message>")

    if not (message.mentions is not None and member in message.mentions):
        return

    # This is only executed at @<this_bot> so!


    await execute(message) # executes commands in msg


    dbg("</on_message>\n")


bot.run('MzQwODkxMjIwMzc5MTcyODk2.DGS_mw.dpKg0Z8V0NF0jESEOBltvxasxxE')
bot.logout()