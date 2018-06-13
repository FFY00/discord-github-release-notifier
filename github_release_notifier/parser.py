#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, feedparser, re, requests, tomd, time

__all__ = ['parse', 'get_package']


def parse(package):
    package_name = get_package(package)
    url = 'https://github.com/%s/releases.atom' % package_name
    feed = feedparser.parse(url)
    entries = []
    for item in feed['entries']:
        owner, repo = package_name.split('/')
        version = re.search('(?<=Repository/)[0-9]+/(.+)', item['id']).group(1)
        authors = item['authors'][0]['name'] if 'authors' in item and item['authors'] and item['authors'][0] and item['authors'][0]['name'] else None,
        author = authors[0]
        content = ""
        for obj in item['content']:
            if obj['type'] == 'text/html':
                content += obj['value']
        content = content.replace("<br />", "\n")
        content = tomd.convert(content[:1024])
        while content.startswith('\n'):
            content = content[1:]
        while content.endswith('\n'):
            content = content[:-1]
        entries.append({
            "embeds": [{
                "title": "New release: %s" % version,
                "description": package_name,
                "url": item['link'],
                "thumbnail": {
                    "url": "https://github.com/%s.png" % owner,
                },
                "author": {
                    "name": author,
                    "url": "https://github.com/%s" % author,
                    "icon_url": "https://github.com/%s.png" % author,
                },
                "fields": [{
                    "name": item['title_detail']['value'],
                    "value": content[:1024],
                }],
                "footer": {
                    "text": time.strftime("%a %d %b, %Y at %I:%M %p", item['updated_parsed']),
                }
            }],
            "version": version,
            "package_name": package_name,
        })
    return entries


def get_package(entry):
    if 'github' in entry:
        entry = re.search('(?<=github.com/)[^/]+/[^/]+', entry).group(0)
    request = requests.get('https://github.com/%s/tags.atom' % entry)
    if request.status_code != 200:
        print('Error: %s is not a valid github url/package' % entry)
    return entry


def main():
    print(parse(sys.argv[1]))


if __name__ == "__main__":
    main()
