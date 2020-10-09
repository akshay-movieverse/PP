import requests
import io
import json
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
token = "4qmFsgLhAxIPRkV3aGF0X3RvX3dhdGNoGpIDQ0dCNnBnSkRhVGhCUVVkV2RVRkJSa3BVWjBGQ1UxVTBRVUZSUWtkU1dHUnZXVmhTWm1SSE9XWmtNa1l3V1RKblFVRlJRVUZCVVVWQ1FVRkJRVUZSUVVKQlFVRkNRVkpDU1VkTGFVYzBabUl0Y0U5M1EwMW5iMGxwVGpOaU5UazJkalZLUldoVGFXOUxTVkZ2Wm1KNlpEQk5lVEZOVlVVMGVtTlZiRlppTUVaV1ZraFdUVTVHVmtST01FWnlWRVV4TlZFeFZrTlplR2xCY21OWVFqQkROV0ZhWjNCclEyaENOV1JHT1hkWlYyUnNXRE5PZFZsWVFucGhSemt3UldnNWRrNHpVWHBNVlhoUlZHcE9lRk5XVm5aUlZsWlZaRlYzTUZaVlRUTlJWM1JOVkZoc1JGWlZTbXBIYVRoQlFVZFdkVUZCUmtwVVowRkNVMVUwUVVGUlFrZFNXR1J2V1ZoU1ptUkhPV1prTWtZd1dUSm5RVUZSUVVGQlVVVkNRVUZCUVVGUlFVSkJRVUZDUVZFJTNEkgIbGhdodHRwczovL3d3dy55b3V0dWJlLmNvbSIAmgIaYnJvd3NlLWZlZWRGRXdoYXRfdG9fd2F0Y2g%3D"

views = []
ids = []
titles = []
thumbnails = []
time = []
channel = []
description = []
pubdate = []
chimage= []
richthumb= []


pids = []
ptitles = []
pthumbnails = []
pvideocount = []
pchannel = []
ppubdate = []
pchimage= []

pdescription = []
pviews = []
ptime = []
s=requests.Session()
def scrape(token):
    x=0
    while x<1:
        
        data = {"context":{"client":{"hl":"en","gl":"IN","deviceMake":"Microsoft","deviceModel":"Edge","visitorData":"CgtCdURrdDlfbExuQSi414D8BQ%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70,gzip(gfe)","clientName":"WEB","clientVersion":"2.20201006.05.00","osName":"Windows","osVersion":"10.0","browserName":"Edge Chromium","browserVersion":"85.0.564.70","screenWidthPoints":982,"screenHeightPoints":754,"screenPixelDensity":1,"screenDensityFloat":1.25,"utcOffsetMinutes":330,"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","connectionType":"CONN_CELLULAR_4G"},"request":{"sessionId":"6881546324221994211","internalExperimentFlags":[],"consistencyTokenJars":[]},"adSignalsInfo":{"consentBumpParams":{"consentHostnameOverride":"https://www.youtube.com","urlOverride":""}},"user":{},"clientScreenNonce":"MC42MjAxNjMyNzU5MjM2OTE1","clickTracking":{"clickTrackingParams":"CBwQ8eIEIhMImPLu2Jen7AIVlPE4Bh3MogAI"}},"continuation":token}
        
        r = s.post("https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", json=data,headers=headers)

        j = r.json()

        loo = j['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']

        for l in loo:
            if True:
                if "richItemRenderer" in l.keys():
                    l = l["richItemRenderer"]["content"]
                    if 'videoRenderer' in l.keys():
                        l = l["videoRenderer"]
                        if "badges" in l.keys():  
                            ids.append(l["videoId"])
                            titles.append(l["title"]["runs"][0]["text"])
                            thumbnails.append(l["thumbnail"]["thumbnails"])
                            description.append(l["descriptionSnippet"]["runs"][0]['text'])
                            channel.append(l["longBylineText"]["runs"][0]['text'])
                            chimage.append(l["channelThumbnailSupportedRenderers"]["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"])
                            if "publishedTimeText" in l.keys():
                                pubdate.append(l["publishedTimeText"]["simpleText"])
                            else :
                                pubdate.append("Null")
                            if "shortViewCountText" in l.keys():
                                views.append(l["shortViewCountText"]["runs"][0]['text'])
                            else :
                                views.append("Null")
                            if "lenthText" in l.keys():
                                time.append(l["lengthText"]["simpleText"])
                            else:
                                time.append('Null')

                            if "richThumbnail" in l.keys():
                                richthumb.append(l["richThumbnail"]["movingThumbnailRenderer"]["movingThumbnailDetails"]["thumbnails"][0])
                            else :
                                richthumb.append("Null")
                                #print("No")

                        else:
                            ids.append(l["videoId"])
                            titles.append(l["title"]["runs"][0]["text"])
                            thumbnails.append(l["thumbnail"]["thumbnails"])
                            channel.append(l["longBylineText"]["runs"][0]['text'])
                            chimage.append(l["channelThumbnailSupportedRenderers"]["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"])
                            views.append(l["shortViewCountText"]["simpleText"])

                            if 'descriptionSnippet' in l.keys():
                                description.append(l["descriptionSnippet"]["runs"][0]['text'])
                            else:
                                description.append("Null")
                            
                            if "publishedTimeText" in l.keys():
                                pubdate.append(l["publishedTimeText"]["simpleText"])
                            else :
                                pubdate.append("Null")
                            if "lengthText" in l.keys():
                                time.append(l["lengthText"]["simpleText"])
                            else:
                                time.append('Null')

                            if "richThumbnail" in l.keys():
                                richthumb.append(l["richThumbnail"]["movingThumbnailRenderer"]["movingThumbnailDetails"]["thumbnails"][0])
                            else :
                                richthumb.append("Null")
                                #print("No")


                    elif 'radioRenderer' in l.keys():
                        l = l["radioRenderer"]
                        pids.append(l["playlistId"])
                        ptitles.append(l["title"]["simpleText"])
                        pthumbnails.append(l["thumbnail"]["thumbnails"])
                        pvideocount.append(l["videoCountText"]['runs'][0]['text'])
                        #l["videos"]["childVideoRenderer"]["title"]
                        pchannel.append(l["shortBylineText"]["runs"][0]["text"])
                        #print(l["shortBylineText"]["runs"][0]["text"])
                        if "channelThumbnailSupportedRenderers" in l.keys():
                            pchimage.append(l["channelThumbnailSupportedRenderers"]["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"])
                            #print(l["channelThumbnailSupportedRenderers"]["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"])
                        else:
                            pchimage.append("Null")
                        #print(l["playlistId"])
                        #print(l["title"]["simpleText"])
                        if "publishedTimeText" in l.keys():
                            ppubdate.append(l["publishedTimeText"]["simpleText"])
                            #print(l["publishedTimeText"]["simpleText"])
 
                        else:
                            ppubdate.append("Null")

                    else:
                        print("nEITHER_video_nor_playlist")
                        pass

                elif "continuationItemRenderer" in l.keys():
                    token=l["continuationItemRenderer"]["continuationEndpoint"]["continuationCommand"]["token"]
                    #print(token)
                else: 
                    print("End neither video nor continue")
                    #print(l)
                    #print(token) 
                    
            else:
                #token=l["continuationItemRenderer"]["continuationEndpoint"]["continuationCommand"]["token"]
                print("Try Except Block Fail")
                pass
        x=x+1



def result():
    scrape(token)
    result = []
    presult=[]
    for index in range(len(ids)):
        result_index = {
                        "index": index,
                        "id": ids[index],
                        "views": views[index],
                        "title": titles[index],
                        "thumbnails": thumbnails[index],
                        "time": time[index],
                        "channel": channel[index],
                        "pubtime": pubdate[index],
                        "description": description [index],
                        "channel_image" : chimage[index],
                        "richthumb": richthumb[index]
        }
        result+=[result_index]
        
    for index in range(len(pids)):
        resultt_index = {
                        "index": index,
                        "id": pids[index],
                        "title": ptitles[index],
                        "thumbnails": pthumbnails[index],
                        "videoCount": pvideocount[index],
                        "channel": pchannel[index],
                        "pubtime": ppubdate[index],
                        "channel_image" : pchimage[index]
        }
        presult+=[resultt_index]
    #print(json.dumps({"Single": result, "playlist" : presult } ))
    return json.dumps({"Single": result, "playlist" : presult } )
    

