import os.path
import time
import sqlite3
import git
import sys
import numpy as np
import matplotlib.pyplot as plt
from rq import Connection, Queue

from CC import get_complexity

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    repo = git.Repo()
    git_url = "https://github.com/VikasDanny/CyclomaticComplexity.git"
    repo_dir = "/home/Vikas/Cyclomatic-Complexity/test"
    directory = "/home/Vikas/Cyclomatic-Complexity/results/"
    
