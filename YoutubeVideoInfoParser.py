# This code goes to your Youtube URL's, grab title, upload date, number of views for each video
# then make Excel file with information about videos.

import random
import time

import pandas as pd
import requests as req
from bs4 import BeautifulSoup

# Add your Youtube URL's in list_of_urls to grab information from it
# Добавь сюда урлы, с которых хочешь собрать информацию:
list_of_urls = ["https://www.youtube.com/watch?v=7I6EyEonVLQ&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=1",
                "https://www.youtube.com/watch?v=D25Btx8srSU&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=2",
                "https://www.youtube.com/watch?v=ZbwqquA7rxE&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=3",
                "https://www.youtube.com/watch?v=E9tSWNPZV6E&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=4",
                "https://www.youtube.com/watch?v=CJbXKYcf7SA&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=5",
                "https://www.youtube.com/watch?v=jxZZldnG7pU&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=6",
                "https://www.youtube.com/watch?v=PV7z6QEbF2k&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=7",
                "https://www.youtube.com/watch?v=q6byv4iGq2Y&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=8",
                "https://www.youtube.com/watch?v=sNzP3yVF8_A&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=9",
                "https://www.youtube.com/watch?v=ng1f3W_WL2s&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=10"]


# Парсер одной страницы
def info_parser(url_):
    resp = req.get(url_)
    soup = BeautifulSoup(resp.text, 'lxml')

    name_ = soup.find(itemprop="name").get("content")
    views_ = soup.find(itemprop="interactionCount").get("content")
    upload_date_ = soup.find(itemprop="uploadDate").get("content")

    return url_, name_, views_, upload_date_


Name_list = []
Views_list = []
UploadDate_list = []


# Последовательно парсит все урлы из списка list_of_urls и формирует будущие колонки с данными
for i in list_of_urls:
    current_video_info = info_parser(i)
    print(current_video_info)  # проверка работает ли парсер

    Name_list.append(current_video_info[1])
    Views_list.append(int(current_video_info[2]))
    UploadDate_list.append(current_video_info[3])
    time.sleep(random.uniform(0, 2))  # рандомная задержка между обходом страниц, чтобы ютьюб не забанил

Current_time = time.strftime("%m-%d-%Y_%Hh%Mmin")  # время завершения сбора данных

# Формирует Excel-файл с данными в виде таблицы
table_from_youtube_list = pd.DataFrame({'URL': list_of_urls,
                                        'Name': Name_list,
                                        'Views': Views_list,
                                        'UploadDate': UploadDate_list
                                        })
table_from_youtube_list.index += 1  # индекс в таблице начинается с 1 вместо 0

# создает файл Excel в папке проекта с указанием даты обхода парсером в имени файла:
table_from_youtube_list.to_excel('./' + Current_time + '_YoutubeVideoInfo.xlsx', sheet_name=Current_time)