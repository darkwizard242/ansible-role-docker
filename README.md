# Ansible Role: docker

Role to install (_by default_) `docker` package or uninstall (_if passed as var_) on **Ubuntu**, **Debian** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

```yaml
docker_app: docker
docker_desired_state: present
docker_gpg_key: https://packagecloud.io/docker/docker/gpgkey
docker_repo_desired_state: present
docker_repo_debian: deb [arch=amd64] https://packagecloud.io/docker/docker/any/ any main
docker_repo_debian_filename: docker
docker_repo_el: https://packagecloud.io/docker/docker/el/7/$basearch
docker_repo_el_name: docker
docker_repo_el_description: docker
docker_repo_el_gpgcheck: no
docker_repo_el_repogpgcheck: yes
docker_repo_el_enabled: yes
docker_repo_el_filename: docker
```

Variable `docker_app`: Defines the app to install i.e. **docker**

Variable `docker_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Variable `docker_gpg_key`: GPG key for docker

Variable `docker_repo_desired_state`: State for repo to download docker from. Can either be 'present' or 'absent'.

Variable `docker_repo_debian`: docker's repo link for Debian based systems.

Variable `docker_repo_debian_filename`: Name of file to save for docker's repo in `/etc/apt/sources.list.d/`

Variable `docker_repo_el`: docker's repo link for EL based systems.

Variable `docker_repo_el_name`: docker repo name for EL based systems.

Variable `docker_repo_el_description`: Description for docker's repo for EL based systems.

Variable `docker_repo_el_gpgcheck`: Boolean operation for performing gpg check against gpg key. Can either be **yes** or **no**.

Variable `docker_repo_el_repogpgcheck`: Boolean operation for performing gpg check against docker's repository gpg. Can either be **yes** or **no**.

Variable `docker_repo_el_enabled`: Boolean operation for setting repository to enabled or disabled. Can either be **yes** or **no**.

Variable `docker_repo_el_filename`: Name of file to save for docker's repo in `/etc/yum.repos.d/`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **docker** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
```

For customizing behavior of role (i.e. installation of latest **docker** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
      vars:
        docker_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **docker** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.docker
      vars:
        docker_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-docker/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
