---
title: "Setting up vantage6 node"
teaching: 1
exercises: 3
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the hardware requirements for vantage6 node?
- What are the software requirements for vantage6 node?
- How to install vantage6 command line?
- What are the commands available in vantage6?
- How to set up a new vantage6 node?
- How to reset an API key for a node?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the requirements for setting up vantage6 node
- Understand the basic `v6` commands
- Be able to create a new vantage6 node using `v6` commands
- Be able to reset an API key for a node
- Be able to observe the logs of vantage6 node

::::::::::::::::::::::::::::::::::::::::::::::::


Vantage6 node is the software that runs on the machine of the data owner. It allows the data owner to share their data within the vantage6 network in a privacy-preserving way. Also, it is responsible for the execution of the federated learning tasks and the communication with the vantage6 server.

Each organization that is involved in a federated learning collaboration has its own node in that collaboration. They should therefore install the node software on a virtual machine hosted in their own infrastructure. The node should have access to the data that is used in the federated learning collaboration.

This chapter will explain how to set up and run the vantage6 node software.


## Requirements on hardware and software

### Hardware requirements

The minimal hardware requirements are:

- x86 CPU architecture + virtualization enabled
- 1 GB memory
- 50GB+ storage
- Stable and fast Internet connection (1 Mbps+)

The hardware requirements of vantage6 node also depend on the algorithms that the node will run. For example, you need much less compute power for a descriptive statistical algorithm than for a machine learning model.


### Software requirements

You need the following software installed first:

- Operating system: Ubuntu 18.04+ , MacOS Big Sur+, or Windows 10+
- Python
    - Python v3.10 for vantage6 vserion 3.8.0 or higher
    - Python v3.7 for other lower versions of vantage6
    - Highly recommended to create a new, clean virtual or conda environment for vantage6 node
- Docker (always latest version)

⚠️ For Linux users, some [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) may be required. Vantage6 needs to be able to run docker without sudo, and these steps ensure just that.

⚠️ For Windows users, if you are using Docker Desktop, it may be preferable to limit the amount of memory Docker can use - in some cases it may otherwise consume much memory and slow down the system. This may be achieved as described [here](https://stackoverflow.com/questions/62405765/memory-allocation-to-docker-containers-after-moving-to-wsl-2-in-windows).


## Installation

The Python package `vantage6` provides a command-line interface (CLI) to manage vantage6 node.

To install this CLI package, run the command in your Python environment:

```shell
# First go to your python virtual environment
# Then install the package

pip install vantage6
```

To verify the installed CLI, run the command:

```shell
# Verify the installation of vantage6 CLI

v6 node --help
```

If the installation is succesful, it will print out the following messages:

```shell
Usage: v6 node [OPTIONS] COMMAND [ARGS]...

  Manage your vantage6 node instances.

Options:
  --help  Show this message and exit.

Commands:
  attach              Show the node logs in the current console.
  clean               Erase temporary Docker volumes.
  create-private-key  Create and upload a new private key
  files               Prints the location of important node files.
  list                Lists all node configurations.
  new                 Create a new node configuration.
  remove              Delete a node permanently.
  set-api-key         Put a new API key into the node configuration file
  start               Start the node.
  stop                Stop one or all running nodes.
  version             Returns current version of a vantage6 node.
```