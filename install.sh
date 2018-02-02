#!/bin/bash
cp cpu_temp.py /usr/lib64/ganglia/python_modules/
rm /usr/lib64/ganglia/python_modules/cpu_temp.pyc
cp cpu_temp.pyconf /etc/ganglia/conf.d

