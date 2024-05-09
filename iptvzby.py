import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import os
import threading
from queue import Queue
from datetime import datetime

#  获取远程国内直播源文件
url = "https://lisa3456.github.io/zb.txt"
r = requests.get(url)
open('zb.txt', 'wb').write(r.content)

keywords = ['CCTV', 'CGTN']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('zb.txt', 'r', encoding='utf-8') as file, open('CN1.txt', 'w', encoding='utf-8') as CN1:
    CN1.write('\n央视频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            CN1.write(line)  # 将该行写入输出文件

keywords = ['卫视']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('zb.txt', 'r', encoding='utf-8') as file, open('CN2.txt', 'w', encoding='utf-8') as CN2:
    CN2.write('\n卫视频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            CN2.write(line)  # 将该行写入输出文件

keywords = ['湖北', '武汉']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('zb.txt', 'r', encoding='utf-8') as file, open('CN3.txt', 'w', encoding='utf-8') as CN3:
    CN3.write('\湖北频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            CN3.write(line)  # 将该行写入输出文件

keywords = ['河南', '郑州']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('zb.txt', 'r', encoding='utf-8') as file, open('CN4.txt', 'w', encoding='utf-8') as CN4:
    CN4.write('\河南频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            CN4.write(line)  # 将该行写入输出文件

keywords = ['北京']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('zb.txt', 'r', encoding='utf-8') as file, open('CN5.txt', 'w', encoding='utf-8') as CN5:
    CN5.write('\北京频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            CN5.write(line)  # 将该行写入输出文件

# 读取要合并的频道文件
file_contents = []
file_paths = ["CN1.txt", "CN2.txt", "CN3.txt", "CN4.txt", "CN5.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)
        
# 生成合并后的文件
with open("CN_temp.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))

# 读取要替换的文本
replacements = {
        "中央":"CCTV",
        "高清":"",
        "HD":"",
        "标清":"",
        "超高":"",
        "频道":"",
        "-":"",
        "":"",
        "PLUS":"+",
        "＋":"+",
        "L":"",
        "CMIPTV":"",
        "cctv":"CCTV",
        "CCTV1综合":"CCTV1",
        "CCTV2财经":"CCTV2",
        "CCTV3综艺":"CCTV3",
        "CCTV4国际":"CCTV4",
        "CCTV4中文国际":"CCTV4",
        "CCTV4欧洲":"CCTV4",
        "CCTV5体育":"CCTV5",
        "CCTV5+体育":"CCTV5+",
        "CCTV6电影":"CCTV6",
        "CCTV7军事":"CCTV7",
        "CCTV7军农":"CCTV7",
        "CCTV7农业":"CCTV7",
        "CCTV7国防军事":"CCTV7",
        "CCTV8电视剧":"CCTV8",
        "CCTV8纪录":"CCTV9",
        "CCTV9记录":"CCTV9",
        "CCTV9纪录":"CCTV9",
        "CCTV10科教":"CCTV10",
        "CCTV11戏曲":"CCTV11",
        "CCTV12社会与法":"CCTV12",
        "CCTV13新闻":"CCTV13",
        "CCTV新闻":"CCTV13",
        "CCTV14少儿":"CCTV14",
        "央视14少儿":"CCTV14",
        "CCTV少儿超":"CCTV14",
        "CCTV15音乐":"CCTV15",
        "CCTV音乐":"CCTV15",
        "CCTV16奥林匹克":"CCTV16",
        "CCTV17农业农村":"CCTV17",
        "CCTV17军农":"CCTV17",
        "CCTV17农业":"CCTV17",
        "CCTV5+体育赛视":"CCTV5+",
        "CCTV5+赛视":"CCTV5+",
        "CCTV5+体育赛事":"CCTV5+",
        "CCTV5+赛事":"CCTV5+",
        "CCTV5+体育":"CCTV5+",
        "CCTV5赛事":"CCTV5+",
        "CCTV4K测试":"CCTV4",
        "CCTV164K":"CCTV16",
        "凤凰中文台":"凤凰中文",
        "凤凰卫视":"凤凰中文",
        "凤凰资讯台":"凤凰资讯",
        "凤凰卫视中文":"凤凰中文",
        "凤凰卫视资讯":"凤凰资讯",
        "凤凰卫视中文台":"凤凰中文",
        "凤凰卫视资讯台":"凤凰资讯",
        "上海东方卫视":"东方卫视",
        "上海卫视":"东方卫视",
        "内蒙卫视":"内蒙古卫视",
        "福建东南卫视":"东南卫视",
        "广东南方卫视":"南方卫视",
        "金鹰卡通卫视":"金鹰卡通",
        "湖南金鹰卡通":"金鹰卡通",
        "炫动卡通":"哈哈炫动",
        "卡酷卡通":"卡酷少儿",
        "卡酷动画":"卡酷少儿",
        "BRTVKAKU少儿":"卡酷少儿",
        "优曼卡通":"优漫卡通",
        "嘉佳卡通":"佳佳卡通",
        "世界地理":"地理世界",
        "CCTV世界地理":"地理世界",
        "BTV文艺":"北京文艺",
        "BTV影视":"北京影视",
        "BTV科教":"北京科教",
        "BTV财经":"北京财经",
        "BTV生活":"北京生活",
        "BTV新闻":"北京新闻",
        "央视,#genre#":"央视频道,#genre#",
        "卫视,#genre#":"卫视频道,#genre#",
        "\湖北,#genre#":"",
        "湖北电信,#genre#":"湖北频道,#genre#",
        "\河南,#genre#":"",
        "河南电信,#genre#":"河南频道,#genre#",
        "河南联通,#genre#":"河南频道,#genre#",
        "\北京,#genre#":"",
        "北京联通,#genre#":"北京频道,#genre#",
}

# 读取要处理的文件
with open("CN_temp.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 进行批量替换
for pattern, replacement in replacements.items():
    text = re.sub(pattern, replacement, text)

# 写入替换后的文本
with open("CN.txt", "w", encoding="utf-8") as f:
    f.write(text)


#  获取远程港澳台直播源文件
url = "https://mirror.ghproxy.com/https://raw.githubusercontent.com/Fairy8o/IPTV/main/DIYP-v4.txt"
r = requests.get(url)
open('DIYP-v4.txt', 'wb').write(r.content)

keywords = ['凤凰卫视', '凤凰资讯', 'TVB翡翠', 'TVB明珠', 'TVB星河', 'J2', '无线', '有线', '天映', 'VIU', 'RTHK', 'HOY',
            '香港卫视']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('DIYP-v4.txt', 'r', encoding='utf-8') as file, open('HK.txt', 'w', encoding='utf-8') as HK:
    HK.write('\n港澳频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            HK.write(line)  # 将该行写入输出文件

keywords = ['民视', '中视', '台视', '华视', '新闻台', '东森', '龙祥', '公视', '三立', '大爱', '年代', '人间卫视',
            '人間', '大立']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
with open('DIYP-v4.txt', 'r', encoding='utf-8') as file, open('TW.txt', 'w', encoding='utf-8') as TW:
    TW.write('\n台湾频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
            TW.write(line)  # 将该行写入输出文件

# 读取要合并的香港频道和台湾频道文件
file_contents = []
file_paths = ["HK.txt", "TW.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)
# 生成合并后的文件
with open("GAT.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))



#  获取远程体育直播源文件
url = "https://mirror.ghproxy.com/https://raw.githubusercontent.com/Cx4x/Cxxx/main/TKTY.m3u"
response = requests.get(url)
m3u_content = response.text

# 移除第一行
# m3u_content = m3u_content.split('\n', 1)[1]

# 初始化变量
group_name = ""
channel_name = ""
channel_link = ""
output_dict = {}

# 处理每两行为一组的情况
for line in m3u_content.split('\n'):
    if line.startswith("#EXTINF"):
        # 获取 group-title 的值
        group_name = line.split('group-title="')[1].split('"')[0]
        
        # 获取频道名
        channel_name = line.split(',')[-1]
    elif line.startswith("http"):
        # 获取频道链接
        channel_link = line
        # 合并频道名和频道链接
        combined_link = f"{channel_name},{channel_link}"

        # 将组名作为键，合并链接作为值存储在字典中
        if group_name not in output_dict:
            output_dict[group_name] = []
        output_dict[group_name].append(combined_link)

# 将结果写入 sport.txt 文件
with open("sport.txt", "w", encoding="utf-8") as output_file:
    # 遍历字典，写入结果文件
    for group_name, links in output_dict.items():
        output_file.write(f"{group_name},#genre#\n")
        for link in links:
            output_file.write(f"{link}\n")

# 扫源
urls = [
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iSGViZWki",                # 河 北
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iYmVpamluZyI%3D",          # 北 京
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iZ3Vhbmdkb25nIg%3D%3D",    # 广 东
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0ic2hhbmdoYWki",            # 上 海
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0idGlhbmppbiI%3D",          # 天 津
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iY2hvbmdxaW5nIg%3D%3D",    # 重 庆
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0ic2hhbnhpIg%3D%3D",        # 山 西
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iU2hhYW54aSI%3D",          # 陕 西
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iamlhbmdzdSI%3D",          # 江 苏
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iemhlamlhbmci",            # 浙 江
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0iRnVqaWFuIg%3D%3D",        # 福 建
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0i5rGf6KW%2FIg%3D%3D",      # 江 西
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0i5bGx5LicIg%3D%3D",        # 山 东
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0i5rKz5Y2XIg%3D%3D",        # 河 南
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0i5rmW5YyXIg%3D%3D",    # 湖 北
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9Ind1aGFuIg%3D%3D",        # 武 汉
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9InNoaXlhbiI%3D",	    # 十 堰
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9ImppbmdtZW4i", 	    # 荆 门
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9Ikppbmd6aG91Ig%3D%3D",    # 荆 州
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9Imh1YW5nZ2FuZyI%3D",	    # 黄 冈
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9Ikh1YW5nc2hpIg%3D%3D",    # 黄 石
    "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIGNpdHk9InhpYW9nYW4i",            # 孝 感
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0iY2hhbmdkZSI%3D",      # 常 德
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0ieWl5YW5nIg%3D%3D",    # 益 阳
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0ieW9uZ3pob3Ui",        # 永 州
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0iaHVhaWh1YSI%3D",      # 怀 化
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0ic2hhb3lhbmci",        # 邵 阳
    # "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY2l0eT0iemhhbmdqaWFqaWUi",    # 张家界

    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22hebei%22",     # 河 北
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22beijing%22",   # 北 京
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22guangdong%22", # 广 东
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22shanghai%22",  # 上 海
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22tianjin%22",   # 天 津
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22chongqing%22", # 重 庆
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22shanxi%22",    # 山 西
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22shaanxi%22",   # 陕 西
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22liaoning%22",  # 辽 宁
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22jiangsu%22",   # 江 苏
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22zhejiang%22",  # 浙 江
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22anhui%22",     # 安 徽
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22fujian%22",    # 福 建
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22jiangxi%22",   # 江 西
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22shandong%22",  # 山 东
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22henan%22",     # 河 南
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22hubei%22",     # 湖 北
    # "https://www.zoomeye.org/searchResult?q=%2Fiptv%2Flive%2Fzh_cn.js%20%2Bcountry%3A%22CN%22%20%2Bsubdivisions%3A%22hunan%22",     # 湖 南
    # "https://www.zoomeye.org/searchResult?q=city:%22changsha%22",	    # 长 沙
    # "https://www.zoomeye.org/searchResult?q=city%3A%22hengyang%22",	    # 衡 阳
    # "https://www.zoomeye.org/searchResult?q=city%3A%22zhuzhou%22",	    # 株 洲
    # "https://www.zoomeye.org/searchResult?q=city%3A%22yueyang%22",	    # 岳 阳
    # "https://www.zoomeye.org/searchResult?q=city%3A%22loudi%22",	    # 娄 底
    # "https://www.zoomeye.org/searchResult?q=city%3A%22chenzhou%22",	    # 郴 州
    # "https://www.zoomeye.org/searchResult?q=city%3A%22xiangtan%22",	    # 湘 潭
    # "https://www.zoomeye.org/searchResult?q=city%3A%22changde%22",	    # 常 德
    # "https://www.zoomeye.org/searchResult?q=city%3A%22yiyang%22",	    # 益 阳
    # "https://www.zoomeye.org/searchResult?q=city%3A%22yongzhou%22",	    # 永 州
    # "https://www.zoomeye.org/searchResult?q=city%3A%22huaihua%22",	    # 怀 化
    # "https://www.zoomeye.org/searchResult?q=city%3A%22xiangxi%22",	    # 湘 西
    # "https://www.zoomeye.org/searchResult?q=city%3A%22shaoyang%22",	    # 邵 阳
    # "https://www.zoomeye.org/searchResult?q=city%3A%22zhangjiajie%22",	# 张家界
]


def modify_urls(url):
    modified_urls = []
    ip_start_index = url.find("//") + 2
    ip_end_index = url.find(":", ip_start_index)
    base_url = url[:ip_start_index]  # http:// or https://
    ip_address = url[ip_start_index:ip_end_index]
    port = url[ip_end_index:]
    ip_end = "/iptv/live/1000.json?key=txiptv"
    for i in range(1, 256):
        modified_ip = f"{ip_address[:-1]}{i}"
        modified_url = f"{base_url}{modified_ip}{port}{ip_end}"
        modified_urls.append(modified_url)

    return modified_urls


def is_url_accessible(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass
    return None


results = []

for url in urls:
    # 创建一个Chrome WebDriver实例
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    # 使用WebDriver访问网页
    driver.get(url)  # 将网址替换为你要访问的网页地址
    time.sleep(10)
    # 获取网页内容
    page_content = driver.page_source

    # 关闭WebDriver
    driver.quit()

    # 查找所有符合指定格式的网址
    pattern = r"http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"  # 设置匹配的格式，如http://8.8.8.8:8888
    urls_all = re.findall(pattern, page_content)
    # urls = list(set(urls_all))  # 去重得到唯一的URL列表
    urls = set(urls_all)  # 去重得到唯一的URL列表
    x_urls = []
    for url in urls:  # 对urls进行处理，ip第四位修改为1，并去重
        url = url.strip()
        ip_start_index = url.find("//") + 2
        ip_end_index = url.find(":", ip_start_index)
        ip_dot_start = url.find(".") + 1
        ip_dot_second = url.find(".", ip_dot_start) + 1
        ip_dot_three = url.find(".", ip_dot_second) + 1
        base_url = url[:ip_start_index]  # http:// or https://
        ip_address = url[ip_start_index:ip_dot_three]
        port = url[ip_end_index:]
        ip_end = "1"
        modified_ip = f"{ip_address}{ip_end}"
        x_url = f"{base_url}{modified_ip}{port}"
        x_urls.append(x_url)
    urls = set(x_urls)  # 去重得到唯一的URL列表

    valid_urls = []
    #   多线程获取可用url
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for url in urls:
            url = url.strip()
            modified_urls = modify_urls(url)
            for modified_url in modified_urls:
                futures.append(executor.submit(is_url_accessible, modified_url))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                valid_urls.append(result)

    for url in valid_urls:
        print(url)
    # 遍历网址列表，获取JSON文件并解析
    for url in valid_urls:
        try:
            # 发送GET请求获取JSON文件，设置超时时间为0.5秒
            ip_start_index = url.find("//") + 2
            ip_dot_start = url.find(".") + 1
            ip_index_second = url.find("/", ip_dot_start)
            base_url = url[:ip_start_index]  # http:// or https://
            ip_address = url[ip_start_index:ip_index_second]
            url_x = f"{base_url}{ip_address}"

            json_url = f"{url}"
            response = requests.get(json_url, timeout=0.5)
            json_data = response.json()

            try:
                # 解析JSON文件，获取name和url字段
                for item in json_data['data']:
                    if isinstance(item, dict):
                        name = item.get('name')
                        urlx = item.get('url')
                        if ',' in urlx:
                            urlx = f"aaaaaaaa"

                        # if 'http' in urlx or 'udp' in urlx or 'rtp' in urlx:
                        if 'http' in urlx:
                            urld = f"{urlx}"
                        else:
                            urld = f"{url_x}{urlx}"

                        if name and urld:
                            # 删除特定文字
                            name = name.replace("中央", "CCTV")
                            name = name.replace("高清", "")
                            name = name.replace("HD", "")
                            name = name.replace("标清", "")
                            name = name.replace("超高", "")
                            name = name.replace("频道", "")
                            name = name.replace("-", "")
                            name = name.replace(" ", "")
                            name = name.replace("PLUS", "+")
                            name = name.replace("＋", "+")
                            name = name.replace("(", "")
                            name = name.replace(")", "")
                            name = name.replace("L", "")
                            name = name.replace("CMIPTV", "")
                            name = name.replace("cctv", "CCTV")
                            name = re.sub(r"CCTV(\d+)台", r"CCTV\1", name)
                            name = name.replace("CCTV1综合", "CCTV1")
                            name = name.replace("CCTV2财经", "CCTV2")
                            name = name.replace("CCTV3综艺", "CCTV3")
                            name = name.replace("CCTV4国际", "CCTV4")
                            name = name.replace("CCTV4中文国际", "CCTV4")
                            name = name.replace("CCTV4欧洲", "CCTV4")
                            name = name.replace("CCTV5体育", "CCTV5")
                            name = name.replace("CCTV5+体育", "CCTV5+")
                            name = name.replace("CCTV6电影", "CCTV6")
                            name = name.replace("CCTV7军事", "CCTV7")
                            name = name.replace("CCTV7军农", "CCTV7")
                            name = name.replace("CCTV7农业", "CCTV7")
                            name = name.replace("CCTV7国防军事", "CCTV7")
                            name = name.replace("CCTV8电视剧", "CCTV8")
                            name = name.replace("CCTV8纪录", "CCTV9")
                            name = name.replace("CCTV9记录", "CCTV9")
                            name = name.replace("CCTV9纪录", "CCTV9")
                            name = name.replace("CCTV10科教", "CCTV10")
                            name = name.replace("CCTV11戏曲", "CCTV11")
                            name = name.replace("CCTV12社会与法", "CCTV12")
                            name = name.replace("CCTV13新闻", "CCTV13")
                            name = name.replace("CCTV新闻", "CCTV13")
                            name = name.replace("CCTV14少儿", "CCTV14")
                            name = name.replace("央视14少儿", "CCTV14")
                            name = name.replace("CCTV少儿超", "CCTV14")
                            name = name.replace("CCTV15音乐", "CCTV15")
                            name = name.replace("CCTV音乐", "CCTV15")
                            name = name.replace("CCTV16奥林匹克", "CCTV16")
                            name = name.replace("CCTV17农业农村", "CCTV17")
                            name = name.replace("CCTV17军农", "CCTV17")
                            name = name.replace("CCTV17农业", "CCTV17")
                            name = name.replace("CCTV5+体育赛视", "CCTV5+")
                            name = name.replace("CCTV5+赛视", "CCTV5+")
                            name = name.replace("CCTV5+体育赛事", "CCTV5+")
                            name = name.replace("CCTV5+赛事", "CCTV5+")
                            name = name.replace("CCTV5+体育", "CCTV5+")
                            name = name.replace("CCTV5赛事", "CCTV5+")
                            name = name.replace("凤凰中文台", "凤凰中文")
                            name = name.replace("凤凰卫视", "凤凰中文")
                            name = name.replace("凤凰资讯台", "凤凰资讯")
                            name = name.replace("CCTV4K测试）", "CCTV4")
                            name = name.replace("CCTV164K", "CCTV16")
                            name = name.replace("上海东方卫视", "东方卫视")
                            name = name.replace("上海卫视", "东方卫视")
                            name = name.replace("内蒙卫视", "内蒙古卫视")
                            name = name.replace("福建东南卫视", "东南卫视")
                            name = name.replace("广东南方卫视", "南方卫视")
                            name = name.replace("金鹰卡通卫视", "金鹰卡通")
                            name = name.replace("湖南金鹰卡通", "金鹰卡通")
                            name = name.replace("炫动卡通", "哈哈炫动")
                            name = name.replace("卡酷卡通", "卡酷少儿")
                            name = name.replace("卡酷动画", "卡酷少儿")
                            name = name.replace("BRTVKAKU少儿", "卡酷少儿")
                            name = name.replace("优曼卡通", "优漫卡通")
                            name = name.replace("优曼卡通", "优漫卡通")
                            name = name.replace("嘉佳卡通", "佳嘉卡通")
                            name = name.replace("世界地理", "地理世界")
                            name = name.replace("CCTV世界地理", "地理世界")
                            name = name.replace("BTV文艺", "北京文艺")
                            name = name.replace("BTV影视", "北京影视")
                            name = name.replace("BTV科教", "北京科教")
                            name = name.replace("BTV财经", "北京财经")
                            name = name.replace("BTV生活", "北京生活")
                            name = name.replace("BTV新闻", "北京新闻")
                            name = name.replace("BTV体育", "北京体育")
                            name = name.replace("BTV青年", "北京青年")  
                            name = name.replace("卡酷少儿", "北京卡酷少儿")
                            name = name.replace("BTV北京卫视", "北京卫视")
                            name = name.replace("BTV冬奥纪实", "北京冬奥纪实")
                            name = name.replace("东奥纪实", "冬奥纪实")
                            name = name.replace("都市", "河南都市")
                            name = name.replace("民生", "河南民生")
                            name = name.replace("法制", "河南法制")
                          # name = name.replace("新闻", "河南新闻")
                            name = name.replace("移动戏曲", "河南移动戏曲")
                            name = name.replace("梨园", "冬奥纪实")
                            name = name.replace("卫视台", "卫视")
                            name = name.replace("湖南电视台", "湖南卫视")
                            name = name.replace("湖北电视台", "湖北卫视")
                            name = name.replace("少儿科教", "少儿")
                            name = name.replace("影视剧", "影视")
                            results.append(f"{name},{urld}")
            except:
                continue
        except:
            continue

channels = []

for result in results:
    line = result.strip()
    if result:
        channel_name, channel_url = result.split(',')
        channels.append((channel_name, channel_url))

with open("iptv.txt", 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result + "\n")
        print(result)
print("频道列表文件iptv.txt获取完成！")

import eventlet

eventlet.monkey_patch()

# 线程安全的队列，用于存储下载任务
task_queue = Queue()

# 线程安全的列表，用于存储结果
results = []

channels = []
error_channels = []
# 从iptv.txt文件内提取其他频道进行检测并分组
with open("iptv.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            channel_name, channel_url = line.split(',')
            if 'genre' not in channel_url:
                channels.append((channel_name, channel_url))


# 定义工作线程函数
def worker():
    while True:
        # 从队列中获取一个任务
        channel_name, channel_url = task_queue.get()
        try:
            channel_url_t = channel_url.rstrip(channel_url.split('/')[-1])  # m3u8链接前缀
            lines = requests.get(channel_url).text.strip().split('\n')  # 获取m3u8文件内容
            ts_lists = [line.split('/')[-1] for line in lines if line.startswith('#') == False]  # 获取m3u8文件下视频流后缀
            ts_lists_0 = ts_lists[0].rstrip(ts_lists[0].split('.ts')[-1])  # m3u8链接前缀
            ts_url = channel_url_t + ts_lists[0]  # 拼接单个视频片段下载链接

            # 多获取的视频数据进行5秒钟限制
            with eventlet.Timeout(5, False):
                start_time = time.time()
                content = requests.get(ts_url).content
                end_time = time.time()
                response_time = (end_time - start_time) * 1

            if content:
                with open(ts_lists_0, 'ab') as f:
                    f.write(content)  # 写入文件
                file_size = len(content)
                # print(f"文件大小：{file_size} 字节")
                download_speed = file_size / response_time / 1024
                # print(f"下载速度：{download_speed:.3f} kB/s")
                normalized_speed = min(max(download_speed / 1024, 0.001), 100)  # 将速率从kB/s转换为MB/s并限制在1~100之间
                # print(f"标准化后的速率：{normalized_speed:.3f} MB/s")

                # 删除下载的文件
                os.remove(ts_lists_0)
                result = channel_name, channel_url, f"{normalized_speed:.3f} MB/s"
                results.append(result)
                numberx = (len(results) + len(error_channels)) / len(channels) * 100
                print(
                    f"可用频道：{len(results)} 个 , 不可用频道：{len(error_channels)} 个 , 总频道：{len(channels)} 个 ,总进度：{numberx:.2f} %。")
        except:
            error_channel = channel_name, channel_url
            error_channels.append(error_channel)
            numberx = (len(results) + len(error_channels)) / len(channels) * 100
            print(
                f"可用频道：{len(results)} 个 , 不可用频道：{len(error_channels)} 个 , 总频道：{len(channels)} 个 ,总进度：{numberx:.2f} %。")

        # 标记任务完成
        task_queue.task_done()


# 创建多个工作线程
num_threads = 10
for _ in range(num_threads):
    t = threading.Thread(target=worker, daemon=True)
    # t = threading.Thread(target=worker, args=(event,len(channels)))  # 将工作线程设置为守护线程
    t.start()
    # event.set()

# 添加下载任务到队列
for channel in channels:
    task_queue.put(channel)

# 等待所有任务完成
task_queue.join()


def channel_key(channel_name):
    match = re.search(r'\d+', channel_name)
    if match:
        return int(match.group())
    else:
        return float('inf')  # 返回一个无穷大的数字作为关键字


# 对频道进行排序
results.sort(key=lambda x: (x[0], -float(x[2].split()[0])))
results.sort(key=lambda x: channel_key(x[0]))
result_counter = 10  # 每个频道需要的个数

with open("hb.txt", 'w', encoding='utf-8') as file:
    channel_counters = {}
    file.write('央视频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' in channel_name or 'CGTN' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
                        
    channel_counters = {}
    file.write('卫视频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if '卫视' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
                        
    channel_counters = {}
    file.write('北京频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if '北京' in channel_name or '海淀' in channel_name or '朝阳' in channel_name or '丰台' in channel_name or '东城' in channel_name or '西城' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
                        
    channel_counters = {}
    file.write('湖北频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if '湖北' in channel_name or '武汉' in channel_name or '黄石' in channel_name or '十堰' in channel_name or '荆门' in channel_name or '荆州' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
                        
    channel_counters = {}
    file.write('河南频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if '河南' in channel_name or '郑州' in channel_name or '开封' in channel_name or '洛阳' in channel_name or '许昌' in channel_name or '驻马店' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1

    channel_counters = {}
    file.write('其他频道,#genre#\n')
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' not in channel_name and '卫视' not in channel_name and '测试' not in channel_name and '湖北' not in channel_name and '北京' not in channel_name and '河南' not in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
                        

# 扫源湖北IPTV
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

urls = ["wuhan","huangshi","shiyan","yichang","xiangyang","ezhou","jingmen","xiaogan","jingzhou","huanggang","xianning","suizhou"]
channelsx = [
    "湖北公共新闻,http://8.8.8.8:8/rtp/239.69.1.40:9880","湖北经视,http://8.8.8.8:8/rtp/239.69.1.41:9886","湖北综合,http://8.8.8.8:8/rtp/239.69.1.42:9892",
"湖北垄上,http://8.8.8.8:8/rtp/239.69.1.43:9898","湖北影视,http://8.8.8.8:8/rtp/239.69.1.204:10866","湖北生活,http://8.8.8.8:8/rtp/239.69.1.205:10872",
"湖北教育,http://8.8.8.8:8/rtp/239.69.1.206:10878","CCTV1,http://8.8.8.8:8/rtp/239.254.96.96:8550","CCTV2,http://8.8.8.8:8/rtp/239.69.1.102:10250",
"CCTV3,http://8.8.8.8:8/rtp/239.69.1.122:10370","CCTV4,http://8.8.8.8:8/rtp/239.69.1.138:10466","CCTV5,http://8.8.8.8:8/rtp/239.69.1.123:10376",
"CCTV5+,http://8.8.8.8:8/rtp/239.254.96.234:9484","CCTV6,http://8.8.8.8:8/rtp/239.69.1.124:10382","CCTV7,http://8.8.8.8:8/rtp/239.69.1.103:10256",
"CCTV8,http://8.8.8.8:8/rtp/239.69.1.125:10388","CCTV9,http://8.8.8.8:8/rtp/239.69.1.104:10262","CCTV10,http://8.8.8.8:8/rtp/239.69.1.105:10268",
"CCTV11,http://8.8.8.8:8/rtp/239.69.1.154:10560","CCTV12,http://8.8.8.8:8/rtp/239.69.1.106:10274","CCTV13,http://8.8.8.8:8/rtp/239.254.96.161:9040",
"CCTV14,http://8.8.8.8:8/rtp/239.69.1.107:10280","CCTV15,http://8.8.8.8:8/rtp/239.69.1.155:10566","CCTV16,http://8.8.8.8:8/rtp/239.69.1.247:11124",
"CCTV17,http://8.8.8.8:8/rtp/239.69.1.152:10548","CCTV第一剧场,http://8.8.8.8:8/rtp/239.69.1.74:10084","CCTV兵器科技,http://8.8.8.8:8/rtp/239.69.1.79:10114",
"CCTV风云足球,http://8.8.8.8:8/rtp/239.69.1.81:10126","CCTV高尔夫网球,http://8.8.8.8:8/rtp/239.69.1.83:10138","CCTV世界地理,http://8.8.8.8:8/rtp/239.69.1.91:10186",
"CCTV央视台球,http://8.8.8.8:8/rtp/239.69.1.98:10224","CCTV16奥林匹克-4K,http://8.8.8.8:8/rtp/239.69.1.249:11136","BestTV测试1-4K,http://8.8.8.8:8/rtp/239.69.1.26:9796",
"BestTV测试2-4K,http://8.8.8.8:8/rtp/239.69.1.27:9802","BestTV测试3-4K,http://8.8.8.8:8/rtp/239.69.1.25:9790","爱上4K,http://8.8.8.8:8/rtp/239.69.1.141:10482",
"湖北卫视,http://8.8.8.8:8/rtp/239.254.96.115:8664","河北卫视,http://8.8.8.8:8/rtp/239.254.96.113:9616","深圳卫视,http://8.8.8.8:8/rtp/239.254.96.137:8896",
"黑龙江卫视,http://8.8.8.8:8/rtp/239.254.96.138:8902","湖南卫视,http://8.8.8.8:8/rtp/239.254.96.139:8908","广东卫视,http://8.8.8.8:8/rtp/239.254.96.140:8914",
"北京卫视,http://8.8.8.8:8/rtp/239.254.96.141:8920","东方卫视,http://8.8.8.8:8/rtp/239.254.96.142:8926","浙江卫视,http://8.8.8.8:8/rtp/239.254.96.143:8932",
"江苏卫视,http://8.8.8.8:8/rtp/239.254.96.144:8938","天津卫视,http://8.8.8.8:8/rtp/239.69.1.68:10048","山东卫视,http://8.8.8.8:8/rtp/239.69.1.69:10054",
"安徽卫视,http://8.8.8.8:8/rtp/239.69.1.70:10060","辽宁卫视,http://8.8.8.8:8/rtp/239.69.1.71:10066","东南卫视,http://8.8.8.8:8/rtp/239.69.1.108:10286",
"江西卫视,http://8.8.8.8:8/rtp/239.69.1.126:10394","重庆卫视,http://8.8.8.8:8/rtp/239.69.1.149:10530","贵州卫视,http://8.8.8.8:8/rtp/239.69.1.150:10536",
"海南卫视,http://8.8.8.8:8/rtp/239.69.1.151:10542","河南卫视,http://8.8.8.8:8/rtp/239.69.1.168:10644","四川卫视,http://8.8.8.8:8/rtp/239.69.1.169:10650",
"广西卫视,http://8.8.8.8:8/rtp/239.69.1.191:10788","吉林卫视,http://8.8.8.8:8/rtp/239.69.1.212:10914","CHC-高清电影,http://8.8.8.8:8/rtp/239.69.1.241:11088",
"CHC-动作电影,http://8.8.8.8:8/rtp/239.69.1.242:11094","CHC-家庭影院,http://8.8.8.8:8/rtp/239.69.1.243:11100","武汉一台新闻综合,http://8.8.8.8:8/rtp/239.69.1.145:10506",
"武汉二台电视剧,http://8.8.8.8:8/rtp/239.69.1.146:10512","武汉三台科技生活,http://8.8.8.8:8/rtp/239.69.1.251:11148","武汉四台经济,http://8.8.8.8:8/rtp/239.69.1.35:9850",
"武汉五台文体,http://8.8.8.8:8/rtp/239.69.1.147:10518","武汉六台外语,http://8.8.8.8:8/rtp/239.69.1.36:9856","武汉教育,http://8.8.8.8:8/rtp/239.69.1.60:9994",
"蔡甸综合,http://8.8.8.8:8/rtp/239.69.1.245:11112","阳新综合,http://8.8.8.8:8/rtp/239.69.1.34:9844","房县综合,http://8.8.8.8:8/rtp/239.69.1.192:10794",
"卡酷少儿,http://8.8.8.8:8/rtp/239.69.1.193:10800","梨园频道,http://8.8.8.8:8/rtp/239.69.1.33:9838","武术世界,http://8.8.8.8:8/rtp/239.69.1.47:9922",
"快乐垂钓,http://8.8.8.8:8/rtp/239.69.1.142:10488","茶频道,http://8.8.8.8:8/rtp/239.69.1.144:10500","金鹰卡通,http://8.8.8.8:8/rtp/239.69.1.248:11130",
"金鹰纪实,http://8.8.8.8:8/rtp/239.69.1.109:10292","CETV1,http://8.8.8.8:8/rtp/239.69.1.110:10298","CCTV5+,http://8.8.8.8:8/rtp/239.69.1.12:9712",
"河北卫视,http://8.8.8.8:8/rtp/239.69.1.157:10578","东方卫视,http://8.8.8.8:8/rtp/239.69.1.173:10674","江苏卫视,http://8.8.8.8:8/rtp/239.69.1.174:10680",
"CCTV16-4K,http://8.8.8.8:8/rtp/239.69.1.13:9718",
]


results = []
channel = []
urls_all = []
resultsx = []
resultxs = []
error_channels = []

for url in urls:
    url_0 = str(base64.b64encode((f'"Server: udpxy" && city="{url}" && org="Chinanet"').encode("utf-8")), "utf-8")
    url_64 = f'https://fofa.info/result?qbase64={url_0}'
    print(url_64)
    try:
        response = requests.get(url_64, headers=headers, timeout=15)
        page_content = response.text
        print(f" {url}  访问成功")
        pattern = r'href="(http://\d+\.\d+\.\d+\.\d+:\d+)"'
        page_urls = re.findall(pattern, page_content)
        for urlx in page_urls:
            try:
                response = requests.get(url=urlx + '/status', timeout=1)
                response.raise_for_status()  # 返回状态码不是200异常
                page_content = response.text
                pattern = r'class="proctabl"'
                page_proctabl = re.findall(pattern, page_content)
                if page_proctabl:
                    urls_all.append(urlx)
                    print(f"{urlx} 可以访问")

            except requests.RequestException as e:
                pass
    except:
        print(f"{url_64} 访问失败")
        pass

urls_all = set(urls_all)  # 去重得到唯一的URL列表
for urlx in urls_all:
    channel = [f'{name},{url.replace("http://8.8.8.8:8", urlx)}' for name, url in
               [line.strip().split(',') for line in channelsx]]
    results.extend(channel)
            
results = sorted(results)
# with open("itv.txt", 'w', encoding='utf-8') as file:
#     for result in results:
#         file.write(result + "\n")
#         print(result)

# 定义工作线程函数
def worker():
    while True:
        result = task_queue.get()
        channel_name, channel_url = result.split(',', 1)
        try:
            response = requests.get(channel_url, stream=True, timeout=3)
            if response.status_code == 200:
                result = channel_name, channel_url
                resultsx.append(result)
                numberx = (len(resultsx) + len(error_channels)) / len(results) * 100
                print(
                    f"可用频道：{len(resultsx)} , 不可用频道：{len(error_channels)} 个 , 总频道：{len(results)} 个 ,总进度：{numberx:.2f} %。")
            else:
                error_channels.append(result)
                numberx = (len(resultsx) + len(error_channels)) / len(results) * 100
                print(
                    f"可用频道：{len(resultsx)} 个 , 不可用频道：{len(error_channels)} , 总频道：{len(results)} 个 ,总进度：{numberx:.2f} %。")
        except:
            error_channels.append(result)
            numberx = (len(resultsx) + len(error_channels)) / len(results) * 100
            print(
                f"可用频道：{len(resultsx)} 个 , 不可用频道：{len(error_channels)} 个 , 总频道：{len(results)} 个 ,总进度：{numberx:.2f} %。")

        # 标记任务完成
        task_queue.task_done()


# 创建多个工作线程
num_threads = 20
for _ in range(num_threads):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

# 添加下载任务到队列
for result in results:
    task_queue.put(result)

# 等待所有任务完成
task_queue.join()


def channel_key(channel_name):
    match = re.search(r'\d+', channel_name)
    if match:
        return int(match.group())
    else:
        return float('inf')  # 返回一个无穷大的数字作为关键字


for resulta in resultsx:
    channel_name, channel_url = resulta
    resultx = channel_name, channel_url
    resultxs.append(resultx)

# 对频道进行排序
resultxs.sort(key=lambda x: channel_key(x[0]))
# now_today = datetime.date.today()

result_counter = 20  # 每个频道需要的个数

with open("itv.txt", 'w', encoding='utf-8') as file:
    channel_counters = {}
    file.write('央视频道,#genre#\n')
    for result in resultxs:
        channel_name, channel_url = result
        if 'CCTV' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
    channel_counters = {}
    file.write('\n卫视频道,#genre#\n')
    for result in resultxs:
        channel_name, channel_url = result
        if '卫视' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
    channel_counters = {}
    file.write('\n湖北频道,#genre#\n')
    for result in resultxs:
        channel_name, channel_url = result
        if '湖北' in channel_name or '武汉' in channel_name or '宜昌' in channel_name or '黄石' in channel_name or '十堰' \
                in channel_name or '荆门' in channel_name or '荆州' in channel_name or '随州' in channel_name or '襄阳' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1
    file.write('其他频道,#genre#\n')
    for resultx in resultxs:
        channel_name, channel_url = resultx
        if 'CCTV' not in channel_name and '卫视' not in channel_name and '湖北' not in channel_name and '武汉' not channel_name and '宜昌' not channel_name and '黄石' not channel_name and '十堰' \
              not in channel_name and '荆门' not in channel_name and '荆州' not in channel_name and '随州' not in channel_name and '襄阳' not in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] += 1
            else:
                file.write(f"{channel_name},{channel_url}\n")
                channel_counters[channel_name] = 1


# 合并自定义频道文件内容
file_contents = []
file_paths = ["CN.txt","hb.txt","itv.txt","GAT.txt","gat2.txt","sport.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)

# 写入合并后的文件
with open("iptv_list.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))

# 写入更新日期时间
    now = datetime.now()
    output.write(f"更新时间,#genre#\n")
    output.write(f"{now.strftime("%Y-%m-%d")},url\n")
    output.write(f"{now.strftime("%H:%M:%S")},url\n")

os.remove("itv.txt")
os.remove("iptv.txt")
os.remove("hb.txt")
os.remove("GAT.txt")
os.remove("DIYP-v4.txt")
os.remove("HK.txt")
os.remove("TW.txt")
os.remove("zb.txt")
os.remove("CN.txt")
os.remove("CN_temp.txt")
os.remove("CN1.txt")
os.remove("CN2.txt")
os.remove("CN3.txt")
os.remove("CN4.txt")
os.remove("CN5.txt")
os.remove("sport.txt")

def txt_to_m3u(input_file, output_file):
    # 读取txt文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 打开m3u文件并写入内容
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#EXTM3U\n')

        # 初始化genre变量
        genre = ''

        # 遍历txt文件内容
        for line in lines:
            line = line.strip()
            if "," in line:  # 防止文件里面缺失“,”号报错
                # if line:
                # 检查是否是genre行
                channel_name, channel_url = line.split(',', 1)
                if channel_url == '#genre#':
                    genre = channel_name
                    print(genre)
                else:
                    # 将频道信息写入m3u文件
                    f.write(f'#EXTINF:-1 group-title="{genre}",{channel_name}\n')
                    f.write(f'{channel_url}\n')


# 将txt文件转换为m3u文件
txt_to_m3u('iptv_list.txt', 'iptv_list.m3u')

print("任务运行完毕，分类频道列表可查看文件夹内iptv_list.txt和iptv_list.m3u文件！")
