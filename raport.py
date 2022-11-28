from datetime import date


class HTMLCreator:
    def __init__(self):
        self.html = open(f"backup/{date.today()}/index.html", "w")
        self.html.write(f"""<!DOCTYPE html>
            <html>
            <head>
            <title>Raport {date.today()}</title>
            <link rel="stylesheet" href="style.css">
            </head>
            <body>\n""")

    def tag(self, tag, content):
        self.html.write(f"<{tag}>{content}</{tag}>\n")

    def opentag(self, tag):
        self.html.write(f"<{tag}>\n")

    def closetag(self, tag):
        self.html.write(f"</{tag}>\n")


raport = HTMLCreator()
