import os
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인됨: {bot.user.name}")
    try:
        synced = await bot.sync_commands()
        print(f"📋 슬래시 명령어 {len(synced)}개 동기화 완료")
    except Exception as e:
        print(f"❌ 동기화 실패: {e}")

@bot.slash_command(name="청소", description="채팅 메시지를 삭제합니다.")
async def 청소(ctx: discord.ApplicationContext, amount: int):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.respond("🚫 메시지 관리 권한이 필요합니다.", ephemeral=True)
        return

    if amount < 1:
        await ctx.respond("⚠️ 1 이상의 숫자를 입력해주세요.", ephemeral=True)
        return

    deleted = await ctx.channel.purge(limit=amount)
    await ctx.respond(f"🧹 {len(deleted)}개의 메시지를 삭제했어요!", ephemeral=True)

bot.run(os.getenv("DISCORD_TOKEN"))
