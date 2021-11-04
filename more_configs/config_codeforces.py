# coding=utf-8
# 这是为 codeforces.com 配置文件
#
# 使用方法:
#   1. 复制本文件到 zmirror 根目录(wsgi.py所在目录), 并重命名为 config.py
#   2. 修改 my_host_name 为你自己的域名
#
# 各项设置选项的详细介绍请看 config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置
#
# 基本全功能完整

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = 'codeforces.live'
my_host_scheme = 'https://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81
verbose_level = 2

# ############## Target Domain Settings ##############
target_domain = 'codeforces.com'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的话)会不断告诉你新域名
external_domains = (
    'assets.codeforces.com',
    'sta.codeforces.com',
    'userpic.codeforces.com',
    'espresso.codeforces.com',
    'm1.codeforces.com',
    'm2.codeforces.com',
    'm3.codeforces.com',
    'www.codeforces.com',
    'codeforces.org',
    'mathjax.codeforces.org',
    'player.vimeo.com',
    'wikimedia.org',
)

# 强制所有 codeforces 站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域名
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = ('*.codeforces.com','*.codeforces.org','*.wikipedia.org','*.codeforces.ru','*.m.wikipedia.org','*.wikimedia.org')

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)
custom_text_rewriter_enable = True
