---
title: "Dual Booting"
confluence_id: "159941119"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941119/Dual+Booting"
version: 30
last_modified: "2022-07-21T23:32:09.000Z"
status: "current"
parent_id: "159940644"
labels:
  - "openreview2014"
---

Installing and using multiple operating systems on your computer

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-toc&locale=en_US&version=2)

Warning

Installing any OS over another can potentially **erase all data, programs, and other operating systems** on that system if installed incorrectly. Be sure to have all important documents and files backed up somewhere other than the local hard drive before attempting any kind of installation.

# What Is Dual Booting?

Dual booting is a way of using two or more different operating systems (OS) on a single computer. Typically each operating system is installed on a separate "partition" on the main hard drive. When a hard drive is "partitioned" in this manner, it means that the drive is divided up into different segments of structure and file types that allow the different operating systems to run on it.

Typically when a dual boot computer starts up the user can select which operating system to start into, if you need to change operating systems you will have to reboot the computer and switch to the desired system. Some methods of dual booting utilize a process of "virtualization" in order to allow you to run two systems simultaneously, one operating system inside of another. These options will be outlined below.

Also, some operating systems offer alternatives to partitioning and are described below.

# Why Would I Want To Dual Boot?

There are many reasons people choose to dual boot between two or more systems. You may prefer to use the Mac operating system but need a specific Windows-only program for a course you are taking. You may want to use Windows for access to Office 365 but need to install Linux in order to gain experience using a Unix-like system without having to purchase a second computer. Maybe you are using Linux but there is a particular game you want to play that requires Windows to run. These are only a few examples of the many reasons that you may want or need to dual boot your machine.

# How can I set up my computer for Dual Booting?

Depending on your computer and the operating systems you wish to use there are different approaches for setting up a computer with multiple operating systems.

Be Careful

It is important to note that things like changing the format (reformatting) of a drive or partition **will** erase all data, programs, and operating systems. It is **always** a good idea to have a backup of your data someplace other than your main hard drive. (such as an external hard drive, backup CD/DVDs, or USB flash memory devices.)

# Options For Mac

## Boot Camp

Boot Camp has come preinstalled on Macs since Mac OS 10.5 Leopard was released in 2007. It works on most late model Macs and is the simplest way to get started with Dual Booting multiple operating systems. Boot Camp is designed for use with Windows in particular, although it is possible to use a Boot Camp partition for Linux it is not supported. The link below outlines the process for installing Windows using the Boot Camp method.

[Boot Camp Assistant User Guide](https://support.apple.com/guide/bootcamp-assistant/welcome/mac)

## Virtual Machine Options

Virtual machines allow you to run one operating system "inside of" another. The major advantage to using this method is that it does not require the user to reboot when they want to change the operating system they are using . The disadvantage is that since you are running two operating systems simultaneously your computer's resources are split, there is also an extra piece of software to buy so it is more expensive as well. Below are links to two popular virtualization programs. An important thing to know about these programs is that they require a separate purchase of Windows in addition to your purchase of their software. Neither piece of software will work unless you have a license to install Windows. Oracle also has a product called Virtual Box

[Parallels](https://www.parallels.com/)

[VMware Fusion](https://www.vmware.com/products/fusion.html)

## Manually Partition and Install Multiple Operating Systems

For advanced users, you can boot to the recovery partition of your Mac, erase and repartion your drive, and install whatever operating systems you would like onto the partitions. As this is a procedure that should only be attempted by someone familiar with installing an OS and comfortable using a computer, we have only outlined the process here.

## Crossover and Wine

Wine is a compatibility layer capable of running Windows software within a UNIX system, e.g. MacOS, Ubuntu, Fedora, and other Linux distributions. Wine is a free open source program that can be installed on Unix systems and run a large and ever growing amount of Windows software. It requires a good degree of technical knowledge but is 100% free.

[winehq.org](https://winehq.org)

Crossover is a commercial application of Wine made by a company called Codeweavers designed to simplify the process of using Wine. It runs like an application and in the event you need help offers support for a fee if you need help. Of the paid options, Crossover is the least expensive. Additionally they also offer versions specifically designed for use on Linux in the event you would like to run Windows programs on your Linux machine.

[Codeweavers](https://www.codeweavers.com/)

## VirtualBox

VirtualBox is an open source virtualization program offered by Oracle. It will virtualize multiple OSes on Windows, Mac, and Linux. In addition to virtualizing an OS, VirtualBox also let's you virtualize hardware. This means that if you want to run an older version of an OS that is not supported by your current hardware, you can virtualize the older hardware to run the OS.

Warning

VirtualBox is an advanced piece of software designed for technology professionals such as Software Developers and Information Security Professionals. It has a steep learning curve, if you are setting up multiple OSes for the first time consider one of the other methods first.

# Options for Windows Machines

## Manually Partition and Install Multiple Operating Systems

You can use tools built in to Linux or Windows installers to reformat and repartion a hard drive. This has to be done from an install cd or USB install image, it cannot be done on the drive you are attempting to format. Both  a Windows Install disk and most Linux Install ISO's contain tools to format a drive as part of the installation of the Operating System. Check the documentation for your OS install to learn how to do this.

## Workstation Pro

Workstation Pro is a product from VMware which allows you to run multiple Operating Systems inside of a Windows (or Linux) system using virtualization. It is designed for use by technology professionals such as Developers and Security Researchers and as such is a fairly advanced program. This software is available for a fee.

[Workstation Pro](https://www.vmware.com/products/workstation-pro.html)

## VirtualBox

VirtualBox is an open source virtualization program offered by Oracle. It will virtualize multiple OSes on Windows, Mac, and Linux. In addition to virtualizing an OS, VirtualBox also let's you virtualize hardware. This means that if you want to run an older version of an OS that is not supported by your current hardware, you can virtualize the older hardware to run the OS.

Warning

VirtualBox is an advanced piece of software designed for technology professionals such as Software Developers and Information Security Professionals. It has a steep learning curve, if you are setting up multiple OSes for the first time consider one of the other methods first.

# Useful Linux Links

[DistroWatch](https://distrowatch.com/)
[Linux Distributions](https://su-jsm.atlassian.net/wiki/display/os/Linux+Distributions)
[Live (bootable) Linux CDs](https://su-jsm.atlassian.net/wiki/display/os/Live+%28bootable%29+Linux+CDs)

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-deck&locale=en_US&version=2)

[#top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941119/Dual+Booting#DualBooting-top)
