#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
import re
import sys

if len(sys.argv)<3:
    print 'Usage: wikitrans [source-lang] [phrase] <target-lang>'
    exit(-1)
    
(dummy, slang, phrase) = sys.argv[0:3]

tlang = sys.argv[3] if len(sys.argv)>3 else ''

print slang, phrase, tlang
    

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)

url = 'https://%s.wikipedia.org/wiki/%s'%(slang, phrase)
try:
    f = urllib2.urlopen(url)
except urllib2.URLError as e:
    print 'url %s does not exist!'%url
    exit(-1)
    
contents = f.read()
mm =  re.findall('<a href=\"\/\/([a-z\-]+?)\.\wikipedia\.org\/wiki\/(.+?)" title=\"(.+?)" lang=\"(.+?)" hreflang="(.+?)">(.+?)<\/a>', contents)

for mmm in mm:
    if (tlang and (mmm[0]==tlang)) or (not tlang):
        print "%s (%s)\t-\t%s\thttps://%s.wikipedia.org/wiki/%s "%(mmm[0], mmm[-1], mmm[2], mmm[0], mmm[1])

print '%s entries in total'%len(mm)

