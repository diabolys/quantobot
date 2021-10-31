import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

TOKEN = "OTA0MzcyODEyODU1Mjc5NjQ2.YX6k0Q.N45ND14zFk38vDg67WqhAJf3I8w"

bot = commands.Bot(command_prefix=('-='))
bot.remove_command('help')

@bot.command()
async def infgenesis(ctx, arg1, arg2):
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424068122562600/sa-mKRUmC4OteMHm9MG6BRuOsNqi9d3HF7VeO2AytRaSR59L3A-bIxQcCsHbDn21JKZe')
        embed = DiscordEmbed(title=arg1, description=arg2, color='567cff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infgenesis* доступна только администраторам.')

@bot.command()
async def infdarkrp(ctx, arg1, arg2):
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424113664315402/mcJ-0pUaTa7JFaV8g2iVy_UAPO98b61lKV7bubx3bB4ECjxDohaUQXsXgXpKGJoIE62R')
        embed = DiscordEmbed(title=arg1, description=arg2, color='ffffff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infdarkrp* доступна только администраторам.')

@bot.command(name="понг")
async def ping(ctx: commands.Context):
    await ctx.send(f"Пинг бота: {round(bot.latency * 1000)}ms")

bot.run(TOKEN)
