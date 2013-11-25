from __future__ import with_statement
from fabric.api import local

__author__ = 'zhouqi'


def deploy(msg=''):
    local('rake generate')
    local('git add .')
    local('git commit -am "%s"' % msg)
    local('git push origin source')
    local('rake deploy')