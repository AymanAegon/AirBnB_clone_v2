#!/usr/bin/python3
""" distributes an archive to your web servers,
using the function do_deploy """

from fabric.api import *
from os import path


def do_deploy(archive_path):
    """ function """
    if not path.isfile(archive_path):
        return False
    try:
        env.hosts = ['52.55.249.213', '54.157.32.137']
        env.user = "ubuntu"
        put(archive_path, "/tmp")
        name = archive_path.split('/')[-1].split('.')[0]
        folder = "/data/web_static/releases/{}".format(name)
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(name, folder))
        run("rm /tmp/{}.tgz".format(name))
        run("rm -rf {}/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    except:
        return False