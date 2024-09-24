---
title: "Chrome Credentials Collector"
draft: false
description: "Collects credentials from Chrome-based browsers"
tags: ["credentials collector", "chrome", "linux", "windows"]
pre: "<i class='fa-brands fa-chrome'></i> "
---

## Description

By default, Chromium-based browsers store saved usernames and passwords in a
recoverable format. Stealing browser credentials can enable access to sensitive
personal and business accounts leading to data exfiltration, identity theft,
financial loss, etc. Users often reuse credentials across accounts which can
support lateral movement and persistence.

The Chrome Credentials Collector steals saved credentials from Chromium-based
browsers. On Linux, it targets Google Chrome and Chromium. On Windows, it
targets Google Chrome and Microsoft Edge.
