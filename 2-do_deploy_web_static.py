#!/usr/bin/python3
""" distributes an archive to your web servers,
using the function do_deploy """

from fabric.api import env, put, run, local, task
from os import path
from datetime import datetime

env.hosts = ['34.204.101.175', '35.153.192.118']
env.user = "ubuntu"

@task
def do_pack():
    """ function """
    try:
        local('mkdir -p versions')
        dt = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'web_static_{}.tgz'.format(dt)
        local('tar -czvf versions/{} web_static/'.format(filename))
        return 'versions/{}'.format(filename)
    except:
        return None


@task
def do_deploy(archive_path):
    """ method doc
        fab -f 2-do_deploy_web_static.py do_deploy:
        archive_path=versions/web_static_20231004201306.tgz
        -i ~/.ssh/id_rsa -u ubuntu
    """
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
