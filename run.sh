#!/bin/bash

conda activate jobagent

# pip install -r requirements.txt

mkdir -p reports

timestamp=`date "+%Y%m%d_%H%M"`

python run_agent.py > reports/log.${timestamp}

