import io
import os.path
import jinja2

from airtest.core.api import *
from airtest.report.report import LogToHtml
from airtest.utils.compat import script_dir_name
from poco.drivers.unity3d import UnityPoco

def login():
    