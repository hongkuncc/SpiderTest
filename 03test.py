# -*- coding: utf-8 -*-
import requests
import time

def push_it(message):
    api = 'https://api.pushover.net/1/messages.json/'
    data = {
        'app_token':'abcdefg'
        'user':'abcdefg',
        'message':message
    }
    requests.post(api,data)

def get_project(last_week,topic):
    api = 'https://api.github.com/search/repositories?q='
    query_created = 'created:>'+last_week
    