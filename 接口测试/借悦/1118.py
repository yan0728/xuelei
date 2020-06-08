#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: 1118.py
@time:2020/1/15 0015
"""
import requests
import json
def api1118_link():
    hj = 'http://loan-api-link.asset.jc3.jieyue.com'
    url = '/loan-api-link/api/appbiz/LoanEasyRest/1118/v1'
    header = {"Content-Type": "application/json"}

    url_params = json.dumps(
        {
            "sysSource":"4",
            "frontTransNo":"20200115154808552",
            "frontTransTime":"2019-07-18 15:15:20",
            "interfaceNo":"1118",
            "busiCode":"CSB18",
            "telephone":"13916250606",
            "appAmount":"30000",
            "appPeriod":"24",
            "custmerManger":"11037385",
            "position":"301000817",
            "telemarketing":"0"
        }
    )

    url_1118 = requests.post(hj+url,url_params,headers=header)
    return url_1118.text

    # print(url_1118.text)

