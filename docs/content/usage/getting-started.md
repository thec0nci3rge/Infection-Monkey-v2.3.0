---
title: "Getting Started"
draft: false
pre: "<i class='fas fa-play-circle'></i> "
tags: ["usage"]
---


<!-- TODO: Update screenshots -->

If you haven't deployed the Monkey Island yet, please [refer to our setup documentation](/setup).

## Using Infection Monkey

After deploying the Monkey Island in your environment, navigate to `https://<server-ip>:5000`.

### First-time login

On your first login, you'll be asked to create a username and password for the Monkey Island Server. [See this page for more details](../../setup/accounts-and-security).

### Installing plugins

Infection Monkey's various features are provided by plugins. No plugins are installed out of the box. To install plugins, click on **Plugins** in the navigation bar and install the plugins you want to use. Clicking on "Download All Safe Plugins" will download all plugins that are considered safe to use in production environments.

Read more about plugins [here](/features/plugins).

![Plugin Installation Screen](/images/island/plugins-page/plugin-installation.PNG "Plugin Installation")

### Running Infection Monkey

To get Infection Monkey running as fast as possible, click **Run Monkey**. Optionally, you can configure Infection Monkey before you continue by clicking on **Configuration** (see [how to configure Infection Monkey](../configuration)).

To run Infection Monkey, select one of the following options:

![Run Page](/images/island/run-monkey-page/run-monkey.png "Run Page")

1. Click **From Island** to run Infection Monkey on the Monkey Island Server. This simulates an attacker trying to propagate through your local network from the Monkey Island machine.
2. Click **Manual**  to download and execute Infection Monkey on a machine of your choice.
Follow the instructions and run the generated command on the machine you selected. This simulates an attacker who has breached one of your servers. Infection Monkey will map all accessible machines and their open services, attempt to steal credentials, and use exploits to propagate.

![Run on machine of your choice](/images/island/run-monkey-page/run-monkey-on-machine.png "Run on machine of your choice")

{{% notice tip %}}
If you're running Infection Monkey in an AWS cloud environment, check out [Usage -> Integrations](../../usage/integrations) for information about how it integrates with AWS.
{{% /notice %}}

### Infection map

Next, click **Infection Map** to see Infection Monkey in action.

![Infection Map](/images/island/infection-map-page/infection-map.png "Infection Map")

As the simulation progresses, the map is updated with data on accessible and "hacked" machines. Once
all Infection Monkey Agents have finished propagating, click **Security Report** to see the reports. See [Infection Monkey's Reports](/features/reports) for more info.

![End of Monkey execution](/images/island/infection-map-page/infection-map-with-arrow-to-report.png "End of Monkey execution")

Congratulations, you finished your first successful execution of Infection Monkey 🎉 ! To thoroughly test your network, you can run Infection Monkey from different starting locations and use different configurations.
