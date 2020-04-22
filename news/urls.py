# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:38:08 2020

@author: Vishal
"""

from django.urls import path
from news.views import scrape, news_list

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
]