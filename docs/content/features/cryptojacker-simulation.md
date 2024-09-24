---
title: "Cryptojacker Simulation"
draft: false
description: "Simulate a cryptojacking attack on your network and assess the potential damage."
pre: "<i class='fa fa-coins'></i> "
---

## Summary

Infection Monkey is capable of simulating the behavior of a cryptojacker by
using the CPU and memory of infected systems to perform cryptographic
operations. It can also send network requests that imitate the network traffic
of Bitcoin miners.

## What is a cryptojacker?

One way to acquire cryptocurrency is through a process called "mining". In
order to mine crytocurrency, computers solve puzzles that unlock new coins.
When the coin is unlocked, the computer that solved the puzzle gets to keep the
new coin.

Mining cryptocurrency can be very lucrative, but it comes with hefty costs.
Mining consumes compute resources as well as significant amounts of
electricity. These costs can offset the profits that miners realize, especially
since the value of a cryptocurrency may plummet at any time. Reducing the cost
of mining is a critical in order to reap maximum profits.

To minimize mining costs, some unscrupulous actors utilize cryptojackers. A
Cryptojacker is malware whose purpose is to mine cryptocurrency using someone
else's resources. In essence, cryptojackers steal compute power and electricity
from their victims to benefit attackers.

## How does Infection Monkey simulate a cryptojacker?

Infection Monkey's cryptojacker plugin simulates a cryptojacker by rapidly
calculating cryptographic hashes, exercising the same system components as many
cryptojackers found in the wild. This process is CPU intensive and will, if
left unchecked, [consume an entire CPU Core.](#production-safety) The plugin
can be configured to consume a percentage (from 0 to 100) of a single CPU core
to simulate more or less stealthy cryptojacker variants.

In addition to utilizing the CPU, the cryptojacker plugin can be configured to:
- Consume a percentage of memory (RAM).
- Send network requests that imitate the network traffic of Bitcoin miners.

In order to simulate the network traffic of Bitcoin miners, the cryptojacker
plugin sends
[getblocktemplate](https://developer.bitcoin.org/reference/rpc/getblocktemplate.html)
requests via HTTP over the network to the Island. Since many NIDSs detect
cryptomining activity by looking for these messages, enabling this capability
can help verify NIDSs are working properly.

### Production safety

This component is not considered to be safe for production environments because
it can consume large amounts of CPU and RAM. If the module is configured to
consume excessive amounts of CPU and RAM, it may cause some systems or services
to become unstable. While [some safeguards are in place,](#limitations) users
are advised to use caution when setting the CPU and memory utilization options
so as not to negatively impact production workloads.

### Limitations
#### Limitations on CPU utilization

In order to reduce the likelihood that this module will impact production
workloads, CPU utilization is limited to a single core.

#### Limitations on memory consumption

An internal safeguard prevents this component from consuming more than 90% of
the _available_ RAM. Therefore, while specifying 100% is possible, this
component has a theoretical upper limit that prevents it from consuming more
than 90% of total system RAM.

The reason for this is that when all of a system's RAM has
been consumed, the OS needs to take action to ensure the system does not crash.
The OS will forcefully kill processes and reclaim their RAM until enough free
RAM is available and the system can resume normal operations. Therefore, to
avoid being forcefully killed, the cryptojacker plugin will not consume more
than 90% of a system's free RAM.

## See also
- [Cryptojacker reference documentation](/reference/payloads/cryptojacker)
- [Using Infection Monkey to simulate a NoaBot infection.](https://www.akamai.com/blog/security-research/mirai-based-noabot-crypto-mining)
