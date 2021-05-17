
import time
import requests
import json
import pickle
from nonebot import *
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, mirai
from nonebot.adapters.cqhttp import MessageEvent, ActionFailed, MessageSegment, Message, GroupMessageEvent

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from random import randint

weather = on_command(".", priority=4)
ship = on_command("来点", priority=5)
anti_niwu = on_command("看看", priority=6)


search_command = on_command("搜索", priority=3)


@search_command.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@search_command.got("city")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    city_weather = await search_image(city)
    await search_command.finish(city_weather)

async def search_image(item: str):
    if item in ["涩图","色图","setu","腿","腿子","奶子","乃子","萝莉","loli","二次元涩图","二次元色图","三次元涩图","三次元色图"]:
        url = "https://unl.box.com/shared/static/k6a2mqrqjnli6qxilwdsq0r7hh69q1tw.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)
    else:
        index = 1
        chrome_options = Options()
        # 设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--window-size=1920,1080");
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(executable_path=r'D:\QQ_Bot\chromedriver.exe', options=chrome_options)

        driver.get('https://www.google.com/imghp?hl=en')
        time.sleep(0.5)
        search_ele = driver.find_element_by_xpath('''//*[@id="sbtc"]/div/div[2]/input''')
        search_ele.send_keys(item)
        login_ele = driver.find_element_by_xpath('''//*[@id="sbtc"]/button''')
        login_ele.click()
        while True:
            login_ele = driver.find_element_by_xpath(r'''//*[@id="islrg"]/div[1]/div[''' + str(index) + ''']''')
            login_ele.click()
            try:
                login_ele = driver.find_element_by_xpath(
                    '''//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img''')
                time.sleep(2)
                url = login_ele.get_attribute('src')
            except:
                pass
            index += 1
            if 'http' in url:
                msg = f"[CQ:image,file={url}]"
                break

        driver.close()
        return Message(msg)

@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


@ship.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@ship.got("city")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    city_weather = await get_image(city)
    # msg = f"[CQ:cardimage,file={city_weather}]"
    # await weather.finish(city_weather)
    await weather.finish(city_weather)

@anti_niwu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@anti_niwu.got("city")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    city_weather = await get_niwu(city)
    # msg = f"[CQ:cardimage,file={city_weather}]"
    # await weather.finish(city_weather)
    await weather.finish(city_weather)



#===============.=================
async def get_weather(city: str):
    if city in ["指令","命令","help","Help","菜单"]:
        return '1)  .Cooky\n'\
               '2)  .奥利\n' \
               '3)  .穷人\n' \
               '4)  .xwh\n' \
               '5)  .尼五\n' \
               '6)  .群大佬\n' \
               '\n' \
               '7)  看看<谁>\n' \
               'EX: 看看腿子, 看看奥利, 看看Cooky\n' \
               '\n' \
               '8)  来点<谁/星际公民旗舰>\n' \
               'EX: 来点北极星, 来点伊德利斯, 来点海妖, 来点Cooky, 来点奥利, etc....' \
               '\n' \
               '\n' \
               '9)  <艾泽拉斯地区>时间\n ' \
               'EX: 奥格瑞玛时间, 七星殿时间, 西瘟疫之地时间, etc....' \
               '\n' \
               '\n' \
               '10) 搜索 <事物>\n ' \
               'EX: 搜索 3090, 搜索 奥利奥, (在谷歌里,抓取第一张图片) ' \

    elif city in ["Cooky","cooky","曲奇"]:
        value = randint(0, 100)

        if (value >= 0) and (value <=15):
            url = "https://unl.box.com/shared/static/rs6ua96q49uq47s9l4hwl1a8ed7oy4si.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value >= 16) and (value <=30):
            return "遇到困难 睡大觉！~"
        elif (value >= 31) and (value <=45):
            return "炉石传说 启动！"
        elif (value >= 46) and (value <=60):
            return "下次一定！咕~"
        elif (value >= 61) and (value <=75):
            return "我曾经也想成为一个艺术家!"
        elif (value >= 76) and (value <=90):
            return "让我再睡5分钟~"
        elif (value >= 91) and (value <=95):
            return "你难道就这么想要了解Cooky么！"
        elif (value >= 91) and (value <=100):
            return "别问了 ＞﹏＜ 别问了"

    elif city in ["奥利"]:
        value = randint(0, 15)

        if (value == 0):
            return "麻烦给尼五一拳!"
        elif (value == 1):
            return "其实我叫always不是奥利"
        elif (value == 2):
            return "代码写的头都秃了"
        elif (value == 3):
            return "做饭好难"
        elif (value == 4):
            return "快给我变！ ☞猫猫"
        elif (value == 5):
            return "来点有趣的视频"
        elif (value == 6):
            return "请务必介绍给我富婆"
        elif (value == 7):
            return "想去人少的地方盖一栋漂亮的房子，种一点地，养一些动物"
        elif (value == 8):
            url = "https://unl.box.com/shared/static/dc9qxevwv58bmjigw9iy9w5qrac5fruf.gif"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 9):
            url = "https://unl.box.com/shared/static/jsmzw2emgm3b0nnnjw9r70qa6l1n0kni.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 10):
            url = "https://unl.box.com/shared/static/zyksinkmy03kiupoydrcfxagpwth00pm.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 11):
            url = "https://unl.box.com/shared/static/a3x730cy489xh4wtlik8qfuqlonn6prb.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 12):
            url = "https://unl.box.com/shared/static/m5hto66nqsbw14pdl9dtn30e2g2eymiu.png"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 13):
            url = "https://unl.box.com/shared/static/h2436fjqzy80cpki0piaes0fs7adiehb.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 14):
            url = "https://unl.box.com/shared/static/y3kch67yxaro6nvixe184phmxs7k5t66.gif"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 15):
            url = "https://unl.box.com/shared/static/u20z97vzd5jvj32dwv07t7t9itdwqzzc.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["test"]:
        value = randint(0, 1)
        if (value == 0):
            return "这是0？"
        elif (value == 1):
            return "这是1？"

    elif city in ["Lucas","lucas"]:
        value = randint(0, 4)
        if (value == 0):
            url = "https://unl.box.com/shared/static/sgxgqutdv45yej6az0a5fj54fb2onpfr.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

        elif (value == 1):
            url = "https://unl.box.com/shared/static/azy4qwdw5vbr3m3pmvtdnje7q72uzkea.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

        elif (value == 2):
            url = "https://unl.box.com/shared/static/f7i1ozoqpiamss3on95g5gwjxywd3hcd.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

        elif (value == 3):
            url = "https://unl.box.com/shared/static/iqqusxmxomc7kl6eznovc90j7x37xxpu.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

        elif (value == 4):
            url = "https://unl.box.com/shared/static/4qg2u5cje0p3vux41rksp0ekknkgjutg.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["穷人"]:
        return "你是在说凯尔萨斯殿下么？"

    elif city in ["星辰"]:
        value = randint(0, 1)
        if (value == 0):
            return "炎黄是什么臭鱼烂虾！ 枪在手跟我肘~ 今晚吃顿熊猫"
        if (value == 1):
            return "穷鬼🈚💴"

    elif city in ["Neon","neon"]:
        value = randint(0, 7)
        if (value == 0):
            return "老板买一艘把~！"
        elif (value == 1):
            return "啊,又一个潜在的客户~"
        elif (value == 2):
            return "弄坏了就得买下来！"
        elif (value == 3):
            return "我能为你的钱包瘦身嘛~"
        elif (value == 4):
            return "啊,又一个潜在的客户~"
        elif (value == 5):
            return "别摸我的脸，这得额外收费!"
        elif (value == 6):
            return "啊～我这里肯定有你需要的东西"
        elif (value == 7):
            return "富婆💴"

    elif city in ["xwh"]:
        value = randint(0, 105)
        if (value >= 0) and (value <=15):
            return "穷人!"
        elif (value >= 16) and (value <=30):
            return "精灵王子出世！"
        elif (value >= 31) and (value <= 45):
            return "魔法，能量，我的人民陷入其中不能自拔"
        elif (value >= 46) and (value <=60):
            return "你们看，我的个人收藏中有许多武器！（召唤7把武器）"
        elif (value >= 61) and (value <=75):
            return "辛多雷是不可战胜的！"
        elif (value >= 76) and (value <= 90):
            return "别打我了 这就掉奥的灰烬给你~"
        elif (value >= 91) and (value <= 105):
            return "银月城第一富豪"

    elif city in ["尼五"]:
        value = randint(0, 120)

        if (value >= 0) and (value <=15):
            return "看看腿子"
        elif (value >= 16) and (value <=30):
            return "看看手手"
        elif (value >= 31) and (value <=45):
            return "看看脚脚"
        elif (value >= 46) and (value <=60):
            return "看看肚子"
        elif (value >= 61) and (value <=75):
            return "看看猫猫"
        elif (value >= 76) and (value <=90):
            return "看看茶几"
        elif (value >= 91) and (value <=105):
            return "让我看看！"
        elif (value >= 106) and (value <=120):
            return "妹妹~ 我是正经人，没那么想的那么坏！"

    elif city in ["群大佬"]:
        value = randint(0, 100)
        if (value >= 0) and (value <= 24):
            return 'xwh: 我买无人机不玩, 就是看'
        elif (value >= 25) and (value <= 49):
            return "Cooky: 我买这个地不种, 就是玩"
        elif (value >= 50) and (value <= 74):
            return "星辰: 我买这个船不开, 就是看"
        elif (value >= 75) and (value <= 100):
            return "奥利: 我打这个缰绳不骑, 就是玩"


#===============来点=================
async def get_image(city: str):
    if city in ["北极星"]:
        value = randint(0, 8)
        if (value ==0 ):
            url = "https://unl.box.com/shared/static/g1hor0kl255r5c0ek46fhjuxs5hktgld.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value ==1 ):
            url = "https://unl.box.com/shared/static/16wfjh6cl1haypvuhr0ghi9zm2xvrekc.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/ugusyr4qqhn18rmyqmm19ahc3cfnbs1v.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/oluvpvsyf9f2t0gkppeiqm9tkkrvwojf.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 4):
            url = "https://unl.box.com/shared/static/q774jduzie91lchkfa5p0881n9kf9xco.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 5):
            url = "https://unl.box.com/shared/static/8f49etyxntvpwn7aub3m1aqg4hhxesph.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 6):
            url = "https://unl.box.com/shared/static/q2dvcgtnk2qj6tacmbgs69y8xczqbh7z.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 7):
            url = "https://unl.box.com/shared/static/hrfv0snvlqmuf63xzxvlf9hm75qls2z8.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 8):
            url = "https://unl.box.com/shared/static/2kmj5n8fxpto5wyr2xr6x4xdeg37stza.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["伊德利斯"]:
        value = randint(0, 9)
        if (value ==0 ):
            url = "https://unl.box.com/shared/static/wv1990czootaa2xcy2elmw0q81d6whkw.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value ==1 ):
            url = "https://unl.box.com/shared/static/n6fj23mqiqorsxu3ezxh0pmfsq4a4rbs.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/yfxvdsrvi16hrbxvh37ike3rze358qzb.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/pr4nbzmuf9mbfv21jbu6vx9c3pl7k1gs.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 4):
            url = "https://unl.box.com/shared/static/wtudzvycjqa4hefc51kcdmsex63l7l3t.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 5):
            url = "https://unl.box.com/shared/static/vdlhuqhx4esyhs5n3egp69pp2mp046uu.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 6):
            url = "https://unl.box.com/shared/static/2040d5050p7j6dcc2olvuwe2ue1f2d1m.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 7):
            url = "https://unl.box.com/shared/static/hfbjj94p4oskzg6cxyccwx0p667hb1x1.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 8):
            url = "https://unl.box.com/shared/static/o3qqunui6oy8eiy9fvesbrs3ual2hzt0.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 9):
            url = "https://unl.box.com/shared/static/ogfe3lnz1w336fdd4kaecjjls6g4wvfl.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["海妖"]:
        value = randint(0, 6)
        if (value ==0 ):
            url = "https://unl.box.com/shared/static/rwl0kk7sqi6plhavr36jvlw6kyryw9e6.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value ==1 ):
            url = "https://unl.box.com/shared/static/ukw58ohb6187a20i7dtz8p7w0mb4s2d7.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/wdsivdtav44pdudnekce5ks8of75psls.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/r697e9p8cbs5wr4fh0g95ws8ey5nq8ya.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 4):
            url = "https://unl.box.com/shared/static/h1ukv9fzig0jdc0cmuxweyypzvnlajkn.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 5):
            url = "https://unl.box.com/shared/static/noz8fr2tvkfg7p4df2ekzxaa4ca1o4qb.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 6):
            url = "https://unl.box.com/shared/static/yvuedfxaccs4aijlyk6ts0y07zp700z9.jpg"
            msg = f"[CQ:image,file={url}]"

    elif city in ["开拓者"]:
        value = randint(0, 5)
        if (value == 0):
            url = "https://unl.box.com/shared/static/3pp2x0emkzwi3sewezzmvo6xq6e0125q.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/5ij5lxor02oage7fda4hg5lm15my1ewd.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/vr0uonet4i5yt8534hdydi86pcrjy3bo.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/avlrak3nsygneucw4l74zwyh0chcnurp.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 4):
            url = "https://unl.box.com/shared/static/fffe5e8lon4x0dzfvmo0fol6ncizy5tc.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 5):
            url = "https://unl.box.com/shared/static/a43lafvr476feceqipcu54tq1blx02ke.jpg"
            msg = f"[CQ:image,file={url}]"

    elif city in ["标枪"]:
        value = randint(0, 3)
        if (value == 0):
            url = "https://unl.box.com/shared/static/fafcy91y6wnzudmwywof198onpigpnpx.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/hhav8lhlhf73ycvcdvz0jtxeewh62qjs.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/o357yslj4hoxve6dfn8y2sxmm1a1b10h.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/rru3s1fl9codktio9o7kaft9frfht8g6.png"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["Cooky","cooky"]:
        url = "https://unl.box.com/shared/static/k6a2mqrqjnli6qxilwdsq0r7hh69q1tw.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["Cooky哥","cooky哥","Cooky哥哥","cooky哥哥","aniki","Aniki"]:
        url = "https://unl.box.com/shared/static/u2qx40w3ei1lja381xfj62c9f6txqfcy.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["Cooky小仙女","cooky小仙女","cooky仙女","Cooky仙女","仙女cooky","仙女Cooky"]:
        value = randint(0, 3)
        if (value == 0):
            url = "https://unl.box.com/shared/static/ky27lhzdf1fet2z87t25j6k979ig9vv2.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/sjdziux0b3vuf2u2r03uqdq5vmqa1jzu.gif"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/gnyl4v4eyr2fj87mpoz0u9ikuba9bdfs.png"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/z8edk08kez7x2x7nytdyus16ex16uxiw.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["猫猫"]:
        url = "https://unl.box.com/shared/static/sjdziux0b3vuf2u2r03uqdq5vmqa1jzu.gif"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["奥利"]:
        url = "https://unl.box.com/shared/static/zyksinkmy03kiupoydrcfxagpwth00pm.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["色图","涩图","setu"]:
        value = randint(0, 3)
        if (value == 0):
            url = "https://unl.box.com/shared/static/qjfaror01stcodbh0h547gkyrz9hwoy1.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/rr8ywa0fa5c8e1sxgqyojkoa5jrg6i18.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/eb5zspwfc9e7rcf8o7mx4iw1xqysk4vn.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

#===============看看=================
async def get_niwu(city: str):

    if city in ["腿","腿子","腿！","腿子！", "锁骨","奶子","乃子","手手","手","肚子","肚肚","jio","脚脚","脚","jiojio"]:
        value = randint(0, 2)
        if (value == 0):
            url = "https://unl.box.com/shared/static/k6a2mqrqjnli6qxilwdsq0r7hh69q1tw.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/qjfaror01stcodbh0h547gkyrz9hwoy1.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/rr8ywa0fa5c8e1sxgqyojkoa5jrg6i18.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)

    elif city in ["猫猫"]:
        url = "https://unl.box.com/shared/static/sjdziux0b3vuf2u2r03uqdq5vmqa1jzu.gif"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["奥利"]:
        url = "https://unl.box.com/shared/static/zyksinkmy03kiupoydrcfxagpwth00pm.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)
    elif city in ["Cooky","cooky"]:
        url = "https://unl.box.com/shared/static/k6a2mqrqjnli6qxilwdsq0r7hh69q1tw.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["Cooky哥","cooky哥","Cooky哥哥","cooky哥哥","aniki","Aniki"]:
        url = "https://unl.box.com/shared/static/u2qx40w3ei1lja381xfj62c9f6txqfcy.jpg"
        msg = f"[CQ:image,file={url}]"
        return Message(msg)

    elif city in ["Cooky小仙女","cooky小仙女","cooky仙女","Cooky仙女","仙女cooky","仙女Cooky"]:
        value = randint(0, 3)
        if (value == 0):
            url = "https://unl.box.com/shared/static/ky27lhzdf1fet2z87t25j6k979ig9vv2.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 1):
            url = "https://unl.box.com/shared/static/sjdziux0b3vuf2u2r03uqdq5vmqa1jzu.gif"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 2):
            url = "https://unl.box.com/shared/static/gnyl4v4eyr2fj87mpoz0u9ikuba9bdfs.png"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
        elif (value == 3):
            url = "https://unl.box.com/shared/static/z8edk08kez7x2x7nytdyus16ex16uxiw.jpg"
            msg = f"[CQ:image,file={url}]"
            return Message(msg)
