import discord
from discord.ext import commands
import datetime

def setup_events(bot_instance: commands.Bot):
    """ Setup the events """
    @bot_instance.event
    async def on_message(message: discord.Message):
        if message.author.bot:
            return
        
        #await message.reply(message.content)

    @bot_instance.event
    async def on_guild_channel_create(channel: discord.abc.GuildChannel):
        print(f"name : {channel.name}")
        print(f"position : {channel.position}")
        print(f"category : {channel.category}")
        print(f"changed_roles : {channel.changed_roles}")
        print(f"created_at : {channel.created_at}")
        print(f"guild : {channel.guild}")
        print(f"jump_url : {channel.jump_url}")
        print(f"mention : {channel.mention}")
        print(f"overwrites : {channel.overwrites}")
        print(f"permissions_synced : {channel.permissions_synced}")

        await bot_instance.get_channel(channel.id).send(f"The channel **{channel.name}** has been created : {channel.mention}")

    @bot_instance.event
    async def on_guild_channel_update(before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        print(f"name : {before.name}")
        print(f"position : {before.position}")
        print(f"category : {before.category}")
        print(f"changed_roles : {before.changed_roles}")
        print(f"created_at : {before.created_at}")
        print(f"guild : {before.guild}")
        print(f"jump_url : {before.jump_url}")
        print(f"mention : {before.mention}")
        print(f"overwrites : {before.overwrites}")
        print(f"permissions_synced : {before.permissions_synced}")

        print(f"name : {after.name}")
        print(f"position : {after.position}")
        print(f"category : {after.category}")
        print(f"changed_roles : {after.changed_roles}")
        print(f"created_at : {after.created_at}")
        print(f"guild : {after.guild}")
        print(f"jump_url : {after.jump_url}")
        print(f"mention : {after.mention}")
        print(f"overwrites : {after.overwrites}")
        print(f"permissions_synced : {after.permissions_synced}")

        await bot_instance.get_channel(after.id).send(f"The channel **{before.name}** has been modified to **{after.name}** : {after.mention}" )

    @bot_instance.event
    async def on_guild_channel_pins_update(channel: discord.abc.GuildChannel, last_pin: datetime.datetime):
        print(f"name : {channel.name}")
        print(f"position : {channel.position}")
        print(f"category : {channel.category}")
        print(f"changed_roles : {channel.changed_roles}")
        print(f"created_at : {channel.created_at}")
        print(f"guild : {channel.guild}")
        print(f"jump_url : {channel.jump_url}")
        print(f"mention : {channel.mention}")
        print(f"overwrites : {channel.overwrites}")
        print(f"permissions_synced : {channel.permissions_synced}")

        print(last_pin)

        date = last_pin.date()

        await bot_instance.get_channel(channel.id).send(f"The channel **{channel.name}** pins got and update at {date}")

    @bot_instance.event
    async def on_typing(channel: discord.abc.GuildChannel, user: discord.Member, when: datetime.datetime):
        print(channel.name)
        print(user.name)
        print(when.date())

        # await bot_instance.get_channel(channel.id).send(f"HEYY {user.mention} ! Why are you typing here ?")

    @bot_instance.event
    async def on_raw_typing(payload: discord.RawTypingEvent):
        print(payload.channel_id)
        print(payload.guild_id)
        print(payload.timestamp)
        print(payload.user)
        print(payload.user_id)

        
        #await bot_instance.get_channel(payload.channel_id).send(payload.user.avatar)

    @bot_instance.event
    async def on_socket_event_type(event_type):
        """ See the events the server got """
        pass
        #print(event_type)
    
