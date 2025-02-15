---
title: "Credentials Leak"
draft: false
description: "Assess the impact of a successful phishing attack, insider threat, or other form of credentials leak."
pre: "<i class='fas fa-droplet'></i> "
---

## Overview

Numerous attack techniques (from phishing to dumpster diving) might result in a credential leak,
which can be **extremely costly** as demonstrated in our report [IResponse to IEncrypt](https://web.archive.org/web/20210117224801/https://www.guardicore.com/2019/04/iresponse-to-iencrypt/).

Infection Monkey can help you assess the impact of stolen credentials by automatically searching
where bad actors can reuse these credentials in your network.

## Configuration

- **Propagation -> Credentials** After setting up the Monkey Island, add your users' **real** credentials
(usernames and passwords) here. Don't worry; this sensitive data is not accessible, distributed or used in any way other than being sent to Infection Monkey Agents. You can easily eliminate it by resetting the configuration of your Monkey Island.
- **Propagation -> Credentials -> SSH key pairs list**  When enabled, Infection Monkey automatically gathers SSH keys on the current system.
For this to work, the Monkey Island or initial Agent needs to access SSH key files.
To make sure SSH keys were gathered successfully, refresh the page and check this configuration value after you run Infection Monkey
(content of keys will not be displayed, it will appear as `<Object>`).

## Suggested run mode

Execute Infection Monkey on a chosen machine in your network using the "Manual" run option.
Run Infection Monkey as a privileged user to make sure it gathers as many credentials from the system as possible.

![Exploit password and user lists](/images/island/configuration-page/credentials-configuration.png "Exploit password and user lists")

## Assessing results

To assess the impact of leaked credentials see the Security report. Examine **Security report -> Stolen credentials** to confirm.
