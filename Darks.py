import os
import sys
import discord
from discord.ext import commands
import asyncio
import requests
import random
import aiohttp
from datetime import datetime, timedelta


intents = discord.Intents.all()

darks = (".")

darks = commands.Bot(command_prefix=darks, case_insensitive=True, self_bot=True, intents=intents)

darks.remove_command("help")

@darks.event
async def on_ready():
    print(f"Logged in as {darks.user}")
    
@darks.command()
async def checkprune(ctx):
    if ctx.author.guild_permissions.kick_members:
        threshold = datetime.utcnow() - timedelta(days=1)

        role_inactive_members = {}
        
        for role in ctx.guild.roles:
            inactive_members = []
            
            for member in ctx.guild.members:
                if member.activity is None and member.status == discord.Status.online:
                    last_message = await ctx.channel.history(limit=1).get(author=member)
                    if last_message and last_message.created_at < threshold and role in member.roles:
                        inactive_members.append(member)

            role_inactive_members[role.name] = len(inactive_members)

        await ctx.send(f'**Prune :\n\n`{role_inactive_members}`**')
    else:
        await ctx.send('You do not have the required permissions to use this command.')
        
@darks.command()
@commands.has_permissions(kick_members=True)
async def prune(ctx, reason="𝐃𝐞𝐬𝐭𝐫𝐨𝐲𝐞𝐫𝐬 𝐑𝐞𝐬𝐢𝐝𝐞𝐧𝐜𝐞 ™ | DARKS X EFENDI X GLADIATOR PAPA AYE THY | .GG/DRONTOP"):
    guild = ctx.guild
    members_to_prune = await guild.prune_members(days=1, compute_prune_count=True, reason=reason)

    await ctx.send(f"**Pruned `{members_to_prune}` members with reason: `{reason}`**")
    
    
token = "PUT YOUR TOKEN HERE"
darks.run(token,bot=False)