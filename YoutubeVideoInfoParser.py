# This code goes to your Youtube URL's, grab title, upload date, number of views for each video
# then make Excel file with information about videos.

import random
import time

import requests as req  # need for download pages
from bs4 import BeautifulSoup  # need for grab markup from Youtube pages
import pandas as pd  # need for create Excel spreadsheet (.xlsx file)

# Add your Youtube URL's below in list_of_urls to grab information about videos:
list_of_urls = ["https://www.youtube.com/watch?v=7I6EyEonVLQ&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=1",
                "https://www.youtube.com/watch?v=D25Btx8srSU&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=2",
                "https://www.youtube.com/watch?v=ZbwqquA7rxE&list=PL66DIGaegedrOcVcDyE8zfSqKgpToMOeM&index=3"]

WAITING_TIME = 2  # set number of seconds waiting until grab next URL (to avoid Youtube blocking)


# Page parser
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


# Sequentially runs URLs from list_of_urls and writes the data to the lists
for url in list_of_urls:
    current_video_info = info_parser(url)
    print(current_video_info)  # prints the collected data

    Name_list.append(current_video_info[1])
    Views_list.append(int(current_video_info[2]))
    UploadDate_list.append(current_video_info[3])
    time.sleep(random.uniform(0, WAITING_TIME))  # set random delay to avoid Youtube blocking

# time of completed data collection
Current_time = time.strftime("%m-%d-%Y_%Hh%Mm")


# Creating an Excel spreadsheet
table_from_youtube_list = pd.DataFrame({'URL': list_of_urls,
                                        'Name': Name_list,
                                        'Views': Views_list,
                                        'UploadDate': UploadDate_list
                                        })
table_from_youtube_list.index += 1  # index in the table starts with 1 instead of 0

# creates the resulting Excel file in the project folder
table_from_youtube_list.to_excel('./' + "result_" + Current_time + '_YoutubeVideoInfo.xlsx', sheet_name=Current_time)
