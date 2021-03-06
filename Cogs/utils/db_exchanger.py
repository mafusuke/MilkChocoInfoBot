import asyncio
import json
import os
import string
from os.path import dirname, join
from typing import List, Optional

import asyncpg
import traceback2
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv(verbose=True)
load_dotenv(join(dirname(__file__), '.env'))

# 36進数用の文字列
numbers = "0123456789"
alphabets = string.ascii_letters
characters = numbers + alphabets

head = {
    "0": "0",
    "1": "74",
    "2": "73",
    "3": "65",
    "4": "64",
    "5": "63",
    "6": "62",
    "7": "61",
    "8": "60",
    "9": "59",
    "10": "58",
    "11": "57",
    "12": "56",
    "13": "55",
    "14": "54",
    "15": "53",
    "16": "50",
    "17": "45",
    "18": "44",
    "19": "40",
    "20": "39",
    "21": "38",
    "22": "37",
    "23": "36",
    "24": "35",
    "25": "33",
    "26": "31",
    "27": "23",
    "28": "22",
    "29": "21",
    "30": "19",
    "31": "18",
    "32": "17",
    "33": "16",
    "34": "15",
    "35": "14",
    "36": "13",
    "37": "12",
    "38": "11",
    "39": "10",
    "40": "9",
    "41": "8",
    "42": "7",
    "43": "6",
    "44": "5",
    "45": "4",
    "46": "3",
    "47": "2",
    "48": "1",
    "49": "24",
    "50": "25",
    "51": "26",
    "52": "30",
    "53": "34",
    "54": "70",
    "55": "75",
    "56": "72",
    "57": "71",
    "58": "69",
    "59": "68",
    "60": "67",
    "61": "66",
    "62": "52",
    "63": "51",
    "64": "49",
    "65": "48",
    "66": "47",
    "67": "46",
    "68": "43",
    "69": "42",
    "70": "41",
    "71": "29",
    "72": "28",
    "73": "27",
    "74": "20",
    "75": "32"
}

body = {
    "0": "0",
    "1": "86",
    "2": "85",
    "3": "84",
    "4": "81",
    "5": "77",
    "6": "76",
    "7": "75",
    "8": "74",
    "9": "73",
    "10": "72",
    "11": "70",
    "12": "69",
    "13": "68",
    "14": "67",
    "15": "66",
    "16": "65",
    "17": "64",
    "18": "63",
    "19": "61",
    "20": "57",
    "21": "53",
    "22": "52",
    "23": "51",
    "24": "50",
    "25": "49",
    "26": "47",
    "27": "43",
    "28": "41",
    "29": "38",
    "30": "37",
    "31": "36",
    "32": "35",
    "33": "34",
    "34": "32",
    "35": "23",
    "36": "22",
    "37": "21",
    "38": "19",
    "39": "18",
    "40": "17",
    "41": "16",
    "42": "15",
    "43": "14",
    "44": "13",
    "45": "12",
    "46": "11",
    "47": "10",
    "48": "9",
    "49": "8",
    "50": "7",
    "51": "6",
    "52": "5",
    "53": "4",
    "54": "3",
    "55": "2",
    "56": "1",
    "57": "24",
    "58": "25",
    "59": "26",
    "60": "33",
    "61": "45",
    "62": "71",
    "63": "83",
    "64": "82",
    "65": "81",
    "66": "80",
    "67": "79",
    "68": "78",
    "69": "62",
    "70": "60",
    "71": "59",
    "72": "58",
    "73": "56",
    "74": "55",
    "75": "54",
    "76": "48",
    "77": "46",
    "78": "44",
    "79": "42",
    "80": "40",
    "81": "39",
    "82": "31",
    "83": "30",
    "84": "29",
    "85": "28",
    "86": "27",
    "87": "20"
}

back = {
    "0": "0",
    "1": "78",
    "2": "77",
    "3": "76",
    "4": "71",
    "5": "70",
    "6": "69",
    "7": "67",
    "8": "66",
    "9": "65",
    "10": "64",
    "11": "63",
    "12": "61",
    "13": "59",
    "14": "58",
    "15": "57",
    "16": "56",
    "17": "54",
    "18": "53",
    "19": "47",
    "20": "46",
    "21": "44",
    "22": "43",
    "23": "41",
    "24": "40",
    "25": "35",
    "26": "34",
    "27": "32",
    "28": "24",
    "29": "23",
    "30": "22",
    "31": "19",
    "32": "18",
    "33": "17",
    "34": "16",
    "35": "15",
    "36": "14",
    "37": "13",
    "38": "12",
    "39": "11",
    "40": "10",
    "41": "9",
    "42": "8",
    "43": "7",
    "44": "6",
    "45": "5",
    "46": "4",
    "47": "3",
    "48": "2",
    "49": "1",
    "50": "25",
    "51": "26",
    "52": "27",
    "53": "33",
    "54": "38",
    "55": "49",
    "56": "68",
    "57": "75",
    "58": "74",
    "59": "73",
    "60": "72",
    "61": "62",
    "62": "60",
    "63": "55",
    "64": "52",
    "65": "51",
    "66": "50",
    "67": "48",
    "68": "45",
    "69": "42",
    "70": "39",
    "71": "37",
    "72": "36",
    "73": "31",
    "74": "30",
    "75": "29",
    "76": "28",
    "77": "24",
    "78": "21",
    "79": "20"
}


def code_to_list(code36: str) -> Optional[List[int]]:
    """装飾コードを番号リストに変換"""
    try:
        code10 = int(code36, base=36)  # 36進数->10進数に変換
    except:
        return None
    item = str(code10).zfill(14)  # 14桁になるよう0埋め
    return [int(item[0:1]), int(item[1:3]), int(item[3:5]), int(item[5:8]), int(item[8:11]), int(item[11:14])]


def list_to_code(item: list) -> str:
    """番号リストを装飾コードに変換"""
    code = f"{item[0]}{str(item[1]).zfill(2)}{str(item[2]).zfill(2)}{str(item[3]).zfill(3)}{str(item[4]).zfill(3)}{str(item[5]).zfill(3)}"
    return parse_to_36(int(code))


def parse_to_36(tmp: int):
    """10進数->36進数に変換"""
    result = ''
    while tmp >= 36:
        idx = tmp % 36
        result = characters[idx] + result
        tmp = int(tmp / 36)
    idx = tmp % 36
    return characters[idx] + result


def update_code(code: str):
    """旧形式の装飾コードを新形式に変換"""
    item = old_ctl(code)
    # 各番号変換
    item[3] = int(head[str(item[3])])
    item[4] = int(body[str(item[4])])
    item[5] = int(back[str(item[5])])
    code = list_to_code(item)
    return code


def old_ctl(item: str) -> list:
    """古い形式のデータ変換"""
    result = int(item, 36)  # 36進数から10進数に変換
    item = str(result).zfill(11)  # 11桁になるように0埋めする
    return [int(item[0:1]), int(item[1:3]), int(item[3:5]), int(item[5:7]), int(item[7:9]), int(item[9:11])]


async def notify():
    # NOTIFY
    """
m!exe ```py
d = bot.GM_update
p = {}
for i in d:
  for a in d[i]:
    c = bot.get_channel(a)
    if c is None:
      continue
    if c.guild.id not in p:
        p[c.guild.id] = {"twitter":None, "facebook_jp":None, "facebook_en":None, "facebook_kr":None, "facebook_es":None, "youtube":None}
    p[c.guild.id][i] = c.id
import json
with open("./dump.json", "a") as f:
    json.dump(p, f)
```
    """
    database: dict
    with open("./dump.json") as f:
        database = json.load(f)
    con = await asyncpg.connect(os.getenv("DB_URL"))
    for guild in tqdm(database):
        g_data = database[guild]
        tw = int(g_data["twitter"]) if g_data["twitter"] is not None else None
        fbjp = int(g_data["facebook_jp"]) if g_data["facebook_jp"] is not None else None
        fben = int(g_data["facebook_en"]) if g_data["facebook_en"] is not None else None
        fbkr = int(g_data["facebook_kr"]) if g_data["facebook_kr"] is not None else None
        fbes = int(g_data["facebook_es"]) if g_data["facebook_es"] is not None else None
        yt = int(g_data["youtube"]) if g_data["youtube"] is not None else None
        await con.execute("INSERT INTO notify VALUES($1, $2, $3, $4, $5, $6, $7)", int(guild), tw, fbjp, fben, fbkr, fbes, yt)


async def user():
    # USER
    database: dict
    with open("./dump.json") as f:
        database = json.load(f)
    """
m!exe ```py
import json
with open("./dump.json", "a") as f:
    json.dump(bot.database, f)
```
    """
    con = await asyncpg.connect(os.getenv("DB_URL"))
    for user_id in tqdm(database):
        user = database[user_id]
        canvas = None
        save = None
        user_lang = user["language"] if "language" in user else 0
        if "costume" in user:
            canvas = update_code(user["costume"]["canvas"])
            save = user["costume"]["save"]
            for index, data in enumerate(save):
                code = update_code(data["data"])
                data["code"] = code
                save[index] = data
            await con.execute("INSERT INTO user_data VALUES($1, $2, $3, $4)", int(user_id), user_lang, canvas, json.dumps(save))
        else:
            await con.execute("INSERT INTO user_data VALUES($1, $2)", int(user_id), user_lang)


if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        print("1 ... Notify\n2 ... User")
        num = input()
        if num == "1":
            loop.run_until_complete(notify())
        elif num == "2":
            loop.run_until_complete(user())
        loop.close()
    except RuntimeError:
        pass
    except:
        print(traceback2.format_exc())
