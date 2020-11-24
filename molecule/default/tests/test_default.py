import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'docker-ce'
PACKAGE_SUPPORT1 = 'docker-ce-cli'
PACKAGE_SUPPORT2 = 'containerd.io'
PACKAGE_USER = 'docker'
PACKAGE_GROUP = 'docker'
PACKAGE_HOME = '/home/docker'
PACKAGE_BINARY = "/usr/bin/docker"


def test_docker_user_exists(host):
    """
    Tests if docker user exists.
    """
    assert host.user(PACKAGE_USER)


def test_docker_group_exists(host):
    """
    Tests if docker group exists.
    """
    assert host.group(PACKAGE_GROUP)


def test_docker_home_exists(host):
    """
    Tests if /home/docker directory exists.
    """
    assert host.file(PACKAGE_HOME).exists


def test_docker_cli_package_installed(host):
    """
    Tests if docker-ce-cli package is in installed state.
    """
    assert host.package(PACKAGE_SUPPORT1).is_installed


def test_docker_containered_package_installed(host):
    """
    Tests if containerd.io package is in installed state.
    """
    assert host.package(PACKAGE_SUPPORT2).is_installed


def test_docker_package_installed(host):
    """
    Tests if docker-ce package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_docker_binary_exists(host):
    """
    Tests if docker binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_docker_binary_file(host):
    """
    Tests if docker binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_docker_repo_exists(host):
    """
    Tests if relevant repository file exists for docker.
    """
    assert host.file('/etc/apt/sources.list.d/docker-ce.list').exists or \
        host.file('/etc/yum.repos.d/docker-ce.repo').exists


def test_docker_repo_file(host):
    """
    Tests if relevant repository file exists for docker.
    """
    assert host.file('/etc/apt/sources.list.d/docker-ce.list').is_file or \
        host.file('/etc/yum.repos.d/docker-ce.repo').is_file


def test_docker_binary_which(host):
    """
    Tests the output to confirm docker's binary location.
    """
    assert host.check_output('which docker') == PACKAGE_BINARY
