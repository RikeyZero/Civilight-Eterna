from nonebot.adapters.onebot.v11 import (
    MessageSegment,
    MessageEvent,
    Bot,
    Message,
    GroupMessageEvent,
)
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.plugin import on_regex

import random
import os
import base64
from pathlib import Path

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_ailixiya",
    description="",
    usage="",
    config=Config,
)

LaoTe = on_regex(pattern=r'^牢(特|普|娅|亚|门)$',rule=to_me,block=True)

LaoTeVoice=[
    '我还记得这间会议室。这是专门为特蕾西娅空着的位置吗？不......我并不需要。',
    '特蕾西娅已经永远离开了，现在留在这里的我，只是一个存在于“魔王”之中的程序。因为阿米娅的情感，我才会以这副模样显现。不要将我当作特蕾西娅，尽管我记得过去的一切。',
    '我会陪在阿米娅身边，也会陪着罗德岛的大家，虽然这也算不上对过去时光的补偿......博士，我不是PRTS那样的程序哦，你看，虽然这个身体没有温度，可我也是会笑的。',
    '罗德岛跨过了战争，该沿着她原本的航线出发了。就从改善后勤保障做起如何？有几间会议室是不是可以腾出来改成病房呢......征求我的意见？博士，我说过的，不要将我当作特蕾西娅。',
    '“罗德岛制药公司”，注册地是阿米娅的故乡呢。这些药物都是凯尔希研制的吗......怎么会遗憾？巴别塔的使命已经完成了，罗德岛会继续航行，治愈病痛。特蕾西娅也一定会很欣慰吧。',
    '我从不后悔曾经的选择。我们做了可以做的一切，然后将希望留给未来。时间会弥合伤口，爱意会抚平疤痕。漫漫长夜后，罗德岛会迎来黎明。许多人在途中离去了，我会留在这里，见证那个结局。',
    '阿米娅看上去还是这么瘦弱，这个年纪的孩子，个子是不是应该更高一点才对？她到底有没有好好吃饭呢......她多想看到阿米娅现在的样子，多想陪她再长大一点。她本该看到的......',
    '凯尔希还是不愿与我讲话，向这顶王冠询问的时候，她都在回避我的眼睛。“魔王”记得她的过去，我可以体谅她的孤独，却不能为她解开枷锁。博士，或许有一天，你可以陪她找到存在的意义。',
    '博士，你的眼里常怀愧疚。可你说，记忆能够决定一个人是谁吗？失去了记忆的你，和只是拥有她记忆的我，又如何解开那个结呢？多去陪陪阿米娅和凯尔希吧，停留在过去的有她就够了。',
    '博士，累了吗？那就休息吧。每个人都有平静入梦的权利，你也一样。',
    '......我在。',
    '......我是不是在作战画面里看到了阿米娅？',
    '我还记得亲手交出去的每一块勋章，这样的仪式也是一种承诺。罗德岛不会放弃理想，不会辜负牺牲，不会遗忘同行的人。我们依然行走在最初所希望的路上。',
    '我知道，还有许多人需要我。不用着急，这一次我不会离开了。',
    '你会再次带领我们走向胜利吗，博士？',
    '我会与罗德岛的战士们站在一起。',
    '罗德岛的战士们，愿你们凯旋。',
    '我能听到你们所有人的悲伤。',
    '别怕，我在。',
    '我在这儿呢，我会一直陪着你。',
    '你们的信念，同样可敬。',
    '继续向前走吧，我会陪在你身边。',
    '别哭，很快就结束了。',
    '终有一天，我们可以点起火焰，燃尽一切腐朽。',
    '如果没有你，我们的伤亡可能会更加严重......谢谢你，博士。',
    '我们一定可以跨过这些伤痛，罗德岛不会在此停下。',
    '你总是可以计算得很清楚，让一切都依照你的计划进行，对吗？',
    '新的安保系统，还认识我吗？',
    '哈！被吓到了吗？',
    '我在注视着你，博士。',
    '新年快乐，博士。罗德岛比过去要热闹很多呢。虽然还有那么多未完成的事情，但是这一时半刻的安宁也弥足珍贵。博士，可以替我把这些故事书和玩偶送给孩子们吗？特蕾西娅总是会这么做。',
    '程序启动，访问人，博士——博士，早上好。',
    '“罗德岛”，这个名字给人一种很柔软的感觉。念出这个名字的时候，想到的一定是很温柔的回忆。我希望罗德岛可以一直一直，带着许多人的期望行驶下去。在将来，她也会成为更多人的家吧。'
    '我会记住你们每一个人。',
    '我也是巴别塔的一分子，必要的时候，还是要贡献自己的力量呀。“而且你看，我的成绩还是挺厉害的，对不对？',
]

@LaoTe.handle()
async def handle_function():
    await LaoTe.send(random.choices(LaoTeVoice))

LaoYa = on_regex(pattern=r"^超级?(小|牢)?特$", rule=to_me, block=True)

# 指定图片文件的路径
img_path = Path(os.path.join(os.path.dirname(__file__), "Set your imgfile here"))
file_name = "Set Your img file name"
file_path = img_path.joinpath(file_name)


@LaoYa.handle()
async def handle_function():
    # 以二进制模式读取图片文件
    with open(file_path, "rb") as f:
        img_bytes = f.read()

    # 将图片转换为 base64 字符串
    base64_str = "base64://"+base64.b64encode(img_bytes).decode()

    # 发送消息，包含图片
    
    await LaoYa.send(MessageSegment.image(base64_str))
    await LaoYa.send("我打罗德岛？真的假的？")




config = get_plugin_config(Config)

