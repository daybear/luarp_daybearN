import discord, asyncio, pytz, datetime

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("봇이 시작되었어요.")

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content.startswith ("!공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = client.get_channel(893723620851974155)
            embed = discord.Embed(title="LUA SERVER - 공지사항", description="{}".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="작성자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/icons/892372254174892044/091e6f323cfdc1cb11aba5d9dd4603e4.png?size=96")
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/892372254174892044/091e6f323cfdc1cb11aba5d9dd4603e4.png?size=96")
            await channel.send ("@everyone", embed=embed)
            await message.channel.send("```**[ LUA RP ]** | 관리자님, 정상적으로 공지사항을 등록하였어요!\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(channel, message.author, notice))
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODk5OTU5NzY3MDIyMzI1Nzky.YW6W2A.hcSNsjSE6B2Bvb4GX2E_-wssQDc')