from email import header
from selenium import webdriver
from selenium.webdriver.common.by import By
from numpy import NaN, outer
from datetime import datetime
import requests
import json
import pandas as pd
import time
from tqdm import tqdm
import multiprocessing
import pymysql
from sqlalchemy import create_engine 

#계정이름을 담을 리스트
user_name_list = []
keyword_list = []

#계정 정보를 담을 리스트
raw_info_list = []

processed_info_list = []

#피쳐링에서 분석되지 않은 계정이름을 담을 리스트
#not_analized_users = []

class Featuring:
    def __init__(self):
        self.headers = {}
        self.cookies = {}

        self.sess = None

    #selenium으로 로그인
    def login(self, username, password):
        link = "https://featuring.co/accounts/login/"
        my_driver = ""

        #options = webdriver.ChromeOptions()
        #options.add_argument("headless")
        
        driver = webdriver.Chrome(my_driver)
        driver.get(link)
        self.sess = requests.session()

        featuring_id_form = driver.find_element(By.NAME, 'login')
        featuring_id_form.send_keys(username)
        featuring_pw_form = driver.find_element(By.NAME, 'password')
        featuring_pw_form.send_keys(password)
        time.sleep(3)
        print("Wait..")

        login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/p[4]/button')
        login_btn.click()
        time.sleep(3)

        _cookies = driver.get_cookies()
        cookie_dict = {}
        for cookie in _cookies:
            cookie_dict[cookie ['name']] = cookie['value']

        header = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        self.sess.headers.update(header)
        self.sess.cookies.update(cookie_dict)
        
        
        #self.sess.headers.update(cookie_dict)
        #print(self.sess.cookies)
        #print(self.sess.headers)

    #키워드로 검색 후 해당 키워드에 있는 계정 수를 반환
    def get_list_size(self, keyword):
        print("initiating..")
        
        url = "https://featuring.co/report/search/api/?q=" + keyword + "&page=0"

        r = self.sess.get(url)

        return r.json()["list_size"]
    
    #계정 정보 반환
    def get_user_names(self, list_size , keyword):
        #한 페이지당 5개의 계정정보 
        if list_size % 5 == 0:
            page_num = int(list_size / 5)
        else:
            page_num = int(list_size / 5) + 1
       
        #print(list_size % 5)
        #print(page_num)

        for i in tqdm(range(page_num), desc="getting usernames"):
            url = "https://featuring.co/report/search/api/?q=" + keyword + "&page=" + str(i)

            r = self.sess.get(url)

            json_list = r.json()["list"]
            
            for user in json_list:
                try:
                    json_username = user["userinfo"]["username"]
                    user_name_list.append(json_username)
                    keyword_list.append(keyword)
                #유튜브 계정일시 발생하는 키에러 제외
                except KeyError:
                    pass

                #print(user)
            
            #print(i)

    #계정 이름 검색
    def get_user_info(self):
        
        #for k in range(10):
        #    user = user_name_list[k]
        for user in tqdm(user_name_list, desc="getting user info"):
            try:
                raw_info = []
                processed_info = []

                #피쳐링에서 각각의 정보가 서로 다른 url에서 나타나기 때문에 각각의 url에 대해 json 불러오기
                audience_url = "https://featuring.co/report/eg/" + user + "/audience_quality?is_engine_request=true"
                fearuting_score_url = "https://featuring.co/report/eg/" + user + "/featuring_score?is_engine_request=true"
                real_engagement_url = "https://featuring.co/report/eg/" + user + "/real_engagement?is_engine_request=true"
                real_influence_url = "https://featuring.co/report/eg/" + user + "/real_influence?is_engine_request=true"
                real_reach_url = "https://featuring.co/report/eg/" + user + "/real_reach?is_engine_request=true"

                audience_r = self.sess.get(audience_url)
                featscore_r = self.sess.get(fearuting_score_url)
                realeng_r = self.sess.get(real_engagement_url)
                realinf_r = self.sess.get(real_influence_url)
                realreach_r = self.sess.get(real_reach_url)

                json_audience_qual = audience_r.json()["real_audience_count"]
                json_featuring_score = featscore_r.json()["featuring_score"]
                json_real_comment = realeng_r.json()["avg_engagement_comment_rate"]
                json_real_like = realeng_r.json()["avg_engagement_like_rate"]
                json_real_influence = realinf_r.json()["real_influence"]
                json_real_reach = realreach_r.json()["reach_quality_follower_count"]
                json_follower = realreach_r.json()["json_parameter"]["follower_count"]
                json_avg_like = realreach_r.json()["json_parameter"]["avg_like_count"]

                processed_info.append(json_audience_qual)
                processed_info.append(json_featuring_score)
                processed_info.append(json_real_comment)
                processed_info.append(json_real_like)
                processed_info.append(json_real_influence)
                processed_info.append(json_real_reach)
                raw_info.append(json_follower)
                raw_info.append(json_avg_like)

                raw_info_list.append(raw_info)
                processed_info_list.append(processed_info)
                #print(user_info)
            except json.JSONDecodeError:
                for i in range(6):
                    processed_info.append(NaN)
                for j in range(2):
                    raw_info.append(NaN)
                
                raw_info_list.append(raw_info)
                processed_info_list.append(processed_info)
                pass

            #print(user_info)
        
        #print(not_analized_users)





username = "roboholic84@gmail.com"
password = "mecha@1234"

featuring = Featuring()
featuring.login(username, password)

while(True):
    user_name_list = []
    keyword_list = []
    raw_info_list = []
    processed_info_list = []

    keyword = input("Enter Keyword: ")

    if keyword == "quit":
        break

    list_size = featuring.get_list_size(keyword)

    featuring.get_user_names(list_size, keyword)
    #print(user_name_list)

    featuring.get_user_info()
    #print(user_info_list)

    _column_user = ['Username']
    df_user = pd.DataFrame(user_name_list, columns=_column_user)
    df_user.insert(0, "Keyword", keyword_list, True)
    print(df_user)

    _column_raw = ['Followers', 'Avg_Likes']
    df_raw = pd.DataFrame(raw_info_list, columns = _column_raw)
    print(df_raw)

    _column_processed = ['Audience_Quality', 'Featuring_Score', 'Real_Comment_Rate', 'Real_Like_Rate', 'Real_Influence', 'Real_Reach']
    df_processed = pd.DataFrame(processed_info_list, columns= _column_processed)
    print(df_processed)


    print(len(user_name_list))
    print(len(raw_info_list))

        #test_list = user_name_list[0:10]
        #df.insert(0, "username", test_list, True)
        #df.insert(0, "username", user_name_list, True)
        #print(df)

    df_user.dropna(inplace=True)

    engine = create_engine("")

    conn = engine.connect()

    #cursor = conn.cursor()

        #db.commit()

    df_user.to_sql(name='Keyword', con=conn, if_exists='append',index=False)

    print("Added to database.")

        #db.commit()
        #db.close()



'''while(True):
    user_name_list = []
    user_info_list = []

    keyword = input("Enter Keyword: ")

    if keyword == "quit":
        break

    list_size = featuring.get_list_size(keyword)

    featuring.get_user_names(list_size, keyword)
    #print(user_name_list)

    featuring.get_user_info()
    #print(user_info_list)

    _column = ['Audience_Quality', 'Featuring_Score', 'Real_Comment_Rate', 'Real_Like_Rate', 'Real_Influence', 'Real_Reach', 'Followers', 'Avg_Likes']
    df1 = pd.DataFrame(user_info_list, columns = _column)

    print(len(user_name_list))
    print(len(user_info_list))

    #test_list = user_name_list[0:10]
    #df.insert(0, "username", test_list, True)
    df1.insert(0, "username", user_name_list, True)
    print(df)

    df1.dropna(inplace=True)

    engine = create_engine("mysql+pymysql://admin:")

    conn = engine.connect()

    #cursor = conn.cursor()

    #db.commit()

    df.to_sql(name='featuring', con=conn, if_exists='append',index=False)

    print("Added to database.")

    #db.commit()
    #db.close()'''
