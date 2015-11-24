from __future__ import with_statement
from fabric.api import *

HYDE_CONFIG = 'site.yaml'


def _hyde(args):
    return local('hyde -x {}'.format(args))


def _clean():
    local('rm -rf deploy')


def _deploy():
    _clean()
    _hyde('gen')


def _run():
    _deploy()
    local('cd deploy && python2 -m SimpleHTTPServer 8123')


@task
def clean():
    _clean()


@task
def deploy():
    _deploy()


@task
def run():
    _run()
