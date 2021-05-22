import codecs
from discord.ext import commands
from config import settings
import story_creator

bot = commands.Bot(command_prefix=settings['prefix'])
path_to_file = "base.txt"


def write_story(file_path, text):
    with codecs.open(file_path, "a", "utf-8") as base:
        base.write(text)


@bot.command()
async def story(ctx):
    await ctx.send(story_creator.gen_story(), tts=False)


@bot.command()
async def tell(ctx, *args):
    text = " ".join(args) + "\n"
    write_story(path_to_file, text)
    await ctx.send("Ахахахахаха. Смешно", tts=False)


@bot.command()
async def read(ctx):
    await ctx.send(story_creator.gen_story(), tts=True)
