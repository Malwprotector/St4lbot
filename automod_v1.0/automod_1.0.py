import discord
import random
'''
This code can be used to perform mainly self-moderation on discord servers. The developer cannot be held responsible for any problems in ANY case. 
information on the various replacements:
the /logs/ mentions must be replaced by the rooms on which you want to send the logs of your bot.
the /banned_word/ indicates the words you want the bot to delete.
The other replacements are indicated in comment in the code.
https://github.com/Malwprotector/Autobotmod
'''

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('Bot is now connected. | Autobotmod made by user - https://github.com/malwprotector')

#command
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('Autobotmod'):
            await message.channel.send(' ? {0.author.mention}'.format(message))


#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message)) 

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

#command
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        randomJokelist=["**Où superman fait-il ses courses? ||Au super marché !|| **", 
        "**Quelle mamie fait peur aux voleurs ? ||Mamie Traillette. ||**", 
        "**J'ai une blague sur les magasins ||mais elle a pas supermarché||**",
        "**Que faisaient les dinosaures quand ils n'arrivaient pas à se décider? ||Des tirageosaures||**",
        "**Pourquoi est-ce que les vêtements sont toujours fatigués quand ils sortent de la machine ? ||Parce qu'ils sont lessivés||**",
        "**Pourquoi est-ce que les livres ont-ils toujours chaud ? ||Parce qu'ils ont une couverture||**",
        "**Que se passe-t-il quand 2 poissons s'énervent ? ||Le thon monte||**",
        "**Que dit une imprimante dans l'eau ? ||J'ai papier||**",
        "**Quel est le sport préféré des insectes? ||Le criquet||**",
        "**Comment est-ce que les abeilles communiquent entre elles ? ||Par e-miel||**",
        "**Pourquoi est ce que le lapin est bleu? ||Parce qu'on lapin||**",
        "**Pourquoi est ce que Potter est triste? ||Parce que personne Harry à sa blague||**",
        "**Deux puces sortent du cinéma : ||L’une dit à l’autre : \n -on rentre à pieds ou on prend un chien ? ||**",
        ]
        if message.content.startswith('/blague'):
            numJoke = random.randint(0,len(randomJokelist))
            await message.channel.send(randomJokelist[numJoke])


client = MyClient()
client.run('/token/') #Instead of /token/ you must indicate the token of your bot available on the discord developer portal.