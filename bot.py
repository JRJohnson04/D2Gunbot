import discord;
from discord.ext import commands
from dotenv import load_dotenv;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

load_dotenv();

#reminder to remove key when uploaded to public github


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents);
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord');

@bot.command()
async def getGun(ctx, message):
        print_text=''
        driver = webdriver.Chrome();
        driver.get('https://www.light.gg/')
        driver.implicitly_wait(1)
        input_element = driver.find_element(by=By.ID, value='nav-search')
        weapon = message
        input_element.send_keys(weapon+'\uE007')
        click_element = driver.find_element(by=By.CLASS_NAME, value='item.show-hover.item-icon')
        click_element.click()
        try:
                popularity_arr= driver.find_elements(by=By.CLASS_NAME, value='popular-bubble')
                print(popularity_arr)
                for e in popularity_arr:
                        print_text+= e.text + "\n"
        except:
                print_text+= "No popularity data available\n"
        top_roll = driver.find_elements(by=By.CLASS_NAME, value = 'perk-names')
        print_text+='Top 3 Popular Perk Combinations:\n'
        for i in range(3):
                print_text+= str(i) + '. '+ top_roll[i].text.replace('\n',' ') + "\n"
        print(print_text)
        await ctx.channel.send(print_text)

#bot.add_command(getGun)
bot.run(TOKEN);
