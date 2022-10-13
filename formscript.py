from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters
import textwrap

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
oldresponses = pd.read_excel("Old_responses.xlsx")
startind = len(oldresponses)

file_obj = drive.CreateFile({'id': 'FILE_ID'}) # replace FILE_ID with file id found in url

file_obj.GetContentFile('File Name.xls',
         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') # replace file name

df = pd.read_excel('File Name.xls')


fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 20)

for index, row in df.iterrows():
    if index >= startind:
        img = Image.new('RGB', (500, 500), color = 'black')
        d = ImageDraw.Draw(img)
        text = textwrap.fill(text=row['SUBMISSION'], width=50)
        d.text(xy=(30, 40), text=text, fill=(255,255,255), font = fnt)
        img.save('filename.png')
    else:
        print("No new submissions")

olddf = df
olddf.to_excel("Old_responses.xlsx")