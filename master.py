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
    async_results = {}
    connection = sqlite3.connect('results.db')
    connection.execute('''CREATE TABLE RESULTS
                                             (FileName TEXT PRIMARY KEY     NOT NULL,
                                              CC            REAL,
                                             TimeTaken      REAL    NOT NULL);''')
    connection.execute('''CREATE TABLE WORKERS
                                                 (WORKER INT PRIMARY KEY     NOT NULL,
                                                 TimeTaken      REAL    NOT NULL);''')
    print "Table Created."
    
