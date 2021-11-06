import discord

client = discord.Client()

token = "봇 토큰"


@client.event
async def on_message(msg):
    if msg.content.startswith("!웹훅생성 "):
        try:
            if msg.author.guild_permissions.administrator:
                name = msg.content.split(" ")[1]
                print(f"{name}")
                web = await msg.channel.create_webhook(name=name)
                print(web.url)
                await msg.channel.author(f"웹훅이 생성되었습니다.\n웹훅이름 : {name}")
            else:
                await msg.channel.author("당신은 관리자가 아닙니 둥가둥가")
        except Exception as e:
            print(str(e))
            if str(e) == "400 Bad Request (error code: 30007): Maximum number of webhooks reached (10)":
                await msg.channel.author("웹훅의 최대 생성 갯수는 9개입니다.")

client.run(token)
