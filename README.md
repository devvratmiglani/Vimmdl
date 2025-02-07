# Vimm's Lair CLI
> Command line tool to search and download roms from [Vimm's Lair](https://vimm.net/).

`vm-cli` allows to search and download roms published by [Vimm's Lair](https://vimm.net/) through command line interface.

![Demo usage of vm-cli](https://raw.githubusercontent.com/devvratmiglani/Vimmdl/main/vmshowff10.gif)


## Installation

### `Aria2` Dependency
_**Requires [Aria2c](https://github.com/aria2/aria2/releases/tag/release-1.37.0) downloader installed and set in Environment variables**_ 
(or paste the execuatble in path which is already an environment variable)

#Shhhhh🤫! install scoop then

```sh 
scoop install aria2
```
For Ubuntu
```sh 
sudo apt-get install aria2
```
*NOTE: SSL is not supported for linux as of now*
This site may also not load on some browsers with limited certificates

### Installing the package

```sh
pip install git+https://github.com/devvratmiglani/Vimmdl.git
```
For linux distributions you can also try pipx to counter the error message `error: externally-managed-environment`
```
pipx install git+https://github.com/devvratmiglani/Vimmdl.git
```
Installing pipx?
[Install pipx](https://github.com/pypa/pipx#install-pipx)

## Usage

### `consoles` command

List available consoles

```sh
vm consoles
```

### `search` command

Basic usage
```sh
vm search genesis sonic
```
or equivalent alias

```sh
vm search GEN sonic
```
### `download` command

`download` command takes the rom's webpage as argument(s)
```sh
vm download https://vimm.net/vault/9663
```
for simultaneous downloads
```sh
vm download https://vimm.net/vault/70794 https://vimm.net/vault/9663 https://vimm.net/vault/68873
```
## Uninstallation
```sh
pip uninstall vm-cli
```
or pipx
```sh
pipx uninstall vm-cli
```