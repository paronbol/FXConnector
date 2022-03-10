#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FXConnector POC
version: 0.1
author: Pau Ronda
"""
# import requests

class FXConnector():
    " Main class "

    def __init__(self, bidmargin=0.001, askmargin=0.001, endpoint="https://localhost/fxdata/api/"):
        " Initialization "
        self.bidmargin = bidmargin
        self.askmargin = askmargin
        self.endpoint = endpoint

    def on_message(self, message:str) -> None:
        " Push data to endpoint "
        data = []
        lines = message.splitlines()
        for l in lines:
            item = l.split(",")
            item[2] = float(item[2]) * (1+self.bidmargin)
            item[3] = float(item[3]) * (1+self.bidmargin)
            data.append(item)

        jsondata = []
        for d in data:
            jsondata.append({
                "id": d[0],
                "instrumentName": d[1],
                "bid": d[2],
                "ask": d[3],
                "timestamp": d[4]
            })

        # Printed instead of sending to the endpoint
        # r = requests.post(url = self.endpoint, data = jsondata)
        print("Simulating data sent to "+self.endpoint)
        print(jsondata)

if __name__ == "__main__":

    example_csv = open("poccurrency.csv", "r")
    exampledata = example_csv.read()
    example_csv.close()

    fxconnector = FXConnector()
    fxconnector.on_message(exampledata)
