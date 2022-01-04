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

re_yes="👍"
re_no="👎"
re_list=[]
re_yes_list=[]
re_no_list=[]

version = "2.001" #버그 없겠찌

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
    await message.add_reaction(re_yes) #반응추가
    await message.add_reaction(re_no)
    await 새로고침(message,helpme)

@bot.event
async def on_message(message, pass_context=True):
    await asyncio.sleep(1)
    if message.channel.id == 채널ID:
        if message.author.bot == False:
            print(f"{message.author.name} : {message.content}")
        if message.author.id == 283812834855616512:
            ch = bot.get_channel(채널ID)
            await message.delete()
            안우진 = await ch.send("죽빵날아감")
            await asyncio.sleep(3)
            await 안우진.delete()
            return
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
    embed.add_field(name=f"{명령어}순서시작",value=f"{명령어}블루 (라인) {명령어}레드 (라인) {명령어}라인제거",inline=False)
    return embed

def embed_play(): #노래 임베드 내용
    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    인원=" ".join(인원1)
    if len(인원1)==0:
        인원=" "
    if 시작종류==0:
        embed = discord.Embed(title=f"팀    찬성:{len(re_yes_list)}명 반대:{len(re_no_list)}명", description=f"명단 \n{인원}", color=0xAAFFFF)
    if 시작종류==1:
        embed = discord.Embed(title=f"팀    찬성:{len(re_yes_list)}명 반대:{len(re_no_list)}명", description=f"명단 \n{인원}", color=0xAAFFFF)
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
            pass

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


@bot.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == re_yes:
        userid = user.name
        if userid in re_list:
            await reaction.remove(user)
            return
        re_list.append(userid)
        re_yes_list.append(userid)
        await reaction.remove(user)
        return
    if str(reaction.emoji) == re_no:
        userid = user.name
        if userid in re_list:
            await reaction.remove(user)
            return
        re_list.append(userid)
        re_no_list.append(userid)
        await reaction.remove(user)
        return
    if str(reaction.emoji) != re_no and str(reaction.emoji) != re_yes:
        await reaction.remove(user)
        return


@bot.command()
async def 확인(ctx,*args):
    print(re_list)
    print(re_yes_list)
    print(re_no_list)

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
    global 시작종류
    시작종류=0
    인원1.clear()
    순서진행.clear()
    순서목록.clear()
    re_yes_list.clear()
    re_no_list.clear()
    re_list.clear()
    팀1.update(탑="",정글="",미드="",원딜="",서폿="")
    팀2.update(탑="",정글="",미드="",원딜="",서폿="")
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
    팀1.update(탑="",정글="",미드="",원딜="",서폿="")
    팀2.update(탑="",정글="",미드="",원딜="",서폿="")
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
    re_yes_list.clear()
    re_no_list.clear()
    re_list.clear()
    await ctx.message.delete()
    
@bot.command()
async def 순서시작(ctx):
    if len(인원1)==0:
        await ctx.message.delete()
        return
    global 시작종류
    시작종류=1
    팀1.update(탑="",정글="",미드="",원딜="",서폿="")
    팀2.update(탑="",정글="",미드="",원딜="",서폿="")
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
    re_yes_list.clear()
    re_no_list.clear()
    re_list.clear()
    await ctx.message.delete()

@bot.command(aliases=["1"])
async def 블루(ctx,라인):
    if 시작종류==0:
        await ctx.message.delete()
        return
    if 라인 == "탑":
        if 팀1.get('탑') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀1.update(탑=순서목록[len(순서진행)])
        순서진행.append(0)
    elif 라인 == "정글":
        if 팀1.get('정글') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀1.update(정글=순서목록[len(순서진행)])
        순서진행.append(1)
    elif 라인 == "미드":
        if 팀1.get('미드') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀1.update(미드=순서목록[len(순서진행)])
        순서진행.append(2)
    elif 라인 == "원딜":
        if 팀1.get('원딜') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀1.update(원딜=순서목록[len(순서진행)])
        순서진행.append(3)
    elif 라인 == "서폿":
        if 팀1.get('서폿') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀1.update(서폿=순서목록[len(순서진행)])
        순서진행.append(4)
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return
    await ctx.message.delete()

    

@bot.command(aliases=["2"])
async def 레드(ctx,라인):
    if 시작종류==0:
        await ctx.message.delete()
        return
    if 라인 == "탑":
        if 팀2.get('탑') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀2.update(탑=순서목록[len(순서진행)])
        순서진행.append(5)
    elif 라인 == "정글":
        if 팀2.get('정글') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀2.update(정글=순서목록[len(순서진행)])
        순서진행.append(6)
    elif 라인 == "미드":
        if 팀2.get('미드') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀2.update(미드=순서목록[len(순서진행)])
        순서진행.append(7)
    elif 라인 == "원딜":
        if 팀2.get('원딜') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀2.update(원딜=순서목록[len(순서진행)])
        순서진행.append(8)
    elif 라인 == "서폿":
        if 팀2.get('서폿') != "":
            있음 = await ctx.send("이미 사람이 있음")
            await asyncio.sleep(5)
            await 있음.delete()
            await ctx.message.delete()
            return
        팀2.update(서폿=순서목록[len(순서진행)])
        순서진행.append(9)
    else:
        msg = await ctx.send("헛소리 ㄴ")
        await ctx.message.delete()
        time.sleep(5)
        await msg.delete()
        return
    await ctx.message.delete()



@bot.command()
async def 라인제거(ctx):
    if 시작종류==0:
        await ctx.message.delete()
        return
    if 순서진행[-1] == 0:
        팀1.update(탑="")
    elif 순서진행[-1] == 1:
        팀1.update(정글="")
    elif 순서진행[-1] == 2:
        팀1.update(미드="")
    elif 순서진행[-1] == 3:
        팀1.update(원딜="")
    elif 순서진행[-1] == 4:
        팀1.update(서폿="")
    elif 순서진행[-1] == 5:
        팀2.update(탑="")
    elif 순서진행[-1] == 6:
        팀2.update(정글="")
    elif 순서진행[-1] == 7:
        팀2.update(미드="")
    elif 순서진행[-1] == 8:
        팀2.update(원딜="")
    elif 순서진행[-1] == 9:
        팀2.update(서폿="")
    순서진행.pop()
    await ctx.message.delete()




bot.run(봇토큰)
