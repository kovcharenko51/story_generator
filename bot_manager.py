import codecs
from discord.ext import commands
from config import settings
from story_creator import gen_story

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def story(ctx):
    await ctx.send(gen_story())


@bot.command()
async def tell(ctx, *args):
    text = " ".join(args) + "\n"
    with codecs.open("base.txt", "a", "utf-8") as base:
        base.write(text)
    await ctx.send("Ахахахахаха. Смешно")


@bot.command()
async def read(ctx):
    await ctx.send(gen_story(), tts=True)
