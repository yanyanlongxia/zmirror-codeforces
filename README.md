# zmirror for Codeforces

**请在遵守当地相关法律法规的前提下使用本项目**  
**本人拒绝为任何商业或非法目的提供任何技术支持**  
**本项目仅为科研人员更方便地查询知识而创建, 请勿大范围传播**

```
<IfModule mod_ssl.c>
    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5
    <VirtualHost *:443>
        # 域名, 记得修改成你自己的
        ServerName codeforces.live

        # 这个没用的
        ServerAdmin yylx@yylx.tech



        # 下面两个log文件路径也建议按实际修改
        # 默认保存在 /var/log/apache2/ 文件夹下
        # ErrorLog 中包含了zmirror产生的stdout输出, 若需要debug可以看它
        ErrorLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_error.log
        CustomLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_access.log combined

        # ##### WSGI 这部分是重点  ######
        WSGIDaemonProcess zmirror_codeforces user=www-data group=www-data threads=16
        #这是刚刚安装的zmirror的路径
        WSGIScriptAlias / /var/www/zmirror/wsgi.py
        WSGIPassAuthorization On

        # 给予zmirror文件夹权限
        <Directory /var/www/zmirror>
            WSGIProcessGroup zmirror_codeforces
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>

       # ######### SSL部分 这部分告诉Apache你的证书和私钥在哪 #########
       # 下面使用的是刚刚let's encrypt给我们的证书, 你也可以用别的
        SSLEngine on
        # 私钥
        SSLCertificateFile /etc/letsencrypt/live/codeforces.live/cert.pem
        # 证书
        SSLCertificateKeyFile /etc/letsencrypt/live/codeforces.live/privkey.pem
        # 证书链
        SSLCertificateChainFile /etc/letsencrypt/live/codeforces.live/chain.pem

       # HTTP/2
        <IfModule http2_module>
            Protocols h2 h2c http/1.1
        </IfModule>
    </VirtualHost>
</IfModule>                                 
```
