# -*- coding: utf-8 -*-
"""
Ebook to pdf file
"""
import os
import time
import pyautogui as p
from img2pdf import convert
print(p.position())


#%% Capture the images
root = "C:\\Users\\a\\Desktop\\Ebook"
p.moveTo(1231,1058)
p.click()
p.moveTo(1489,247)
p.click()
p.moveTo(1919,500)
time.sleep(3)

for ii in range(195):
    if ii < 10:
        p.screenshot(root+'\\temp\\page_00{}.jpg'.format(ii), region=(0,0,1920,1080))
    elif ii <100:
        p.screenshot(root+'\\temp\\page_0{}.jpg'.format(ii), region=(0,0,1920,1080))
    elif ii <1000:
        p.screenshot(root+'\\temp\\page_{}.jpg'.format(ii), region=(0,0,1920,1080))
    
    p.press('right')

#%% Convert to pdf
inpath = root + "\\temp"

with open("out.pdf", "wb") as f:
	pdf_list = []

	for file in os.listdir(inpath):
		if file.endswith(".jpg"):
			pdf_list.append(inpath+"\\"+file)

	pdf = convert(pdf_list)
	f.write(pdf)

