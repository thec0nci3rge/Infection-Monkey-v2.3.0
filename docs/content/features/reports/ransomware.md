---
title: "Ransomware report"
draft: false
description: "Provides information about ransomware simulation on your network"
pre: "<i class='fa fa-lock'></i> "
---

{{% notice info %}}
Check out [the documentation for other available reports](/features/reports).
{{% /notice %}}

Infection Monkey can be configured to [simulate a ransomware
attack](/features/ransomware-simulation) on your network. After running,
it generates a **Ransomware Report** that provides you with insight into how
ransomware might behave within your environment.

The report is split into three sections:

- [Breach](#breach)
- [Lateral Movement](#lateral-movement)
- [Attack](#attack)

## Breach

The breach section shows when and where the ransomware infection began.

![Breach](/images/island/reports-page/ransomware-report-breach.png "Breach")


## Lateral movement

The lateral movement section provides information about how the simulated
ransomware was able to propagate through your network.


![Lateral Movement](/images/island/reports-page/ransomware-report-lateral-movement.png "Lateral Movement")


## Attack

The attack section shows the details of what the simulated ransomware
successfully encrypted, including a list of specific files.

![Attack](/images/island/reports-page/ransomware-report-attack.png "Attack")
