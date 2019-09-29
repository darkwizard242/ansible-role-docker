import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


DOCKER_PACKAGE = 'docker'
DOCKER_BINARY_PATH = '/usr/bin/docker'
DOCKER_DEBIAN_REPO = '/etc/apt/sources.list.d/docker.list'
DOCKER_EL_REPO = '/etc/yum.repos.d/docker.repo'


def test_docker_package_installed(host):
    host.package("DOCKER_PACKAGE").is_installed


def test_docker_binary_exists(host):
    host.file('DOCKER_BINARY_PATH').exists


def test_docker_binary_file(host):
    host.file('DOCKER_BINARY_PATH').is_file


def test_docker_repo_exists(host):
    host.file('DOCKER_DEBIAN_REPO').exists or \
      host.file('DOCKER_EL_REPO').exists


def test_docker_repo_file(host):
    host.file('DOCKER_DEBIAN_REPO').is_file or \
      host.file('DOCKER_EL_REPO').is_file


def test_docker_binary_which(host):
    host.check_output('which docker') == DOCKER_BINARY_PATH or \
      host.check_output('whereis docker') == DOCKER_BINARY_PATH
