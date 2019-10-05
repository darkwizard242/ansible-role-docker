import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


DOCKER_USER = 'docker'
DOCKER_GROUP = 'docker'
DOCKER_HOME = '/home/docker'
DOCKER_PACKAGE = ['docker-ce', 'docker-ce-cli', 'containerd']
DOCKER_BINARY_PATH = '/usr/bin/docker'
DOCKER_EL_REPO = '/etc/yum.repos.d/docker-ce.repo'
DOCKER_DEBIAN_REPO = '/etc/apt/sources.list.d/docker.list'
DOCKER_UBUNTU_REPO = '/etc/apt/sources.list.d/docker.list'
DOCKER_SERVICE = 'docker'


def test_docker_user_exists(host):
    host.user('DOCKER_USER')


def test_docker_group_exists(host):
    host.group('DOCKER_GROUP')


def test_docker_home_exists(host):
    host.file('DOCKER_HOME').exists


def test_docker_packages_installed(host):
    host.package("DOCKER_PACKAGE").is_installed


def test_docker_binary_exists(host):
    host.file('DOCKER_BINARY_PATH').exists


def test_docker_binary_file(host):
    host.file('DOCKER_BINARY_PATH').is_file


def test_docker_repo_exists(host):
    host.file('DOCKER_DEBIAN_REPO').exists or \
      host.file('DOCKER_EL_REPO').exists or \
      host.file('DOCKER_UBUNTU_REPO').exists


def test_docker_repo_file(host):
    host.file('DOCKER_DEBIAN_REPO').is_file or \
      host.file('DOCKER_EL_REPO').is_file or \
      host.file('DOCKER_UBUNTU_REPO').is_file


def test_docker_service_is_running(host):
    host.service('DOCKER_SERVICE').is_running


def test_docker_service_is_enabled(host):
    host.service('DOCKER_SERVICE').is_enabled


def test_docker_binary_which(host):
    host.check_output('which docker') == DOCKER_BINARY_PATH
