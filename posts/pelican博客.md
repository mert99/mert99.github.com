Title: pelican博客
Date: 2012-11-23
Tags: pelican, git

[pelican][1]是个用python做的静态网站生成器。把生成好的东西挂到github上就得到了这个博客。

首先
-------------
注册一个[github]帐号，比如abc。创建名为abc.github.com的仓库。

其次
-------------
安装pelican。

    sudo apt-get install python-pip
    sudo pip install pelican

可以用[markdown]或者[rst]来编辑文章,pelican默认支持rst,如要用markdown：

    sudo pip install Markdown

然后
-------------
创建和你的仓库同名的目录，比如abc.github.com。

    mkdir ~/abc.github.com

进入目录，编辑配置文件settings.py。

    cd ~/abc.github.com
    vim settings.py

配置文件示例如下，按个人实际情况修改：

    # -*- coding: utf-8 -*-
    import sys

    TIMEZONE = 'Asia/Shanghai'

    DEFAULT_LANG = 'zhs'

    DATE_FORMATS = {
            'zhs' :( (u'zh_CN','utf8'), u'%Y-%m-%d',)
    }

    SITENAME = "mert99's Blog"
    AUTHOR = 'mert99'

    DISQUS_SITENAME = 'mert99sblog'
    GITHUB_URL = '<https://github.com/mert99>'#github链接
    SITEURL = '<http://mert99.github.com>'
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

这里用的是bootstrap2主题，可以这样获取:

    cd ~/abc.github.com
    git clone https://github.com/getpelican/pelican-themes

创建文件夹~/abc.github.com/posts，编辑要发表的博文:

    mkdir posts
    cd posts
    vim xxx.md

用pelican生成：

    cd ~/abc.github.com
    pelican -s ~/abc.github.com/settings.py -t ~/abc.github.com/pelican-themes/bootstrap2

最后
-------------
上传至github:

    cd ~/abc.github.com
    git init
    git add .
    git commit -m 'pelican blog'
    git remote add origin https://github.com/abc/abc.github.com
    git push -u origin master

其他的特性请参见pelican的[文档][1]。

  [1]: http://pelican.readthedocs.org/en/latest/
  [github]: https://github.com/
  [markdown]: http://wowubuntu.com/markdown/
  [rst]: https://beinggeekbook.readthedocs.org/en/latest/rst.html
