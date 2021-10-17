import os
from typing import final
import discord
from random import choice
TOKEN = **

FRASES = ['comassim, não entendi','familia?','voce ta puto?','me ajuda macho','vou tomar banho','bila','pota','bilola','morri :c','ah nao mah']
intents = discord.Intents.default()
intents.members = True


def is_command(msg: discord.Message) -> bool:
    if msg.content.startswith('!muck'):
        return True
    return False

async def xupeta(self,msg: discord.Message) -> None:
    ch = self.get_channel(896769566523424822)
    return await ch.send(f"{choice(FRASES)}")



class MinhaSec(discord.Client):

    async def voice_loggin(self,msg: discord.Message):
        ch = self.get_channel(896769566523424822)
        audio_play = discord.FFmpegPCMAudio('vuv.mp3')
        print(audio_play)
        if msg.author.voice is None:
            return await ch.send(f"muck! >:C")
        fin_channel = msg.author.voice.channel

        try:
            self.bot_invoice = await fin_channel.connect()
        except:
            await self.bot_invoice.move_to(fin_channel)
        
        
        

    async def on_message(self, message):
        message.content = message.content.lower()
        if message.author == self.user:
            return
        # if not is_command(msg = message):
        #     return

        if message.content.startswith('!xupeta'):
            await xupeta(self,msg=message)
        # await self.voice_loggin(message)


        
        

    async def on_connect(self):
        game = discord.Game("Muck")
        await self.change_presence(status=discord.Status.idle, activity=game)

    async def on_member_join(self,member):
        channel = self.get_channel(896769566523424822)
        await channel.send("MUCK!!!!!!!!")


client = MinhaSec(intents=intents)



client.run(TOKEN)
