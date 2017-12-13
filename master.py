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
    q = Queue()
    commits_touching_path = list(repo.iter_commits('master'))
    for root, dirs, files in os.walk(repo_dir):
        for file in files:
            for i in range(len(commits_touching_path)):
                commits = commits_touching_path[i]
                if file.endswith(".py"):
                    try:
                        file_contents = repo.git.show('{}:{}'.format(commits.hexsha, file))
                        f1 = open(directory + 'test_' + str(i) + '.py', 'a')
                        f1.write(file_contents)
                    except git.exc.GitCommandError:
                        continue
    f1.close()
    for root, dirs, files in os.walk(directory):
        for file in files:
            q1 = str(os.path.join(directory, file))
            async_results[file] = q.enqueue(get_complexity, q1) 
            
    worker = 50
    start_time = time.time()
    done = False

