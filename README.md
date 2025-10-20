
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

    创建数据表

        python manage.py migrate

    为模型的改变生成迁移文件

        python manage.py makemigrations polls
            为polls  app中的模型改变生成迁移文件
    
    应用数据库迁移
        
        再执行一遍 python manage.py migrate
    
    创建一个能登录管理页面的用户

        python manage.py createsuperuser
    
    查看项目下的django内置数据表
    
        sqlite3 db.sqlite3
        .tables
        执行上述两行命令后就可以在终端看到你本项目的数据表了




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


### *** 下面是关于本项目V1.1版本的详细的说明 ***

    2025.10.18  实现了游客注册账号的功能
    2025.10.18  实现了游客登录的功能
    2025.10.18  实现了登录账号后进行所有用户信息的增删改查的功能
    2025.10.19  实现了模型选择界面的布局、样式与基本的选择功能

## 关于V1.2版本

    V1.2版本是本人基于V1.1版本的整理与进一步进行的功能扩展等

### *** 下面是关于本项目V1.2版本的详细的说明 ***
    2025.10.19  对于V1.1版本的系统功能和代码进行了进一步的整理与归纳
    2025.10.19  增加了鼠标的滑动与点击的效果
    2025.10.20  继续加了个页面
    
    要重新审视和规划一下整个网站的布局与目标等了--------!
    (感觉上面的功能等等都太常规了，还是要再好好想想看)
