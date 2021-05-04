# zmirror for Codeforces

**请在遵守当地相关法律法规的前提下使用本项目**  
**本人拒绝为任何商业或非法目的提供任何技术支持**  
**本项目仅为科研人员更方便地查询知识而创建, 请勿大范围传播**

```
<IfModule mod_ssl.c>
    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5
    <VirtualHost *:443>
        # �~_~_�~P~M, 记�~W修�~T��~H~P�| �~G�己�~Z~D
        ServerName codeforces.live

        # �~Y个没�~T��~Z~D
        ServerAdmin yylx@yylx.tech



        # �~K�~]�两个log�~V~G件路�~D�~_建议�~L~I�~^�~Y~E修�~T�
        # �~X认�~]�~X�~\� /var/log/apache2/ �~V~G件夹�~K
        # ErrorLog 中�~L~E�~P��~Fzmirror产�~T~_�~Z~Dstdout�~S�~G�, �~K��~\~@�~Adebug�~O�以�~\~K�~C
        ErrorLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_error.log
        CustomLog ${APACHE_LOG_DIR}/zmirror-codeforces_ssl_access.log combined

        # ##### WSGI �~Y�~C��~H~F�~X��~G~M�~B�  ######
        WSGIDaemonProcess zmirror_codeforces user=www-data group=www-data threads=16
        #�~Y�~X��~H~Z�~H~Z�~I�~E�~Z~Dzmirror�~Z~D路�~D
        WSGIScriptAlias / /var/www/zmirror/wsgi.py
        WSGIPassAuthorization On

        # �~Y�~Hzmirror�~V~G件夹�~]~C�~Y~P
        <Directory /var/www/zmirror>
            WSGIProcessGroup zmirror_codeforces
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>

       # ######### SSL�~C��~H~F �~Y�~C��~H~F�~Q~J�~IApache�| �~Z~D�~A书�~R~L�~A�~R��~\��~S� #########
       # �~K�~]�使�~T��~Z~D�~X��~H~Z�~H~Zlet's encrypt�~Y�~H~Q们�~Z~D�~A书, �| �~_�~O�以�~T��~H��~Z~D
        SSLEngine on
        # �~A�~R�
        SSLCertificateFile /etc/apache2/cert/cert.pem
        # �~A书
        SSLCertificateKeyFile /etc/apache2/cert/privkey.pem
        # �~A书�~S�
        SSLCertificateChainFile /etc/apache2/cert/chain.pem

       # HTTP/2
        <IfModule http2_module>
            Protocols h2 h2c http/1.1
        </IfModule>
    </VirtualHost>
</IfModule>                                
```
