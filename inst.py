from numpy import outer
import requests
from datetime import datetime
import json
import pandas as pd
import time
from tqdm import tqdm
import re
from sqlalchemy import create_engine
import os

#load_dotenv()


# searching_tag_list = ["#골프웨어", "#캠핑", "#요리", "#화장품", "#공구", "#광고", "#협찬", "#골프", "#뷰티", "#육아", "#맛집", "#육아", "#요리", "#데일리룩", "#ootd", "#운동", "#직장인", "#다이어트", "#테니스", "#라이딩", "#댕댕이", "#화장품", "#산책", "#발색", "#카페", "#분위기", "#일상", "#오늘", "#여친", "#남친", "#커플", "#데이트", "#가족", "#먹방", "#서울", "#호캉스", "#아이폰", "#차박", "#자동차", "#호텔", "#책", "#영화", "#주방"]
# searching_tag_list = ["여행", "캠핑", "골프", "음식"]
# searching_tag_list = ["헬스", "오운완", "하체", "운동", "PT", "헬스화", "헬스용품", "프로틴", "단백질보충제"]
# searching_tag_list = ["패션", "패션용품", "ootd", "비니", "모자", "후드티", "후디", "맨투맨", "코트", "청바지", "데님", "자켓", "패딩", "경량패딩", "패션아이템", "패션스타그램"]
# searching_tag_list = ["낚시", "낚시용품", "배낚시"]

#searching_tag_list = ["캠핑", "캠핑용품", "캠핑요리", "캠핑꿀템", "캠핑아이템", "캠핑협찬", "캠핑의류"]
# searching_tag_list = ["공스타", "공부", "순공", "필기구", "필기구추천", "공스타", "공스타그램"]
#searching_tag_list = ["골프", "골프용품", "골프추천", "골프추천용품", "골프의류", "골프웨어", "골프장", "캐디", "골프", "버디", "이븐", "홀인원", "골프채", "골프공"]

# 초기 검색 해시태그
searching_tag_list = ["#캠핑", "#캠핑용품"]#, "#골프", "#골프웨어", "#조명", "#실내조명"]

# 초기 검색 해시태그로부터 얻는 추천 해시태그
recommend_tag_list = []  # "캠핑", "골프", "요리", "뷰티", "육아", "맛집", "육아", "요리", "데일리룩", "ootd", "운동", "직장인", "다이어트", "테니스", "라이딩", "댕댕이", "화장품", "산책", "발색", "카페", "분위기", "일상", "오늘", "여친", "남친", "커플", "데이트", "가족", "먹방", "서울", "호캉스", "아이폰", "차박", "자동차", "호텔", "책", "영화", "주방"]

# 계정명
account_tag_list  = []
account_list = []
insert_account_list = []
# 계정정보
account_info_list = []

'''engine = create_engine(f"mysql+pymysql://{os.getenv('dbus')}:{os.getenv('dbpw')}@{os.getenv('dbip')}/{os.getenv('dbnm')}")

conn = engine.connect()

raw_info = pd.read_sql("SELECT * FROM RawInfo;",conn)
id_list = raw_info['Username'].to_list()
print(id_list)'''


# 인스타그램의 API는 로그인 정보가 필요하므로
# 먼저 로그인을 진행한 후 사용
class Instagram:
    def __init__(self):  # 로그인 실행 시 값들이 채워짐
        self.csrf_token = ""
        self.session_id = ""
        self.headers = {}
        self.cookies = {}

        self.sess = None  # 로그인 유지를 위해 requests의 session 클래스를 사용

    def login(self, username, password):  # 인스타그램 로그인
        link = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
        login_url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

        self.sess = requests.session()

        time = int(datetime.now().timestamp())
        response = self.sess.get(link) #로그인 링크에 대한 세션을 반환
        csrf = response.cookies['csrftoken']

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        self.headers = {#로그인시 전송해야할 헤더값들을 설정
            # "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            # 특정 User-Agent를 사용하지 않으면 에러를 반환
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        } 

        login_response = self.sess.post(login_url, data=payload, headers=self.headers) #로그인 api에 parameter들을 post
        json_data = json.loads(login_response.text)

        print(login_response.status_code, login_response.text)

        # 토큰 등 로그인 정보를 받아온 후 cookies 변수에 저장
        if json_data["authenticated"]:
            self.cookies = login_response.cookies
        else:
            print("login failed ", login_response.text)

    def get_search_data_tag_name(self, tag_name):  # 해쉬태그를 검색하여 나오는 게시물 정보
        url = "https://i.instagram.com/api/v1/tags/web_info"

        r = self.sess.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            params={
                "tag_name": tag_name
            }
        )

        return r.json()["data"]  # ["top"]["sections"]

    def get_top_search_tag(self, tag_name):  # 인스타그램 검색창에 입력 시 실행되는 api, 추천 검색어를 반환함
        url = "https://www.instagram.com/web/search/topsearch/"

        r = self.sess.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            params={
                "context": "blended",
                "query": tag_name,
                "include_reel": "true"
            }
        )

        return r.json()["hashtags"]

    def get_user_info(self, user_id):  # 단일 계정에 대한 팔로워 수를 반환
        url = "https://i.instagram.com/api/v1/users/web_profile_info"

        r = self.sess.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            params={
                "username": user_id
            }
        )

        return r.json()["data"]

    def get_comment(self, medium_id):
        url = "https://i.instagram.com/api/v1/media/" + medium_id + "/comments"

        r = self.sess.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            params={
                "can_support_threading": "true",
                "permalink_enabled": "false"
            }
        )
        return r.json()["comments"]



## id, pw를 입력해주세요.
username = 
password = 



instagram = Instagram()
instagram.login(username, password)


# 초기 검색 해시태그 리스트로 추천 해시태그 리스트 생성

print(searching_tag_list)

try:
    for searching_tag in searching_tag_list:
        time.sleep(10)
        recommend_tag_list.append(searching_tag)
        tags = instagram.get_top_search_tag(searching_tag)  
        for tag in tags:
            this_tag = tag["hashtag"]["name"]
            recommend_tag_list.append(this_tag)

except:
    pass

print(recommend_tag_list)

# 추천 해시태그 리스트로 계정명 리스트 생성

for recommend_tag in tqdm(recommend_tag_list, desc="getting usernames"):
    try:
        time.sleep(20)
        outer_hashtag_id = instagram.get_search_data_tag_name(recommend_tag)
        dig_outer = outer_hashtag_id["top"]["sections"]
        print(recommend_tag)

        for row in dig_outer:  # outer_hashtag_id:
            inner_hashtag_id = row["layout_content"]["medias"]
            for point in inner_hashtag_id:
                point_id = point["media"]["user"]["username"]
                account_tag_list.append(recommend_tag)
                account_list.append(point_id)
    except:
        pass


print(account_list)

# 계정명 리스트로 계정정보 리스트 생성
for account in tqdm(account_list, desc="getting userinfo"):
    try:
        time.sleep(30)
        individual_info_list = []
        account_info = instagram.get_user_info(account) # 유저 페이지에 대한 url

        bio = account_info["user"]["biography"]
        followers = account_info["user"]["edge_followed_by"]["count"]
        following = account_info["user"]["edge_follow"]["count"]

        temp = re.compile('[A-Za-z0-9가-힣#]+').findall(bio)
        bios = ' '.join(temp)
        print("bios: "+bios)

        individual_info_list.append(bios)
        individual_info_list.append(followers)
        individual_info_list.append(following)

        like = 0
        comment_size = 0
        mediatext = ""
        media_id = []
        commenttext = ""
        timestamp_list = []

        media_list = account_info["user"]["edge_owner_to_timeline_media"]["edges"] # 유저 페이지 url 내에서 json 요청 및 반환
        media_length = len(media_list)
        for medium in media_list: # 유저 페이지 내에서 루프 도는 중

            media_text_list = medium["node"]["edge_media_to_caption"]["edges"]
            for text in media_text_list:
                mediatext += text["node"]["text"]
                
            like += medium["node"]["edge_liked_by"]["count"]
            comment_size += medium["node"]["edge_media_to_comment"]["count"]
            timestamp_list.append(medium["node"]["taken_at_timestamp"])
            media_id.append(medium["node"]["id"])

# ccc
        for medium_id in media_id:
            comments = instagram.get_comment(medium_id)  # 첫번째 게시글 url로 이동 > 반복문 실행 오류 발생

            for comment in comments:
                commenttext += comment["text"]

        avg_like = like / media_length
        avg_comment = comment_size / media_length

        print("check: " + mediatext)
        media_text = ' '.join(re.compile('[#-.가-힣A-Za-z0-9ㄱ-ㅣ]+').findall(mediatext))
        print("media text: " + media_text)
        
        individual_info_list.append(media_text)
        individual_info_list.append(avg_like)
        individual_info_list.append(avg_comment)

        er_rate = (avg_like + avg_comment) / followers
        individual_info_list.append(er_rate)
        individual_info_list.append(tuple(timestamp_list))

        print(individual_info_list)
        account_info_list.append(individual_info_list)
        insert_account_list.append(account)
    except:
        pass

column = ['소개글', '팔로잉', '팔로워', '게시글 본문', '평균 좋아요', '평균 댓글수', 'ER 지수', '타임스탬프']
df = pd.DataFrame(account_info_list, columns=column)
print(account_tag_list)
print(insert_account_list)
#df.insert(0, "검색태그", account_tag_list, True)
df.insert(0, "account_id", insert_account_list, True)
df.drop_duplicates(ignore_index=True, inplace=True)
print(df)

df.to_excel("filename.xlsx")

