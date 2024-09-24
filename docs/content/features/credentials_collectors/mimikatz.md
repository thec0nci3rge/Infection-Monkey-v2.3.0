---
title: "Mimikatz Credentials Collector"
draft: false
description: "Collects credentials from Windows Credential Manager"
tags: ["credentials collector", "mimikatz", "windows"]
pre: "<i class='fa fa-cat'></i> "
---

## Description

[Mimikatz](https://github.com/gentilkiwi/mimikatz) is an open-source tool
widely used by attackers to extract credentials, including plaintext passwords,
hashes, PINs, and Kerberos tickets, from memory. The extracted credentials can
then be used to escalate privileges or move laterally through a network.

Infection Monkey's Mimikatz Credentials Collector uses
[pypykatz](https://github.com/skelsec/pypykatz), a pure-Python implementation
of [mimikatz](https://github.com/gentilkiwi/mimikatz).

![Mimikatz
Configuration](/images/island/configuration-page/mimikatz-credentials-collector-configuration.png
"Mimikatz configuration")
