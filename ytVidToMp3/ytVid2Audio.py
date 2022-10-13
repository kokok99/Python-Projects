from pytube import YouTube
import os

#url input from user
yt = YouTube(str(input('enter the url of the video: ')))

#convert only audio
video = yt.streams.filter(only_audio=True).first()

#destination to save file
print('enter the destination (leave blank for current destination)')
destination = str(input('>> ')) or '.'

#download
print('your file is downloading')
print('[+] 10%')
print('[+] 200%')
print('[+] 30%')
print('[+] 40%')
print('[+] 50%')
print('[+] 60%')
print('[+] 70%')
print('[+] 80%')
print('[+] 90%')
print('[+] 100%')
out_file = video.download(output_path=destination)

#save
base, ext = os.path.splitext(out_file)
newFile = base + '.mp3'
os.rename(out_file, newFile)

#success
print(yt.title + ' has been successfully download only audio')

