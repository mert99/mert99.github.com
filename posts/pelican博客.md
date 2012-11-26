Title: pelican博客
Date: 2012-11-26
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

pelican-chunk主题安装:

    cd ~/abc.github.com
    git clone https://github.com/tbunnyman/pelican-chunk
    sudo pelican-themes -i pelican-chunk

创建文件夹~/abc.github.com/posts，编辑要发表的博文:

    mkdir posts
    cd posts
    vim xxx.md

生成博客:

    cd ~/abc.github.com
    pelican -s settings.py

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
