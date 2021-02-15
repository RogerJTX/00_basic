import signal
import sys
import time

def quit(signum, frame):
    sys.exit(0)

if __name__ == "__main__":
	## SIGINT 终止进程 中断进程
    signal.signal(signal.SIGINT, quit)
    ## signal.signal(signal.SIGTERM, quit)
    while True:
        time.sleep(0.1)