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

            message_content = message.content
            if "@" in message_content:
                msg = message_content.split("@")
                if len(msg) >= 1:
                    if len(msg) > 1:
                        name = msg[1].split("#")[0]
                        code = msg[1].split("#")[1].split(" ")[0]
                    else:
                        name = msg[0].split("#")[0]
                        code = msg[0].split("#")[1].split(" ")[0]

                    guild = self.bot.get_guild(channel_id)
                    
                    mention = f"{name}#{code}"
                    user_id_to_mention = ""
                    for m in guild.members:
                        if str(m) == mention:
                            user_id_to_mention = f"<@{m.id}>"
                            break
                    
                    message_content = message_content.replace(f"@{mention}", user_id_to_mention)

            await self.bot.get_channel(channel_id).send(message_content)