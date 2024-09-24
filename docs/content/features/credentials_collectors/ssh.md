---
title: "SSH Credentials Collector"
draft: false
description: "Collects SSH keys from Linux users"
tags: ["credentials collector", "ssh", "linux"]
pre: "<i class='fa fa-terminal'></i> "
---

## Description

SSH public/private key pairs are credentials that allow users to remotely
access systems using the [Secure Shell Protocol
(SSH)](https://en.wikipedia.org/wiki/Secure_Shell). Stealing them could enable
an attacker to:

- Gain access to sensitive systems
- Steal data
- Move laterally through the network
- Escalate their privileges
- Establish a persistent presence

While SSH key pairs can be encrypted to mitigate this risk, many users skip this
step and trade security for convenience. This leaves the SSH keys vulnerable to
theft. Infection Monkey's SSH Credentials Collector seeks out and steals
unprotected SSH key pairs. After compromising a Linux host, the SSH Credentials
Collector will locate the `$HOME/.ssh` directory for each user and attempt to
steal unencrypted SSH key pairs from it.

The SSH Credentials Collector will attempt to steal any key pair matching all
of the following criteria:

- The key pair is stored in `$HOME/.ssh` for any user on the system.
- The key pair is readable by the user running the Infection Monkey Agent.
- The key pair is not encrypted.
- The key pair is stored in one of the supported formats (RSA, DSA, EC, or
  ECDSA).
