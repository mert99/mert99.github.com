# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'

SITENAME = "mert99's Blog"
AUTHOR = 'mert99'

DISQUS_SITENAME = 'mert99sblog'
GITHUB_URL = '<https://github.com/mert99>'#github链接
SITEURL = '<http://mert99.github.com>'
GOOGLE_ANALYTICS = 'UA-30756331-1'#谷歌站点分析
TAG_FEED  = 'feeds/%s.atom.xml'

DEFAULT_PAGINATION = 4#默认每一页有多少篇文章

DEFAULT_CATEGORY ='misc'
OUTPUT_PATH = '.'
#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把index.html上传到repo的master分支的根目录才可以!
PATH = 'posts'#这个是指定放置.md/.rst文件的目录

LINKS = (('x-wei', '<http://x-wei.github.com>'),
         ('farseerfc', "<http://farseerfc.github.com/>"),
         )#友情链接~

SOCIAL = (
          ('github', '<https://github.com/mert99>'),
          )#社交网络链接
          #~ ('twitter', '<http://twitter.com/farseerfc>'),
          #~ ('facebook', '<http://www.facebook.com/farseerfc>'),
          #~ ('weibo', '<http://weibo.com/farseerfc>'),
          #~ ('renren', '<http://www.renren.com/farseer>'),

#这个是farseerfc同学自己加的, 可以显示他的新浪微博内容, 有微博的话可以把这些加上~
#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
#~ </iframe>
#~ """

#google自定义搜索(大概是站内搜索吧)
#~ GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
#~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"
