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
    async def nevim(self, ctx: commands.Context):
        vtipne = ['nevim', 'vim']
        await ctx.send(f'{random.choice(vtipne)}')

    # GitHub repository command
    @commands.command()
    async def github(self, ctx: commands.Context):
        await ctx.send('Twitch bot GitHub repository: ' + ' https://github.com/zalivo/Twitch-Bot')

    # Comparing command
    # arg is the number that chatter chooses and then the number is compared with random generated number
    # TODO
    # Choose different emotes for printouts
    @commands.command()
    async def compare(self, ctx: commands.Context, arg):
        random_number = random.randint(1, 100)
        if int(arg) < random_number:
            await ctx.send('Vybrané číslo ' + str(arg) + ' je menší než ' + str(random_number) + ' PoroSad')
        else:
            await ctx.send('Vybrané číslo ' + str(arg) + ' je větší než ' + str(random_number) + ' :)')


bot = Bot()
bot.run()
