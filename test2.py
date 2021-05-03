#!/opt/homebrew/bin/python3
string = """lol
lol
Source: [url]https://riff.cc[/url] """

for line in string.splitlines():
    if "Source: [url]" in line:
        print(line)
