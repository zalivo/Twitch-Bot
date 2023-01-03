from dotenv import load_dotenv
from twitchio.ext import commands
import os
import random
import time

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TWITCH_TOKEN'], prefix='?', initial_channels=['Riccc0_'])

    # Check if bot has established connection with the channel
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # Listen to messages in the channel
    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)

    # Simple hello command
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    # Based copy pasta command
    # ?? Bot cannot send two messages at once??
    @commands.command()
    async def based(self, ctx: commands.Context):
        #await ctx.send((' '.join(dir(ctx)))[:499])
        await ctx.channel.send('Založeno? Založeno na čem? Na tvojem kokotovi? Prosím zavři hubu a používej slova normálně, ty stupidní troglodyte, myslíš si, že nám Bůh dal svobodu slova, jen abychom říkali náhodná slova, které nemají s tématem konverzace nic společného? Vždycky se ptáš, proč se s tebou nikdo nebaví, nebo proč s tebou nikdo nesdílí jejich názory, protože říkáš náhodné sračky jako poggers, based, cringe a když se je snažíš vysvětlit tak jen řekneš, že jsou vtipné. Jako cože?')
        #await ctx.channel.send('Co si kurva myslíš, že je na tom vtipného, jako myslíš si, že se jen tak staneš stand-up komikem, který dostane bouřlivý potlesk, jen proto, že řekl "cum" na jevišti. ANI NÁHODOU IDIOTE. Takže prosím zavři hubu a používej slova, tak jak mají být používány debile.')

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
