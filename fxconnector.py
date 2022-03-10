#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FXConnector POC
version: 0.1
author: Pau Ronda
"""

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
        print(data)

if __name__ == "__main__":

    example_csv = open("poccurrency.csv", "r")
    exampledata = example_csv.read()
    example_csv.close()

    fxconnector = FXConnector()
    fxconnector.on_message(exampledata)
