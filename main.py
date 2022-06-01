import discord  # discord.py module


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):  # When a message is sent
        if (message.author.bot == False):  # If the message is not from a bot
            await message.reply('Hello World!')
            channel = message.channel.name
            restricted_channels = ["bot-commands"] # List of restricted channels

            prefix = ".mike."  # Replace with your prefix
            # If the message starts with the prefix
            if message.content.startswith(prefix):
                if channel in restricted_channels: # If the message was sent in a restricted channel
                    command = message.content[len(prefix):]  # Get the command
                    # Check if the user is an admin
                    isAdmin = [role.name ==
                            "Admin" for role in message.author.roles][0]
                    # Check for commands
                    if command == "hello" and isAdmin:
                        # Send a message
                        await message.channel.send("Hello Admin!")

                    if command == "help":
                        await message.channel.send("```\n"
                                                "Commands:\n"
                                                "help - This is the help §erver stats\n"
                                                "```")

                    else:
                        # If the command is not found
                        await message.channel.send("This command doesn't exist")
                else:
                    await message.delete()
                    await message.author.send(f"You can't use commands in #{channel}")
                    # await message.channel.send("You can't use commands in this channel")\

client = MyClient()
# Replace with your token
client.run('YOUR_TOKEN_GOES_HERE')
