import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


class MyBot(commands.Bot):
    def __init__(self, prefix):
        my_intents = discord.Intents.default()
        my_intents.message_content = True
        super().__init__(command_prefix=prefix, intents=my_intents)


class CustomEmbed(discord.Embed):
    def __init__(
        self,
        title,
        url,
        description,
        color,
    ):
        super().__init__(title=title, url=url, description=description, color=color)

    def set_properties(
        self, author_name, thumbnail_url, field_name, field_value, footer_text
    ):
        self.set_author(name=author_name)
        self.set_thumbnail(url=thumbnail_url)
        self.add_field(name=field_name, value=field_value, inline=True)
        self.set_footer(text=footer_text)
        


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


bot = MyBot("!")


@bot.command()
async def embed(ctx):
    """
    Creates and sends the embed.

    Args:
        ctx (str): context of the embed
    """
    thumbnail = "https://images.stockcake.com/public/0/8/1/08143e8f-beee-4d51-bb33-8b28558f5dc5_large/designing-virtual-worlds-stockcake.jpg"
    myEmbed = CustomEmbed(
        title="CustomEmbed",
        url="https://google.com",
        description="This is a description.",
        color=0x06600,
    )
    myEmbed.set_properties(
        "Vuk", thumbnail, "Football wins", "Real Madrid", "Tiny text"
    )
    await ctx.send(embed=myEmbed)


def main():
    """
    Main function

    """
    bot_token = os.getenv("bot_token")
    if bot_token is not None:
        try:
            bot.run(bot_token)
        except discord.LoginFailure:
            print("Login failed. Check your bot token and permissions.")
    else:
        print("Bot token is None! Check .env file")


if __name__ == "__main__":
    main()
