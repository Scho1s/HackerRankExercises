from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for _, __ in attrs:
                print(f"-> {_} > {__}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for _, __ in attrs:
                print(f"-> {_} > {__}")

    def handle_comment(self, attrs):
        pass

string = ""
for _ in range(int(input())):
    string += input()

parser = MyHTMLParser()
parser.feed(string)