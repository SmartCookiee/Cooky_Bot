import time
from pytz import timezone
import nonebot
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from datetime import datetime


from .config import Config

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())


Cooky_time = on_command("", priority=5)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

format = "%H:%M"


@Cooky_time.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/时间 上海，则args为上海
    if args:
        state["city"] = args.replace("时间", "")  # 如果用户发送了参数则直接赋值


@Cooky_time.got("city", prompt="你想查询哪里的时间呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    #if city not in ["诺森德", "银色试炼场","北风苔原", "索拉查盆地","冬拥湖", "冰冠冰川","冰封王座","晶歌森林", "龙骨荒野", "风暴峭壁", "祖达克","灰熊丘陵", "嚎风峡湾",
    #                "暴风城","诺莫瑞根","铁炉堡","幽暗城","银月城","藏宝湾","南海镇","通灵学院","斯坦索姆", "闪金镇","提瑞斯法领地", "银松森林", "艾尔文森林", "西部荒野",
    #                "西瘟疫之地","奥特兰克山脉","希尔斯布莱德丘陵","阿拉斯高地","丹莫罗","炽热峡谷","燃烧平原","荆棘谷","逆风小径","奎尔丹纳斯岛","永歌森林","幽魂之地",
    #                "东瘟疫之地","辛特兰","湿地","洛克莫丹","荒芜之地","赤脊山","悲伤沼泽","诅咒之地",
    #                "奥格瑞玛","回音群岛","达纳苏斯","加基森","雷霆崖","泰达希尔","时光之穴","秘蓝岛","秘血岛","埃索达","月光林地","黑海岸","灰谷","费伍德森林","石爪山脉","凄凉之地","菲拉斯","希利苏斯",
    #                "莫高雷","安戈洛","千针石林","莫高雷","贫瘠之地","海加尔山","冬泉谷","艾萨拉","尘泥沼泽","塔纳利斯","杜隆塔尔",
    #               "七星殿","螳螂高原","恐惧废土","昆莱山","锦绣谷","四风谷","卡桑琅丛林","翡翠林","雷神岛",
    #                "库尔提拉斯","伯拉勒斯","德鲁斯瓦","斯托颂谷地","提拉加德海峡","麦卡贡",
    #                "赞达拉","达萨罗","沃顿","纳兹米尔","祖达萨","纳沙塔尔"
    #                "大漩涡","科赞","破碎群岛"]:

    #    await Cooky_time.reject("你想查询的地区暂不支持，请重新输入！")
    city_time = await get_time(city)
    await Cooky_time.finish(city_time)


async def get_time(city: str):
    if city in ["潘达利亚","七星殿" , "锦绣谷" , "四风谷" , "昆莱山" , "卡桑琅丛林" , "翡翠林" , "诺森德" , "银色试炼场" , "晶歌森林" , "龙骨荒野" , "风暴峭壁" , "祖达克" , "灰熊丘陵" , "嚎风峡湾"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Asia/Shanghai'))
        now_gmt_8 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_8

    elif city in ["赞达拉" , "达萨罗" , "沃顿" , "纳兹米尔" , "祖达萨" , "纳沙塔尔"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Pacific/Auckland'))
        now_gmt_12 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_12

    elif city in ["库尔提拉斯" , "伯拉勒斯" , "德鲁斯瓦" , "斯托颂谷地" , "提拉加德海峡" , "麦卡贡"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Pacific/Niue'))
        now_gmt_n11 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_n11

    elif city in ["螳螂高原" , "恐惧废土" , "北风苔原" , "索拉查盆地" , "冬拥湖" , "冰冠冰川" , "冰封王座" , "雷神岛" , "大漩涡" , "科赞" , "破碎群岛"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Asia/Tokyo'))
        now_gmt_9 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_9

    elif city in ["秘蓝岛" , "秘血岛" , "埃索达"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Europe/London'))
        now_gmt_0 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_0

    elif city in ["达纳苏斯" , "泰达希尔" , "月光林地" , "黑海岸" , "灰谷" , "费伍德森林" , "石爪山脉" , "凄凉之地" ,"菲拉斯" , "希利苏斯"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Europe/Berlin'))
        now_gmt_1 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_1

    elif city in ["莫高雷" , "安戈洛" , "千针石林" , "莫高雷" , "贫瘠之地" , "海加尔山" , "冬泉谷" , "雷霆崖"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Europe/Warsaw'))
        now_gmt_2 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_2

    elif city in ["艾萨拉" , "尘泥沼泽" , "塔纳利斯" , "杜隆塔尔" , "奥格瑞玛" , "回音群岛" , "加基森" , "时光之穴"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('Europe/Moscow'))
        now_gmt_3 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_3

    elif city in ["暴风城" , "诺莫瑞根" , "铁炉堡" , "闪金镇" , "藏宝湾" , "西部荒野" , "艾尔文森林" , "暮色森林","提瑞斯法领地", "银松森林", "艾尔文森林"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('America/Vancouver'))
        now_gmt_n8 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_n8

    elif city in ["幽暗城" , "南海镇" , "通灵学院" , "西瘟疫之地", "奥特兰克山脉" , "希尔斯布莱德丘陵" , "阿拉斯高地" , "丹莫罗" , "炽热峡谷" , "燃烧平原" , "荆棘谷" , "逆风小径"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('America/Edmonton'))
        now_gmt_n7 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_n7

    elif city in ["银月城" , "斯坦索姆" , "奎尔丹纳斯岛" , "永歌森林" , "幽魂之地" ,"东瘟疫之地" , "辛特兰" , "湿地" , "洛克莫丹" , "荒芜之地" , "赤脊山" , "悲伤沼泽" , "诅咒之地"]:
        now_utc = datetime.now(timezone('UTC'))
        where_time = now_utc.astimezone(timezone('America/Winnipeg'))
        now_gmt_n6 = (where_time.strftime(format))

        return f"现在是{city}时间" + now_gmt_n6

