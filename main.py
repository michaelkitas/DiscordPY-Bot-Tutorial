import discord # discord.py module

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): # When a message is sent
        prefix = ".mike." #Replace with your prefix
        if message.content.startswith(prefix): # If the message starts with the prefix
            command = message.content[len(prefix):] # Get the command
            isAdmin = [role.name == "Admin" for role in message.author.roles][0] # Check if the user is an admin
            # Check for commands
            if command == "hello" and isAdmin:
                await message.channel.send("Hello Admin!") # Send a message

            if command == "help":
                await message.channel.send("```\n"
                                           "Commands:\n"
                                           "help - This is the help command\n"
                                           "stats - It returns the server stats\n"
                                           "```")
            else:
                # If the command is not found
                await message.channel.send("This command doesn't exist") 
                       



client = MyClient()
client.run('######') # Replace with your token
