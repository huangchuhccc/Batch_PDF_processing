# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:37:46 2019

@author: Administrator
"""

import os
movie_name = os.listdir('./July')
i=1
for temp in movie_name:
    new_name = '2019 Jul-' + str(i)+'.pdf'
    i=i+1
    os.rename('./July/'+temp,'./July/'+new_name)