import json, requests, subprocess


if __name__ == '__main__':
    with Connection():
        q = Queue()
        Worker(q).work()
