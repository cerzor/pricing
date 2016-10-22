#!/bin/bash
# $(date +%x%H:%M:%S)
python main.py | tee -a "logs/load_symbols_log.txt"
exit
