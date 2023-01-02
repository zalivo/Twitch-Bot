from dotenv import load_dotenv
from twitchio.ext import commands
import os
import random

load_dotenv()
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TWITCH_TOKEN'], prefix='?', initial_channels=['Riccc0_'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)

    # Function: When someone from chat types ?hello
    # Bot will respond with Hello message back to the chatter
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    # Function: printout random strings from array
    # TODO
    # properly rename command nevim
    # fill list with Strings
    @commands.command()
    async def nevim(self, ctx:commands.Context):
        vtipne = ['nevim', 'vim']
        await ctx.send(f'{random.choice(vtipne)}')

    # Link command
    @commands.command()
    async def link(self, ctx: commands.Context):
        await ctx.send(f'google.com')

bot = Bot()
bot.run()
