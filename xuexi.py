import pyautogui
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def study():
    #打开浏览器
    pyautogui.click(x=153, y=48,clicks=2)
    time.sleep(10)
    #开始学习
    pyautogui.click(x=95, y=166)

def kill_browser():
    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')

sched = BlockingScheduler()
sched.add_job(study,'cron',hour=13,minute=00,jitter=1200)
sched.add_job(kill_browser,'cron',hour=14,minute=30,jitter=1200)
sched.start()