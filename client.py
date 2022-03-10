#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FXConnector POC
version: 0.1
author: Pau Ronda
"""
import json

instruments = {}
data = []
with open('lastdata.json') as f:
    data = json.load(f)
f.close()

for d in data:
    if d['timestamp'] > instruments.get(d['instrumentName'], {"timestamp":"0"}).get("timestamp"):
        instruments.update({d['instrumentName']:d})

print("Last Prices")
for i in instruments.values():
    print("Timestamp: %s InstrumentName: %s BID: %s ASK: %s" % (i['timestamp'], i['instrumentName'], i['bid'], i['ask']) )
