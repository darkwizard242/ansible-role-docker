import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_user_exists(host):
    assert host.user('docker')


def test_docker_group_exists(host):
    assert host.group('docker')


def test_docker_home_exists(host):
    assert host.file('/home/docker').exists


def test_docker_cli_package_installed(host):
    assert host.package("docker-ce-cli").is_installed


def test_docker_containered_package_installed(host):
    assert host.package("containerd.io").is_installed


def test_docker_package_installed(host):
    assert host.package("docker-ce").is_installed


def test_docker_binary_exists(host):
    assert host.file('/usr/bin/docker').exists


def test_docker_binary_file(host):
    assert host.file('/usr/bin/docker').is_file


def test_docker_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/docker-ce.list').exists or \
      host.file('/etc/yum.repos.d/docker-ce.repo').exists or \
      host.file('/etc/apt/sources.list.d/docker-ce.list').exists


def test_docker_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/docker-ce.list').is_file or \
      host.file('/etc/yum.repos.d/docker-ce.repo').is_file or \
      host.file('/etc/apt/sources.list.d/docker-ce.list').is_file


def test_docker_binary_which(host):
    assert host.check_output('which docker') == '/usr/bin/docker'
