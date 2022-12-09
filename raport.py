import os
from datetime import date, datetime
from os import listdir
from os.path import isfile, join, exists


class HTMLCreator:
    def __init__(self):
        if exists("raport.html"):
            os.remove("raport.html")

        self.outputfiles = [file for file in listdir("output") if isfile(join("output", file))]
        self.inputfiles = [file for file in listdir("input") if isfile(join("input", file))]

        now = datetime.now()
        self.fulldate = now.strftime("%d-%m-%Y %H:%M:%S")
        self.css = open("resources/style.css", "r")
        self.html = open("raport.html", "w")
        self.html.write(f"""<!DOCTYPE html>
            <html>
            <head>
                <title>Raport {self.fulldate}</title>
                <style>
                {self.css.read()}
                </style>
            </head>
            <body>
                <div class="container">
                <h1>Raport {self.fulldate}</h1>
                <table>
                <tr>
                    <th>Input</th>
                    <th>Output</th>
                </tr>\n""")

    def doubletag(self, tag, content=""):
        self.html.write(f"<{tag}>{content}</{tag}>\n")

    def singletag(self, tag):
        self.html.write(f"<{tag}>\n")


raport = HTMLCreator()

for x in range(len(raport.outputfiles)):
    raport.singletag("tr")
    inputfile = open(f"input/{raport.inputfiles[x]}", "r")
    raport.doubletag("td", f"{inputfile.read()}")

    raport.singletag("td")
    outputfile = open(f"output/{raport.outputfiles[x]}", "r")
    lines = outputfile.readlines()
    for index, singleline in enumerate(lines):
        raport.doubletag("div", f"{singleline.strip()}")
    raport.singletag("/td")

    raport.singletag("/tr")

raport.singletag("/table")
raport.doubletag("footer", "@Kamil Ptak 2022r.")
raport.singletag("/div")
raport.singletag("/body")
raport.singletag("/html")
