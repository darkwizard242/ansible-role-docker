# Ansible Role: docker

Role to install (_by default_) `docker` package or uninstall (_if passed as var_) on **Ubuntu**, **Debian** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
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
docker_ubuntu_pre_reqs:
  - apt-transport-https
  - ca-certificates
  - curl
  - gnupg-agent
  - software-properties-common
docker_ubuntu_pre_reqs_desired_state: present
docker_repo_ubuntu_gpg_key: https://download.docker.com/linux/ubuntu/gpg
docker_repo_ubuntu: "deb [arch={{ ansible_architecture }}] https://download.docker.com/linux/ubuntu {{ ansible_lsb['codename'] }} stable"
docker_repo_ubuntu_when_x86_64: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_lsb['codename'] }} stable"
docker_repo_ubuntu_filename: docker-ce
docker_repo_ubuntu_desired_state: present
docker_debian_pre_reqs:
  - apt-transport-https
  - ca-certificates
  - curl
  - gnupg2
  - software-properties-common
docker_debian_pre_reqs_desired_state: present
docker_repo_debian_gpg_key: https://download.docker.com/linux/debian/gpg
docker_repo_debian: "deb [arch={{ ansible_architecture }}] https://download.docker.com/linux/debian {{ ansible_lsb['codename'] }} stable"
docker_repo_debian_when_x86_64: "deb [arch=amd64] https://download.docker.com/linux/debian {{ ansible_lsb['codename'] }} stable"
docker_repo_debian_filename: docker-ce
docker_repo_debian_desired_state: present
```

### Variables table:

Variable                             | Value (default)                                                                                                         | Description
------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
docker_apps                          | docker-ce, docker-ce-cli, containerd.io                                                                                 | Name of docker application packages require to be installed i.e. `docker-ce, docker-ce-cli, containerd.io`
docker_apps_desired_state            | present                                                                                                                 | State of the docker_apps packages (i.e. `docker-ce, docker-ce-cli, containerd.io` packages). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
docker_service_name                  | docker                                                                                                                  | Default service name for Docker.
docker_service_desired_state         | restarted                                                                                                               | Desired state for Docker service.
docker_service_desired_boot_enabled  | yes                                                                                                                     | Desired enabled/disabled state for Docker service.
docker_service_desired_boot_enabled  | yes                                                                                                                     | Desired enabled/disabled state for Docker service.
docker_group                         | docker                                                                                                                  | Name of the group that the docker owner will belong to. Any user that requires using docker app requires to be a member in the `docker` group.
docker_group_desired_state           | present                                                                                                                 | `present` indicates creating the group if it doesn't exist. Alternative is `absent`.
docker_user                          | docker                                                                                                                  | Name of the user that the docker will be owned by.
docker_user_home                     | /home/docker                                                                                                            | Home directory for docker user.
docker_user_shell                    | /bin/bash                                                                                                               | Shell for `docker_user`.
docker_user_desired_state            | present                                                                                                                 | `present` indicates creating the user if it doesn't exist. Alternative is `absent`.
docker_centos_pre_reqs               | device-mapper-persistent-data, lvm2                                                                                     | Docker recommends the installation of both these packages on the EL/CentOS docker host system and as such, they are considered pre-requisites.
docker_centos_pre_reqs_desired_state | present                                                                                                                 | Desired state for Docker pre-requisite apps on EL/CentOS systems.
docker_repo_centos                   | <https://download.docker.com/linux/centos/7/$basearch/stable>                                                           | Repository `baseurl` for Docker on EL/CentOS based systems.
docker_repo_centos_gpg_key           | <https://download.docker.com/linux/centos/gpg>                                                                          | Docker GPG required on EL/CentOS based systems.
docker_repo_centos_name              | docker-ce-stable                                                                                                        | Repository name for Docker on EL/CentOS based systems.
docker_repo_centos_description       | Docker CE Stable - $basearch                                                                                            | Description to be added in EL/CentOS based repository file for Docker.
docker_repo_centos_gpgcheck          | yes                                                                                                                     | Boolean for whether to perform gpg check against Docker on EL/CentOS based systems.
docker_repo_centos_enabled           | yes                                                                                                                     | Boolean to set so that Docker repository is enabled on EL/CentOS based systems.
docker_repo_centos_filename          | docker-ce                                                                                                               | Name of the repository file that will be stored at `/yum/sources.list.d/docker-ce.repo` on EL/CentOS based systems.
docker_repo_centos_desired_state     | present                                                                                                                 | `present` indicates creating the repository file if it doesn't exist on EL/CentOS based systems. Alternative is `absent` (not recommended as it will prevent from installation of **docker** packages).
docker_ubuntu_pre_reqs               | apt-transport-https, ca-certificates, curl, gnupg-agent, software-properties-common                                     | Docker recommends the installation of both these packages on the Ubuntu docker host system and as such, they are considered pre-requisites.
docker_ubuntu_pre_reqs_desired_state | present                                                                                                                 | Desired state for Docker pre-requisite apps on Ubuntu systems.
docker_repo_ubuntu_gpg_key           | <https://download.docker.com/linux/ubuntu/gpg>                                                                          | Docker GPG required on Ubuntu based systems.
docker_repo_ubuntu                   | "deb [arch={{ ansible_architecture }}] <https://download.docker.com/linux/ubuntu> {{ ansible_lsb['codename'] }} stable" | Docker repo URL for Ubuntu systems. Utilized facts such as `ansible_architecture`.
docker_repo_ubuntu_when_x86_64       | "deb [arch=amd64] <https://download.docker.com/linux/ubuntu> {{ ansible_lsb['codename'] }} stable"                      | This variable is used only against systems that are x86_64 type as the architecture is overridden to `arch=amd64` as per Docker's Installation steps.
docker_repo_ubuntu_filename          | docker-ce                                                                                                               | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Ubuntu based systems.
docker_repo_ubuntu_desired_state     | present                                                                                                                 | `present` indicates creating the repository file if it doesn't exist on Ubuntu based systems. Alternative is `absent` (not recommended as it will prevent from installation of **docker** packages).
docker_debian_pre_reqs               | apt-transport-https, ca-certificates, curl, gnupg2, software-properties-common                                          | Docker recommends the installation of both these packages on the Ubuntu docker host system and as such, they are considered pre-requisites.
docker_debian_pre_reqs_desired_state | present                                                                                                                 | Desired state for Docker pre-requisite apps on Debain systems.
docker_repo_ubuntu_gpg_key           | <https://download.docker.com/linux/debian/gpg>                                                                          | Docker GPG required on Debian based systems.
docker_repo_debian                   | "deb [arch={{ ansible_architecture }}] <https://download.docker.com/linux/debain> {{ ansible_lsb['codename'] }} stable" | Docker repo URL for Debain systems. Utilized facts such as `ansible_architecture`.
docker_repo_debian_when_x86_64       | "deb [arch=amd64] <<https://download.docker.com/linux/debian> {{ ansible_lsb['codename'] }} stable"                     | This variable is used only against systems that are x86_64 type as the architecture is overridden to `arch=amd64` as per Docker's Installation steps.
docker_repo_debain_filename          | docker-ce                                                                                                               | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
docker_repo_debian_desired_state     | present                                                                                                                 | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **docker** packages).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **docker** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
```

For customizing behavior of role (i.e. utilizing an existing or creating a new user to be added to docker group - example shown below is using `darkwizard242` as a user) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
      vars:
        docker_user: darkwizard242
```

For customizing behavior of role (i.e. un-installation of **docker-ce, docker-ce-cli, containerd.io** packages) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
      vars:
        docker_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-docker/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
