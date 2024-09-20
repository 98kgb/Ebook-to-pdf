# -*- coding: utf-8 -*-
"""

This file is main part.

Define your file pages, E-reader posistion.

And convert your e reader file to pdf:)

"""
import sys
from converter import Processor

root = "C:\\Users\\a\\Desktop\\Ebook"
page = 400
pos_icon = [1231,1058]
pos_fullsc = [1489,247]
file_name = "test"

process = Processor(root, file_name, pos_icon, pos_fullsc, page)
process.capturing()
process.converting()
