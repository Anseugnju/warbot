#내전싸개
import discord
from discord.ext import commands
import time
import os, random
import asyncio
봇토큰=os.environ.get('token')
채널ID=int(os.environ.get('chid'))
명령어="!"
bot = commands.Bot(command_prefix=명령어)
시작종류=0 #랜덤시작=0 순서시작=1

인원1=[] #참가한 사람들 목록
순서목록=[] #순서시작에서 순서목록
순서진행=[] #순서시작시 얼마나 쳤는지 확인
팀1={
    '탑':"",
    '정글':"",
    '미드':"",
    '원딜':"",
    '서폿':""}#파랑이
팀2={
    '탑':"",
    '정글':"",
    '미드':"",
    '원딜':"",
    '서폿':""}#빨강이


version = "2.1"

@bot.event
async def on_ready(): 
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    global message
    ch = bot.get_channel(채널ID)
    await ch.purge(limit=100)
    embed=도움()
    helpme = await ch.send(embed=embed)
    embed = embed_play()
    message = await ch.send(embed = embed)
    await 새로고침(message,helpme)

@bot.event
async def on_message(message, pass_context=True):
    if message.author.bot == False:
        print(f"{message.author.name} : {message.content}")
    time.sleep(3)
    if message.channel.id == 채널ID:
        if not message.content.startswith(명령어):
            if message.author.bot == 1:
                return
            await message.delete()
            return
        if message.content==명령어:
            await message.delete()
            return
        await bot.process_commands(message)


def 도움(): #도움말 내용
    embed = discord.Embed(
        title="도움말",
        colour=0x0097ff)

    embed.add_field(name=f"{명령어}참가",value="내전에 들어가짐",inline=False)
    embed.add_field(name=f"{명령어}제거",value="내전에서 나가짐",inline=False)
    embed.add_field(name=f"{명령어}랜덤시작",value="랜덤하게 팀이 정해짐",inline=False)
    embed.add_field(name=f"{명령어}순서시작",value=f"{명령어}블루 (라인) {명령어}레드 (라인)",inline=False)
    return embed

def embed_play(): #노래 임베드 내용
    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    인원=" ".join(인원1)
    if len(인원1)==0:
        인원=" "
    if 시작종류==0:
        embed = discord.Embed(title="팀", description=f"명단 \n{인원}", color=0xAAFFFF)
    if 시작종류==1:
        embed = discord.Embed(title="팀", description=f"명단 \n{인원}", color=0xAAFFFF)
        embed.add_field(name="순서", value=" ".join(순서목록), inline=False)
    embed.add_field(name="블루팀", value=블루팀)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    return embed


async def 새로고침(message,helpme): #노래 상태 1초마다 변경
    while not bot.is_closed():
        try:
            embed=embed_play()
            await message.edit(embed=embed)
            embed=도움()
            await helpme.edit(embed=embed)
            await asyncio.sleep(1)
        except:
            os.exit()


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

@bot.command()
async def 버전(ctx):
    await ctx.send(version)

@bot.command(aliases=["1"])
async def 블루(ctx,라인):
    if 라인 == "탑":
        팀1.update(탑=순서목록[len(순서진행)])
        순서진행.append(0)
    elif 라인 == "정글":
        팀1.update(정글=순서목록[len(순서진행)])
        순서진행.append(1)
    elif 라인 == "미드":
        팀1.update(미드=순서목록[len(순서진행)])
        순서진행.append(2)
    elif 라인 == "원딜":
        팀1.update(원딜=순서목록[len(순서진행)])
        순서진행.append(3)
    elif 라인 == "서폿":
        팀1.update(서폿=순서목록[len(순서진행)])
        순서진행.append(4)
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return
    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.message.delete()

    

@bot.command(aliases=["2"])
async def 레드(ctx,라인):
    if 라인 == "탑":
        팀2.update(탑=순서목록[len(순서진행)])
        순서진행.append(5)
    elif 라인 == "정글":
        팀2.update(정글=순서목록[len(순서진행)])
        순서진행.append(6)
    elif 라인 == "미드":
        팀2.update(미드=순서목록[len(순서진행)])
        순서진행.append(7)
    elif 라인 == "원딜":
        팀2.update(원딜=순서목록[len(순서진행)])
        순서진행.append(8)
    elif 라인 == "서폿":
        팀2.update(서폿=순서목록[len(순서진행)])
        순서진행.append(9)
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return

    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.message.delete()



@bot.command()
async def 라인제거(ctx):
    순서진행.pop()
    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    await ctx.message.delete()



@bot.command(aliases=["참여","추가"])
async def 참가(ctx,*args):
    인원1.extend(args)
    await ctx.message.delete()

@bot.command(aliases=["삭제","제외"])
async def 제거(ctx,*args):
    if len(인원1)==0:
        await ctx.message.delete()
        return
    dellist=[]
    dellist.extend(args)
    i = 0
    while i < len(dellist):
        if dellist[i] in 인원1:
            인원1.remove(dellist[i])
            i +=1
        else:
            i +=1

    await ctx.message.delete()



@bot.command()
async def 명단초기화(ctx):
    인원1.clear()
    await ctx.message.delete()


@bot.command()
async def 랜덤시작(ctx):
    if len(인원1)==0:
        await ctx.message.delete()
        return
    global 시작종류
    시작종류=0
    인원수=len(인원1)
    num=random.randrange(0,인원수)
    팀1.update(탑='',정글='',미드='',원딜='',서폿='')
    팀2.update(탑='',정글='',미드='',원딜='',서폿='')
    랜덤라인=[]
    for i in range(인원수):
        while num in 랜덤라인:
            num = random.randrange(0,인원수)
        랜덤라인.append(num)
    try:
        팀1.update(탑=인원1[랜덤라인[0]])
        팀2.update(탑=인원1[랜덤라인[1]])
        팀1.update(정글=인원1[랜덤라인[2]])
        팀2.update(정글=인원1[랜덤라인[3]])
        팀1.update(미드=인원1[랜덤라인[4]])
        팀2.update(미드=인원1[랜덤라인[5]])
        팀1.update(원딜=인원1[랜덤라인[6]])
        팀2.update(원딜=인원1[랜덤라인[7]])
        팀1.update(서폿=인원1[랜덤라인[8]])
        팀2.update(서폿=인원1[랜덤라인[9]])
    except:
        pass

    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    embed = discord.Embed(title="팀", description="", color=0xAAFFFF)
    embed.add_field(name="블루팀", value=(블루팀), inline=True)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    
    await ctx.message.delete()
    
@bot.command()
async def 순서시작(ctx):
    if len(인원1)==0:
        await ctx.message.delete()
        return
    global 시작종류
    시작종류=1
    팀1.update(탑='',정글='',미드='',원딜='',서폿='')
    팀2.update(탑='',정글='',미드='',원딜='',서폿='')
    순서목록.clear()
    순서진행.clear()
    num=random.randrange(0,(len(인원1)))
    순서=[]
    for i in range((len(인원1))):
        while num in 순서:
            num = random.randrange(0,(len(인원1)))
        순서.append(num)
    i=0
    while i<len(순서):
        순서목록.append(인원1[순서[i]])
        i+=1
    await ctx.message.delete()


bot.run(봇토큰)
