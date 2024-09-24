---
title: "Credentials Collectors"
chapter: true
pre: "<i class='fas fa-key'></i> "
---

# Credentials Collectors

Credentials Collectors attempt to steal credentials from systems that the
Infection Monkey Agent has infected.

## Mimicking attackers

In real-world network attacks, malicious actors often attempt to extract
credentials from compromised systems. Stolen credentials enable attackers to
penetrate deeper into the environment in many ways, such as lateral movement,
privilege escalation, data theft, and persistence. To mimic this behavior,
Infection Monkey has multiple plugins, called "credentials collectors", that
steal credentials from compromised hosts.

## How credentials collectors work

When an Infection Monkey Agent is started, it begins the reconnaissance phase
of its attack. The first step in this phase is to use all enabled credentials
collectors to steal credentials. Any stolen credentials are then sent to the
Monkey Island, where they become immediately available for any Agent to use.

After the reconnaissance phase, the Agent will begin the propagation phase and
attempt to compromise other hosts on the network using [exploiters](
/features/exploiters). Some exploiters can use the credentials stolen by credentials
collectors to gain access to other systems on the network. First, the exploiter
will query the Monkey Island to retrieve credentials that were configured by
the user and any credentials that were stolen by credentials collectors. Next,
the exploiters will use the stolen credentials to attempt to authenticate with
a target system. If authentication is successful, the exploiter will execute
the Agent on the target system, spreading the infection throughout the network.

## Techniques
To read more about the techniques Infection Monkey can use to steal
credentials, click the links below:

{{% children /%}}
