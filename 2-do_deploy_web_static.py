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
    """ function """
    if path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except:
        return False
