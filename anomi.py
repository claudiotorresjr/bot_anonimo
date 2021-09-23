import discord
from discord.ext import commands


class AnonimousBot(commands.Cog):
    """

    """


    def __init__(self, bot):
        """
            __init__
        """

        self.bot = bot


    
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.channel.DMChannel):
            channel_id = 259108205798359040
            await self.bot.get_channel(channel_id).send(message.content)