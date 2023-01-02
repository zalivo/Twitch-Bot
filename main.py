from dotenv import load_dotenv
from twitchio.ext import commands
import os
import random

load_dotenv()
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TWITCH_TOKEN'], prefix='?', initial_channels=['Riccc0_'])

    # Function: When someone from chat types ?hello
    # Bot will respond with Hello message back to the chatter
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    # Function: printout random strings from array
    # TODO
    # properly rename command nevim
    @commands.command()
    async def nevim(self, ctx:commands.Context):
        vtipne = ['nevim', 'vim']
        await ctx.send(f'{random.choice(vtipne)}')

bot = Bot()
bot.run()
