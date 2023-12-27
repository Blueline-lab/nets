import requests
import time
import os

NB_PING = 10


def dl_speed(url):
    begin = time.time()
    file = requests.get(url, stream=True)
    file_size = file.headers.get('content-length')
    timing = (time.time() - begin) %60
    download_speed = int(file_size) / timing
    return download_speed


url = "https://immatriculation.ants.gouv.fr/files/1e4341b6-4695-4f74-a51a-5ef962fba392/ef4ec059-07a7-4cc7-804f-e16944afeb5e/7c2580e6-f917-4ae1-9097-192377fd7cef/notice_51291#02.pdf"
speed = dl_speed(url)
print("Download Speed: ", speed / 100000)




