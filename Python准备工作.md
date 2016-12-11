# 安装pyenv
## pyenv
    1. 依赖安装
    $ yum -y install git
    2. 安装pyenv
    $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    3. 配置环境变量：~/.bash_profile
    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    4. 如果未生效：
        a. source ~/.bash_profile or . ~/.bash_profile
        b. 退出重新登录

# 安装Python
## Centos：
    1. 安装编译工具：
    $ yum -y install gcc make patch
    2. 安装依赖
    $ yum -y install gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel
    3. 安装Python 3.5.2
    $ pyenv install 3.5.2
    4. 可以手动建立cache目录
    $ mkdir ~/.pyenv/cache
## Ubuntu：搜索工具apt-cache 
    1.安装编译工具：
    $ apt-get -y install gcc make patch
    2. 安装依赖：
    $ apt-get -y install libgdbm-dev libssl-dev libsqlite-dev libreadline-dev zlib1g-dev libbz2-dev
    3. 安装Python 3.5.2:
    $ pyenv install 3.5.2

# 使用Pyenv
## Pyenv：
    1. 第三方安装包目录：
        eg：
        ~/.pyenv/versions/3.5.2/lib/python3.5/site-packages/
    2. local:
        切换当前目录及其子目录的Python版本，可以通过删除.python-version恢复默认Python版本；
        ~/.pyenv/version：全局配置，不存在，则表示使用的system版本
    3. global：
        切换全局默认Python版本；
        永远不要使用global命令；
    4. virtualenv: 用来隔离项目间使用的第三方包，创建的过程是一个copy的过程 
        创建虚拟环境：$ pyenv virtualenv $bash_version $name
    5. uninstall：
        卸载某个版本，包括虚拟环境

# 安装ipython
## ipython: python交互式shell的增强工具
    1. 配置国内Pip源
    $ mkdir ~/.pip
    $ vim ~/.pip/pip.conf
        [global]
        index-url = http://mirrors.aliyun.com/pypi/simple/
        trusted-host = mirrors.aliyun.com
    2. 安装ipython:
    $ pip install ipython

# 使用Jupyter：
## jupyter:
    1. 安装：
    $ pip install jupyter
    2. 使用：
    本地：jupyter notebook
    供远程使用：jupyter notebook --ip=0.0.0.0 --no-browser

    