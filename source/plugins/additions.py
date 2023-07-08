from pyrogram import Client, filters,enums
from config import *
import asyncio
import telegram
from autoname import main as name
import string_utils
import time
import csv
import json

#سورس فينوم بيمسي - @R_R_B0

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"
    
@Client.on_message(filters.command("مسح جهاتي$",prefixes=f".") & filters.me )
async def my_con(c,msg):
  list_c = await c.get_contacts()
  ids = []
  for contact in list_c :
     ids.append(contact.id)
  await c.delete_contacts(ids)
  await msg.edit(f"✪ تم مسح {len(ids)} من جهاتك")
      

@Client.on_message(filters.command("جلب الاعضاء$",prefixes=f".") & filters.me )
async def get_members(c,msg):
  with open("members.txt","w") as f:
    ids = ""
    async for m in c.get_chat_members(msg.chat.id):
      ids += f"{m.user.id}\n"
    f.write(ids)
  await msg.reply_document(f"./members.txt")
  

@Client.on_message(filters.command("قلب$",prefixes=f".") & filters.me )
async def haert(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("مطر$",prefixes=f".") & filters.me )
async def rain(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    time.sleep(0.5)

@Client.on_message(filters.command("مكعبات$",prefixes=f".") & filters.me )
async def mokbt(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    time.sleep(0.5)

@Client.on_message(filters.command("نجمه$",prefixes=f".") & filters.me )
async def ngom(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🦋✨🦋✨🦋✨🦋✨"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("مح$",prefixes=f".") & filters.me )
async def bosh(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("💋😙😘😽💋😘😙😽💋"))
    time.sleep(0.5)

@Client.on_message(filters.command("افكر$",prefixes=f".") & filters.me )
async def afkr(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🤔🧐🤔🧐🤔🧐"))
    time.sleep(0.5)

@Client.on_message(filters.command("بموتت$",prefixes=f".") & filters.me )
async def dhkk(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("😹🤣😂😹🤣😂"))
    time.sleep(0.5)

@Client.on_message(filters.command("ساعه$",prefixes=f".") & filters.me )
async def time(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    time.sleep(0.5)

@Client.on_message(filters.command("جيم$",prefixes=f".") & filters.me )
async def gym(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    time.sleep(0.5)

@Client.on_message(filters.command("الارض$",prefixes=f".") & filters.me )
async def alard(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🌍🌎🌎🌍🌏🌍🌎"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("قلوب$",prefixes=f".") & filters.me )
async def haerts(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)

@Client.on_message(filters.command(["قمر$","اقمار$"],prefixes=f".") & filters.me )
async def moon(c,msg):
  listt = ["🌑🌒🌓🌔🌕🌖🌗🌘","🌒🌓🌔🌕🌖🌗🌘🌑","🌓🌔🌕🌖🌗🌘🌑🌒","🌔🌕🌖🌗🌘🌑🌒🌓","🌕🌖🌗🌘🌑🌒🌓🌔","🌖🌗🌘🌑🌒🌓🌔🌕","🌗🌘🌑🌒🌓🌔🌕🌖","🌘🌑🌒🌓🌔🌕🌖🌗","🌑🌒🌓🌔🌕🌖🌗🌘"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["قلوب$","قلب$"],prefixes=f".") & filters.me )
async def moon(c,msg):
  listt = ["💙❤️🧡🤍🤎🖤","❤️🧡💛💚💙💜","💖🤍🖤🤎💜💙","❤️‍🔥🧡💜💚💛","💗💜🖤🤍💙💜","🖤💛🤎💜🖤🤍","❤️‍🩹💛💚💙💜🖤","❤️❤️‍🔥❤️‍🩹💖🤎🤍","❤️💙💜🖤💛💚"]
  for x in range(1,3):
   for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["غبي$","غبيي$"],prefixes=f".") & filters.me )
async def dmah(c,msg):
  listt = ["- عقلك ➡️ 🧠\n\n🧠         <(^_^ <)🗑","- عقلك ➡️ 🧠\n\n🧠       <(^_^ <)  🗑","- عقلك ➡️ 🧠\n\n🧠     <(^_^ <)    🗑","- عقلك ➡️ 🧠\n\n🧠   <(^_^ <)      🗑","- عقلك ➡️ 🧠\n\n🧠 <(^_^ <)        🗑","- عقلك ➡️ 🧠\n\n🧠<(^_^ <)         🗑","- عقلك ➡️ 🧠\n\n(> ^_^)>🧠         🗑","- عقلك ➡️ 🧠\n\n  (> ^_^)>🧠       🗑","- عقلك ➡️ 🧠\n\n           <(^_^ <)🗑"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
        
@Client.on_message(filters.command(["تفجير$"],prefixes=f".") & filters.me )
async def boom(c,msg):
  listt = ["جاري تفجير","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n","بوووووم تم تفجير الضحيه"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["طوبه$"],prefixes=f".") & filters.me )
async def tobah(c,msg):
  listt = ["⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴","⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜","⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜","🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜","🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["مربعات$"],prefixes=f".") & filters.me )
async def morbat(c,msg):
  listt = ["⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛","⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛","⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜","👉🔴👈"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass        
        
@Client.on_message(filters.command(["تهكير$"],prefixes=f".") & filters.me )
async def hacker(c,msg):
  listt = ["** جـاري التـهكير ⚠️**","** جـاري الاتصـال بجهـاز الضحـية لأختـراقـة  📳**","** أختـراق جهـاز الضحـية الهـددف محـدد جـاري أختـراقـة ㊙️**","** تحـميل الاخـتراق  ㊙️ .. 0%**\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 4%**\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ ..10%**\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 20%**\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 36%**\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 52%**\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 84%**\n█████████████████████▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 100%**\n████████████████████████`","** تـم اخـتراق الضحـية 🆘 بواسطه : `{سورس فينوم}` . بـدون تنـازل**"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(2)
      except :
        pass

      

@Client.on_message(filters.command(["حلويات$"],prefixes=f".") & filters.me )
async def hlyat(c,msg):
  listt = ["🍧🍩🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍩🎂🍰🧁🍫🍬🍭","🍦🍧🍩🍪🎂🍰🍫🍬🍭","🍦🍧🍩🍪🎂🍰🧁🍫🍭","🍦🍧🍩🍪🍰🧁🍫🍭","🍦🍧🍩🍪??🍰🧁🍫🍬","🍦🍩🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍩🍪🎂🍰🍫🍬🍭"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
 
@Client.on_message(filters.command(["مزاج$"],prefixes=f".") & filters.me )
async def mzgg(c,msg):
  listt = ["😁","😧","😡","😢","😁","😧","😡","😢"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["قرد$"],prefixes=f".") & filters.me )
async def qrdd(c,msg):
  listt = ["🙉","🙈","🙊","🐵","🙉","🙈","🙊","🐵"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["ايد$"],prefixes=f".") & filters.me )
async def hand(c,msg):
  listt = ["👈","👉","☝️","👆","🖕","👇","✌️","🤞","🖖","🤘","🤙","🖐️","👌"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["العد التنازلي$"],prefixes=f".") & filters.me )
async def alwd(c,msg):
  listt = ["🔟","9️⃣","8️⃣","7️⃣","6️⃣","5️⃣","4️⃣","3️⃣","2️⃣","1️⃣","0️⃣","🆘"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["رموز شيطانيه$","شيطان$"],prefixes=f".") & filters.me )
async def romoz(c,msg):
  listt = ["🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️","◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️","◼️◼️\n◼️◼️","◼️"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["اسعاف$"],prefixes=f".") & filters.me )
async def asaf(c,msg):
  listt = ["_____🚑","_____🚑","____🚑_","___🚑__","__🚑___","🚑_____","🚑_____","________"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(3)
      except :
        pass
                
@Client.on_message(filters.command(["شرطه$"],prefixes=f".") & filters.me )
async def police(c,msg):
  listt = ["🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
      
@Client.on_message(filters.command(["دائره$"],prefixes=f".") & filters.me )
async def dara(c,msg):
  listt = ["⚫","⬤","●","∘",""]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.9)
      except :
        pass

@Client.on_message(filters.command("نسبة الحب$", prefixes=f".") & filters.me)
async def permalink_hob(c, msg):
    roz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rza = random.choice(roz)
    await msg.edit( f"⌔ العضو {get_name(msg.reply_to_message)} \n⌔ نسبه الحب بينك وبينه هي {rza}"
    )
        
@Client.on_message(filters.command("اذكار الصباح$", prefixes=f".") & filters.me)
async def jio_2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
#اذكار_الصباح
«أعُوذُ بِكَلِمَاتِ اللهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ»

- ٣ مرَّات.

-----------------------‐

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلَائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«أمْسَيْنَا وَأمْسَى المُلْكُ للهِ رَبِّ العَالَمِينَ ،
اللَّهُمَّ إنِّي أسْألُكَ خَيْرَ هَذِهِ اللَّيْلَةِ ، فَتْحَهَا ، وَنَصْرَهَا ، وَنُورَهَا ، وَبَرَكَتَهَا ، وَهُدَاهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِيهَا وَشَرِّ مَا بَعْدَهَا»

-----------------------‐

«أمْسَيْنَا عَلَى فِطْرَةِ الإسْلَامِ ، وَعَلَى كَلِمَةِ الإخْلَاصِ ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ ، وَعَلَى مِلَّةِ أبِينَا إبْرَاهِيمَ ، حَنِيفًا مُسْلِمًا وَمَا كَانَ مِنَ المُشْرِكِينَ»

-----------------------‐

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلَهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ» .
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command(["اوامري$","اوامر$","الاوامر"], prefixes=f".") & filters.me)
async def shark(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر سورس فينوم  ⦒
• ( `.م1` )  ⦙ اوامر الخاص 
• ( `.م2` )  ⦙ اوامر الجروبات
• ( `.م3` )  ⦙ اوامر اليوتيوب
• ( `.م4` )  ⦙ اوامر الاذاعه 
• ( `.م5` )  ⦙ اوامر الرفع 
• ( `.م6` )  ⦙ اوامر اضافيه 
• ( `.م7` )  ⦙ اوامر التسليه 1
• ( `.م8` )  ⦙ اوامر التسليه 2
• ( `.م9` )  ⦙ اوامر التسليه 3
• ( `.م10` ) ⦙ اوامر الالعاب
• ( `.م11` ) ⦙ اوامر الالعاب المتطوره
• ( `.م12` ) ⦙ اوامر الميمز
• ( `.م13` ) ⦙ اوامر الميمز 2
• ( `.م14` ) ⦙ اوامر الميمز 3
• ( `.م15` ) ⦙ اوامر النسب
• ( `.م16` ) ⦙ اوامر الزخرفه

✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م1$", prefixes=f".") & filters.me)
async def shark1(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الخاص في سورس فينوم  ⦒
✪ تفعيل ، تعطيل الترحيب 
✪ قبول ، رفض
✪ كتم ، الغاء كتم 
✪ سبام + الكلمه + الرقم (سبام فينوم 22)
✪ ايدي + ايدي بالرد
✪ انتحال ● رجوع
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م2$", prefixes=f".") & filters.me)
async def shark2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الجروبات في سورس فينوم  ⦒
✪ حظر ، الغاء حظر
✪ مسح المحظورين
✪ كتم ، الغاء كتم 
✪ مسح المكتومين
✪ ايدي + ايدي بالرد
✪ مسح رسايله (بالرد)
✪ تدمير (لتحظر جميع اعضاء المجموعه او القناه)
✪ مسح الروابط 
✪ مسح الصور 
✪ مسح + العدد
✪ اضف جهاتي
✪ فتح الكول
✪ قفل الكول
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م3$", prefixes=f".") & filters.me)
async def shark3(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر اليوتيوب في سورس فينوم  ⦒
✪ غ + اسم الاغنيه
✪ ف + اسم الفيديو
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م4$", prefixes=f".") & filters.me)
async def shark4(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الاذاعه في سورس فينوم  ⦒
✪ اذاعه خاص (بالرد علي النص)
✪ اذاعه للمجموعات (بالرد علي النص)
✪ اذاعه للقنوات (بالرد علي النص)

✪ توجيه للخاص (بالرد علي الرساله)
✪ توجيه للمجموعات (بالرد علي الرساله)
✪ توجيه للقنوات (بالرد علي الرساله)
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
     
@Client.on_message(filters.command("م5$", prefixes=f".") & filters.me)
async def shark5(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الرفع في سورس فينوم  ⦒
✪ زواج ، طلاق  زوجاتي  مسح زوجاتي
✪ رفع ، تنزيل خول  الخولات  مسح الخولات 
✪ رفع ، تنزيل بنتي  بناتي  مسح بناتي
✪ رفع ، تنزيل شاذ  الشواذ  مسح الشواذ
✪ رفع ، تنزيل عرص  المعرصين  مسح المعرصين
✪ رفع ، تنزيل قرد  القرود  مسح القرود
✪ رفع ، تنزيل ابن متناكه  ولاد المتناكه  مسح ولاد المتناكه
✪ رفع ، تنزيل اخويا  اخواتي  مسح اخواتي
✪ رفع ، تنزيل بقلبي  القلوب  مسح القلوب 
✪ رفع ، تنزيل ابني  اولادي  مسح اولادي
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م6$", prefixes=f".") & filters.me)
async def shark6(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة الاوامر الاضافيه في سورس فينوم  ⦒
✪ تلجراف (بالرد علي صوره لرفعها علي تليجراف)
✪ وش يقول (بالرد علي صوت)
✪ اذكار الصباح
✪ تفعيل تعطيل الساعه 
✪ تغيير اسمي + الاسم (تغيير اسمي VENOM)
✪ سورس
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م7$", prefixes=f".") & filters.me)
async def shark7(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر التسليه في سورس فينوم  ⦒
✪ `.مكعبات`
✪ `.قمر`
✪ `.قلوب`
✪ `.قلب`
✪ `.بموتت`
✪ `.افكر`
✪ `.جيم`
✪ `.مطر`
✪ `.الارض`
✪ `.نجمه`
✪ `.ساعه`
✪ `.مح`
✪ `.تحميل`
✪ `.هينه`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م8$", prefixes=f".") & filters.me)
async def shark8(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر التسليه 2 في سورس فينوم  ⦒
✪ `.غبي`
✪ `.تفجير`
✪ `.طوبه`
✪ `.مربعات`
✪ `.تهكير`
✪ `.حلويات`
✪ `.مزاج`
✪ `.قرد`
✪ `.ايد`
✪ `.العد التنازلي`
✪ `.دائره`
✪ `.قياس`
✪ `.بشره`
✪ `.مربع`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م9$", prefixes=f".") & filters.me)
async def shark9(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر التسليه 3 في سورس فينوم  ⦒
✪ `.رموز شيطانيه`
✪ `.اسعاف`
✪ `شرطه`
✪ `.زعلت`
✪ `.فليم`
✪ `.رسم`
✪ `.موسيقي`
✪ `.مصه`
✪ `.قطار`
✪ `.فايروس`
✪ `.مايكرو`
✪ `.ولد`
✪ `.افعي`
✪ `.عبقري`
✪ `.قتل`
✪ انتظرو تحديثات عظمه ل تليثون سورس فينوم 🔥
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م10$", prefixes=f".") & filters.me)
async def shark10(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الالعاب في سورس فينوم  ⦒
 ✪ `.اكس او` 
✪ `.حجره` لعبة حجره ورقه مقص
✪ `.ريفرسي`
✪ انتظرو تحديثات عظمه ل تليثون سورس فينوم 🔥
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م11$", prefixes=f".") & filters.me)
async def shark11(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الالعاب المتطوره في سورس فينوم  ⦒
 ✪ `.القط المجنون` 
✪ `.ركل الكره`
✪ `.السمك الشائك`
✪ `.كرة السله`
✪ `.اطلاق النار`
✪ `.كرة القدم`
✪ `.موتسيكلات`
✪ `.تبديل النجوم`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م12$", prefixes=f".") & filters.me)
async def shark12(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الميمز في سورس فينوم  ⦒
✪ `.هنضحك`
✪ `.مينفعش`
✪ `.عاوزين نعملك بني ادم`
✪ `.ي حوستي السوده`
✪ `.هنضحك حاضر`
✪ `.انا تعبان ي حامد`
✪ `.نعم انها المخدرات`
✪ `.قول كلام غير ده`
✪ `.ءنا عملت ءيه`
✪ `.عيب يجدعان`
✪ `.هتتحرقو في نار جهنم`
✪ `.يالي هتتحرقو`
✪ `.احترمي نفسك يوليه`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م13$", prefixes=f".") & filters.me)
async def shark13(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الميمز 2 في سورس فينوم  ⦒
✪ `.في رمضان`
✪ `.مش عارف اقوم`
✪ `.دمك خفيف اوي`
✪ `.لا تقتل المتعه ي مسلم`
✪ `.يختاااي`
✪ `.بيكدب`
✪ `.احنا جامدين اوي`
✪ `.اي الهبل دا`
✪ `.فاشل فاشل`
✪ `.اجمد كدا متعيطش`
✪ `.يا لاهوي`
✪ `.دا اي الهم دا`
✪ `.هعوره`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م14$", prefixes=f".") & filters.me)
async def shark14(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر الميمز 3 في سورس فينوم  ⦒
✪ `.تاخد نفس عميق`
✪ `.ربنا نصرني`
✪ `.لو معايا خنجرين`
✪ `.اماااال`
✪ `.خخ امال`
✪ `.اهلا بيكم`
✪ `.اخلاقك العاليه دي`
✪ `.علي مهلك`
✪ `.خبر اي ي مرا`
✪ `.انا بيه بن بيه`
✪ `.اتكلم بادب يولد`
✪ `.انا رمضان جانا يعم`
✪ `.انت مش مظبوط ياض`
✪ `.ي حلو ي جميل`
✪ `.خلصانه`
✪ `.انا في دوامه`
✪ `.مش اسمحلك`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م15$", prefixes=f".") & filters.me)
async def shark15(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر النسب في سورس فينوم  ⦒
✪ `.نسبة الانوثة`
✪ `.نسبة الغباء`
✪ `.نسبة الرجولة`
✪ `.نسبة المنيكه`
✪ `.نسبة التعريص`
✪ `.نسبة الكره`
✪ `.نسبة الجمدان`
✪ `.نسبة الايمان`
✪ `.نسبة الجمال`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م16$", prefixes=f".") & filters.me)
async def shark16(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
: ⦑   قائمة اوامر زخرفه في سورس فينوم  ⦒
✪ `.رموز1`
✪ `.رموز2`
✪ `.تمبلريه`
✪ `.البايو`
✪ `.الاختصارات`
✪ `.اشهر مزغرفه`
✪ `.المواليد`
✪ `.اختصارات1`
✪ `.اختصارات2`
✪ `.اختصارات3`
✪ `.اختصارات4`
✪ `.اختصارات5`
✪ `.بايو1`
✪ `.بايو2`
✪ `.بايو3`
✪ `.بايو4`
✪ `.بايو5`
✪ `.بايوهات1`
✪ `.بايوهات2`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])


 
@Client.on_message(filters.command("مسح الروابط$",prefixes=f".") & filters.me & filters.group)
async def del_urls(c,msg):
  await msg.reply("✪ جاري جلب الروابط ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.URL):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"✪ تم مسح {num} رساله تحتوي علي روابط")


@Client.on_message(filters.command(["سورس$","السورس$"],prefixes=f".") & filters.me )
async def source(c,msg):
  await msg.edit("⋖⊶◎⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 ✪ VENOM⌯⊶◎⊷⋗\n✪ ¦ [↱  DEV VENOM ↲](t.me/R_R_B0)\n✪ ¦ [𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𖧊 VENOM](t.me/RB_RO)\n✪ ¦ [𝐒𝐎𝐔𝐑𝐂𝐄 𖧊 VENOM](t.me/RB_RO)\n⋖⊶◎⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 ✪ VENOM⌯⊶◎⊷⋗")
  

@Client.on_message(filters.command("مسح الصور$",prefixes=f".") & filters.me & filters.group)
async def del_photos(c,msg):
  await msg.reply("✪ جاري جلب الصور ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.PHOTO):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"✪ تم مسح {num} رساله تحتوي علي صور")

  
  
@Client.on_message(filters.command("تفعيل الترحيب$",prefixes=f".") & filters.me )
async def wel(c,msg):
  r.set(f"{sudo_id}welcome","on")
  await msg.edit("✪ تم تفعيل الترحيب")

@Client.on_message(filters.command("تعطيل الترحيب$",prefixes=f".") & filters.me )
async def unwel(c,msg):
  r.delete(f"{sudo_id}welcome")
  await msg.edit("✪ تم تعطيل الترحيب")
  

@Client.on_message(filters.command("تعطيل الساعه$",prefixes=f".") & filters.me )
async def clockk(c,msg):
  r.delete(f"{sudo_id}clockk")
  get = await c.get_chat("me")
  await c.update_profile(first_name=f'{get.last_name}' ,last_name="")
  await msg.edit("✪ تم تعطيل الساعه")
@Client.on_message(filters.command("تفعيل الساعه$",prefixes=f".") & filters.me )
async def unclockk(c,msg):
  get = await c.get_chat("me")
  if get.last_name:
    my_name = f"{get.first_name} {get.last_name}"
  else :
    my_name = get.first_name
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit("✪ تم تفعيل الساعه")
  await name()
  
@Client.on_message(filters.regex("^.تغيير اسمي (.*)") & filters.me )
async def chang_name(c,msg):
  my_name = msg.text
  my_name = my_name.replace(".تغيير اسمي","")
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit(f"✪ تم تغيير اسمك الي {my_name}")
  await name()
  
@Client.on_message(filters.regex("^.مسح [0-9]+$") & filters.me )
async def del_message(c,msg):
  textt = msg.text
  num = int(textt.split(" ")[1])
  list1 = []
  msg_id = msg.id
  for i in range(1,num):
    list1.append(msg_id)
    msg_id = msg_id - 1
  try :
    await c.delete_messages(msg.chat.id, list1)
  except Exception as e :
    await msg.reply(e)
    
@Client.on_message(filters.regex("^.سبام (.*?) [0-9]+$") & filters.me )
async def spam_message(c,msg):
  await msg.delete()
  textt = msg.text
  num = int(textt.split(" ")[2])
  word = textt.split(" ")[1]
  for i in range(1,num):
    await c.send_message(msg.chat.id,word)
    
@Client.on_message(filters.regex("^.بحث (.*)") & filters.me )
async def search_word(c,msg):
  textt = msg.text
  word = textt.replace(".بحث ","")
  num = 0
  async for message in c.search_messages(msg.chat.id, query=word):
    try :
      await c.send_message(msg.chat.id,".",reply_to_message_id=message.id)
      num += 1
    except : 
      pass
  await message.reply(f"✪ العدد {num}")
  
@Client.on_message(filters.command("مسح رسايله$",prefixes=f".") & filters.me & filters.reply )
async def dell_all_msg(c,msg):
  if msg.reply_to_message.from_user.id in sudo_command:
    return await msg.edit("✪ لا يمكنك استخدام الامر علي مبرمجين السورس")
  try :
    await c.delete_user_history(msg.chat.id,msg.reply_to_message.from_user.id)
    await c.send_message(msg.chat.id,"✪ تم مسح رسايله")
  except Exception as e:
    await msg.edit("✪ ليس لديك صلاحيه المسح")

@Client.on_message(filters.command("رموز1$", prefixes=f".") & filters.me)
async def shark17(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
`𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 
𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻 
 ☤ 𓅾 𓅿 𓆀 𓆁 𓆂
𓀀 𓀁 𓀂 𓀃 𓀄 𓀅 𓀆 𓀇 𓀈 𓀉 𓀊 𓀋 𓀌 𓀍 𓀎 𓀏 𓀐 𓀑 𓀒 𓀓 𓀔 𓀕 𓀖 𓀗 𓀘 𓀙 𓀚 𓀛 𓀜 𓀝 𓀞 𓀟 𓀠 𓀡 𓀢 𓀣 𓀤 𓀥 𓀦 𓀧 𓀨 𓀩 𓀪 𓀫 𓀬 𓀭 𓀮 𓀯 𓀰 𓀱 𓀲 𓀳 𓀴 𓀵 𓀶 𓀷 𓀸 𓀹 𓀺 𓀻 𓀼 𓀽 𓀾 𓀿 𓁀 𓁁 𓁂 𓁃 𓁄 𓁅 𓁆 𓁇 𓁈 𓁉 𓁊 𓁋 𓁌 𓁍 𓁎 𓁏 𓁐 𓁑 𓁒 𓁓 𓁔 𓁕 𓁖 𓁗 𓁘 𓁙 𓁚 𓁛 𓁜 𓁝 𓁞 𓁟 𓁠 𓁡 𓁢 𓁣 𓁤 𓁥 𓁦 𓁧 𓁨 𓁩 𓁪 𓁫 𓁬 𓁭 𓁮 𓁯 𓁰 𓁱 𓁲 𓁳 𓁴 𓁵 𓁶 𓁷 𓁸 𓁹 𓁺 𓁻 𓁼 𓁽 𓁾 𓁿 𓂀𓂅 𓂆 𓂇 𓂈 𓂉 𓂊 𓂋 𓂌 𓂍 𓂎 𓂏 𓂐 𓂑 𓂒 𓂓 𓂔 𓂕 𓂖 𓂗 𓂘 𓂙 𓂚 𓂛 𓂜 𓂝 𓂞 𓂟 𓂠 𓂡 𓂢 𓂣 𓂤 𓂥 𓂦 𓂧 𓂨 𓂩 𓂪 𓂫 𓂬 𓂭 𓂮 𓂯 𓂰 𓂱 𓂲 𓂳 𓂴 𓂵 𓂶 𓂷 𓂸 𓂹 𓂺 𓂻 𓂼 𓂽 𓂾 𓂿 𓃀 𓃁 𓃂 𓃃 𓃅 𓃆 𓃇 𓃈 𓃉 𓃊 𓃋 𓃌 𓃍 𓃎 𓃏 𓃐 𓃑 𓃒 𓃓 𓃔 𓃕 𓃖 𓃗 𓃘 𓃙 𓃚 𓃛 𓃜 𓃝 𓃞 𓃟 𓃠 𓃡 𓃢 𓃣 𓃤 𓃥 𓃦 𓃧 𓃨 𓃩 𓃪 𓃫 𓃬 𓃭 𓃮 𓃯 𓃰 𓃱 𓃲 𓃳 𓃴 𓃵 𓃶 𓃷 𓃸 𓃹 𓃺 𓃻 𓃼 𓃽 𓃾 𓃿 𓄀 𓄁 𓄂 𓄃 𓄄 𓄅 𓄆 𓄇 𓄈 𓄉 𓄊 𓄋 𓄌 𓄍 𓄎 𓄏 𓄐 𓄑 𓄒 𓄓 𓄔 𓄕 𓄖 𓄙 𓄚 𓄛 𓄜 𓄝 𓄞 𓄟 𓄠 𓄡 𓄢 𓄣 𓄤 𓄥 𓄦 𓄧 𓄨 𓄩 𓄪 𓄫 𓄬 𓄭 𓄮 𓄯 𓄰 𓄱 𓄲 𓄳 𓄴 𓄵 𓄶 𓄷 𓄸 𓄹 𓄺   𓄼 𓄽 𓄾 𓄿 𓅀 𓅁 𓅂 𓅃 𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔 𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅪 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻 𓅼 𓅽 𓅾 𓅿 𓆀 𓆁 𓆂 𓆃 𓆄 𓆅 𓆆 𓆇 𓆈 𓆉 𓆊 𓆋 𓆌 𓆍 𓆎 𓆐 𓆑 𓆒 𓆓 𓆔 𓆕 𓆖 𓆗 𓆘 𓆙 𓆚 𓆛 𓆜 𓆝 𓆞 𓆟 𓆠 𓆡 𓆢 𓆣 𓆤 𓆥 𓆦 𓆧 𓆨 𓆩𓆪 𓆫 𓆬 𓆭 𓆮 𓆯 𓆰 𓆱 𓆲 𓆳 𓆴 𓆵 𓆶 𓆷 𓆸 𓆹 𓆺 𓆻 𓆼 𓆽 𓆾 𓆿 𓇀 𓇁 𓇂 𓇃 𓇄 𓇅 𓇆 𓇇 𓇈 𓇉 𓇊 𓇋 𓇌 𓇍 𓇎 𓇏 𓇐 𓇑 𓇒 𓇓 𓇔 𓇕 𓇖 𓇗 𓇘 𓇙 𓇚 𓇛 𓇜 𓇝 𓇞 𓇟 𓇠 𓇡 𓇢 𓇣 𓇤 𓇥 𓇦 𓇧 𓇨 𓇩 𓇪 𓇫 𓇬 𓇭 𓇮 𓇯 𓇰 𓇱 𓇲 𓇳 𓇴 𓇵 𓇶 𓇷 𓇸 𓇹 𓇺 𓇻 𓇼 𓇾 𓇿 𓈀 𓈁 𓈂 𓈃 𓈄 𓈅 𓈆 𓈇 𓈈 𓈉 𓈊 𓈋 𓈌 𓈍 𓈎 𓈏 𓈐 𓈑 𓈒 𓈓 𓈔 𓈕 𓈖 𓈗 𓈘 𓈙 𓈚 𓈛 𓈜 𓈝 𓈞 𓈟 𓈠 𓈡 𓈢 𓈣 𓈤  𓈥 𓈦 𓈧 𓈨 𓈩 𓈪 𓈫 𓈬 𓈭 𓈮 𓈯 𓈰 𓈱 𓈲 𓈳 𓈴 𓈵 𓈶 𓈷 𓈸 𓈹 𓈺 𓈻 𓈼 𓈽 𓈾 𓈿 𓉀 𓉁 𓉂 𓉃 𓉄 𓉅 𓉆 𓉇 𓉈 𓉉 𓉊 𓉋 𓉌 𓉍 𓉎 𓉏 𓉐 𓉑 𓉒 𓉓 𓉔 𓉕 𓉖 𓉗 𓉘 𓉙 𓉚 𓉛 𓉜 𓉝 𓉞 𓉟 𓉠 𓉡 𓉢 𓉣 𓉤 𓉥 𓉦 𓉧 𓉨 𓉩 𓉪 𓉫 𓉬 𓉭 𓉮 𓉯 𓉰 𓉱 𓉲 𓉳 𓉴 𓉵 𓉶 𓉷 𓉸 𓉹 𓉺 𓉻 𓉼 𓉽 𓉾 𓉿 𓊀 𓊁 𓊂 𓊃 𓊄 𓊅 𓊈 𓊉 𓊊 𓊋 𓊌 𓊍 𓊎 𓊏 𓊐 𓊑 𓊒 ?? 𓊔 𓊕 ?? ?? 𓊘 𓊙 𓊚 𓊛 𓊜 𓊝 𓊞 𓊟 𓊠 𓊡 𓊢 𓊣 𓊤 𓊥 𓊦 𓊧 𓊨 𓊩 𓊪 𓊫 𓊬 𓊭 𓊮 𓊯 𓊰 𓊱 𓊲 𓊳 𓊴 𓊵 𓊶 𓊷 𓊸 𓊹 𓊺 𓊻 𓊼 ?? ?? 𓊿 𓋀 𓋁 𓋂 𓋃 𓋄 𓋅 𓋆 𓋇 𓋈 𓋉 𓋊 𓋋 𓋌 𓋍 𓋎 𓋏 𓋐 𓋑 𓋒 𓋓 𓋔 𓋕 𓋖 𓋗 𓋘 𓋙 𓋚 𓋛 𓋜 𓋝 𓋞 𓋟 𓌰 𓌱 𓌲 𓌳 𓌴 𓌵 𓌶 𓌷 𓌸 𓌹 𓌺 𓌻 𓌼 𓌽 𓌾 𓌿 𓍀 𓍁 𓍂 𓍃 𓍄 𓍅 𓍆 𓍇 𓍈 𓍉 𓍊 𓍋 𓍌 𓍍 𓍎 𓍏 𓍐 𓍑 𓍒 𓍓 𓍔 𓍕 𓍖 𓍗 𓍘 𓍙 𓍚 𓍛 𓍜 𓍝 𓍞 𓍟 𓍠 𓍡 𓍢 𓍣 𓍤 𓍥 𓍦 𓍧 𓍨 𓍩 𓍪 𓍫 𓍬 𓍭 𓍮 𓍯 𓍰 𓍱 𓍲 𓍳 𓍴 𓍵 𓍶 𓍷 𓍸 𓍹 𓍺 𓍻 𓍼 𓍽 𓍾 𓍿 𓎀 𓎁 𓎂 𓎃 𓎄 𓎅 𓎆 𓎇 𓎈 𓎉 𓎊 𓎋 𓎌 𓎍 𓎎 𓎏 𓎐 𓎑 𓎒 𓎓 𓎔 𓎕 𓎖 𓎗 𓎘 𓎙 𓎚 𓎛 𓎜 𓎝 𓎞 𓎟 𓎠 𓎡 𓏋 𓏌 𓏍 𓏎 𓏏 𓏐 𓏑 𓏒 𓏓 
 𓏕 𓏖 𓏗 𓏘 𓏙 𓏚 𓏛 𓏜 𓏝 𓏞 𓏟 𓏠 𓏡 𓏢 𓏣 𓏤 𓏥 𓏦 𓏧 𓏨 𓏩 𓏪 𓏫 𓏬 𓏭 𓏮 𓏯 𓏰 𓏱 𓏲 𓏳 𓏴 𓏶 𓏷 𓏸 𓏹 𓏺 𓏻 𓏼 𓏽 𓏾 𓏿 𓐀 𓐁 𓐂 𓐃 𓐄 𓐅 𓐆
- 𖣨 ، ෴ ، 𖡺  ، 𖣐 ، ✜ ، ✘ ، 𖡻 ،
- ༄ ، ༺༻ ، ༽༼ ،  ╰☆╮،  
- ɵ̷᷄ˬɵ̷᷅ ، ⠉̮⃝ ، ࿇࿆ ، ꔚ، ま ، ☓ ،
𓆉 . 𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱 . 𓅓 . 𐂃  . ꕥ  . ⌘ . ♾ .    ꙰  .  . ᤑ .  ﾂ .
✦ ,✫ ,✯, ✮ ,✭ ,✰, ✬ ,✧, ✤, ❅ , 𒀭,✵ , ✶ , ✷ , ✸ , ✹ ,⧫, . 𐂂 
-〘 𖢐 ، 𒍦 ، 𒍧 ، 𖢣 ، 𝁫 ، 𒍭 ، 𝁅 ، 𝁴 ، 𒍮 ، 𝁵 ، 𝀄 ، 𓏶 ، 𓏧 ، 𓏷 ، 𓏯 ، 𓏴 ، 𓏳 ، 𓏬 ، 𓏦 ، 𓏵 ، 𓏱 ، ᳱ ، ᯼ ، 𐃕 ، ᯥ ، ᯤ ، ᯾ ، ᳶ ، ᯌ ، ᢆ ،
 ᥦ ، ᨙ ، ᨚ  ، ᨔ  ، ⏢ ، ⍨ ، ⍃ ، ⏃ ، ⍦ ، ⏕ ، ⏤ ، ⏁ ، ⏂ ، ⏆ ، ⌳ ، ࿅ ، ࿕ ، ࿇ ، ᚙ ، ࿊ ، ࿈ ، ྿ ،
 ࿂ ، ࿑ ،  ᛥ ، ࿄ ، 𐀁 ، 𐀪 ، 𐀔 ، 𐀴 ، 𐀤 ، 𐀦 ، 𐀂 ، 𐀣 ، 𐀢 ، 𐀶 ، 𐀷 ، 𐂭 ، 𐂦 ، 𐂐 ، 𐂅 ، 𐂡 ، 𐂢 ، 𐂠 ، 𐂓 ، 𐂑 ، 𐃸 ، 𐃶 ، 𐂴 ، 𐃭 ، 𐃳 ، 𐃣 ، 𐂰 ، 𐃟 ، 𐃐 ، 𐃙 ، 𐃀 ، 𐇮 ، 𐇹 ، 𐇲 ، 𐇩 ، 𐇪 ، 𐇶 ، 𐇻 ، 𐇡 ، 𐇸 ، 𐇣 ، 𐇤 ، 𐎅 ، 𐏍 ، 𐎃 ، 𐏒 ، 𐎄 ، 𐏕 〙.
╔ ╗. 𓌹  𓌺 .〝  〞. ‹ ›  .「  」.〖 〗. 《》 .  < > . « »  . ﹄﹃
₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀
𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 𝟖 𝟗 𝟎
𝟭 𝟮 𝟯 𝟰 𝟱 𝟲 𝟳 𝟴 𝟵 𝟬
①②③④⑤⑥⑦⑧⑨⓪
❶❷❸❹❺❻❼❽❾⓿
⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("رموز2$", prefixes=f".") & filters.me)
async def shark18(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
`———————×———————
 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾  𝟿
 ? 𝟙  𝟚  𝟛  𝟜  𝟝  𝟞  𝟟  𝟠 𝟡
 𝟬 𝟭  𝟮  𝟯  𝟰  𝟱   𝟲  𝟳  𝟴  𝟵  
 𝟎  𝟏  𝟐  𝟑  𝟒   𝟓   𝟔  𝟕   𝟖   𝟗
０ １ ２ ３ ４ ５ ６ ７８９
———————×———————
ᾋ ᾌ ᾍ ᾎ ᾏ ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ ᾰ ᾱ ᾲ ᾳ ᾴ ᾶ ᾷ Ᾰ Ᾱ Ὰ Ά ᾼ ᾽ ι ᾿ ῀ ῁ ῂ ῃ ῄ ῆ ῇ Ὲ Έ Ὴ Ή ῌ ῍ ῎ ῏ ῐ ῑ ῒ ΐ ῖ ῗ Ῐ Ῑ Ὶ Ί ῝ ῞ ῟ ῠ ῡ ῢ ΰ ῤ ῥ ῦ ῧ Ῠ Ῡ Ὺ Ύ Ῥ ῭ ΅ ` ῲ ῳ ῴ ῶ ῷ Ὸ Ό Ὼ Ώ ῼ ´ ῾ ῿                         ‌ ‍ ‎ ‏ ‐ ‑ ‒ – — ― ‖ ‗ ‘ ’ ‚ ‛ “ ” „ ‟ † ‡ • ‣ ․ ‥ … ‧       ‰ ‱ ′ ″ ‴ ‵ ‶ ‷ ‸ ‹ › ※  ‽ ‾ ‿ ⁀ ⁁ ⁂ ⁃ ⁄ ⁅ ⁆ ⁇  ⁊ ⁋ ⁌ ⁍ ⁎ ⁏ ⁐ ⁑ ⁒ ⁓ ⁔ ⁕ ⁖ ⁗ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞   ⁠ ⁡ ⁢ ⁣ ⁤ ⁥ ‌ ‌ ⁨ ⁩ ⁪ ⁫ ⁬ ⁭ ⁮ ⁯ ⁰ ⁱ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₐ ₑ ₒ ₓ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ ₝ ₞ ₟ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ € ₭ ₮ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ℀ ℁ ℂ ℃ ℄ ℅ ℆ ℇ ℈ ℉ ℊ ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟ ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ ℶ ℷ ℸ  ℺ ℻ ℼ ℽ ℾ ℿ ⅀ ⅁ ⅂ ⅃ ⅄ ⅅ ⅆ ⅇ ⅈ ⅉ ⅊ ⅋ ⅌ ⅍ ⅎ ⅏ ⅐ ⅑ ⅒ ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ↀ ↁ ↂ Ↄ ↉ ↊ ↋ ← ↑ → ↓  ↚ ↛ ↜ ↝ ↞ ↟ ↠ ↡ ↢ ↣ ↤ ↥ ↦ ↧ ↨  ↫ ↬ ↭ ↮ ↯ ↰ ↱ ↲ ↳ ↴ ↵ ↶ ↷ ↸ ↹ ↺ ↻ ↼ ↽ ↾ ↿ ⇀ ⇁ ⇂ ⇃ ⇄ ⇅ ⇆ ⇇ ⇈ ⇉ ⇊ ⇋ ⇌ ⇍ ⇎ ⇏ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟ ⇠ ⇡ ⇢ ⇣ ⇤ ⇥ ⇦ ⇧ ⇨ ⇩ ⇪ ⇫ ⇬ ⇭ ⇮ ⇯ ⇰ ⇱ ⇲ ⇳ ⇴ ⇵ ⇶ ⇷ ⇸ ⇹ ⇺ ⇻ ⇼ ⇽ ⇾ ⇿ ∀ ∁ ∂ ∃ ∄ ∅ ∆ ∇ ∈ ∉ ∊ ∋ ∌ ∍ ∎ ∏ ∐ ∑ − ∓ ∔ ∕ ∖ ∗ ∘ ∙ √ ∛ ∜ ∝ ∞ ∟ ∠ ∡ ∢ ∣ ∤ ∥ ∦ ∧ ∨ ∩ ∪ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂ ⌃ ⌄ ⌅ ⌆ ⌇ ⌈ ⌉ ⌊ ⌋ ⌌ ⌍ ⌎ ⌏ ⌐ ⌑ ⌒ ⌓ ⌔ ⌕ ⌖ ⌗ ⌘ ⌙  ⌛️ ⌜ ⌝ ⌞ ⌟ ⌠ ⌡ ⌢ ⌣ ⌤ ⌥ ⌦ ⌧ ⌨️ 〈 〉 ⌫ ⌬ ⌭ ⌮ ⌯ ⌰ ⌱ ⌲ ⌳ ⌴ ⌵ ⌶ ⌷ ⌸ ⌹ ⌺ ⌻ ⌼ ⌽ ⌾ ⌿ ⍀ ⍁ ⍂ ⍃ ⍄ ⍅ ⍆ ⍇ ⍈ ⍉ ⍊ ⍋ ⍌ ⍍ ⍎ ⍏ ⍐ ⍑ ⍒ ⍓ ⍔ ⍕ ⍖ ⍗ ⍘ ⍙ ⍚ ⍛ ⍜ ⍝ ⍞ ⍟ ⍠ ⍡ ⍢ ⍣ ⍤ ⍥ ⍦ ⍧ ⍨ ⍩ ⍪ ⍫ ⍬ ⍭ ⍮ ⍯ ⍰ ⍱ ⍲ ⍳ ⍴ ⍵ ⍶ ⍷ ⍸ ⍹ ⍺ ⍻ ⍼ ⍽ ⍾ ⍿ ⎀ ⎁ ⎂ ⎃ ⎄ ⎅ ⎆ ⎇ ⎈ ⎉ ⎊ ⎋ ⎌ ⎍ ⎎ ⎏ ⎐ ⎑ ⎒ ⎓ ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞ ⎟ ⎠ ⎡ ⎢ ⎣ ⎤ ⎥ ⎦ ⎧ ⎨ ⎩ ⎪ ⎫ ⎬ ⎭ ⎮ ⎯ ⎰ ⎱ ⎲ ⎳ ⎴ ⎵ ⎶ ⎷ ⎸ ⎹ ⎺ ⎻ ⎼ ⎽ ⎾ ⎿ ⏀ ⏁ ⏂ ⏃ ⏄ ⏅ ⏆ ⏇ ⏈ ⏉ ⏋ ⏌ ⏍ ⏎  ⏐ ⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙ ⏚ ⏛ ⏜ ⏝ ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ␋ ␢ ␣ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ  Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿ ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟ ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯ ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╬﹌ ╭ ╮ ╯ ╰ ╰☆╮ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿ ▀ ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓ ▔ ▕ ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪️ ▫️ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿  ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◔ʊ ◕ ◖ ◗ ◘ ◙ ◚ ◛ ◜ ◝ ◞ ◟ ◠ ◡ ◢ ◣ ◤ ◥ ◦ ◧ ◨ ◩ ◪ ◫ ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺  ☓ ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷  ♡ ♢   ♰ ♱  ⚆   ⚊ ⚋ ⚌ ⚍ ⚎ ⚏  ✐ ✑  ✓ ✔️ ✕ ✖️ ✗ ✘ ✙ ✚ ✛ ✜  ✞ ✟ ✠ ✢ ✣ ✤ ✥ ✦ ✧ ✧♱ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ✱ ✲  ✵ ✶ ✷ ✸ ✹ ✺ ✻ ✼ ✽ ✾ ✿ ❀ ❁ ❂ ❃ ❅ ❆ ❈ ❉ ❊ ❋ ❍ ❏ ❐ ❑ ❒ ❖  ❘ ❙ ❚ ❛ ❜ ❝ ❞ ❡ ❢ ❥ ❦ ❧ ❨ ❩ ❪ ❫ ❬ ❭ ❮ ❯ ❰ ❱ ❲ ❳ ❴ ❵ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ➀ ➁ ➂ ➃ ➄ ➅ ➆ ➇ ➈ ➉ ➊ ➋ ➌ ➍ ➎ ➏ ➐➑ ➒ ➓ ➔ ➘ ➙ ➚ ➛ ➜ ➝ ➞ ➟ ➠  ➢ ➣ ➤ ➥ ➦ ➧ ➨ ➩ ➪ ➫ ➬ ➭ ➮ ➯ ➱ ➲ ➳ ➴ ➵ ➶ ➷ ➸ ➹ ➺ ➻ ➼ ➽ ➾ ⟀ ⟁ ⟂ ⟃ ⟄ ⟇ ⟈ ⟉ ⟊ ⟐ ⟑ ⟒ ⟓ ⟔ ⟕ ⟖ ⟗ ⟘ ⟙ ⟚ ⟛ ⟜ ⟝ ⟞ ⟟ ⟠ ⟡ ⟢ ⟣ ⟤ ⟥ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟰ ⟱ ⟲ ⟳ ⟴ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ⟻ ⟼ ⟽ ⟾ ⟿ ⤀ ⤁ ⤂ ⤃ ⤄ ⤅ ⤆ ⤇ ⤈ ⤉ ⤊ ⤋ ⤌ ⤍ ⤎ ⤏ ⤐ ⤑ ⤒ ⤓ ⤔ ⤕ ⤖ ⤗ ⤘ ⤙ ⤚ ⤛ ⤜ ⤝ ⤞ ⤟ ⤠ ⤡ ⤢ ⤣ ⤤ ⤥ ⤦ ⤧ ⤨ ⤩ ⤪ ⤫ ⤬ ⤭ ⤮ ⤯ ⤰ ⤱ ⤲ ⤳ ⤶ ⤷ ⤸ ⤹ ⤺ ⤻ ⤼ ⤽ ⤾ ⤿ ⥀ ⥁ ⥂ ⥃ ⥄ ⥅ ⥆ ⥇ ⥈ ⥉ ⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡ ⥢ ⥣ ⥤ ⥥ ⥦ ⥧ ⥨ ⥩ ⥪ ⥫ ⥬ ⥭ ⥮ ⥯ ⥰ ⥱ ⥲ ⥳ ⥴ ⥵ ⥶ ⥷ ⥸ ⥹ ⥺ ⥻ ⥼ ⥽ ⥾ ⥿ ⦀ ⦁ ⦂ ⦃ ⦄ ⦅ ⦆ ⦇ ⦈ ⦉ ⦊ ⦋ ⦌ ⦍ ⦎ ⦏ ⦐ ⦑ ⦒ ⦓ ⦔ ⦕ ⦖ ⦗ ⦘ ⦙ ⦚ ⦛ ⦜ ⦝ ⦞ ⦟ ⦠ ⦡ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦰ ⦱ ⦲ ⦳ ⦴ ⦵ ⦶ ⦷ ⦸ ⦹ ⦺ ⦻ ⦼ ⦽ ⦾ ⦿ ⧀ ⧁ ⧂ ⧃ ⧄ ⧅ ⧆ ⧇ ⧈ ⧉ ⧊ ⧋ ⧌ ⧍ ⧎ ⧏ ⧐ ⧑ ⧒ ⧓ ⧔ ⧕ ⧖ ⧗ ⧘ ⧙ ⧚ ⧛ ⧜ ⧝ ⧞ ⧟ ⧡ ⧢ ⧣ ⧤ ⧥ ⧦ ⧧ ⧨ ⧩ ⧪ ⧫ ⧬ ⧭ ⧮ ⧯ ⧰ ⧱ ⧲ ⧳ ⧴ ⧵ ⧶ ⧷ ⧸ ⧹ ⧺ɷ
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎`
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
@Client.on_message(filters.command("البايو$", prefixes=f".") & filters.me)
async def shark19(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
**⎈ ⦙  - 𝑩𝑰𝑶 𝑳𝑰𝑺𝑻 : **\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⎈ ⦙  قائـمه البايو :** \n⎈ ⦙  `.بايو1 ` \n⎈ ⦙  `.بايو2` \n⎈ ⦙  `.بايو3 ` \n⎈ ⦙  `.بايو4 ` \n⎈ ⦙  `.بايو5` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
@Client.on_message(filters.command("تمبلريه$", prefixes=f".") & filters.me)
async def shark20(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⎈ ⦙  قائـمه اوامر الزغرفه :** \n⎈ ⦙  `.المواليد ` \n⎈ ⦙  `.اشهر مزغرفه` \n⎈ ⦙  `.الاختصارات` \n⎈ ⦙  `.البايو` \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])        

@Client.on_message(filters.command("اشهر مزغرفه$", prefixes=f".") & filters.me)
async def shark21(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "-₁₉₉₀\n"
                "-₁₉₉₁\n"
                "-₁₉₉₂\n"
                "-₁₉₉₃\n"
                "-₁₉₉₄\n"
                "-₁₉₉₅\n"
                "-₁₉₉₆\n"
                "-₁₉₉₇\n"
                "-₁₉₉₈\n"
                "-₁₉₉₉\n"
                "-₂₀₀₀\n"
                "-₂₀₀₁\n"
                "-₂₀₀₂\n"
                "-₂₀₀₃\n"
                "-₂₀₀₄\n"
                "-₂₀₀₅-\n"
                "-₂₀₀₆\n"
                "-₂₀₀₇\n"
                "---\n"
                "-𝒋𝒂𝒏𝒖𝒂𝒓𝒚.💞\n"
                "-𝒇𝒆𝒃𝒓𝒖𝒂𝒓𝒚.💞\n"
                "-𝒎𝒂𝒓𝒄𝒉.💞\n"
                "𝒂𝒑𝒓𝒊𝒍.💞\n"
                "-𝒎𝒂𝒚.💞\n"
                "-𝒋𝒖𝒏𝒆.💞\n"
                "-𝒋𝒖𝒍𝒚.💞\n"
                "-𝒂𝒖𝒈𝒖𝒔𝒕 .💞\n"
                "-𝒔𝒆𝒑𝒕𝒆𝒎𝒃𝒆𝒓 .💞\n"
                "-𝒐𝒄𝒕𝒐𝒃𝒆𝒓.💞\n"
                "-𝒏𝒐𝒗𝒆𝒎𝒃𝒆𝒓.💞\\n"
                "-𝒅𝒆𝒄𝒆𝒎𝒃𝒆𝒓.💞\n"
                "------\n"
                "-𝐒𝐔𝐍𝐃𝐀𝐘.♡\n"
                "-𝐌𝐎𝐍𝐃𝐀𝐘.♡\n"
                "-𝐓𝐔𝐄𝐒𝐃𝐀𝐘.♡\n"
                "-𝐖𝐄𝐃𝐍𝐄𝐒𝐃𝐀𝐘.♡\n"
                "-𝐓𝐇𝐔𝐑𝐒𝐃𝐀𝐘.♡\n"
                "-𝐅𝐑𝐈𝐃𝐀𝐘.♡\n"
                "-𝐒𝐀𝐓𝐔𝐑𝐃𝐀𝐘.♡"
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])        
@Client.on_message(filters.command("المواليد$", prefixes=f".") & filters.me)
async def shark22(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "₁₉₉₅\n"
                "₁₉₉₆\n"
                "₁₉₉₇\n"
                "₁₉₉₈\n"
                "₁₉₉₉\n"
                "₂₀₀₀\n"
                "₂₀₀₁\n"
                "₂₀₀₂\n"
                "₂₀₀₃"
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])              

@Client.on_message(filters.command("اختصارات1$", prefixes=f".") & filters.me)
async def shark23(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "ڪݪخـرا .\n"
                "نجَبـيہ .\n"
                "ۿـا .\n"
                "ـلا .\n"
                "حَياتـჂ̤ .\n"
                "سَـرسَحي .\n"
                "ڪياتۿهۃ .\n"
                "فدوۿهۃ .\n"
                "حَبيبـჂ̤ .\n"
                "حَبيبتـჂ̤ .\n"
                "مَڪدࢪ .\n"
                "حَيوانۿهۃ .\n"
                "ﺂوڪيـۃ .\n"
                "ۿـلو .\n"
                "وَلـჂ̤ .\n"
                "ههههۃ .\n"
                "لَـطيف .\n"
                "لَطيفهۃ .\n"
                "رﯢحـيہ .\n"
                "راحتـჂ̤ .\n"
                "ڪݪبـيہ .\n"
                "ﺂنام .\n"
                "ﺂڪل .\n"
                "طالـ؏ .\n"
                "طالعهۃ .\n"
                "مَۃ ﺂدرჂ̤ .\n"
                "شَڪو ؟ .\n"
                "؏َـليهۃ .\n"
                "؏َـليَك .\n"
                "ﺂوفـٰہ .\n"
                "ﺂمـﯢ؏ .\n"
                "حَبڪـٰہ .\n"
                "حَبجـٰہ .\n"
                "ﺂحـح .\n"
                "يـﺂჂ̤ .\n"
                "بـﺂჂ̤ .\n"
                "نـﺂنـჂ̤ .\n"
                "ﺂبـﯢﺳـہ .\n"
                "ﺂڪࢪط .\n"
                "ﺂ؏ـضـہ .\n"
                "يَـۃ فِـدﯢا\n"
                "ۿـواჂ̤ .\n"
                "ساعۿۃ .\n"
                "دَقيقهۃ .\n"
                "لَحضهۃ .\n"
                "ﺂمـوتہ .\n"
                "غَصيتہ .\n"
                "يـما .\n"
                "قَنـﺂتـჂ̤ .\n"
                "بـۅتـჂ̤ .\n"
                "مݪصَقاتہ .\n"
                "مُسـﺂبقهۃ .\n"
                "ﺂسمـჂ̤ .\n"
                "نتعَࢪفـہ ؟.\n"
                "ࢪاحتـჂ̤ .\n"
                "ﺂنـჂ̤ .\n"
                "رﺂنتـჂ̤ .\n"
                "؏ـشقيہ .\n"
                "وݪيدჂ̤ .\n"
                "بنَيتيہ .\n"
                "طِفݪتيہ .\n"
                "تَـعي .\n"
                "وَݪـيہ .\n"
                "موتبيڪہ .\n"
                "موتبيجہ .\n"
                "موتعَليڪہ .\n"
                "نصعَد ؟.\n"
                "صۅتَڪ .\n"
                "كصۅتِجہ .\n"
                "ﺂبـوسـہ.\n"
                "نَعَست .\n"
                "ﺂجيت.\n"
                " نجَبـჂ̤ .\n"
                "ڪݪزَقہ .\n"
                "نَـعـال .\n"
                "زَࢪبـۿهۃ .\n"
                "زاحفَۿهۃ .\n"
                "حَڪـہ .\n"
                "ﮪـہلاﯠﯠ\n"
                "ههيہلآﯛﯛ\n"
                "أههہـﯠﯠ\n"
                "شنـيہ\n"
                "هآيـہ\n"
                "يـ؏\n"
                "أﯠﯠ؏\n"
✪┉ ┉ ┉ ┉⧼ [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])      
@Client.on_message(filters.command("اختصارات3$", prefixes=f".") & filters.me)
async def shark24(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "• ھھݪـﯠ\n"
                "• شلـﯛنڪہ\n"
                "• شلـﯛنجهہ\n"
                "• ٲلحـﻣډ للّْهہ\n"
                "• يـٱ ࢪّبـــہ\n"
                "• تـﻣـاﻣـہۧ\n"
                "• زيـنۿۂ\n"
                "• شَـنـﯛ؟\n"
                "• ݪيٓش‏ـہ\n"
                "• ؏ــزهہ\n"
                "• خـࢪّبـہ\n"
                "• يڵهہ ؏ـاديـہ،\n"
                "• شڪډ ؏ـيبـہ\n"
                "• مُـحـࢪّ۾\n"
                "• نـُلـطمـہ\n"
                "• زيـاࢪّهہ\n"
                "• حـࢪّٲ۾\n"
                "• ارگـصـہۧ\n"
                "• ٲسبـحہَۧ\n"
                "• ٲرڪضـہۧ\n"
                "• زاحـفـہۧ\n"
                "• زاحـفـهہۧ\n"
                "• مُـتاحـہ،\n"
                "• مُـتاحۿۂ،\n"
                "• فـاۿيـهہ،\n"
                "• متتـــہ\n"
                "• ؏ـــشقجٰہ\n"
                "• ڪيـيوتـہ\n"
                "• ڪـافــيہۛ\n"
                "• بـ؏ـد \n"
                "• ليـشہ\n"
                "• ۿﮧـﺎ \n"
                "• ـآحنهٰــہ\n"
                "• ؏ـليك\n"
                "• حــب\n"
                "• حــبيہ\n"
                "• ؏ـنيہ\n"
                "• ﮪۛـوِٰاي\n"
                "• ؏ـليۿ\n"
                "• ؏ــيني"
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])              
@Client.on_message(filters.command("اختصارات4$", prefixes=f".") & filters.me)
async def shark25(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "؏ـليڪ\n"
                "أඋـبڪ\n"
                "أنيہ\n"
                "شبيڪ\n"
                "يڪول\n"
                "لآ\n"
                "بسہ \n"
                "ليشہ\n"
                "أڪرۿڪ\n"
                "أڪول\n"
                "أڪلڪ\n"
                "أڪلج\n"
                "شلونڪ\n"
                "ﺎﻟلهۂَ \n"
                "ﺣــِلاﯛتيہ\n"
                "ٵڪوݪك\n"
                "شــ؏ـليه \n"
                "ٵڪﯙلـﭻ \n"
                "اﻧـييہ \n"
                "פـلوٰ \n"
                "ٵࢪيد \n"
                "ٵࢪوحـہ \n"
                "ا؏ـࢪفہ \n"
                "ٵدࢪيہ \n"
                "آ؏ـشقـجہ \n"
                "ﭑ؏ـشقڪہ \n"
                "تفضـࢦيہ\n"
                "تفضـࢦ\n"
                "פـباببهـہ\n"
                "פـباب\n"
                "פـاسـﯢب\n"
                "آميٰـטּ\n"
                "ﺑـسـہ \n"
                "ضَݪـ؏ـييہ\n"
                "ضَݪـ؏ـتيـہ\n"
                "؏َـندʊ̤\n"
                "ﺂجتمـا؏\n"
                "ٵჂ̤"
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])                      
@Client.on_message(filters.command("اختصارات2$", prefixes=f".") & filters.me)
async def shark26(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "ע\n"
                "ليـشـہٰ \n"
                "مِہטּ\n"
                "مِمـححِـہٰ\n"
                "ههههہ\n"
                "واللــہٰ\n"
                "؏َيـﯠﯢنڪك .\n"
                "رﯠﯢحڪكَ .\n"
                "حتـرﯠﯢحَ .\n"
                "؏َـمرڪك .\n"
                "اﯠﯢفَ . \n"
                "جـمـ؏ـﮫـہ\n"
                "مـبارڪـهـہ\n"
                "ـاٌلحمډ للۿ 💗.\n"
                "مــنــﹻـو \n"
                "آتـرخـصــہ\n"
                "اتمۂــنى\n"
                "ﺎتـﯡب .\n"
                "ﭑحنۿ \n"
                "ﺂﺣﺣَـم .\n"
                "د؏ۛـم .\n"
                "دقـِـِۧيۧقـِـِهہ.\n"
                "ډلينييہَ .\n"
                "ﻏﻏِـادرييہَ .\n"
                "حبچـჂَ̤\n"
                "ٲפـبج \n"
                "حــچي\n"
                "حـاڕِهۃ\n"
                "بـاردۿ`"

✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])                      
@Client.on_message(filters.command("اختصارات5$", prefixes=f".") & filters.me)
async def shark27(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "- مٰنۅِ 💕.\n"
                "- شٰخصَ 💕.\n"
                "- مٖتستاۿَݪ 💕.\n"
                "- ﺂݪتحِبۿم 💕.\n"
                "- يديمَݪج 💕.\n"
                "- ﻼَטּَ 💕.\n"
                "- ﺂݪحِبٰ 💕.\n"
                "- شٰݛطَ 💕.\n"
                "- ۈيَاجٖ 💕.\n"
                "- ڪِﯡليٰ 💕.\n"
                "- ؏ـلمِودِ 💕.\n"
                "- ﺂݪطِايٰݛ 💕.\n"
                "- صفٰحۿَہٰ 💕.\n"
                "- ﺂڪِݪتٰ 💕 .\n"
                "- نٰفسَكٰ 💕.\n"
                "- تِݛۿَ 💕.\n"
                "- طٰبيعَيٰ💕.\n"
                "- ڪِݪشيٰ 💕.\n"
                "- صٰديقِتيٰ 💕.\n"
                "- تَفيدكٰ 💕.\n"
                "- ڪٰمݪتِ 💕.\n"
                "- ﺂڪِݪ 💕.\n"
                "- ﺂݛيَدۿَ 💕.\n"
                "- مٖݛيضِۿَہٰ 💕.\n"
                "- ڪِݪتِ 💕.\n"
                "- خَتوݪيٰ 💕.\n"
                "- ݪزِڪٰۿَہٰ 💕.\n"
                "- ڪِافيٰ 💕.\n"
                "- صٰدﺂ؏َ 💕.\n"
                "- ﭑبوٰيۿَ 💕.\n"
                "- مِامَا 💕.\n"
                "- مٖخصِكٰ 💕.\n"
                "- ﺂݪكِ 💕.\n"
                "- ﺎرﯠﯢح ففدوۿَ ﺂݪعمَݛك 💕 .\n"
                "- ﺂتفضِݪ 💕.\n"
                "- ﺂچذبٰ 💕.\n"
                "- ﺂجِيتكٰ 💕.\n"
                "- غيَݛ 💕.\n"
                "- ڪٰيوِتَ 💕.\n"
                "- ﺂنِيٰ 💕.\n"
                "- ﺂحِبۿا 💕.\n"
                "- ﺂشِوفكٰ 💕.\n"
                "- ﺂسݪوِبكٰ 💕.\n"
                "- شٰوڪٰتِ 💕.\n"
                "- ݪوڪٰيہٰ 💕.\n"
                "- ﺂݪظَۿَݛ 💕.\n"
                "- شٰتحِسٰ 💕.\n"
                "- ﺂطِݪقِ💕 . \n"
                "- ﺂڪِوݪك 💕 .\n"
                "- ﺂحِبۿمٖ 💕.\n"
                "- ﺂݪۿِم 💕.\n"
                "- ﺂنشِاݪلۿَ 💕.\n"
                "- ﺂݪمۅفقيۿٰ 💕 . \n"
                "- بٰـﭑჂ̤ 💕 .\n"
                "- بِسرعۿِ 💕.\n"
                "- ﺂڪِوݪج  💕.\n"
                "- ﺂݪفِاضكٰ 💕.\n"
                "- ﺂ؏َـݛفِ 💕.\n"
                "- ح٘قيٰݛ 💕.\n"
                "- ﺂڪَثݛ 💕.\n"
                "- ڪِيبوٰݛد 💕.\n"
                "- بوسَنـჂ̤ 💕 .\n"
                "- تسَݪمينٰ 💕.\n"
                "- פـِبيبَتيٰ 💕.\n"
                "-  ؏ـنِديٰ 💕.\n"
                "- حِݪۅ 💕.\n"
                "- مٖتݪزِكٰ 💕."
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
@Client.on_message(filters.command("بايو1$", prefixes=f".") & filters.me)
async def shark28(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
☁️ : 🕊\n" "☁️ :   ✨\n" "☁️ :   🤍\n\n" "بريئۃ ۿي، بصورۿ لطيفۃ ڪالاطفال🎀
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])                                                    
@Client.on_message(filters.command("بايو2$", prefixes=f".") & filters.me)
async def shark29(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
☘️ 💕\n" "☘️ 💕\n" "☘️ 💕\n" "☘️ دمت لي شيئاً جميلاً لا ينتهي💕
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
@Client.on_message(filters.command("بايو3$", prefixes=f".") & filters.me)
async def shark30(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "𓋜┊𓆩 ➝  ˛⁽🇪🇬₎⇣ 𓆪\n"
                "𓋜┊𓆩  𓆪\n"
                "𓋜┊𓆩  𓆪\n"
                "𓋜┊𓆩  𓆪\n"
                "𓋜┊𓆩 ﭑميرۿ ـلآ يُليق بها ﭑلانحنا🍂 𓆪\n"
                "⁞ ωєℓ¢σмє тo му ρяσƒιℓє ⁞"
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])                              
@Client.on_message(filters.command("بايو4$", prefixes=f".") & filters.me)
async def shark31(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
                "🜟 ↬ ᑎᗩᗰE ، • •😌❤️\n"
                "🜟 ↬ ᖴᖇOᗰ ، EGYPT 🇪🇬\n"
                "🜟 ↬ ᗩGE ، y.o ♥️.\n\n"
                "🧿🍃  .....  🧿🍃."
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])                              
@Client.on_message(filters.command("بايو5$", prefixes=f".") & filters.me)
async def shark32(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
𓂅| •\n" "𓂅| •\n" "𓂅| •🖤☁️ .\n" "• 𝙸 𝙻𝙸𝙺𝙴 𝙼𝙾𝚄𝙽𝚃𝙰𝙸𝙼𝚂 𝙽𝙾𝚃 𝙵𝙰𝙻𝙻 .
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])    

@Client.on_message(filters.command("بايوهات1$", prefixes=f".") & filters.me)
async def shark33(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
— — — — — — — — —
`𓆦 : أيـۿ  ◡‌ 💙🧿.
𓆦 : ذأت الـ ١٤ ؏ـام ◡‌ 💙🧿.
𓆦 : انت دائماً بقلبي وأنا دائـماً #أحبك ◡‌ 💙🧿 .`
— — — — — — — — —
`𓆦 : مَريـم  ◡‌ 🤎🦦.
𓆦 : ذأت الـ ١٩ ؏ـام ◡‌ 🤎🦦.
𓆦 : أنت فرحة عُـمري أنت #أصدق شعور ◡‌ 🤎🦦 .`
— — — — — — — — —
`𓆦 : بَنيـن  ◡‌ 💛🍋.
𓆦 : ذأت الـ ١٦ ؏ـام ◡‌ 💛🍋.
𓆦 : ‏تسـرني إذا مريت في #بالي ◡‌ 💛🍋 .`
— — — — — — — — —
`𓆦 : ۿبـة  ◡‌ 🤍🕊.
𓆦 : ذأت الـ ٢١ ؏ـام ◡‌ 🤍🕊.
𓆦 : ‏لتكُن أصـابعي #بأمان يديك دائماً ◡‌ 🤍🕊 .`
— — — — — — — — —
`𓆦 : ﺄيـة  ◡‌ 🎈.
𓆦 : ذأت الـ ١٩ ؏ـام ◡‌ 🎈.
𓆦 : ‏ماياخذوُنك منَي مهما #زعلنا وأخذنا البُعد ‏ ◡‌ 🎈.`
— — — — — — — — —
`𓆦 : شۿـد  ◡‌ 🎈.
𓆦 : ذأت الـ ١٤ ؏ـام ◡‌ 🎈.
𓆦 : ‏ ‏اتمنى أن تمتلك عذراً كافٍ لكل ما تفعله معي حتى الآن . ◡‌ 🎈.`
— — — — — — — — —
`𓆦 : زۿـࢪأء  ◡‌ 🎈.
𓆦 : ذأت الـ ١٥ ؏ـام ◡‌ 🎈.
𓆦 : ‏ #حَسباليّ تحِن تاليتك بسابعّ حضن . ◡‌ 🎈.`
— — — — — — — — —
`𓆦 : مـينآ  ◡‌ 🎈.
𓆦 : ذأت الـ ١٩ ؏ـام ◡‌ 🎈.
𓆦 : ‏ كافي تكابر #عيونك حچن حزنك . ◡‌ 🎈.`
— — — — — — — — —
`𓆦 : ࢪوأن  ◡‌ 🎈.
𓆦 : ذأت الـ ١٦ ؏ـام ◡‌ 🎈.
𓆦 : ‏إذا اعتنيت #بالاشياء ، فهي تدوم .  ◡‌ 🎈.`
— — — — — — — — —
`𓆦 : رزﺄن  ◡‌ 🍇.
𓆦 : ذأت الـ ١٤ ؏ـام ◡‌ 🍇.
𓆦 : الوطن ليس مكان بل #انت  ◡‌ 🍇.`
— — — — — — — — —
`𓆦 : سَـارۿ  ◡‌ 🍇.
𓆦 : ذأت الـ ٢٠ ؏ـام ◡‌ 🍇.
𓆦 : اعَرف اجرح بلكِلام بسہِ الرفقَ #بالحيوان واجَب  ◡‌ 🍇.``
— — — — — — — — —
`𓆦 : سَـجى  ◡‌ 🍇.
𓆦 : ذأت الـ ١٦ ؏ـام ◡‌ 🍇.
𓆦 : اگدر اهين #كرامتك بَس أني ماگدر اهين شي مموجود اصلاً  ◡‌ 🍇.`
— — — — — — — — —
`𓆦 : فَـرح  ◡‌ 🍇.
𓆦 : ذأت الـ ١٩ ؏ـام ◡‌ 🍇.
𓆦 : ذيل الجلب عمره مَ #ينـ؏ـدل  ◡‌ 🍇.`
— — — — — — — — —
`𓆦 : رؤأن  ◡‌ 🍇.
𓆦 : ذأت الـ ١٨ ؏ـام ◡‌ 🍇.
𓆦 : تُبچيني اغنية عن ايَ #قساوة تحچون؟  ◡‌ 🍇.`
— — — — — — — — —
`𓆦 : زۿـݛأء  ◡‌ 💞💌.
𓆦 : ذأت الـ ١٧ ؏ـام ◡‌ 💞💌.
𓆦 : وإنك كـل مَا أحب فِي هذه #الحياة ◡‌ 💞💌.`
— — — — — — — — —
`𓆦 : مَـ؏ـشۈقته ◡‌ 🦌💞.
𓆦 : ذآت ﺄلـ  ١٦ ؏َـام ◡‌ 🦌💞.
𓆦 : - أسافِر والأغانـي لـوجهَك #تردنـي ◡‌ 🦌💞.`

— — — — — — — — —
`𓆦 : بنَيتـۿ ◡‌ 🍋🌿.
𓆦 : ذآت ﺄلـ  ٢٠ ؏ـام ◡‌ 🍋🌿.
𓆦 : - إتباهـاا بيِّڪ هوايـَْه يَسمر #يحـلو ◡‌ 🍋🌿.`

— — — — — — — — —
`𓆦 : مݛيتـۿ ◡‌ 🤍💧.
𓆦 : ذآت ﺄلـ ١٨ ؏ـام ◡‌ 🤍💧.
𓆦 : - عينـاكَ بحر ومـا ڪان الغريـق الاَّ #أنـا ◡‌ 🤍💧.`
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
@Client.on_message(filters.command("بايومات2$", prefixes=f".") & filters.me)
async def shark34(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
⠀ ⠀ ⠀⠀⠀`. ғʀᴏᴍ #egypt ↻.  
         𓆩 نحن ڪـ الفرص لا نأتي مرتين 𓆪
⠀ ⠀⠀ - ᴡᴇʟᴄᴏᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ ❔ `

— — — — — — — — —⠀ ⠀
 ⠀⠀      ⠀⠀    ⠀ `- 𝟪.𝟣𝟨 𝑚𝑎𝑟𝑐ℎ 🕊: 
 ⠀⠀⠀⠀     - 𝑓𝑟𝑜𝑚 . . cairo egypt 📌.
       -رقيقـٰۿۃ‏ ڪہ ٱجنحۿۃ‏ ٱلفراشۿۃ‏🦋 `⠀⠀⠀⠀

— — — — — — — — —⠀⠀             ⠀⠀⠀ ⠀⠀⠀ 
⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀ ` ❲ 21 𝒚.𝒐 ❳
     ⠀⠀         ⠀⠀• َ𝒊𝒏 • egypt ❄️  .
-ء ୪ أُعَوَّض ୪ ꪆ أُسَتبدَل ୪ ꪆ أُقارَن✋🏼. 📨!. `    
⠀⠀  ⠀⠀⠀   

— — — — — — — — —⠀⠀ ⠀ ⠀
 ⠀⠀        ⠀       `- :17y.o. 
                    - : 𝑖𝑛 egypt 🇪🇬. 
 ⠀⠀       كَـ حبة المَـطر، رقـيقة ☁️ . 
• 𝙻𝙸𝙺𝙴 𝙰 𝚁𝙰𝙸𝙽𝙳𝚁𝙾𝙿, 𝚃𝙷𝙸𝙽 . ❤️.`
  ⠀⠀         

— — — — — — — — —
 ⠀⠀ ⠀` - 𝒊𝒏 #Basra
 ⠀⠀     - ℒ𝒐𝒗𝒆 𝒎𝒚 𝒔𝒆𝒍𝒇
 ⠀⠀ ⠀ -  • أنيــــہ الإستثنائيـۃ  ، المختلفـۃ 🖤❕`

— — — — — — — — —⠀ ⠀ ⠀
 ⠀⠀      ⠀⠀    ⠀ `- 𝟒: 𝟏𝟏🏷: 
 ⠀⠀⠀⠀     -  cairo: 𝐚𝐫𝐩𝐢𝐥🍂.
     - ﭑنـا بزوديَ ارتفع محد يعليني .` ⠀⠀⠀⠀

— — — — — — — — —⠀⠀             ⠀⠀⠀ ⠀⠀⠀ 
⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀ ` ❲ 01:23 ❳
     ⠀⠀         ⠀⠀- 𝐼𝑛 : 𝐷ℎ𝑖 𝑄𝑎𝑟 .
-يڪرهونَـيَ، وَيقلدون ﭑلمشـي الآمشيُـهہۛ 📨!. `    
⠀⠀  ⠀⠀⠀   

— — — — — — — — —
`‎  ‌‎  ‎  ‎  ‎  ‎  ‎  ‎  ‎  ‎  ‎ ‎ 𐄐 𝓑𝗮𝗴𝗵𝗱𝗮𝗱 🇪🇬 ⸃.
 ‎  .❕ ۿادئۃ مُتصالحۃة مع ڪل شيئَ : 
 ‎  ‎  ‎  ‌‎ ‎  ‎  ‎  ‎  ‎  ‎ ‎  ‎  ‎  𐄐 ‎ 𝟭𝟴  𝗬.𝗢 ⌝.`

— — — — — — — — —⠀ 
                ⠀⠀⠀⠀⠀    `˹ ↯  .
            ❥ ғʀᴏᴍ ɪʀᴀǫ 🇪🇬✿
    - هادئۿۃ‏، #قويۿۃ‏، جميلۿۃ‏، وحيدۿۃ‏🐆.`
          

— — — — — — — — —⠀⠀                
⠀ ⠀ ⠀⠀`⠀. ғʀᴏᴍ #egypt ↻.  
         𓆩 قـآتل مُـن ٱجل حلـمڪٰ دائما 𓆪
⠀ ⠀⠀ - ᴡᴇʟᴄᴏᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ ❔`

— — — — — — — — —
⠀ ⠀ ⠀⠀`⠀. ғʀᴏᴍ #egypt ↻.  
         𓆩 نحن ڪـ الفرص لا نأتي مرتين 𓆪
⠀ ⠀⠀ - ᴡᴇʟᴄᴏᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ ❔`
⠀

— — — — — — — — —

⠀` ‌⠀ ‌⠀ ‌ ⠀⠀ ⠀⠀ ‌   .𓆸 #𝘋𝘪𝘺𝘢𝘭𝘢 𑁍.
‌ ⠀ ‌ ⠀ ‌ ⠀ ‌ ⠀ - 𝘐 𝘯𝘦𝘦𝘥 𝘢 𝘯𝘦𝘷𝘦𝘳 𝘦𝘯𝘥𝘪𝘯𝘨 𝘩𝘶𝘨 .
‌ ⠀ ‌ ⠀ ‌ ⠀ ‌‌ ‌ ⠀ ⠀‌       .⧼ 𝟤𝟶𝟶𝟥 ☆. ⧽.`

✪┉ ┉ ┉ ┉⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 VENOM](https://t.me/RB_RO) ⧽┉ ┉ ┉ ┉✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])   






