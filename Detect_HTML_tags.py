from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for _, __ in attrs:
                print(f"-> {_} > {__}")

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print(tag)
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