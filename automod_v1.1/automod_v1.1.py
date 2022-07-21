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
        await client.change_presence(activity=discord.Game('/info | Developped by user')) #here you can change activity by "discord.Game", "discord.ActivityType.listenting" and "discord.ActivityType.watching". For more informations, go to https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea ;) .
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('Bot is now connected. | Autobotmod made by @user#0000  - https://github.com/malwprotector')

#BASE
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('/info'):
            await message.channel.send(' {0.author.mention} **/Autobotmod, made by @user#0000, 1.1 version |** https://github.com/malwprotector \n *use # prefix to send command.*'.format(message))
        if message.content.startswith('/update_info_fr'):
            await message.channel.send(' {0.author.mention} ** Automod a été mis à jour vers sa version 1.1! ** \n **ajouts:** La commande / a été remplacée par # - Possibilité de connexion à un serveur externe - ajout du plugin AUTOCORRECTOR - ajout du plugin BASE \n **Langue actuelle:** French 🇧🇪​ - 🇨🇵​ \n **Informations sur le développeur:** @user#0000  - https://github.com/malwprotector \n *Contactez le développeur pour les informations complémentaires.*'.format(message))
        if message.content.startswith('autobotmod'):
            await message.channel.send(' ? {0.author.mention}'.format(message))


#AUTOMOD
        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message)) 

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))

        if message.content.startswith('/banned_word/'):
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message))
     
        if message.content.startswith('/banned_word/'):
            await message.channel.send("⚠️​ {0.author.mention} **a été banni définitivement pour spam! \n action: suppression de l'intégration discord \n effectué par: @Autobotmod#8086 \n logs: logs indisponibles**".format(message))


#JOKE_plugin

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


#AUTOCORRECTOR_plugin
        if message.content.startswith('sa va'):
            await message.channel.send('​ℹ️​ **Hey** {0.author.mention} **, tu viens de commettre une faute!  ** \n tu dois utiliser **ça** au lieu de **sa** dans ta phrase. Pour le vérifier, tu peux remplacer **ça** par **cela** ! *:)* \n *source:* https://www.lalanguefrancaise.com/orthographe/ca-va-ou-sa-va'.format(message))

        if message.content.startswith('appart'):
            await message.channel.send("​ℹ️​ **Hey** {0.author.mention} **, tu viens de commettre une faute!  ** \n appart s'écrit **à part** !   ".format(message))


client = MyClient()
client.run('/token/') #Instead of /token/ you must indicate the token of your bot available on the discord developer portal.
