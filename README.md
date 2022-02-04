[![build-test](https://github.com/darkwizard242/ansible-role-docker/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-docker/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-docker/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-docker/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43814?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43814?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43814?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-docker&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-docker) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-docker&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-docker) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-docker&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-docker) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-docker&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-docker) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-docker?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-docker?color=orange&style=flat-square)

# Ansible Role: docker

Role to install (_by default_) [docker](https://www.docker.com/) package or uninstall (_if passed as var_) on **Ubuntu**, **Debian** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
docker_architecture_map:
  amd64: amd64
  x86_64: amd64
  armv6l: armhfv6
  armv7l: armhfv6
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
docker_apps:
  - docker-ce
  - docker-ce-cli
  - containerd.io
docker_apps_desired_state: present
docker_service_name: docker
docker_service_desired_state: restarted
docker_service_desired_boot_enabled: yes
docker_group: docker
docker_group_desired_state: present
docker_user: docker
docker_user_home: "/home/{{ docker_user }}"
docker_user_shell: /bin/bash
docker_user_desired_state: present
docker_repo_gpg_key: https://download.docker.com/linux/{{ ansible_distribution | lower }}/gpg
docker_nonroot_users:
  - darkwizard242
  - ubuntu
docker_add_nonroot_users: false
docker_centos_pre_reqs:
  - device-mapper-persistent-data
  - lvm2
docker_centos_pre_reqs_desired_state: present
docker_repo_centos: https://download.docker.com/linux/centos/7/$basearch/stable
docker_repo_centos_gpg_key: https://download.docker.com/linux/centos/gpg
docker_repo_centos_name: docker-ce-stable
docker_repo_centos_description: Docker CE Stable - $basearch
docker_repo_centos_gpgcheck: yes
docker_repo_centos_enabled: yes
docker_repo_centos_filename: docker-ce
docker_repo_centos_desired_state: present
docker_debian_pre_reqs:
  - apt-transport-https
  - ca-certificates
  - curl
  - gnupg
  - lsb-release
docker_debian_pre_reqs_desired_state: present
docker_repo_debian: "deb [arch={{ ansible_architecture }}] https://download.docker.com/linux/debian {{ ansible_lsb['codename'] }} stable"
docker_repo_debian_filename: docker-ce
docker_repo_debian_desired_state: present
```

### Variables table:

Variable                             | Description
------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
docker_architecture_map              | Variable for system architecture types.
docker_apps                          | Name of docker application packages require to be installed i.e. `docker-ce, docker-ce-cli, containerd.io`
docker_apps_desired_state            | State of the docker_apps packages (i.e. `docker-ce, docker-ce-cli, containerd.io` packages). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
docker_service_name                  | Default service name for Docker.
docker_service_desired_state         | Desired state for Docker service.
docker_service_desired_boot_enabled  | Desired enabled/disabled state for Docker service.
docker_service_desired_boot_enabled  | Desired enabled/disabled state for Docker service.
docker_group                         | Name of the group that the docker owner will belong to. Any user that requires using docker app requires to be a member in the `docker` group.
docker_group_desired_state           | `present` indicates creating the group if it doesn't exist. Alternative is `absent`.
docker_user                          | Name of the user that the docker will be owned by.
docker_user_home                     | Home directory for docker user.
docker_user_shell                    | Shell for `docker_user`.
docker_user_desired_state            | `present` indicates creating the user if it doesn't exist. Alternative is `absent`.
docker_nonroot_users                 | List of users to add to the `docker` group
docker_add_nonroot_users             | Boolean variable. Values can either be `true` or `false`. Setting to `true` will run the task that will add additionally provided users in the variable `docker_nonroot_users` to the `docker` group. If set to `false`, the specific task that adds user to `docker` group will be skipped. Defaults to `false`
docker_repo_gpg_key                  | GPG repo for docker repository
docker_centos_pre_reqs               | Docker recommends the installation of both these packages on the EL/CentOS docker host system and as such, they are considered pre-requisites.
docker_centos_pre_reqs_desired_state | Desired state for Docker pre-requisite apps on EL/CentOS systems.
docker_repo_centos                   | Repository `baseurl` for Docker on EL/CentOS based systems.
docker_repo_centos_name              | Repository name for Docker on EL/CentOS based systems.
docker_repo_centos_description       | Description to be added in EL/CentOS based repository file for Docker.
docker_repo_centos_gpgcheck          | Boolean for whether to perform gpg check against Docker on EL/CentOS based systems.
docker_repo_centos_enabled           | Boolean to set so that Docker repository is enabled on EL/CentOS based systems.
docker_repo_centos_filename          | Name of the repository file that will be stored at `/yum/sources.list.d/docker-ce.repo` on EL/CentOS based systems.
docker_repo_centos_desired_state     | `present` indicates creating the repository file if it doesn't exist on EL/CentOS based systems. Alternative is `absent` (not recommended as it will prevent from installation of **docker** packages).
docker_debian_pre_reqs_desired_state | Desired state for Docker pre-requisite apps on Debian family systems.
docker_repo_debian                   | Docker repo URL for Debain systems. Utilized facts such as `ansible_architecture`.
docker_repo_debain_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
docker_repo_debian_desired_state     | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **docker** packages).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **docker** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.docker
```

For customizing behavior of role (i.e. adding a list of users to be added to docker group - example shown below is adding `ubuntu` && `darkwizard` to `docker` group) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.docker
  vars:
    docker_add_nonroot_users: true
    docker_nonroot_users:
      - darkwizard242
      - ubuntu
```

For customizing behavior of role (i.e. skipping the task that adds a list of users to be added to `docker` group) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.docker
  vars:
    docker_add_nonroot_users: false
```

For customizing behavior of role (i.e. un-installation of **docker-ce, docker-ce-cli, containerd.io** packages) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.docker
  vars:
    docker_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-docker/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
