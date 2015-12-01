from __future__ import with_statement
from fabric.api import *

HYDE_CONFIG = 'site.yaml'
PORT = 8123


def _hyde(args):
    return local('hyde -x {}'.format(args))


def _clean():
    local('rm -rf deploy')


def _deploy():
    _clean()
    _hyde('gen')


def _run():
    _deploy()
    kill()
    _hyde('serve -p {}'.format(PORT))
    #local('cd deploy && python2 -m SimpleHTTPServer 8123')


@task
def kill():
    try:
        local('pkill -f "hyde -x serve"')
    except:
        pass


@task
def clean():
    _clean()


@task
def deploy():
    _deploy()


@task(default=True)
def run():
    _run()
