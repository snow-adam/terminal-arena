import time

def line_break():
    for i in range(10):
        print("\n")

def timed_line_break():
    time.sleep(3)
    for i in range(10):
        print("\n")