---
title: "FAQ"
draft: false
pre: "<i class='fas fa-question'></i> "
weight: 100
---

Below are some of the most common questions we receive about Infection Monkey. If the answer you're looking for isn't here, talk with us [on our Slack channel](https://join.slack.com/t/infectionmonkey/shared_invite/zt-2cm5qiayf-yiEg5RPau0zQhki9xTlORA), email us at [support@infectionmonkey.com](mailto:support@infectionmonkey.com) or [open an issue on GitHub](https://github.com/guardicore/monkey).

{{< table_of_contents >}}

## Where can I get the latest version of Infection Monkey?

For the latest **stable** release, visit [our downloads
page](https://github.com/guardicore/monkey/releases/latest). **This is the
recommended and supported version**!

If you want to see what has changed between versions, refer to the [releases page on GitHub](https://github.com/guardicore/monkey/releases). For the latest development version, visit the [develop version on GitHub](https://github.com/guardicore/monkey/tree/develop).

## I updated to a new version of Infection Monkey and I'm being asked to delete my existing data directory. Why?

The [data directory](/reference/data-directory) contains Infection Monkey's
database and other internal data. For the new version of Infection Monkey to
work flawlessly, a data directory with a compatible structure needs to be set
up.

If you would like to save the data gathered from the Monkey's previous runs,
you can make a backup of your [existing data directory](/reference/data-directory) before deleting it.

## How can I use an old data directory?

To use the data stored in a data directory from an older version, reinstall the
version of the Monkey Island which matches your data directory's version. Then,
copy the backup of your old data directory to the [appropriate location](/reference/data-directory).

## How long does a single Infection Monkey Agent run? Is there a time limit?

The Infection Monkey Agent shuts off either when it can't find new victims or it has exceeded the quota of victims as defined in the configuration.

## How long does it take to stop all running Infection Monkey Agents?

On the Infection Map page, when <b>Kill All Monkeys</b> is pressed, the Agents
try to finish execution safely. This can take up to 2 minutes, but will be much
shorter on average.

## Is Infection Monkey a malware/virus?

Infection Monkey is not malware, but it uses similar techniques to safely
simulate malware on your network.

Because of this, Infection Monkey gets flagged as malware by some antivirus
solutions during installation. If this happens, [verify the integrity of the
downloaded installer](/reference/release-artifact-hashes) first. Then,
create a new folder and disable antivirus scan for that folder. Lastly,
re-install Infection Monkey in the newly created folder.

## How do I reset the Monkey Island password?

In order to reset the Monkey Island password, you'll need to [perform a factory
reset](/howtos/factory-reset).

## Should I run Infection Monkey continuously?

Yes! This will allow you to verify that Infection Monkey identified no new security issues since the last time you ran it.

## Does Infection Monkey require a connection to the internet?

Infection Monkey does not require internet access to function.

If internet access is available, Infection Monkey will use the internet for two purposes:

- To check for updates.
- To check if machines can reach the internet.

### Exactly what internet queries does Infection Monkey perform?

1. While the Monkey Island Server is being set up, a GET request with the deployment
type and version number is sent to the analytics server. This information is
collected to understand which deployment types and versions are no longer used
and can be deprecated.

1. After the Monkey Island starts, a GET request with the deployment type
is sent to the update server to fetch the latest version number and a
download link for it. This information is used by the Monkey Island to
suggest an update if one is available.

1. When you install a plugin it is downloaded from our official repository.

## Logging and how to find logs

### Downloading logs

Both the Agent and Island logs can be downloaded from the Infection Map page. See [how
to download logs](../howtos/download-logs) for more information.

### Log locations

See the [logs reference page](../reference/logs).


## Running Infection Monkey in a production environment

### How much of a footprint does Infection Monkey leave?

The Agent does its best to leave no trace. It will, however, leave
[log files in temporary directories.](/reference/logs/#agent)

### What's the Infection Monkey Agent's impact on system resources usage?

The Infection Monkey Agent uses less than a single-digit percent of CPU time and very low RAM usage. For example, on a single-core Windows Server machine, the Infection Monkey Agent consistently uses 0.06% CPU, less than 80MB of RAM and a small amount of I/O periodically.

If you do experience any performance issues please let us know on [our Slack channel](https://join.slack.com/t/infectionmonkey/shared_invite/zt-2cm5qiayf-yiEg5RPau0zQhki9xTlORA) or [open an issue on GitHub](https://github.com/guardicore/monkey).

### What are the system resource requirements for the Monkey Island?

See the [system requirements](/reference/system-requirements) page.


### Is it safe to use real passwords and usernames in Infection Monkey's configuration?

Absolutely! User credentials are stored encrypted in the Monkey Island Server.
This information can only be seen by individuals that have the credentials to
access the Monkey Island.

### How do you store sensitive information on Monkey Island?

Sensitive data such as passwords, SSH keys and hashes are stored on the Monkey Island's database in an encrypted fashion. This data is transmitted to Infection Monkey Agents in an encrypted fashion (HTTPS) and is not stored locally on victim machines.

When you reset the Monkey Island configuration, the Monkey Island wipes the information.

### How stable are the exploits used by Infection Monkey? Will Infection Monkey crash my systems with its exploits?

Infection Monkey does not use any exploits or attacks that may impact the victim system.

This means we avoid using some powerful (and famous) exploits such as [EternalBlue](https://www.guardicore.com/2017/05/detecting-mitigating-wannacry-copycat-attacks-using-guardicore-centra-platform/). This exploit was used in WannaCry and NotPetya with huge impact, but, because it may crash a production system, we aren't using it.

## After I've set up Monkey Island, how can I execute the Infection Monkey Agent?

Work through our [tutorials](/tutorials/) or see our detailed [getting
started](/usage/getting-started) guide.

## How can I make the Infection Monkey Agent propagate "deeper" into the network?

If you wish to simulate a very "deep" attack into your network, you can increase the *Maximum scan depth* parameter in the configuration. This parameter tells Infection Monkey how far to propagate into your network from the "patient zero" machine.

To do this, change the `Configuration -> Propagation -> General -> Maximum scan depth` configuration option:

![How to increase propagation depth](/images/island/configuration-page/max-scan-depth-configuration.png "How to increase propagation depth")


## Can I limit how Infection Monkey propagates through my network?

Yes! To limit how Infection Monkey propagates through your network, you can:

### Adjust the scan depth

The scan depth limits the number of hops that the Infection Monkey Agent will
spread from patient zero. If you set the scan depth to one, the Agent will only
reach a single hop from the initially infected machine. Scan depth does not
limit the number of devices, just the number of hops.

- **Example**: In this example, the scan depth is set to two. _Host A_ scans the
network and finds hosts _B, C, D_ and _E_. The Infection Monkey Agent
successfully propagates from _Host A_ to _Host C_. Since the scan depth is 2,
the Agent will pivot from _Host C_ and continue to scan other machines on the
network. However, if _Host C_ successfully breaches _Host E_, it will not pivot
further nor continue to scan or propagate.

![What is scan depth](/images/island/others/propagation-depth-diagram.png "What is scan
depth")

### Enable or disable scanning the local subnet

You can find the settings that define how Infection Monkey will scan your
network in `Configuration -> Propagation -> Network analysis`. If enabled,
the `Scan Agent's networks` setting instructs an Agent to scan its entire local subnet.

### Add IPs to the IP allow list

You can specify which hosts you want Infection Monkey Agents to attempt to
scan in the `Configuration -> Propagation -> Network analysis -> Scan target list` section.

### Add IPs to the IP block list

If there are any hosts on your network that you would like to prevent the
Infection Monkey from scanning or exploiting, you can add them to the list of
"Blocked IPs" in `Configuration -> Propagation -> Network analysis -> Blocked IPs`.


## How can I get involved with the project?

Infection Monkey is an open-source project, and we welcome contributions and contributors. Check out the [contribution documentation](/development) for more information.

## About the project 🐵

### How did you come up with Infection Monkey?

Oddly enough, the idea of proactively breaking a network to test its survival wasn't born in the security industry. In 2011, the streaming giant Netflix released Chaos Monkey, a tool designed to randomly disable the company's production servers to verify that they could survive network failures without any customer impact. Netflix's Chaos Monkey became a popular network resilience tool, breaking the network in a variety of failure modes, including connectivity issues, invalid SSL certificates and randomly deleting VMs.

Inspired by this concept, Guardicore Labs developed its own attack simulator - Infection Monkey - to run non-intrusively within existing production environments. The idea was to test the resiliency of modern data centers against attacks and give security teams the insights they need to make informed decisions and enforce tighter security policies. Since its launch in 2017, Infection Monkey has been used by hundreds of information technology teams from across the world to find weaknesses in their on-premises and cloud-based data centers.
