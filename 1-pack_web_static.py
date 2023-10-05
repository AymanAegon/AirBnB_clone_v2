#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder of
your AirBnB Clone repo, using the function do_pack """

from fabric.api import run
from datetime import datetime


def do_pack():
    run('mkdir -p versions')
    y = datetime.now().year
    m = datetime.now().month
    d = datetime.now().day
    h = datetime.now().hour
    n = datetime.now().minute
    s = datetime.now().second
    filename = 'web_static_{}{}{}{}{}{}.tgz'.format(y, m, d, h, n, s)
    run('tar -czvf versions/{}'.format(filename))