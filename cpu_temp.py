#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File system disk space usage for Ganglia

import subprocess

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata



def acquire_heatInfo(name):
    result= []
    cmd="/usr/bin/sensors | egrep \"Physical|Package\" | awk '{print $4}'"
    out, err = subprocess_open(cmd)
    a =out.split()
    temp =[]
    for x in a :
        temp.append(float(x.replace("\xc2\xb0C","")))
    temp.sort()
    return int(temp[-1])

def metric_init(params):
    global descriptors

    d1 = {'name': 'cpu_temp',
        'call_back': acquire_heatInfo,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'C',
        'slope': 'both',
        'format': '%u',
        'description': 'Temperature of host',
        'groups': 'health'}

    descriptors = [d1]

    return descriptors

def metric_cleanup():
    '''Clean up the metric module.'''
    pass

#This code is for debugging and unit testing
if __name__ == '__main__':
    metric_init({})
    for d in descriptors:
        v = d['call_back'](d['name'])
        print 'value for %s is %u' % (d['name'],  v)



