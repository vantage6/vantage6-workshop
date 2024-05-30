---
title: "Setting up a vantage6 node"
teaching: 1.5
exercises: 4
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the requirements for a vantage6 node?
- How to install vantage6 command line interface?
- What are the commands available in the vantage6 CLI?
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


Vantage6 node is the software that runs on a data station. It allows the data owner to share their data within the vantage6 network in a privacy-preserving way. Also, it is responsible for the execution of the federated learning tasks and the communication with the vantage6 server.

Each organization that is involved in a federated learning collaboration has its own node in that collaboration. They should therefore install the node software on a virtual machine hosted in their own infrastructure. The node should have access to the data that is used in the federated learning collaboration.

This chapter will explain how to set up and run the vantage6 node software.


## Requirements on hardware and software

### Hardware requirements

The minimal hardware requirements are:

- x86 CPU architecture + virtualization enabled. This setting is usually the default in most of the systems.
- 1 GB memory
- Sufficient storage to install Python, docker and vantage6, and to store the required docker images (50GB+ recommended).
- Stable and fast Internet connection (1 Mbps+).

The hardware requirements of vantage6 node also depend on the algorithms that the node will run. For example, you need much less compute power for a descriptive statistical algorithm than for a machine learning model.

Even though a vantage6 node can be installed and run on Linux, Windows and Mac, Linux is the recommended OS.


### Software requirements

The following software must be installed before installing the vantage6 node:

- Operating system: Ubuntu 18.04+ , MacOS Big Sur+, or Windows 10+
- Python
    - Python v3.10 for vantage6 version 3.8.0 or higher
    - Python v3.7 for other lower versions of vantage6
    - Highly recommended to create a new, clean virtual or conda environment for vantage6 node
- Docker (always latest version)

::: callout
## ⚠️ Docker installation 
  - For Linux users, some [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) may be required. Vantage6 needs to be able to run docker without sudo, and these steps ensure just that.

  - For Windows users, if you are using Docker Desktop, it may be preferable to limit the amount of memory Docker can use - in some cases it may otherwise consume much memory and slow down the system. This may be achieved as described [here](https://stackoverflow.com/questions/62405765/memory-allocation-to-docker-containers-after-moving-to-wsl-2-in-windows).
:::

## Installation

The Python package `vantage6` provides a command-line interface (CLI) to manage the vantage6 infrastructure.

To install this CLI package, run the command in your Python environment,

```bash
# First go to your python virtual environment

conda activate myenv

# Then install the package

pip install vantage6
```

To verify the installed CLI, run the command,

```bash
v6
```
or
```bash
v6 --help
```

If the installation is successful, it will print out a message explaining the CLI usage.


::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Install vantage6 CLI

Check the hardware and software requirements and install the vantage6 CLI package in your Python environment.

Make sure you create a new virtual or conda environment for vantage6 CLI installation.

Run the command `v6 --help` to verify the installation. What are the available commands?

::: solution

If the vantage6 CLI has been correctly installed, by running:

```bash
v6 --help
```

the following messages will be printed:

```bash

Usage: v6 [OPTIONS] COMMAND [ARGS]...

  The `v6` command line interface allows you to manage your vantage6
  infrastructure.

  It provides a number of subcommands to help you with this task.

Options:
  --help  Show this message and exit.

Commands:
  algorithm        Manage your vantage6 algorithms.
  algorithm-store  Manage your vantage6 algorithm store server instances.
  dev              Quickly manage a test network with a server and...
  node             Manage your vantage6 node instances.
  server           Manage your vantage6 server instances.
  test             Execute tests on your vantage6 infrastructure.
```
You can see that vantage6 CLI provides commands to manage the server (`v6 server`), node (`v6 node`) and algorithms (`v6 algorithm`) and algorithm store (`algorithm-store`).

:::

::::::::::::::::::::::::::::::::::::::::::::::::


## `v6 node` commands

The vantage6 CLI provides the `v6 node` command to manage the vantage6 node instances.

To see how to use it, run the command `v6 node --help` in your terminal, and it will print out the following messages:

```bash
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

For example, to create a new node configuration, you can run the command `v6 node new`, then you can start the new node by running `v6 node start`, and then stop the node with `v6 node stop` command.

⚠️ Please make sure Docker is running when you're using the `v6 node` commands.


## Configure a new node

We will now create a new node configuration using the `v6 node new` command. 
This process will create a configuration `yaml` file that the vantage6-node requires to run.

Let's run the command:

```bash
v6 node new
```

The command will show a wizard to guide you through the configuration process in a step-by-step manner:

```bash
? Please enter a configuration-name: node1
? Enter given api-key: ***
? The base-URL of the server: https://portal.cotopaxi.vantage6.ai/
? Enter port to which the server listens: 5000
? Path of the api: /api
? Task directory path: ***/vantage6/node/node1
? Do you want to add a database? Yes
? Enter unique label for the database: default
? Database URI: ***/data.csv
? Database type: csv
? Do you want to add a database? Yes
? Enter unique label for the database: default
? Database URI: ***/data.sql
? Database type: sql
? Do you want to add a database? No
? Which level of logging would you like? DEBUG
? Do you want to connect to a VPN server? No
? Enable encryption? No
```

It is important to note the meaning of following configuration parameters:
  - The `api-key` is the API key that you received from the vantage6 server administrator. It is used to authenticate the node at the server.
  - The `base-URL of the server` is the URL of the vantage6 server. If you are running the server on your local machine using Docker, the URL has to be set to `http://host.docker.internal`.
  - The `path of the api` is the path of the API of the server. It is usually `/api`.
  - The `database URI` is the path of the database file. You can add multiple databases by repeating the process. The database type can be 'csv', 'parquet', 'sql', 'sparql', 'excel' or 'omop'.


To see all configuration options, please check https://docs.vantage6.ai/en/main/node/configure.html#all-configuration-options.

When you finish the configuration, you will see the following message:

```bash
[info ] - New configuration created: ***/vantage6/node/node1.yaml
[info ] - You can start the node by running v6 node start
```

It means that the node configuration file is created successfully, and it also gives the path of the configuration file.


### Where is the node configuration file?

You can always use the `v6 node files` command to check the location of the node configuration file:

```bash
v6 node files
```

It will ask you which node you want to see. You can choose the one you just created:

```bash
? Select the configuration you want to use: (Use arrow keys)
 » node1
   node2
   node3
```

In the printed message the path to the configuration file.

You can see that not only the path of the configuration file is printed out, but also the locations of the log file, the data folders and the database files are shown.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Create a new node configuration

1. Create a new node configuration using the `v6 node new` command.
2. Find the path to the configuration file using the `v6 node files` command. Open the configuration file with a text editor and check the configuration options. Are they correct?

::::::::::::::::::::::::::::::::::::::::::::::::

## Start a node

Before starting a vantage6 node, you need to make sure the vantage6 server is running and the internet connection is stable.

To start a node, you can run the command `v6 node start`:

```bash
v6 node start
```

It will ask you which node you want to start. You can choose the one you just created:

```bash
[info ] - Starting node...
[info ] - Finding Docker daemon
? Select the configuration you want to use: (Use arrow keys)
 » node1
   node2
   node3
```

then it will start the node and print out the following messages:

```bash
? Select the configuration you want to use: node1
[info ] - Starting node...
[info ] - Finding Docker daemon
[info ] - Checking that data and log dirs exist
[info ] - Connecting to server at 'http://localhost:5000/api'
[info ] - Pulling latest node image 'harbor2.vantage6.ai/infrastructure/node:4.5'
[info ] - Creating file & folder mounts
[warn ] - private key file provided ***/private_key.pem, but does not exists
[info ] - Setting up databases
[info ] -   Processing csv database default: ***/data.csv
[debug] -   - non file-based database added
[info ] -   Processing csv database default: ***/data.csv
[debug] -   - non file-based database added
[info ] - Running Docker container
[info ] - Node container was successfully started!
[info ] - To see the logs, run: v6 node attach --name node1
```

🎉 Now, the node is started successfully!


## Watch the logs

You can show the logs in the current console by running the command:

```bash
v6 node attach --name node1
```

then it will print out the logs of the node in the console:

```bash
2024-05-24 14:15:14 - context        - INFO     - ---------------------------------------------
2024-05-24 14:15:14 - context        - INFO     -  Welcome to
2024-05-24 14:15:14 - context        - INFO     -                   _                     __
2024-05-24 14:15:14 - context        - INFO     -                  | |                   / /
2024-05-24 14:15:14 - context        - INFO     - __   ____ _ _ __ | |_ __ _  __ _  ___ / /_
2024-05-24 14:15:14 - context        - INFO     - \ \ / / _` | '_ \| __/ _` |/ _` |/ _ \ '_ \
2024-05-24 14:15:14 - context        - INFO     -  \ V / (_| | | | | || (_| | (_| |  __/ (_) |
2024-05-24 14:15:14 - context        - INFO     -   \_/ \__,_|_| |_|\__\__,_|\__, |\___|\___/
2024-05-24 14:15:14 - context        - INFO     -                             __/ |
2024-05-24 14:15:14 - context        - INFO     -                            |___/
2024-05-24 14:15:14 - context        - INFO     -
2024-05-24 14:15:14 - context        - INFO     -  --> Join us on Discord! https://discord.gg/rwRvwyK
2024-05-24 14:15:14 - context        - INFO     -  --> Docs: https://docs.vantage6.ai
2024-05-24 14:15:14 - context        - INFO     -  --> Blog: https://vantage6.ai
2024-05-24 14:15:14 - context        - INFO     - ------------------------------------------------------------
2024-05-24 14:15:14 - context        - INFO     - Cite us!
2024-05-24 14:15:14 - context        - INFO     - If you publish your findings obtained using vantage6,
2024-05-24 14:15:14 - context        - INFO     - please cite the proper sources as mentioned in:
2024-05-24 14:15:14 - context        - INFO     - https://vantage6.ai/vantage6/references
2024-05-24 14:15:14 - context        - INFO     - ------------------------------------------------------------
2024-05-24 14:15:14 - context        - INFO     - Started application vantage6
2024-05-24 14:15:14 - context        - INFO     - Current working directory is '/'
2024-05-24 14:15:14 - context        - INFO     - Successfully loaded configuration from '/mnt/config/node1.yaml'
2024-05-24 14:15:14 - context        - INFO     - Logging to '/mnt/log/node_user.log'
2024-05-24 14:15:14 - context        - INFO     - Common package version '4.5.0'
2024-05-24 14:15:14 - context        - INFO     - vantage6 version '4.5.0'
2024-05-24 14:15:14 - context        - INFO     - vantage6 version '4.5.0'
2024-05-24 14:15:14 - context        - INFO     - Node package version '4.5.0'
2024-05-24 14:15:14 - node           - INFO     - Connecting server: http://host.docker.internal:5000/api
2024-05-24 14:15:14 - node           - DEBUG    - Authenticating
2024-05-24 14:15:14 - common         - DEBUG    - Authenticating node...
2024-05-24 14:15:17 - common         - INFO     - Successfully authenticated
2024-05-24 14:15:17 - common         - DEBUG    - Making request: GET | http://host.docker.internal:5000/api/node/18 | None
2024-05-24 14:15:17 - common         - DEBUG    - Making request: GET | http://host.docker.internal:5000/api/organization/2 | None
2024-05-24 14:15:17 - node           - INFO     - Node name: ZEPPELIN - Small Organization
2024-05-24 14:15:17 - common         - DEBUG    - Making request: GET | http://host.docker.internal:5000/api/collaboration/1 | None
2024-05-24 14:15:17 - node           - WARNING  - Disabling encryption!
2024-05-24 14:15:17 - node           - INFO     - Setting up proxy server
2024-05-24 14:15:17 - node           - INFO     - Starting proxyserver at 'proxyserver:80'
2024-05-24 14:15:17 - node           - INFO     - Setting up VPN client container
2024-05-24 14:15:17 - vpn_manager    - INFO     - Updating VPN images...
2024-05-24 14:15:17 - vpn_manager    - DEBUG    - Pulling Alpine image
2024-05-24 14:15:19 - addons         - DEBUG    - Succeeded to pull image harbor2.vantage6.ai/infrastructure/alpine:4.5
2024-05-24 14:15:19 - vpn_manager    - DEBUG    - Pulling VPN client image
2024-05-24 14:15:21 - addons         - DEBUG    - Succeeded to pull image harbor2.vantage6.ai/infrastructure/vpn-client:4.5
2024-05-24 14:15:21 - vpn_manager    - DEBUG    - Pulling network config image
2024-05-24 14:15:33 - addons         - DEBUG    - Succeeded to pull image harbor2.vantage6.ai/infrastructure/vpn-configurator:4.5
2024-05-24 14:15:33 - vpn_manager    - INFO     - Done updating VPN images
2024-05-24 14:15:33 - vpn_manager    - DEBUG    - Used VPN images:
2024-05-24 14:15:33 - vpn_manager    - DEBUG    -   Alpine: harbor2.vantage6.ai/infrastructure/alpine:4.5
2024-05-24 14:15:33 - vpn_manager    - DEBUG    -   Client: harbor2.vantage6.ai/infrastructure/vpn-client:4.5
2024-05-24 14:15:33 - vpn_manager    - DEBUG    -   Config: harbor2.vantage6.ai/infrastructure/vpn-configurator:4.5
2024-05-24 14:15:33 - node           - WARNING  - VPN subnet is not defined! VPN disabled.
2024-05-24 14:15:33 - node           - INFO     - No SSH tunnels configured
2024-05-24 14:15:33 - node           - INFO     - No squid proxy configured
2024-05-24 14:15:33 - node           - DEBUG    - Setting up the docker manager
2024-05-24 14:15:33 - docker_manager - DEBUG    - Initializing DockerManager
2024-05-24 14:15:33 - docker_manager - WARNING  - No policies on allowed algorithms have been set for this node!
2024-05-24 14:15:33 - docker_manager - WARNING  - This means that all algorithms are allowed to run on this node.
2024-05-24 14:15:33 - docker_manager - DEBUG    - Databases: {'default': {'uri': '/data/data.csv', 'is_file': False, 'type': 'csv', 'env': {}}}
2024-05-24 14:15:33 - node           - DEBUG    - Creating websocket connection with the server
2024-05-24 14:15:33 - node           - INFO     - Connected to host=http://host.docker.internal on port=5000
2024-05-24 14:15:33 - node           - DEBUG    - Starting thread to ping the server to notify this node is online.
2024-05-24 14:15:33 - network_man..  - DEBUG    - Connecting vantage6-node1-user to network 'vantage6-node1-user-net'
2024-05-24 14:15:33 - socket         - INFO     - (Re)Connected to the /tasks namespace
2024-05-24 14:15:33 - common         - DEBUG    - Making request: GET | http://host.docker.internal:5000/api/run | {'state': 'open', 'node_id': 18, 'include': 'task'}
2024-05-24 14:15:34 - node           - DEBUG    - Start thread for sending messages (results)
2024-05-24 14:15:34 - node           - DEBUG    - Waiting for results to send to the server
2024-05-24 14:15:34 - node           - DEBUG    - Starting thread for incoming messages (tasks)
2024-05-24 14:15:34 - node           - DEBUG    - Listening for incoming messages
2024-05-24 14:15:34 - node           - INFO     - Init complete
2024-05-24 14:15:34 - node           - INFO     - Waiting for new tasks....
2024-05-24 14:15:34 - socket         - INFO     - Node <ZEPPELIN - Small Organization> joined room <collaboration_1>
2024-05-24 14:15:34 - socket         - INFO     - Node <ZEPPELIN - Small Organization> joined room <collaboration_1_organization_2>
2024-05-24 14:15:34 - socket         - INFO     - Websocket connection established
2024-05-24 14:15:34 - node           - DEBUG    - task_results: []
2024-05-24 14:15:34 - node           - INFO     - Received 0 tasks
2024-05-24 14:15:34 - socket         - DEBUG    - Tasks synced again with the server...
2024-05-24 14:15:34 - docker_manager - ERROR    - Database with label default is not a file. Cannot determine columns without query
2024-05-24 14:15:34 - node           - DEBUG    - Sharing node configuration: {'encryption': False, 'allowed_algorithms': 'all', 'database_labels': ['default', 'default'], 'database_types': {'db_type_default': 'sql'}, 'database_columns': {'columns_default': []}}
```

From there, you can see the running status of the node, the connection to the server, the databases, the websocket connection, and the incoming tasks.


::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: Start a node and watch the logs

1. Start the node you just created using the `v6 node start` command.
2. Watch the logs of the node using the `v6 node attach --name xxx` command. Observe the logs and see if the node is running correctly.

::::::::::::::::::::::::::::::::::::::::::::::::

## Stop a node

To stop a running node, you can run the command:

```bash
v6 node stop
```

then it will ask you which node you want to stop:

```bash
? Select the node you wish to stop: (Use arrow keys)
 » vantage6-node1-user
```

after you choose the node, it will print out the following messages:

```bash
? Select the node you wish to stop: vantage6-node1-user
2024-05-24 16:29:11 - context        - INFO     - ---------------------------------------------
2024-05-24 16:29:11 - context        - INFO     -  Welcome to
2024-05-24 16:29:11 - context        - INFO     -                   _                     __
2024-05-24 16:29:11 - context        - INFO     -                  | |                   / /
2024-05-24 16:29:11 - context        - INFO     - __   ____ _ _ __ | |_ __ _  __ _  ___ / /_
2024-05-24 16:29:11 - context        - INFO     - \ \ / / _` | '_ \| __/ _` |/ _` |/ _ \ '_ \
2024-05-24 16:29:11 - context        - INFO     -  \ V / (_| | | | | || (_| | (_| |  __/ (_) |
2024-05-24 16:29:11 - context        - INFO     -   \_/ \__,_|_| |_|\__\__,_|\__, |\___|\___/
2024-05-24 16:29:11 - context        - INFO     -                             __/ |
2024-05-24 16:29:11 - context        - INFO     -                            |___/
2024-05-24 16:29:11 - context        - INFO     -
2024-05-24 16:29:11 - context        - INFO     -  --> Join us on Discord! https://discord.gg/rwRvwyK
2024-05-24 16:29:11 - context        - INFO     -  --> Docs: https://docs.vantage6.ai
2024-05-24 16:29:11 - context        - INFO     -  --> Blog: https://vantage6.ai
2024-05-24 16:29:11 - context        - INFO     - ------------------------------------------------------------
2024-05-24 16:29:11 - context        - INFO     - Cite us!
2024-05-24 16:29:11 - context        - INFO     - If you publish your findings obtained using vantage6,
2024-05-24 16:29:11 - context        - INFO     - please cite the proper sources as mentioned in:
2024-05-24 16:29:11 - context        - INFO     - https://vantage6.ai/vantage6/references
2024-05-24 16:29:11 - context        - INFO     - ------------------------------------------------------------
2024-05-24 16:29:11 - context        - INFO     - Started application vantage6
2024-05-24 16:29:11 - context        - INFO     - Current working directory is '/Users/clgeng/Library/Application Support/vantage6/node'
2024-05-24 16:29:11 - context        - INFO     - Successfully loaded configuration from '/Users/clgeng/Library/Application Support/vantage6/node/node1.yaml'
2024-05-24 16:29:11 - context        - INFO     - Logging to '/Users/clgeng/Library/Logs/vantage6/node/node1/node_user.log'
2024-05-24 16:29:11 - context        - INFO     - Common package version '4.5.0'
2024-05-24 16:29:11 - context        - INFO     - vantage6 version '4.5.0'
[info ] - Stopped the vantage6-node1-user Node.
```

## Update the API key of your node

If you get a new API key for a node from the server administrator, or if the organization administrator creates a new API key, you need to reset the API key in the node configuration file.

For that, you can run the command:

```bash
v6 node set-api-key
```

then it will ask you which node you want to update the API key of:

```bash
? Select the configuration you want to use: (Use arrow keys)
 » node1
   node2
   node3
```

after you choose the node, it will ask you to enter the new API key:

```bash
? Select the configuration you want to use: node1
? Please enter your new API key: the-new-api-key-you-received-from-the-server-administrator
2024-05-24 16:28:16 - context        - INFO     - ---------------------------------------------
2024-05-24 16:28:16 - context        - INFO     -  Welcome to
2024-05-24 16:28:16 - context        - INFO     -                   _                     __
2024-05-24 16:28:16 - context        - INFO     -                  | |                   / /
2024-05-24 16:28:16 - context        - INFO     - __   ____ _ _ __ | |_ __ _  __ _  ___ / /_
2024-05-24 16:28:16 - context        - INFO     - \ \ / / _` | '_ \| __/ _` |/ _` |/ _ \ '_ \
2024-05-24 16:28:16 - context        - INFO     -  \ V / (_| | | | | || (_| | (_| |  __/ (_) |
2024-05-24 16:28:16 - context        - INFO     -   \_/ \__,_|_| |_|\__\__,_|\__, |\___|\___/
2024-05-24 16:28:16 - context        - INFO     -                             __/ |
2024-05-24 16:28:16 - context        - INFO     -                            |___/
2024-05-24 16:28:16 - context        - INFO     -
2024-05-24 16:28:16 - context        - INFO     -  --> Join us on Discord! https://discord.gg/rwRvwyK
2024-05-24 16:28:16 - context        - INFO     -  --> Docs: https://docs.vantage6.ai
2024-05-24 16:28:16 - context        - INFO     -  --> Blog: https://vantage6.ai
2024-05-24 16:28:16 - context        - INFO     - ------------------------------------------------------------
2024-05-24 16:28:16 - context        - INFO     - Cite us!
2024-05-24 16:28:16 - context        - INFO     - If you publish your findings obtained using vantage6,
2024-05-24 16:28:16 - context        - INFO     - please cite the proper sources as mentioned in:
2024-05-24 16:28:16 - context        - INFO     - https://vantage6.ai/vantage6/references
2024-05-24 16:28:16 - context        - INFO     - ------------------------------------------------------------
2024-05-24 16:28:16 - context        - INFO     - Started application vantage6
2024-05-24 16:28:16 - context        - INFO     - Current working directory is '***/vantage6/node'
2024-05-24 16:28:16 - context        - INFO     - Successfully loaded configuration from '***/vantage6/node/node1.yaml'
2024-05-24 16:28:16 - context        - INFO     - Logging to '***/vantage6/node/node1/node_user.log'
2024-05-24 16:28:16 - context        - INFO     - Common package version '4.5.0'
2024-05-24 16:28:16 - context        - INFO     - vantage6 version '4.5.0'
2024-05-24 16:28:16 - context        - INFO     - vantage6 version '4.5.0'
[info ] - Your new API key has been uploaded to the config file ***/vantage6/node/node1.yaml.
```

When you finish the process, the node configuration file will be updated with the new API key.

To make the new API key effective, you need to restart the node by running the command `v6 node stop` and then `v6 node start`.


::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: Reset the API key of a node

1. How do you update the API key of a node? Try to update the API key of the node you just created, without using the `v6 node set-api-key` command.
2. How do you make sure the new API key is effective?

::: solution
1. We can update the API key in the configuration file:
  - Run the `v6 node files` command to locate the configuration file.
  - Open the configuration file and write the new API key in the `api_key` field.
  - Stop the node with the `v6 node stop` command.
  - Restart the node with the `v6 node start` command.

2. In order to verify the effectiveness of the API key change, we can restart the node with active logging:
```bash
v6 node start --attach
```

In the log, we have to look for the node authentication message:

```bash
2024-05-30 14:41:13 - common         - DEBUG    - Authenticating node...
2024-05-30 14:41:13 - common         - INFO     - Successfully authenticated

```

:::

::::::::::::::::::::::::::::::::::::::::::::::::



::::::::::::::::::::::::::::::::::::: keypoints
- Install the vantage6 CLI package by running `pip install vantage6`.
- Use the `v6 --help` command to see the available commands of the vantage6 CLI.
- Use the `v6 node` command to manage the vantage6 node instances.
- Use the `v6 node new` command to create a new node configuration.
- Use the `v6 node start` command to start a node.
- Use the `v6 node attach --name xxx` command to show the logs of the node `xxx`.
- Use the `v6 node stop` command to stop a node.
- Use the `v6 node set-api-key` command to reset the API key of a node.
- Use the `v6 node files` command to check the location of the node configuration file.
- The commands similar to the ones presented for the node are also available for `v6 server` and `v6 algorithm-store`. 
::::::::::::::::::::::::::::::::::::::::::::::::