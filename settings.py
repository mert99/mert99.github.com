# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zhs' :( (u'zh_CN','utf8'), u'%Y-%m-%d',)
}

DEFAULT_LANG = 'zhs'

SITENAME = "mert99's Blog"
SITEURL = 'http://mert99.github.com'
AUTHOR = 'mert99'
DISQUS_SITENAME = 'mert99sblog'

THEME='pelican-chunk'

#DEFAULT_PAGINATION = 4
DEFAULT_CATEGORY ='misc'
OUTPUT_PATH = '.'
PATH = 'posts'

# settings used by the pelican-chunk theme
SITESUBTITLE = 'A pelican blog with the pelican-chunk theme.'
#DISPLAY_CATEGORIES_ON_MENU = True
LINKS = (('github', 'https://github.com/mert99'),)
SINGLE_AUTHOR = True

