import json
import os
import re
import requests
from pprint import pprint

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

    res = []
    dic = {}
    for item in response:
        title = re.search(r'<.*?>', item)
        s = re.search(r'<!\[CDATA\[.*?\]\]>', item)
        if s:
            title = title.group()[1:-1].lstrip()
            s = s.group()[9:-3].lstrip()

            if title == "prof":
                dic[title] = list(map(lambda x: x.strip(), s.split(",")))
            else:
                dic[title] = s

            if title == "kwamokgubun":
                res.append(dic)
                dic = {}
    pprint(res)
