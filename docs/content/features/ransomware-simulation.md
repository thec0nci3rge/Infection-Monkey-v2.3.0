---
title: "Ransomware Simulation"
draft: false
pre: "<i class='fa fa-lock'></i> "
tags: ["usage", "ransomware"]
---

## Summary
Infection Monkey is capable of simulating a ransomware attack on your network
using a set of configurable behaviors. In order to simulate the behavior of
ransomware as accurately as possible, Infection Monkey can [encrypt
user-specified
files](/reference/payloads/ransomware/#files-targeted-for-encryption) using a
[fully reversible algorithm](#how-files-are-encrypted). A number of mechanisms
are in place to ensure that all actions performed by the encryption routine are
safe for production environments.

## What is ransomware?

Cybercriminals often use ransomware, a type of malicious software, to extort
money from individuals or organizations. It works by encrypting the victim's
files or locking them out of their systems, making the data inaccessible. The
attackers then demand a ransom payment in exchange for the decryption key. A
ransomware attack can have severe consequences, including significant downtime,
data loss, and financial damage.

## Encrypting files

### How files are encrypted

In order to ensure that no permanent damage is done to your environment,
Infection Monkey simulates the encryption behavior of ransomware by
adopting safe and easily reversible methods. Data encryption is simulated by
manipulating the files in place with a simple bit flip. The "encrypted" files
are then renamed to have a file extension (`.m0nk3y` by default) appended to
their names. You can even provide no file extension, but take caution: you'll
no longer be able to tell if the file has been encrypted based on the filename
alone. If required, you can "decrypt" your files by simply performing a bit flip
on the files again and renaming them to remove the appended `.m0nk3y` extension.

Flipping a file's bits is sufficient to simulate the encryption behavior of
ransomware, as the data in your files has been manipulated (leaving them
temporarily unusable). Files are then renamed with a new extension appended,
which is similar to the way that many ransomwares behave. As this is a
simulation, your security solutions should be triggered to notify you or
prevent these changes from taking place.

### Files targeted for encryption

Certain precautions are taken to prevent Infection Monkey from accidentally
encrypting files that you didn't intend to encrypt. During the ransomware
simulation, attempts will be made to encrypt only regular files with [targeted
file extensions](/reference/payloads/ransomware/#files-targeted-for-encryption)
in the configured directory. The simulation is not recursive, i.e. it will not
touch any files in sub-directories of the configured directory. Infection
Monkey will not follow any symlinks or shortcuts. If no directory is specified,
no files will be encrypted.

In order to take full advantage of Infection Monkey's ransomware simulation,
add a "ransomware target" directory (containing files that are safe for
encryption) to each machine in your environment. The recommended approach to do
so is by using a configuration management tool, such as
[Ansible](https://docs.ansible.com/ansible/latest/user_guide/) or
[PsExec](https://theitbros.com/using-psexec-to-run-commands-remotely/), or even
a Windows GPO.

## Leaving a README.txt file

Many ransomware packages leave a README.txt file on the victim machine with an
explanation of what has occurred and instructions for paying the attacker. The
Infection Monkey will also leave a README.txt file in the target directory on
the victim machine in order to replicate this behavior.

The README.txt file informs the user that a ransomware simulation has taken
place and that they should contact their administrator. The contents of the
file can be found
[here](https://github.com/guardicore/monkey/blob/master/monkey/agent_plugins/payloads/ransomware/src/ransomware_readme.txt).

## Changing the desktop wallpaper

Often, ransomware will change the desktop wallpaper to immediately grab the
victim's attention, display ransom instructions, and create a sense of urgency
and fear. Infection Monkey can change the desktop wallpaper as a more
conspicuous indication that a ransomware attack has occurred. This feature is
currently only applicable to victim machines running Windows.

When this feature is enabled, the desktop background will be changed to this:

![Ransomware
wallpaper](/images/island/others/ransomware-wallpaper-downsized.png
"Ransomware wallpaper")


## See also
- [How to simulate a ransomware attack](/howtos/simulate-ransomware)
- [Ransomware tutorial](/tutorials/ransomware/)
- [Ransomware reference documentation](/reference/payloads/ransomware)
