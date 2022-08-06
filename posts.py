import feedparser
import re

feed = feedparser.parse('https://zenn.dev/blancpanda/feed')

dist_md = ''

for entry in feed.entries[:10]:
    dist_md += f'- ![](img/zenn.svg) [{entry.title}]({entry.link})\n'

with open('README.md', 'r') as file:
    data = file.read()

with open('README.md', 'w') as file:
    pattern = re.compile(r'<!--\[START POSTS\]-->.*<!--\[END POSTS\]-->', re.DOTALL)
    file.write(re.sub(pattern, f'<!--[START POSTS]-->\n{dist_md}<!--[END POSTS]-->', data))
