import time
import os
import re
import base64
import datetime
import requests
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


# 扫源湖北IPTV

# 线程安全的队列，用于存储下载任务
task_queue = Queue()

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
# with open("hb.txt", 'w', encoding='utf-8') as file:
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

with open("hb.txt", 'w', encoding='utf-8') as file:
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
        if 'CCTV' not in channel_name and '卫视' not in channel_name and '湖北' not in channel_name and '武汉' not in channel_name and '宜昌' not in channel_name and '黄石' not in channel_name and '十堰' \
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
file_paths = ["CN.txt","hb.txt","GAT.txt","gat2.txt","sport.txt"]  # 替换为实际的文件路径列表
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
