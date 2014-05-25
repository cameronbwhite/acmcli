acmcli
======

Command line utility for the @pdxacm

## Installation

You can use pip to download and install straight from github

```sh
pip install git+git://github.com/pdxacm/acmcli.git#egg=acmcli
```

## Examples

### List all people

```sh
acmcli people list
```

### List a person

```sh
acmcli people list bob
```

### Add a person

```sh
acmcli people add bob bobspassword --name "Bob FooBar"
```
