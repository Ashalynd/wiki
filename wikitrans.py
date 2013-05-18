#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
import re
import sys

if len(sys.argv)<3:
    print 'Usage: wikitrans [source-lang] [phrase] <target-lang>'
    exit(-1)
    
(dummy, slang, urllast) = sys.argv[0:3]

tlang = sys.argv[3] if len(sys.argv)>3 else ''

print slang, urllast, tlang
    

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)

urlpart = 'https://%s.wikipedia.org/wiki/'%slang

f = urllib2.urlopen(urlpart + urllast)
contents = f.read()
mm =  re.findall('<a href=\"\/\/([a-z\-]+?)\.\wikipedia\.org\/wiki\/(.+?)" title=\"(.+?)"', contents)

for mmm in mm:
    if (tlang and (mmm[0]==tlang)) or (not tlang):
        print mmm[0], mmm[2]



