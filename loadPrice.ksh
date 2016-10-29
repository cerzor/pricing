#!/bin/bash
# $(date +%x%H:%M:%S)
python loadPrices.py | tee -a "logs/load_prices_log.txt"
%exit

