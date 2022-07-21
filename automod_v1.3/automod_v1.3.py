import discord
from discord.ext import commands
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
        version = 1.3
        lang = 'fr'
        await client.change_presence(activity=discord.Game('/info | Developped by user')) #here you can change activity by "discord.Game", "discord.ActivityType.listenting" and "discord.ActivityType.watching". For more informations, go to https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea ;) .
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('Bot is now connected. | Autobotmod made by @user#0000  \n see on github: \n https://github.com/Malwprotector/Autobotmod')
        channel = client.get_channel(/logs/)
        await channel.send(" ** ------------------------------------------------------- \n Autobotmod version {} has been initialized. \n -------------------------------------------------------**".format(version))
        await channel.send(" **lang: {} **".format(lang))

    async def on_message(self, message):



#BASE      
        if message.author.id == self.user.id:
            return
        if message.content.startswith('/info'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the BASE plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send(' {0.author.mention} **Autobotmod, made by @user#0000, 1.3 version |** https://github.com/malwprotector \n **source code:** https://github.com/Malwprotector/Autobotmod  \n *use / prefix to send command.*'.format(message))

        if message.content.startswith('/update_info_fr'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the BASE plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.purge(limit=1)
            await message.channel.send("** Automod a été mis à jour vers sa version 1.3 ! ** \n **ajouts:** Corrections de divers bugs, publication du code source \n **Informations sur le développeur:** @user#0000  - https://github.com/malwprotector \n **Code source:** https://github.com/Malwprotector/Autobotmod \n *Contactez le développeur pour les informations complémentaires.*".format(message))    
        if message.content.startswith('autobotmod'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the BASE plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send(' ? {0.author.mention}'.format(message))
        if message.content.startswith('/ping'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the BASE plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.purge(limit=1)
            await message.channel.send('**pong!** {0.author.mention}'.format(message), delete_after=2,)





#AUTOMOD

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/') or message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send('⚠️​ **Attention** {0.author.mention} **, tu utilises du vocabulaire inapproprié! **'.format(message), delete_after=2,)

        if message.content.startswith('/banned_word/'):
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** received a warning for use of vocabulary. \n server: {0.guild.name} **".format(message))
            await message.channel.send("⚠️​ {0.author.mention} **a été banni définitivement pour spam! \n action: suppression de l'intégration discord \n effectué par: @Autobotmod#8086 \n logs: logs indisponibles**".format(message), delete_after=2,)

#AUTORESPOND_plugin
        if message.content.startswith('salut') or message.content.startswith('Salut'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTORESPOND plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send('**Hey** {0.author.mention} **, comment vas-tu?**'.format(message))

        if message.content.startswith('bonjour') or message.content.startswith('Bonjour'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTORESPOND plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send('**Hey** {0.author.mention} **, comment vas-tu?**'.format(message))

        if message.content.startswith('ca va et toi') or message.content.startswith('ça va et toi') or message.content.startswith('Ca va et toi') or message.content.startswith('Ça va et toi') or message.content.startswith('bien') or message.content.startswith('Bien') or message.content.startswith('ouais et toi') or message.content.startswith('ouais ca va et toi toi') or message.content.startswith('ouais ça va et toi toi') or message.content.startswith('Ouais ca va et toi et toi') or message.content.startswith('Ouais ça va et toi') or message.content.startswith('oui et toi') or message.content.startswith('oui ca va et toi') or message.content.startswith('oui ça va et toi') or message.content.startswith('Oui et toi') or message.content.startswith('Oui ca va et toi') or message.content.startswith('Oui ça va et toi'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTORESPOND plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send(" {0.author.mention} **Aucun problème pour moi! :) \n n'hésite pas à faire `/info` pour obtenir des informations à propos de moi! \n `/blague` pour que je te raconte une blague!**".format(message))
       
        if message.content.startswith('bonne nuit') or message.content.startswith('Bonne nuit') or message.content.startswith('a demain') or message.content.startswith('A demain') or message.content.startswith('à demain') or message.content.startswith('À demain'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTORESPOND plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send('**Passe une bonne nuit** {0.author.mention} **^^**'.format(message))

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
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the JOKE plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send(randomJokelist[numJoke])





#AUTOCORRECTOR_plugin
        if message.content.startswith('sa'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTOCORRECTOR plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send('ℹ️​ **Hey** {0.author.mention} **, tu viens de commettre une faute!  ** \n tu dois utiliser **ça** au lieu de **sa** dans ta phrase. Pour le vérifier, tu peux remplacer **ça** par **cela** ! *:)* \n *source:* https://www.lalanguefrancaise.com/orthographe/ca-va-ou-sa-va'.format(message), delete_after=10,)

        if message.content.startswith('appart'):
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} ** used the AUTOCORRECTOR plugin. \n server: {0.guild.name} **".format(message))
            await message.channel.send("ℹ️​ **Hey** {0.author.mention} **, tu viens de commettre une faute!  ** \n appart s'écrit **à part** !   ".format(message), delete_after=10,)





#LOCKED_channels
        if str(message.channel) == "📢┊annonces" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} **tried to send a message in the channel #📢┊annonces \n server: {0.guild.name} **".format(message))
   
        if str(message.channel) == "📣┊publicité" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send("{0.author.mention} **tried to send a message in the channel #📣┊publicité \n server: {0.guild.name} **".format(message))
            await message.channel.send("⚠️​ **Tu dois demander l'autorisation à un administrateur avant de poster ici!** {0.author.mention} ".format(message), delete_after=5,)

        if str(message.channel) == "📸┊médias" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} **tried to send a message in the channel #📸┊médias \n server: {0.guild.name} **".format(message))

        if str(message.channel) == "📋┊neofetch" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} **tried to send a message in the channel #📋┊neofetch \n server: {0.guild.name} **".format(message))

        if str(message.channel) == "🪐┊rôles" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} **tried to send a message in the channel #🪐┊rôles \n server: {0.guild.name} **".format(message))

        if str(message.channel) == "⬆┊bot-updates" and message.content != "":
            await message.channel.purge(limit=1)
            channel = client.get_channel(/logs/)
            await channel.send(" {0.author.mention} **tried to send a message in the channel #⬆┊bot-updates \n server: {0.guild.name} **".format(message))


client = MyClient()
client.run('/token/') #Instead of /token/ you must indicate the token of your bot available on the discord developer portal.
