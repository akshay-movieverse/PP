
import requests

data={'link':'suzu'}
r = requests.post("http://127.0.0.1:5000/api2/",json={'link':'https://www.youtube.com/watch?v=IKOke_QKR0w'})
#
print(r.json())
'''
import pytube
from pytube import YouTube

link='https://www.youtube.com/watch?v=GLk7-imcjiI'
video = YouTube(link)
#print(video.streams[0].url)
#print(video.extract.get_ytplayer_config)

import pafy


link='https://www.youtube.com/watch?v=GLk7-imcjiI'
v = pafy.new(link)

#best = video.streams
data={'link_360': 0 , 'link_480':0 ,   'link_720': 0, 'link_1080': 0 ,'link_m4a': 0}
#print(best[])
#for s in streams:
#    print(s.resolution, s.extension, s.get_filesize(), s.url)

for s in v.allstreams:

    if ('x360' in s.resolution):
        data['link_360']=s.url
    elif ('x480' in s.resolution):

        data['link_480']=s.url
    elif ('x720' in s.resolution):

        data['link_720']=s.url
    elif ('x1080' in s.resolution):

        data['link_1080']=s.url
    elif ('m4a' in s.extension):
        data['link_m4a']=s.url

    else:
        pass

#for s in v.m4astreams:
#best = video.allstreams
#print(best('audio'))
#print(best[-6].url)
print(data) '''