# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'

DATE_FORMATS = {
        'zhs' :( (u'zh_CN','utf8'), u'%Y-%m-%d',)
}

DEFAULT_LANG = 'zhs'

SITENAME = "mert99's Blog"
AUTHOR = 'mert99'

DISQUS_SITENAME = 'mert99sblog'
GITHUB_URL = 'https://github.com/mert99'
SITEURL = 'http://mert99.github.com'
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

SOCIAL = (('github', 'https://github.com/mert99'), 
         )

THEME='bootstrap2'

DEFAULT_PAGINATION = 4
DEFAULT_CATEGORY ='misc'
OUTPUT_PATH = '.'
PATH = 'posts'
