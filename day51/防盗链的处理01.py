import requests

#拿到contId
#拿到视频的videoStatus的json->srcURL
#srcURL里面的内容进行修复
#下载视频
url='https://www.pearvideo.com/video_1799616'
contId=url.split('_')[1]

headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#refer防盗链  溯源，本次的请求是上一级的谁
'referer': url
}
videoStatusUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.638663787890395"
resp=requests.get(videoStatusUrl,headers=headers)
dic=resp.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
real='https://video.pearvideo.com/mp4/short/20250421/cont-1799616-16050084-hd.mp4'
#     https://video.pearvideo.com/mp4/short/20250421/1745411177877-16050084-hd.mp4