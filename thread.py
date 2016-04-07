#import subprocess

#subprocess.call(['ls', '-l'])

import multiprocessing
import random
from time import sleep

def worker(n):

    """worker function"""
    print 'Worker', n
    choices = [1,4]
    sleep(random.choice(choices))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

