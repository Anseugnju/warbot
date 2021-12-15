#내전싸개
import base64

from asyncio.tasks import sleep
from tokenize import ContStr
import discord
from discord.ext import commands
from pathlib import Path
import time
import os, random
from os.path import getsize
from discord.utils import get
import re
import asyncio
import sys
mod = sys.modules[__name__]

intents = discord.Intents.default()
intents.members = True 

import random
from discord import channel
from discord import member
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()#Creates Client
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        msg = await ctx.send("헛소리 ㄴ")
    if isinstance(error, commands.MissingRequiredArgument):
        msg = await ctx.send('이게 무슨 오류일까')
    if isinstance(error, commands.MissingPermissions):
        msg = await ctx.send("권한이 없습니다")
    await ctx.message.delete()
    time.sleep(5)
    await msg.delete()

intents = discord.Intents.default()
intents.members = True
인원=[]
인원2=[]
인원3=[]
linelist=[]
dellinelist=[]
redlinelist=[]
bluelinelist=[]
dlsrn=[]
dlsdnjs = []
팀라인=[]
xnvy=[]
벤리스트=[]

version = "1.9.1"

@bot.command()
async def 버전(ctx):
    await ctx.send(version)

@bot.command()
async def 벤(ctx,id):
    if ctx.author.roles[1].id==851810384850845736 or ctx.author.roles[1].id==452750932363706399:
        벤리스트.append(id)
        await ctx.send("벤됨")
    
@bot.command()
async def 벤취소(ctx,id):
    if ctx.author.roles[1].id==851810384850845736 or ctx.author.roles[1].id==452750932363706399:
        벤리스트.remove(id)
        await ctx.send("벤취소")
        


@bot.command()
async def 투표(ctx, 시간, *args):
    xnvy.clear()
    xnvy.extend(args)
    msg = ' '.join(xnvy)
    msg2 = msg.split(",")
    emoji=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    await ctx.send(msg2)
    

    if 1 == len(msg2):
        embed1 = discord.Embed(title=msg2[0], description="", color=0xAAFFFF)
        embed1.add_field(name="찬성", value="투표 대기중", inline=False)
        embed1.add_field(name="반대", value="투표 대기중", inline=False)
        imotion = await ctx.send(embed=embed1)
        await imotion.add_reaction("👍")
        await imotion.add_reaction("👎")
        await sleep(int(시간))
        positive = 0
        negative = 0
        message = await ctx.channel.fetch_message(imotion.id)
        for reaction in message.reactions:
            if reaction.emoji == '👍':
                positive = reaction.count - 1 # compensate for the bot adding the first reaction
            if reaction.emoji == '👎':
                negative = reaction.count - 1

        embed2 = discord.Embed(title=msg2[0], description="", color=0xAAFFFF)
        embed2.add_field(name="찬성", value=f"{positive}명이 찬성하였습니다", inline=False)
        embed2.add_field(name="반대", value=f"{negative}명이 반대하였습니다", inline=False)
        await imotion.edit(embed=embed2)
    elif 1 < len(msg2):
        
        i=0
        embed1 = discord.Embed(title=msg2[0], description="", color=0xAAFFFF)
        while i+1<len(msg2):
            embed1.add_field(name=msg2[i+1], value="투표 대기중", inline=False)
            i+=1
        imotion = await ctx.send(embed=embed1)
        
        i2 = 0
        while i > i2:
            await imotion.add_reaction(emoji[i2])
            i2+=1
        await sleep(int(시간))
        message = await ctx.channel.fetch_message(imotion.id)
        i3=0
        Var_0 = 0
        Var_1 = 0
        Var_2 = 0
        Var_3 = 0
        Var_4 = 0
        Var_5 = 0
        Var_6 = 0
        Var_7 = 0
        Var_8 = 0
        Var_9 = 0
        var=[Var_0,Var_1,Var_2,Var_3,Var_4,Var_5,Var_6,Var_7,Var_8,Var_9]
        while i>i3:
            for reaction in message.reactions:
                if reaction.emoji == emoji[i3]:
                    var[i3] = reaction.count - 1 # compensate for the bot adding the first reaction
                    i3+=1
        i4=0
        embed2 = discord.Embed(title=msg2[0], description="", color=0xAAFFFF)
        while i4+1<len(msg2):
            embed2.add_field(name=msg2[i4+1], value=f"{var[i4]}명이 찬성하였습니다", inline=False)
            i4+=1
        
        await imotion.edit(embed=embed2)

            

@bot.command()
async def 초기화(ctx,*args):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
    sys.exit()

@bot.command()
async def 라인(ctx,*args):
    aaa =[]
    aaa.clear()
    aaa.extend(args)
    i = 0
    while i < len(aaa):
        bbb = int(aaa[i])
        redlinelist.append(bbb)
        i+=1
    
    await ctx.send(redlinelist)


@bot.command(aliases=["1"])
async def 블루(ctx,라인):
    if 라인 == "탑":
        redlinelist.append(0)
        팀라인.append("1탑")
    elif 라인 == "정글":
        redlinelist.append(1)
        팀라인.append("1정글")
    elif 라인 == "미드":
        redlinelist.append(2)
        팀라인.append("1미드")
    elif 라인 == "원딜":
        redlinelist.append(3)
        팀라인.append("1원딜")
    elif 라인 == "서폿":
        redlinelist.append(4)
        팀라인.append("1서폿")
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return
    블루ㅌ =""
    블루ㅈㄱ =""
    블루ㅁㄷ=""
    블루ㅇㄷ=""
    블루ㅅㅍ=""
    레드ㅌ=""
    레드ㅈㄱ=""
    레드ㅁㄷ=""
    레드ㅇㄷ=""
    레드ㅅㅍ=""
    i=0
    블루탑 =""
    블루정글 =""
    블루미드=""
    블루원딜=""
    블루서폿=""
    레드탑=""
    레드정글=""
    레드미드=""
    레드원딜=""
    레드서폿=""

    while i <len(redlinelist):
        if redlinelist[i] == 0:
            블루탑 = 블루ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 1:
            블루정글 = 블루ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 2:
            블루미드 = 블루ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 3:
            블루원딜 = 블루ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 4:
            블루서폿 = 블루ㅅㅍ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 5:
            레드탑 = 레드ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 6:
            레드정글 = 레드ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 7:
            레드미드 = 레드ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 8:
            레드원딜= 레드ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 9:
            레드서폿=레드ㅅㅍ+str(인원2[i])
            i+=1
        else :
            i+=1
    await ctx.send(인원2)
    블루팀 =f"{블루탑:ㅤ<5} \n {블루정글} \n {블루미드} \n {블루원딜} \n {블루서폿}"
    레드팀 =f"ㅤㅤ{레드탑} \n ㅤㅤ{레드정글} \n ㅤㅤ{레드미드} \n ㅤㅤ{레드원딜} \n ㅤㅤ{레드서폿}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.send(embed=embed)

    

@bot.command(aliases=["2"])
async def 레드(ctx,라인):
    if 라인 == "탑":
        redlinelist.append(5)
        팀라인.append("2탑")
    elif 라인 == "정글":
        redlinelist.append(6)
        팀라인.append("2정글")
    elif 라인 == "미드":
        redlinelist.append(7)
        팀라인.append("2미드")
    elif 라인 == "원딜":
        redlinelist.append(8)
        팀라인.append("2원딜")
    elif 라인 == "서폿":
        redlinelist.append(9)
        팀라인.append("2서폿")
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return
    블루ㅌ =""
    블루ㅈㄱ =""
    블루ㅁㄷ=""
    블루ㅇㄷ=""
    블루ㅅㅍ=""
    레드ㅌ=""
    레드ㅈㄱ=""
    레드ㅁㄷ=""
    레드ㅇㄷ=""
    레드ㅅㅍ=""
    i=0
    블루탑 =""
    블루정글 =""
    블루미드=""
    블루원딜=""
    블루서폿=""
    레드탑=""
    레드정글=""
    레드미드=""
    레드원딜=""
    레드서폿=""

    while i <len(redlinelist):
        if redlinelist[i] == 0:
            블루탑 = 블루ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 1:
            블루정글 = 블루ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 2:
            블루미드 = 블루ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 3:
            블루원딜 = 블루ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 4:
            블루서폿 = 블루ㅅㅍ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 5:
            레드탑 = 레드ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 6:
            레드정글 = 레드ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 7:
            레드미드 = 레드ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 8:
            레드원딜= 레드ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 9:
            레드서폿=레드ㅅㅍ+str(인원2[i])
            i+=1
        else :
            i+=1
    await ctx.send(인원2)
    블루팀 =f"{블루탑:ㅤ<5} \n {블루정글} \n {블루미드} \n {블루원딜} \n {블루서폿}"
    레드팀 =f"ㅤㅤ{레드탑} \n ㅤㅤ{레드정글} \n ㅤㅤ{레드미드} \n ㅤㅤ{레드원딜} \n ㅤㅤ{레드서폿}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.send(embed=embed)



@bot.command()
async def 라인제거(ctx):
    redlinelist.pop()
    팀라인.pop()

    await ctx.send(팀라인)

@bot.command()
async def 라인확인(ctx):
    await ctx.send(팀라인)
    await ctx.send(redlinelist)

@bot.command()
async def 라인초기화(ctx):
    redlinelist.clear()
    팀라인.clear()


@bot.command()
async def 도움(ctx):
    await ctx.send("등록 이름")
    await ctx.send("참가 사람 목록")
    await ctx.send("제거 사람 목록")
    await ctx.send("랜덤시작")
    await ctx.send("!벤 id (우클릭후 id복사해서 붙여넣기) , !벤취소 id")


@bot.command(aliases=["참여","추가"])
async def 참가(ctx,*args):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
        
        
    인원.extend(args)
    await ctx.send(len(인원))
    await ctx.send(인원)

@bot.command(aliases=["삭제","제외"])
async def 제거(ctx,*args):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
    dellinelist.clear()
    dellinelist.extend(args)
    i = 0
    while i < len(dellinelist):
        if dellinelist[i] in 인원:
            인원.remove(dellinelist[i])
            i +=1
        else:
            i +=1

    await ctx.send(len(인원))
    await ctx.send(인원)
    

@bot.command()
async def 분배(ctx):
    i = 0
    while i < 10:
        if i < 5:
            time.sleep(1)
            channel = bot.get_channel(457477454085226496)
            f = open(f"./dlsrn/{인원[linelist[i]]}.txt", 'r')
            data = f.read()
            b = await ctx.guild.fetch_member(data)
            await b.move_to(channel)
            i+=1
        else :
            time.sleep(1)
            channel = bot.get_channel(723593125695717452)
            f = open(f"./dlsrn/{인원[linelist[i]]}.txt", 'r')
            data = f.read()
            b = await ctx.guild.fetch_member(data)
            await b.move_to(channel)
            i+=1




        

@bot.command()
async def 명단(ctx):
    await ctx.send(len(인원))
    await ctx.send(인원)
    await ctx.send(인원2)


@bot.command()
async def 명단초기화(ctx):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
    인원.clear()
    await ctx.send(인원)



@bot.command()
async def 랜덤라인(ctx):
    i=0
    while i == 0:
        num=random.randrange(0,10)
        if num not in redlinelist:
            redlinelist.append(num)
            i+=1
        else:
            continue

        
    블루ㅌ =""
    블루ㅈㄱ =""
    블루ㅁㄷ=""
    블루ㅇㄷ=""
    블루ㅅㅍ=""
    레드ㅌ=""
    레드ㅈㄱ=""
    레드ㅁㄷ=""
    레드ㅇㄷ=""
    레드ㅅㅍ=""
    i=0
    블루탑 =""
    블루정글 =""
    블루미드=""
    블루원딜=""
    블루서폿=""
    레드탑=""
    레드정글=""
    레드미드=""
    레드원딜=""
    레드서폿=""

    while i <len(redlinelist):
        if redlinelist[i] == 0:
            블루탑 = 블루ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 1:
            블루정글 = 블루ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 2:
            블루미드 = 블루ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 3:
            블루원딜 = 블루ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 4:
            블루서폿 = 블루ㅅㅍ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 5:
            레드탑 = 레드ㅌ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 6:
            레드정글 = 레드ㅈㄱ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 7:
            레드미드 = 레드ㅁㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 8:
            레드원딜= 레드ㅇㄷ+str(인원2[i])
            i+=1
        elif redlinelist[i] == 9:
            레드서폿=레드ㅅㅍ+str(인원2[i])
            i+=1
        else :
            i+=1
    블루팀 =f"{블루탑:ㅤ<5} \n {블루정글} \n {블루미드} \n {블루원딜} \n {블루서폿}"
    레드팀 =f"ㅤㅤ{레드탑} \n ㅤㅤ{레드정글} \n ㅤㅤ{레드미드} \n ㅤㅤ{레드원딜} \n ㅤㅤ{레드서폿}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def 랜덤시작(ctx):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
    인원1 = list(filter(None, 인원))
    if len(인원1)>=10:
        numb=len(인원1)
    else:
        numb=10

    num=random.randrange(0,numb)
    linelist.clear()
    for i in range(numb):
        while num in linelist:
            num = random.randrange(0,numb)
        linelist.append(num)
    print(linelist)
    if len(인원1)<=10:
        i=len(인원1)
        while i<10:
            인원1.append("")
            print(len(인원1))
            i+=1

    블루팀 =f"{인원1[linelist[0]]:ㅤ<5} \n {인원1[linelist[1]]} \n {인원1[linelist[2]]} \n {인원1[linelist[3]]} \n {인원1[linelist[4]]}"
    레드팀 =f"ㅤㅤ{인원1[linelist[5]]} \n ㅤㅤ{인원1[linelist[6]]} \n ㅤㅤ{인원1[linelist[7]]} \n ㅤㅤ{인원1[linelist[8]]} \n ㅤㅤ{인원1[linelist[9]]}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def 순서시작(ctx):
    if str(ctx.author.id) in 벤리스트:
        await ctx.send("님 벤됨")
        return
    redlinelist.clear()
    팀라인.clear()
    num=random.randrange(0,(len(인원)))
    linelist.clear()
    for i in range((len(인원))):
        while num in linelist:
            num = random.randrange(0,(len(인원)))
        linelist.append(num)
    
    순서 =f"{인원[linelist[0]]} {인원[linelist[1]]} {인원[linelist[2]]} {인원[linelist[3]]} {인원[linelist[4]]} {인원[linelist[5]]} {인원[linelist[6]]} {인원[linelist[7]]} {인원[linelist[8]]} {인원[linelist[9]]}"
    await ctx.send(순서)
    인원2.clear()
    인원2.append(인원[linelist[0]])
    인원2.append(인원[linelist[1]])
    인원2.append(인원[linelist[2]])
    인원2.append(인원[linelist[3]])
    인원2.append(인원[linelist[4]])
    인원2.append(인원[linelist[5]])
    인원2.append(인원[linelist[6]])
    인원2.append(인원[linelist[7]])
    인원2.append(인원[linelist[8]])
    인원2.append(인원[linelist[9]])


bot.run(os.environ['token'])
