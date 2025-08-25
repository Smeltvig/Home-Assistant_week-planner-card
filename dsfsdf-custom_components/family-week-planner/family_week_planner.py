from __future__ import annotations

import logging
from .const import DOMAIN

_LOGGER: logging.Logger = logging.getLogger(__package__)
_LOGGER = logging.getLogger(__name__)

# RAW API CODE BELOW
from bs4 import BeautifulSoup as BS
from datetime import date, datetime, timedelta, time
import requests
import os
import re
import gc
import json

DEBUG = False

INPUT_FINGERPRINT = "fingerprint"
INPUT_PASSWORD = "Password"
INPUT_USERNAME = "UserName"
INPUT_RETURN_URL = "returnUrl"

AJAX = "&ajax=1"
PAGESIZE = "&pagesize=100000"
VIEW = "&view=List"
HOME = "&home=true"
USER_ID = "&userId="
BBS = "BBS"
BBS_DETAILS = "BBS_DETAILS"
LOGOUT = "LOGOUT"
MSG_DETAILS = "MSG_DETAILS"
MSG_FOLDER = "MSG_FOLDER"
MSG_FOLDERS = "MSG_FOLDERS"
RELATIONS = "RELATIONS"
SCHEDULE = "SCHEDULE"
HOMEWORKANDASSIGNMENT = "HOMEWORKANDASSIGNMENT"

MONTHS = [
    "jan",
    "feb",
    "mar",
    "apr",
    "maj",
    "jun",
    "jul",
    "aug",
    "sep",
    "okt",
    "nov",
    "dec",
]
URLS = {}


class family_week_planner:
    session = requests.Session()
    fingerPrint, logoUrl, schoolName, userFullName, userImg = (
        None,
        None,
        None,
        None,
        None,
    )
    loggedIn = False
    unreadMsg, unreadBbs = -1, -1
    bbs, relations = {}, {}

    def __init__(self, url="", username="", password=""):
        self.baseUrl = url
        self.username = username
        self.password = password
        self.fingerPrintFile = DOMAIN + "_" + self.username

    def update(self):
        gc.collect()
        return True