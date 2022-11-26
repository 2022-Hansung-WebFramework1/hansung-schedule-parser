import json
import os
import re
from datetime import datetime

import requests
from pprint import pprint


time_dict = {
    "MON": {
        "1~2": {
            "start": datetime(2022, 1, 1, 9, 0, 0),
            "end": datetime(2022, 1, 1, 10, 15, 0)
        },
        "2~3M": {
            "start": datetime(2022, 1, 1, 9, 30, 0),
            "end": datetime(2022, 1, 1, 11, 45, 0)
        },
        "2M~3M": {
            "start": datetime(2022, 1, 1, 10, 30, 0),
            "end": datetime(2022, 1, 1, 11, 45, 0)
        },
        "4~5": {
            "start": datetime(2022, 1, 1, 12, 00, 0),
            "end": datetime(2022, 1, 1, 13, 15, 0)
        },
        "4~5M": {
            "start": datetime(2022, 1, 1, 12, 30, 0),
            "end": datetime(2022, 1, 1, 14, 00, 0)
        },
        "5M~6M": {
            "start": datetime(2022, 1, 1, 13, 30, 0),
            "end": datetime(2022, 1, 1, 14, 45, 0)
        },
        "7~8": {
            "start": datetime(2022, 1, 1, 15, 00, 0),
            "end": datetime(2022, 1, 1, 16, 15, 0)
        },
        "8~9M": {
            "start": datetime(2022, 1, 1, 16, 0, 0),
            "end": datetime(2022, 1, 1, 17, 15, 0)
        },
        "8M~9M": {
            "start": datetime(2022, 1, 1, 16, 30, 0),
            "end": datetime(2022, 1, 1, 17, 50, 0)
        },
        "9~10": {
            "start": datetime(2022, 1, 1, 17, 00, 0),
            "end": datetime(2022, 1, 1, 18, 15, 0)
        },
        "10~11": {
            "start": datetime(2022, 1, 1, 18, 00, 0),
            "end": datetime(2022, 1, 1, 19, 15, 0)
        },
        "10~11M": {
            "start": datetime(2022, 1, 1, 18, 00, 0),
            "end": datetime(2022, 1, 1, 19, 40, 0)
        },
        "10M~11M": {
            "start": datetime(2022, 1, 1, 18, 25, 0),
            "end": datetime(2022, 1, 1, 19, 40, 0)
        },
        "11M~12M": {
            "start": datetime(2022, 1, 1, 19, 0, 0),
            "end": datetime(2022, 1, 1, 20, 15, 0)
        },
        "11M~13": {
            "start": datetime(2022, 1, 1, 19, 0, 0),
            "end": datetime(2022, 1, 1, 21, 5, 0)
        },
        "12~13": {
            "start": datetime(2022, 1, 1, 19, 50, 0),
            "end": datetime(2022, 1, 1, 21, 5, 0)
        },
        "13M~14M": {
            "start": datetime(2022, 1, 1, 21, 15, 0),
            "end": datetime(2022, 1, 1, 22, 30, 0)
        },
    },
    "TUE": {
        "1~1M": {
            "start": datetime(2022, 1, 1, 9, 0, 0),
            "end": datetime(2022, 1, 1, 9, 50, 0)
        },
        "2~2M": {
            "start": datetime(2022, 1, 1, 10, 0, 0),
            "end": datetime(2022, 1, 1, 10, 50, 0)
        },
        "2~3M": {
            "start": datetime(2022, 1, 1, 10, 0, 0),
            "end": datetime(2022, 1, 1, 11, 50, 0)
        },
        "3~3M": {
            "start": datetime(2022, 1, 1, 11, 0, 0),
            "end": datetime(2022, 1, 1, 11, 50, 0)
        },
        "4~4M": {
            "start": datetime(2022, 1, 1, 12, 0, 0),
            "end": datetime(2022, 1, 1, 12, 50, 0)
        },
        "5~5M": {
            "start": datetime(2022, 1, 1, 13, 0, 0),
            "end": datetime(2022, 1, 1, 13, 50, 0)
        },
        "5~7M": {
            "start": datetime(2022, 1, 1, 13, 0, 0),
            "end": datetime(2022, 1, 1, 15, 50, 0)
        },
        "6~6M": {
            "start": datetime(2022, 1, 1, 14, 0, 0),
            "end": datetime(2022, 1, 1, 14, 50, 0)
        },
        "7~7M": {
            "start": datetime(2022, 1, 1, 15, 0, 0),
            "end": datetime(2022, 1, 1, 15, 50, 0)
        },
        "8~8M": {
            "start": datetime(2022, 1, 1, 16, 0, 0),
            "end": datetime(2022, 1, 1, 16, 50, 0)
        },
        "9~9M": {
            "start": datetime(2022, 1, 1, 17, 0, 0),
            "end": datetime(2022, 1, 1, 17, 50, 0)
        },
        "10~10M": {
            "start": datetime(2022, 1, 1, 18, 0, 0),
            "end": datetime(2022, 1, 1, 18, 50, 0)
        },
        "11~11M": {
            "start": datetime(2022, 1, 1, 18, 55, 0),
            "end": datetime(2022, 1, 1, 19, 45, 0)
        },
        "12~12M": {
            "start": datetime(2022, 1, 1, 19, 50, 0),
            "end": datetime(2022, 1, 1, 20, 40, 0)
        },
        "13~13M": {
            "start": datetime(2022, 1, 1, 20, 45, 0),
            "end": datetime(2022, 1, 1, 21, 35, 0)
        },
        "14~14M": {
            "start": datetime(2022, 1, 1, 21, 40, 0),
            "end": datetime(2022, 1, 1, 22, 30, 0)
        },
    },
    "WED": {
        "1~2": {
            "start": datetime(2022, 1, 1, 9, 0, 0),
            "end": datetime(2022, 1, 1, 10, 15, 0)
        },
        "2M~3M": {
            "start": datetime(2022, 1, 1, 10, 30, 0),
            "end": datetime(2022, 1, 1, 11, 45, 0)
        },
        "4~5": {
            "start": datetime(2022, 1, 1, 12, 00, 0),
            "end": datetime(2022, 1, 1, 13, 15, 0)
        },
        "5M~6M": {
            "start": datetime(2022, 1, 1, 13, 30, 0),
            "end": datetime(2022, 1, 1, 14, 45, 0)
        },
        "6~8M": {
            "start": datetime(2022, 1, 1, 14, 00, 0),
            "end": datetime(2022, 1, 1, 16, 50, 0)
        },
        "7~8": {
            "start": datetime(2022, 1, 1, 15, 00, 0),
            "end": datetime(2022, 1, 1, 16, 15, 0)
        },
        "8M~9M": {
            "start": datetime(2022, 1, 1, 16, 30, 0),
            "end": datetime(2022, 1, 1, 17, 45, 0)
        },
        "10~11": {
            "start": datetime(2022, 1, 1, 18, 00, 0),
            "end": datetime(2022, 1, 1, 19, 15, 0)
        },
        "11M~12M": {
            "start": datetime(2022, 1, 1, 19, 25, 0),
            "end": datetime(2022, 1, 1, 20, 40, 0)
        },
        "13~14": {
            "start": datetime(2022, 1, 1, 20, 45, 0),
            "end": datetime(2022, 1, 1, 22, 0, 0)
        },
    },
    "THU": {
        "1~2": {
            "start": datetime(2022, 1, 1, 9, 0, 0),
            "end": datetime(2022, 1, 1, 10, 15, 0)
        },
        "2M~3M": {
            "start": datetime(2022, 1, 1, 10, 30, 0),
            "end": datetime(2022, 1, 1, 11, 45, 0)
        },
        "4~5": {
            "start": datetime(2022, 1, 1, 12, 00, 0),
            "end": datetime(2022, 1, 1, 13, 15, 0)
        },
        "5M~6M": {
            "start": datetime(2022, 1, 1, 13, 30, 0),
            "end": datetime(2022, 1, 1, 14, 45, 0)
        },
        "7~8": {
            "start": datetime(2022, 1, 1, 15, 00, 0),
            "end": datetime(2022, 1, 1, 16, 15, 0)
        },
        "8M~9M": {
            "start": datetime(2022, 1, 1, 16, 30, 0),
            "end": datetime(2022, 1, 1, 17, 45, 0)
        },
        "10~11": {
            "start": datetime(2022, 1, 1, 18, 00, 0),
            "end": datetime(2022, 1, 1, 19, 15, 0)
        },
        "11M~12M": {
            "start": datetime(2022, 1, 1, 19, 25, 0),
            "end": datetime(2022, 1, 1, 20, 40, 0)
        },
        "13~14": {
            "start": datetime(2022, 1, 1, 20, 45, 0),
            "end": datetime(2022, 1, 1, 22, 0, 0)
        },
    },
    "FRI": {
        "1~1M": {
            "start": datetime(2022, 1, 1, 9, 0, 0),
            "end": datetime(2022, 1, 1, 9, 50, 0)
        },
        "2~2M": {
            "start": datetime(2022, 1, 1, 10, 0, 0),
            "end": datetime(2022, 1, 1, 10, 50, 0)
        },
        "3~3M": {
            "start": datetime(2022, 1, 1, 11, 0, 0),
            "end": datetime(2022, 1, 1, 11, 50, 0)
        },
        "4~4M": {
            "start": datetime(2022, 1, 1, 12, 0, 0),
            "end": datetime(2022, 1, 1, 12, 50, 0)
        },
        "5~5M": {
            "start": datetime(2022, 1, 1, 13, 0, 0),
            "end": datetime(2022, 1, 1, 13, 50, 0)
        },
        "5~6M": {
            "start": datetime(2022, 1, 1, 13, 0, 0),
            "end": datetime(2022, 1, 1, 14, 50, 0)
        },
        "6~6M": {
            "start": datetime(2022, 1, 1, 14, 0, 0),
            "end": datetime(2022, 1, 1, 14, 50, 0)
        },
        "7~7M": {
            "start": datetime(2022, 1, 1, 15, 0, 0),
            "end": datetime(2022, 1, 1, 15, 50, 0)
        },
        "7~8M": {
            "start": datetime(2022, 1, 1, 15, 0, 0),
            "end": datetime(2022, 1, 1, 16, 50, 0)
        },
        "8~8M": {
            "start": datetime(2022, 1, 1, 16, 0, 0),
            "end": datetime(2022, 1, 1, 16, 50, 0)
        },
        "9~9M": {
            "start": datetime(2022, 1, 1, 17, 0, 0),
            "end": datetime(2022, 1, 1, 17, 50, 0)
        },
        "10~10M": {
            "start": datetime(2022, 1, 1, 18, 0, 0),
            "end": datetime(2022, 1, 1, 18, 50, 0)
        },
        "11~11M": {
            "start": datetime(2022, 1, 1, 18, 55, 0),
            "end": datetime(2022, 1, 1, 19, 45, 0)
        },
        "12~12M": {
            "start": datetime(2022, 1, 1, 19, 50, 0),
            "end": datetime(2022, 1, 1, 20, 40, 0)
        },
        "13~13M": {
            "start": datetime(2022, 1, 1, 20, 45, 0),
            "end": datetime(2022, 1, 1, 21, 35, 0)
        },
        "14~14M": {
            "start": datetime(2022, 1, 1, 21, 40, 0),
            "end": datetime(2022, 1, 1, 22, 30, 0)
        },
    }
}

KOR_DAY_TO_ENG = {
    "월": "MON",
    "화": "TUE",
    "수": "WED",
    "목": "THU",
    "금": "FRI"
}

# 헤더 꼭 필요함
header = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,ja;q=0.5',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'info.hansung.ac.kr',
    'Referer': 'https://info.hansung.ac.kr/jsp/sugang/h_sugang_sincheong_main.jsp',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

secret_file = 'secrets.json'
with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_env_variable(var_name):
    try:
        return secrets[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        print(error_msg)


if __name__ == "__main__":
    # 아이디, 비밀번호 입력
    data = {
        'id': get_env_variable("id"),
        'passwd': get_env_variable("password"),
        'changePass': '',
        'return_url': 'null'
    }

    # 세션값 구해오기
    session = requests.Session()
    session.post("https://info.hansung.ac.kr/servlet/s_gong.gong_login_ssl", data=data)

    data = {
        "gubun": "history",
        "syearhakgi": "20222",
        "sjungong": "V024"
    }

    response = session.post("https://info.hansung.ac.kr/jsp_21/student/kyomu/siganpyo_aui_data.jsp", headers=header, data=data).text.replace("\r", "").replace("\t", "")
    response = response.split("\n")

    res = {"data": []}
    dic = {}
    index = 1
    for item in response:
        title = re.search(r'<.*?>', item)
        s = re.search(r'<!\[CDATA\[.*?\]\]>', item)
        if s:
            title = title.group()[1:-1].lstrip()
            s = s.group()[9:-3].lstrip()

            if title == "prof":
                dic[title] = list(map(lambda x: x.strip(), s.split(",")))
            elif title == "classroom":
                temp = s.split("/")
                temp = [x.lstrip().rstrip().replace("  ", " ") for x in temp]

                # 온라인강좌 있을경우
                if len(temp) >= 2:
                    dic["online"] = temp[0]

                    classroom, time = temp[1].split(" ")
                    dic["classroom"] = classroom
                    dic["day"] = time[0]

                    if len(time[1:]) <= 10:
                        dic["startTime"] = time_dict[KOR_DAY_TO_ENG[time[0]]][time[1:]]["start"].strftime("%H:%M")
                        dic["endTime"] = time_dict[KOR_DAY_TO_ENG[time[0]]][time[1:]]["end"].strftime("%H:%M")

                else:
                    classroom, time = temp[0].split(" ")
                    dic["classroom"] = classroom
                    dic["day"] = time[0]

                    if len(time[1:]) <= 10:
                        dic["startTime"] = time_dict[KOR_DAY_TO_ENG[time[0]]][time[1:]]["start"].strftime("%H:%M")
                        dic["endTime"] = time_dict[KOR_DAY_TO_ENG[time[0]]][time[1:]]["end"].strftime("%H:%M")

                dic["id"] = str(index)
                index += 1
            else:
                dic[title] = s

            if title == "kwamokgubun":
                res["data"].append(dic)
                dic = {}

    # print(json.dumps(res, indent=4, ensure_ascii=False))

    file_path = "./data.json"
    with open(file_path, 'w') as outfile:
        json.dump(res, outfile, indent=4, ensure_ascii=False)
