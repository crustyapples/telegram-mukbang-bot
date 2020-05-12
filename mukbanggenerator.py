from __future__ import unicode_literals
from selenium import webdriver
##from pytube import YouTube
##import moviepy.editor as mp
import os
##import re

browser = webdriver.Chrome()
def getMukbangURL(ingredient):
    url = f'https://www.youtube.com/results?search_query=no+talking+mukbang+{ingredient}'
    browser.get(url)
    firstMukbang = browser.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
    firstMukbang.click()
    MukbangURL = browser.current_url
    return MukbangURL

# def outputMP3():
#     target_folder = os.getcwd()
#     y = YouTube(getMukbangURL())
#     t = y.streams.filter(only_audio=True).all()
#     t[0].download(output_path=target_folder)

#     for file in [n for n in os.listdir(target_folder) if re.search('mp4',n)]:
#         full_path = os.path.join(target_folder, file)
#         output_path = os.path.join(target_folder, os.path.splitext(file)[0] + '.mp3')
#         clip = mp.AudioFileClip(full_path).subclip(10,) # disable if do not want any clipping
#         clip.write_audiofile(output_path)

def outputURL(URL):
    browser.get("https://ytmp3.cc/en13/")
    convertedInput = browser.find_element_by_xpath('//*[@id="input"]')
    convertedInput.send_keys(URL)
    convertButton = browser.find_element_by_xpath('//*[@id="submit"]')
    convertButton.click()

    while True:
        try:
            downloadURL = browser.find_element_by_link_text('Download') 
        except:
            continue
        else:
            print(downloadURL.get_attribute("href"))
            return downloadURL.get_attribute("href")
            break


