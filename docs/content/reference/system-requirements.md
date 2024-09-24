---
title: "System requirements"
draft: false
pre: '<i class="fas fa-laptop"></i> '
tags: ["setup", "reference", "windows", "linux"]
---

{{< table_of_contents >}}

## Monkey Island


### Supported operating systems

#### Linux

{{% notice info %}}
AppImages require
[FUSE](https://www.kernel.org/doc/html/next/filesystems/fuse.html) version 2 to
run.
{{% /notice %}}

The Infection Monkey AppImage package should run on most modern Linux
distributions. The latest version of the Monkey Island has been tested with the
following distributions:

- BlackArch 2023.04.01
- CentOS/Rocky/RHEL 8+
- Debian 11
- Kali 2023.1
- Parrot 5.2
- openSUSE Leap 15.4
- Ubuntu Bionic 18.04, Focal 20.04, Jammy 22.04
- WSL 2

#### Windows

The latest version of the Monkey Island has been tested with the following
versions of Microsoft Windows:
- Windows Server 2016
- Windows Server 2019
- Windows 10

### Hardware requirements
#### Supported architectures
The Monkey Island runs on x86-64 processors only.

#### Linux
**CPU**: Intel(R) Xeon(R) CPU @ 2.20GHz or better

**CPU Cores**: 2

**RAM**: 4GB

#### Windows
**CPU**: Intel(R) Xeon(R) CPU @ 2.20GHz or better

**CPU Cores**: 4

**RAM**: 6GB

## Agent

### Supported operating systems
#### Linux

The Monkey Agent should run on any Linux distribution with a version of
GLIBC >= 2.23[^1]. The latest version of Infection Monkey has been tested
with the following distributions:

- CentOS/Rocky/RHEL 8+
- Debian 9+
- Kali 2019+
- openSUSE 15+
- Ubuntu 16+

#### Windows

- Windows server 2012+
- Windows server 2012_R2+
- Windows 7/Server 2008_R2 (if
  [KB2999226](https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows)
  is installed.)
- Windows 10

### Hardware requirements
#### Supported architectures
The Monkey Agent runs on x86-64 processors only.

[^1]: The Infection Monkey Agent was built with the oldest version of GLIBC
    that is compatible with Python 3.11 (i.e. version 2.23). Since GLIBC is
    forward but not backwards compatible,  the agent will not run on versions
    of Linux with GLIBC < 2.23.
