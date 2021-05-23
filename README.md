# zmirror for Codeforces

**请在遵守当地相关法律法规的前提下使用本项目**  
**本人拒绝为任何商业或非法目的提供任何技术支持**  
**本项目仅为科研人员更方便地查询知识而创建, 请勿大范围传播**

```
<IfModule mod_ssl.c>
    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5
    <VirtualHost *:443>
        ServerName codeforces.live
        ServerAdmin yylx@yylx.tech


        ErrorLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_error.log
        CustomLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_access.log combined

        WSGIDaemonProcess zmirror_codeforces user=www-data group=www-data threads=16
        WSGIScriptAlias / /var/www/zmirror/wsgi.py
        WSGIPassAuthorization On
        <Directory /var/www/zmirror>
            WSGIProcessGroup zmirror_codeforces
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
        SSLEngine on

        SSLCertificateFile /etc/apache2/cert/codeforces.live_cert.pem

        SSLCertificateKeyFile /etc/apache2/cert/codeforces.live_privkey.pem

        SSLCertificateChainFile /etc/apache2/cert/codeforces.live_chain.pem


        <IfModule http2_module>
            Protocols h2 h2c http/1.1
        </IfModule>
    </VirtualHost>
</IfModule>                                
```
