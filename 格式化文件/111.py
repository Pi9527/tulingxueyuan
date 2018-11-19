import re
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m = p.match("I am really love taozi")
print(m)
print(m.group(0))
print(m.start(0))
print(m.end(0))