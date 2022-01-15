# Ansible role: yadm

Install [yadm](https://yadm.io)

## Variables

The variables for this role are pretty straight forward and can be found [here](defaults/main.yml).

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
