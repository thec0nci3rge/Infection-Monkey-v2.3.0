---
title: "How to simulate a ransomware attack"
draft: false
pre: '<i class="fa fa-lock"></i> '
tags: ["howtos", "simulate ransomware"]
---

Infection Monkey's ransomware simulation can help you test the resiliency of
your environment to a ransomware attack. To ensure the safety of your network,
the simulation will only encrypt files that are allowed by you. Follow these
steps to successfully simulate a ransomware attack on your network.

1. **Prepare your ransomware target directory.**

    Create a ransomware target directory and add some files to it that are safe
    to encrypt. The simulation is not recursive, so any sub-directories of the
    target directory will not be touched.

1. **Prepare your environment for a ransomware simulation.**

    Prepare your network by adding the target directory created in the previous
    step to each machine in your environment. This can be done using a
    configuration management tool, such as
    [Ansible](https://docs.ansible.com/ansible/latest/user_guide/) or
    [PsExec](https://theitbros.com/using-psexec-to-run-commands-remotely/), or
    a Windows GPO.

    {{% notice note %}}
For the ransomware simulation to succeed on a machine, the user running the
Infection Monkey Agent must have read and write permissions for the target
directory and its contents.
    {{% /notice %}}

1. **Configure the simulation.**

    In the configuration, specify which directory Infection Monkey should
    target for encryption and provide a file extension that Infection Monkey
    should use to rename the encrypted files.

    Modify the other options as desired.

    ![Ransomware configuration](
    /images/island/configuration-page/ransomware-configuration.png
    "Ransomware configuration")

1. **Configure propagation.**

    If you would like Infection Monkey to propagate through the network,
    [Configure](/usage/configuration/) the network settings and enable one or
    more exploiters.

1. **Run the Agent.**

    Once everything is configured to your liking,
    [run the agent](/usage/getting-started#running-infection-monkey).

1. **Clean up.**

    After the simulation is complete, use the same mechanism you used in step 1
    to either remove the target directory or replace the encrypted files with
    the originals so the simulation can be run again.


### See also
- [Ransomware simulation](/features/ransomware-simulation)
- [Ransomware tutorial](/tutorials/ransomware/)
- [Ransomware reference documentation](/reference/payloads/ransomware)
