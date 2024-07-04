import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def embed(ctx):
    """
    Creates discord embeds

    Args:
        ctx (str): parametar
    """
    embed = discord.Embed(
        title="Football",
        url="https://google.com",
        description="I love football",
        color=0x06600,
    )
    embed.set_author(name=ctx.author.display_name, url="https://instagram.com")
    embed.set_thumbnail(
        url="https://images.stockcake.com/public/0/8/1/08143e8f-beee-4d51-bb33-8b28558f5dc5_large/designing-virtual-worlds-stockcake.jpg"
    )
    embed.add_field(name="Real madrid", value="Vinicius Jr", inline="True")
    embed.add_field(name="Real Atletic", value="Neymar", inline="True")
    embed.set_footer(text="This is a footer!")

    await ctx.send(embed=embed)


def configure():
    """Starts load_dotenv() function"""
    load_dotenv()


def main():
    """
    Main function

    Raises:
        ValueError: If bot_token is None, raises ValueError
    """

    bot_token = os.getenv("bot_token")
    if bot_token is not None:
        bot.run(bot_token)
    else:
        raise ValueError("Bot token is None! Check .env file")


if __name__ == "__main__":
    main()
