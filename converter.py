# -*- coding: utf-8 -*-
"""

Ebook to pdf file

"""
import os
import time
import pyautogui as p
from img2pdf import convert
print(p.position())

class Processor:
    def __init__(self, root, file_name, pos_icon, pos_fullsc, page):
        self.root = root
        self.file_name = file_name
        self.page = page
        self.position = pos_icon
        
        p.moveTo(pos_icon[0],pos_icon[1]) # click icon
        p.click()
        p.moveTo(pos_fullsc[0],pos_fullsc[1]) # click the full screen button
        p.click()
        p.moveTo(1900,500) # put away from the full screen button
        time.sleep(3)
    
    def capturing(self): # Capture the images
        for ii in range(self.page):
            if ii < 10:
                p.screenshot(self.root+'\\temp\\page_0000{}.jpg'.format(ii), region=(0,0,1920,1080))
            elif ii <100:
                p.screenshot(self.root+'\\temp\\page_000{}.jpg'.format(ii), region=(0,0,1920,1080))
            elif ii <1_000:
                p.screenshot(self.root+'\\temp\\page_00{}.jpg'.format(ii), region=(0,0,1920,1080))
            elif ii <10_000:
                p.screenshot(self.root+'\\temp\\page_0{}.jpg'.format(ii), region=(0,0,1920,1080))
            elif ii <100_000:
                p.screenshot(self.root+'\\temp\\page_{}.jpg'.format(ii), region=(0,0,1920,1080))
            
            p.press('right')

    def converting(self): # Convert the format jpg to pdf
        inpath = self.root + "\\temp"
        
        with open("{}.pdf".format(self.file_name), "wb") as f:
        	pdf_list = []
         
        	for file in os.listdir(inpath):
        		if file.endswith(".jpg"):
        			pdf_list.append(inpath+"\\"+file)
        
        	pdf = convert(pdf_list)
        	f.write(pdf)
        
