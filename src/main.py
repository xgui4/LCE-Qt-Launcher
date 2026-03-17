#!/usr/bin/env python3

import launcher
import cli

import sys

argv = sys.argv

if len(argv) >= 1:
    if argv[1] == "cli" : 
        cli.main()
    else:
        launcher.main()
else: 
    launcher.main()
