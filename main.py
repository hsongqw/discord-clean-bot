import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # 메시지 읽기 허용

bot = commands.Bot(command_prefix='', intents=intents)  # 접두사 없이 명령어 사용

@bot.event
async def on_ready():
    print(f'✅ 봇 로그인됨: {bot.user.name}')

@bot.command(name="청소", aliases=["삭제", "clear"], help="최근 메시지를 원하는 개수만큼 삭제합니다.")
@commands.has_permissions(manage_messages=True)
async def 청소(ctx, amount: int):
    if amount < 1:
        await ctx.send("⚠️ 1 이상의 숫자를 입력해주세요.")
        return
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 {len(deleted) - 1}개의 메시지를 삭제했어요!", delete_after=3)

@청소.error
async def 청소_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 이 명령어를 사용하려면 '메시지 관리' 권한이 필요해요!", delete_after=5)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❗ 숫자를 정확하게 입력해주세요. 예: `청소 10`", delete_after=5)
    else:
        await ctx.send("⚠️ 알 수 없는 오류가 발생했어요.", delete_after=5)

bot.run(os.getenv("DISCORD_TOKEN"))
