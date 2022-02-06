#내전싸개
import discord
from discord.ext import commands
import time
import os, random
import asyncio
봇토큰=os.environ.get('token')
채널ID=int(os.environ.get('chid'))
안라톤=int(os.environ.get('an'))
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

emoji="<:emoji_6:899211615025631252>" 
불="<:qnf:901485308502220800>"
꽃="<:Rhc:901485361128161280>"
가="<:rk:901485405734567996>"
능="<:smd:901485427263950900>"
종배="<:tjsrmffktm:926832012248113172>"
태호="<:11:892457457853554738>"
상붕이="<:rrr:913054165641592832>"
김우희1="🐮"
김우희2="🐶"
드디어1="<:e1:913051502824792104>"
드디어2="<:e2:913051554632830998>"
드디어3="<:e3:913051572940963840>"
드디어4="<:e4:913051586908012594>"
호준="🦾"
동현="🦥"

version = "2.002" #버그 없겠찌

@bot.event
async def on_ready(): 
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    global teamc
    global helpme
    ch = bot.get_channel(채널ID)
    await ch.purge(limit=100)
    embed=도움()
    helpme = await ch.send(embed=embed)
    embed = embed_play()
    teamc = await ch.send(embed = embed)
    await teamc.add_reaction(re_yes) #반응추가
    await teamc.add_reaction(re_no)
    await 새로고침(teamc,helpme)

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
    if message.channel.id == 안라톤:
        print(message.guild.id)
        if message.author.bot == 1:
            return
        if message.author.id == 273096208904486918 :
            await message.add_reaction(종배) #step
            return
        if message.author.id == 289770515499974658 :
            await message.add_reaction(가) #step
            await message.add_reaction(능) #step
            return
        if message.author.id == 283801341774790660 :
            await message.add_reaction(태호) #step
            return
        if message.author.id == 857622190459846706 :
            await message.add_reaction(상붕이) #step
            return
        if message.author.id == 347390605447528449 :
            await message.add_reaction(상붕이) #step
            return
        if message.author.id == 261105504095436800 :
            await message.add_reaction(김우희1) #step
            await message.add_reaction(김우희2) #step
            return
        if message.author.id == 796718250221371403 :
            await message.add_reaction(김우희2) #step
            return
        
        if message.author.id == 360998052342923265 :
            await message.add_reaction(호준) #step
            return
        if message.author.id == 283826716424798208 :
            await message.add_reaction(동현) #step
            return
        await message.add_reaction(emoji) #step


def 도움(): #도움말 내용
    embed = discord.Embed(
        title="도움말",
        colour=0x0097ff)
    embed.add_field(name=f"{명령어}참가",value="내전에 들어가짐",inline=False)
    embed.add_field(name=f"{명령어}제거",value="내전에서 나가짐",inline=False)
    embed.add_field(name=f"{명령어}랜덤시작",value="랜덤하게 팀이 정해짐",inline=False)
    embed.add_field(name=f"{명령어}순서시작",value=f"{명령어}블루 (라인) {명령어}레드 (라인) {명령어}라인제거",inline=False)
    return embed

def embed_play(): #임베드 내용
    블루팀 =f"{팀1.get('탑'):ㅤ<5} \n {팀1.get('정글')} \n {팀1.get('미드')} \n {팀1.get('원딜')} \n {팀1.get('서폿')}"
    레드팀 =f"ㅤㅤ{팀2.get('탑')} \n ㅤㅤ{팀2.get('정글')} \n ㅤㅤ{팀2.get('미드')} \n ㅤㅤ{팀2.get('원딜')} \n ㅤㅤ{팀2.get('서폿')}"
    라인=f"탑 \n 정글 \n 미드 \n 원딜 \n 서폿"
    인원=" ".join(인원1)
    if len(인원1)==0:
        인원=" "
    if 시작종류==0:
        embed = discord.Embed(title=f"팀    찬성:{len(re_yes_list)}명 반대:{len(re_no_list)}명", description=f"명단 {len(인원1)}명 \n{인원}", color=0xAAFFFF)
    if 시작종류==1:
        embed = discord.Embed(title=f"팀    찬성:{len(re_yes_list)}명 반대:{len(re_no_list)}명", description=f"명단 {len(인원1)}명 \n{인원}", color=0xAAFFFF)
        embed.add_field(name="순서", value=" ".join(순서목록), inline=False)
    embed.add_field(name="블루팀", value=블루팀)
    embed.add_field(name="라인", value=(라인), inline=True)
    embed.add_field(name="ㅤㅤ레드팀", value=(레드팀), inline=True)
    return embed

async def 새로고침(teamc,helpme): #노래 상태 1초마다 변경
    try:
        embed=embed_play()
        await teamc.edit(embed=embed)
        embed=도움()
        await helpme.edit(embed=embed)
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
    if reaction.message.channel.id != 채널ID:
        return
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
        await 새로고침(teamc,helpme)
        return
    if str(reaction.emoji) == re_no:
        userid = user.name
        if userid in re_list:
            await reaction.remove(user)
            return
        re_list.append(userid)
        re_no_list.append(userid)
        await reaction.remove(user)
        await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
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
    await 새로고침(teamc,helpme)
    await ctx.message.delete()




bot.run(봇토큰)
