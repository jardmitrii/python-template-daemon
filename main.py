#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include.daemon import Daemon
from sys import argv
pidfile = '/var/run/mydaemon.pid'

def usage():
    print """
Script usage parameters:
    debug   - Run script in current console with debug mode.
    start   - Run script as daemon
    stop    - Stop daemon
    restart - Rerun script as daemon
    help    - Show this help
"""

def exit_with_error():
    usage()
    exit(2)

def main():
    try:
        while True:
            pass
            
    except KeyboardInterrupt:
        exit(0)
    
class MyDaemon(Daemon):
    def run(self):
        main()

if __name__ == "__main__":
    daemon = MyDaemon(pidfile)
    actions = { 'debug': main,
                'start': daemon.start,
                'stop': daemon.stop,
                'restart': daemon.restart,
                'help': usage
                }
    
    if len(argv) == 2:
        actions.get(argv[1], exit_with_error)()            
        exit(0)
        
    else:
        exit_with_error()
