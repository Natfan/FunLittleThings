# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Script to download ECMWF weather data

@author: Chris Fairless
adapted from ECMWF template

"""

from ecmwfapi import ECMWFDataServer
    
server = ECMWFDataServer()
    
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "1988-09-08/to/1988-09-09",
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "165.128/166.128/167.128",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "format": "netcdf",
    "target": "temp.nc",
})