
# 基于python的Web项目学习

## 创建虚拟环境
    
    conda create -n next_web python=3.11

## 启动虚拟环境，安装依赖包

    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask

    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
    
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django




## 关于django的使用

    创建一个django的项目

        django-admin startproject main_files ./next_Web_V1.1/
        这个就是将在./next_Web_V1.1/目录内创建一个名为main_files的项目
    
    运行项目
    
        python ./manage.py runserver

    创建一个应用模块
    
        python ./manage.py startapp polls
        这个polls的应用模块已经创建了，后面运行项目后就可以用了




## 关于debian 13 安装数据库 (MariaDB)
    
    对于大多数用户，安装 MariaDB 是更直接稳妥的选择。它在兼容 MySQL 的同时，由 Debian 官方仓库直接提供，安装顺利。
    
    执行以下命令，初步安装与配置数据库
    sudo apt update
    sudo apt upgrade
    sudo apt install mariadb-server
    sudo systemctl start mariadb    # 启动服务
    sudo systemctl enable mariadb   # 设置开机自启
    sudo systemctl status mariadb   # 检查服务状态
    
    
    
    连接到 MariaDB：
    sudo mysql -u root -p
    
    
    可以首先展示一下数据表

        MariaDB [(none)]> USE mysql
        
            Reading table information for completion of table and column names
            
            You can turn off this feature to get a quicker startup with -A

            Database changed
            
        MariaDB [mysql]> SHOW DATABASES;
        
            +--------------------+
            
            | Database           |
            
            +--------------------+
            
            | information_schema |
            
            | mysql              |
            
            | performance_schema |
            
            | sys                |
            
            +--------------------+
            
            4 rows in set (0.001 sec)
            
            
        
        MariaDB [mysql]> 
    
    



## 关于V1.0版本

    V1.0版本主要是本人进行的django相关环境的搭建过程，无需仔细查看，还是很乱。





## 关于V1.1版本
    
    V1.1版本是本人根据django的官方文档一步一步进行搭建的一个简陋的网站示例。


### *** 下面是关于本项目V1.1版本的相信说明 ***




