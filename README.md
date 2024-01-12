# Vimm's Lair CLI
> CLI tool to search and download roms from [Vimm's Lair](https://vimm.net/).

`vm-cli` allows to search and download roms published by [Vimm's Lair](https://vimm.net/) through command line interface.

![Demo usage of vm-cli][demo-gif]


## Installation

### `Aria2` Dependency
_**Requires [Aria2c](https://github.com/aria2/aria2/releases/tag/release-1.37.0) downloader installed and set in Environment variables**_ 
(or paste the execuatble in path which is already an environment variable)


```sh
## clone the repository
git clone https://github.com/devvratmiglani/Vimmdl.git

## go to main directory (which contains setup.py)
cd .\Vimmdl

## install as
pip install .

```

## Usage example

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
vm download https://vimm.net/vault/70794  https://vimm.net/vault/9663 https://vimm.net/vault/68873
```