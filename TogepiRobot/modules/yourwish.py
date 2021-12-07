import random
from TogepiRobot import telethn as tbot
from telethon import events

@tbot.on(events.NewMessage(pattern="/wish"))
async def wish(Togepi):
   if vegeta.is_reply:
         mm = random.randint(1,100)
         lol = await Togepi.get_reply_message()
         await tbot.send_message(Togepi.chat_id, f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol)
   if not Togepi.is_reply:
         mm = random.randint(1,100)
         Togepi = "https://telegra.ph/file/10139851d5bf597ce8c25.jpg"
         await tbot.send_file(Togepi.chat_id, Togepi,caption=f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=Togepi)
         lol = await Togepi.get_reply_message()
         await tbot.send_file(Togepi.chat_id, f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol, file=Togepi)
   if not Togepi.is_reply:
         mm = random.randint(1,100)
         Togepi = "https://telegra.ph/file/5a4dc8f8cc2cdb408df18.jpg"
         await tbot.send_file(Togepi.chat_id,f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol, file=Togepi)
         await tbot.send_file(Togepi.chat_id, Togepi,caption=f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=Togepi)
         lol = await Togepi.get_reply_message()
         await tbot.send_file(Togepi.chat_id, f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=lol)
   if not Togepi.is_reply:
         mm = random.randint(1,100)
         Togepi = "https://telegra.ph/file/f5cf989ff59da5bc122c5.jpg"
         await tbot.send_file(Togepi.chat_id, Togepi,caption=f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=lol,file=Togepi)

        
   
        #thanks to @h0daka for image
      #Codes by @Tamilvip008
#Kang With Else Gay
