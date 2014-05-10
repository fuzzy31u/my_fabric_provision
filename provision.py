# -*- coding: utf-8 -*-

from fabric.api import run, sudo, cd
from fabric.contrib.files import sed, append, contains

def execute():
    update_yum()
    install()
    change_network_config()
    config_httpd()
    link_www_dir()
    epel()
    remi()
    mysql55()
    python3()

def update_yum():
    sudo('yum update -y')

def install():
    sudo('yum -y install httpd')
    sudo('yum -y install emacs')
    sudo('yum -y install wget')

def change_network_config():
    sudo('service iptables stop')
    sudo('chkconfig iptables off')

def config_httpd():
    sudo ('service httpd start')
    sudo('chkconfig httpd on')

def link_www_dir():
    sudo('rm -rf /var/www/html')
    sudo('ln -fs /vagrant /var/www/html')

def epel():
    run('wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
    sudo('/bin/rpm -Uvh epel-release-6-8.noarch.rpm')
    sed('/etc/yum.repos.d/epel.repo', before='enabled=1', after='enabled=0', use_sudo=True)

def remi():
    run('wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm')
    sudo('rpm -Uvh remi-release-6.rpm')

def mysql55():
    sudo('yum install -y --enablerepo=remi mysql-server')
    if not contains('/etc/my.cnf', 'character_set_server=utf8'):
        append('/etc/my.cnf', 
               '\ncharacter_set_server=utf8\ndefault-storage-engine=InnoDB\ninnodb_file_per_table\n[mysql]\ndefault-character-set=utf8\n[mysqldump]\ndefault-character-set=utf',
           use_sudo=True)
    sudo('service mysqld start')
    sudo('chkconfig mysqld on')

def python3():
    run('wget https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tgz')
    run('tar xzvf Python-3.4.0.tgz')
    with cd('Python-3.4.0'):
        run('./configure --enable-shared --with-threads')
        run('make')
        sudo('make install')
        sudo('cp -p libpython3.4m.so libpython3.4m.so.1.0 /usr/lib')
        sudo('/sbin/ldconfig')
        run('source ~/.bash_profile')
        run('python3 --version')
