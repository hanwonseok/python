from asyncio.windows_events import NULL
from cmath import e
import time
import logging

import win32con, win32api, win32gui, ctypes
#win32 모듈 설치필요 -> pip install pypiwin32
import requests
#requests 모듈 설치필요 -> pip install requests
from bs4 import BeautifulSoup
#BeautifulSoup 모듈 설치필요 -> pip install beautifulsoup4
from apscheduler.schedulers.background import BackgroundScheduler
#BackgroundScheduler 모듈 설치필요 -> pip install apscheduler
from pywinauto import clipboard # 채팅창내용 가져오기 위해
#clipboard 모듈 설치 필요 -> pip install pywinauto
import pandas as pd # 가져온 채팅내용 DF로 쓸거라서
#pandas 모듈 설치 필요 -> pip install pandas

