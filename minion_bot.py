import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    await client.change_presence(game=discord.Game(name = 'Say ~help'))

@client.event
async def on_message(message):
    #-- Check for permissions of user --#
    if message.content.startswith('~'):
        if not permissions_check(message.author):
            await client.send_message(message.channel, '<@%s> I dont speak to strangers...' % message.author.id)
            with open('not_friend.jpg', 'rb') as f:
                await client.send_file(message.channel, f)
            return

    #-- help command --#
    if message.content.startswith('~help'):
        await client.send_message(message.author, 'Commands coming soon - JJ')

    #-- add user to white list --#
    if message.content.startswith('~adduser '):
        with open('uselist.txt', 'r+') as f:
            username = sanitisecommand(message.content)
            member = discord.utils.get(message.server.members, name=username)
            userid = member.id
            if userid == None:
                await client.send_message(message.channel, 'Are you imagining things? {0} doesn\'t exist!'.format(username))
            else:
                if checkforduplicates(userid, f):
                    await client.send_message(message.channel, 'Dont be a retard, {0} is already my friend!'.format(username))
                else:
                    f.write(userid + '\n')
                    await client.send_message(message.channel, '{0} is now my friend and can command me.'.format(username))

# --- Helper functions ---#
# TODO: Add them to a different file later
def sanitisecommand(command):
    user_arg = command[len('~adduser '):]
    return user_arg

def checkforduplicates(userid, f):
    for line in f:
        print(line)
        if userid in line:
            return True
        else:
            return False

def permissions_check(member):
    with open('uselist.txt', 'r') as f:
        for line in f:
            if member.id in line:
                return True
    return False

client.run('MjM1MTMxNTU3Njg4Mzc3MzY0.Cv9i_A.TWbpJt_IASagKlsCV-bfl0XKCA4')




