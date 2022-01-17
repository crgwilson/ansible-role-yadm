# Ansible role: yadm

Install [yadm](https://yadm.io)

## Variables

The variables for this role are pretty straight forward and can be found [here](defaults/main.yml).

## Modules

This role comes with a bare-bones yadm module similar to ansible's built in `git`
module. You will need `git` installed for it to work, and there aren't a ton of
checks in it at the moment, so YMMV.

```yaml
- name: "Download my dotfiles"
  yadm:
    repo: https://githhub.com/bob/bobs-awesome-dotfiles.git
    dest: /home/bob
    update: true
```

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
