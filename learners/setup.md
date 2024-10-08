---
title: Setup
---

**Before you jump to the installation instructions, consider the following**. This course can be divided into two parts, depending on wether you are only participating in the first part or both parts the setup requirements are different:

- part one, chapters 1 to 4, is about understanding and using vantage6 through the User Interface (UI). In case you are _only_ participating in the part one, you need a web browser and internet in order to access the vantage6 UI. You can skip this setup episode and start the course right away.
- part two, chapters 5 to 8, is more advanced and requires programming experience. Your laptop should be able to run the all the vantage6 software components locally. In this episode, we will guide you through the installation. Please make sure to complete the installation before starting the course.

:::::::::::::::::::::::::::::::::::::::::: callout

### Need additional help?

Have you followed the instructions in this lesson and still have issues with the installation?

Please reach out to us on the [vantage6 Discord channels](https://discord.gg/yAyFf6Y). Or alternatively, you can send an email to [f.martin@iknl.nl](mailto:f.martin@iknl.nl) or [d.smits@esciencecenter.nl](mailto:d.smits@esciencecenter.nl).

::::::::::::::::::::::::::::::::::::::::::::::::::

## Software setup

Vantage6 requires the following software to be installed on your system. In this lesson, we will explain how to install it:

- Recommended operating system: Ubuntu 20.04+ , MacOS Big Sur+, or Windows 10+
- Docker Desktop (Windows, MacOS) or the Docker Engine (Linux)
- Miniconda (latest version)
- Python v3.10
- Python packages:
  - [jupyterlab](https://pypi.org/project/jupyterlab/)
  - [vantage6==4.7.1](https://pypi.org/project/vantage6/)
  - [vantage6-client==4.7.1](https://pypi.org/project/vantage6-client/)
  - [vantage6-algorithm-tools==4.7.1](https://pypi.org/project/vantage6-algorithm-tools/)
- A code editor [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/) or something similar

### Docker

#### Windows and MacOS

We recommend installing Docker Desktop on your system, which is the easiest way to install Docker. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop). Docker Desktop is available for MacOS, Windows, and Linux.

You can follow the official instructions to install Docker Desktop on [MacOS](https://docs.docker.com/desktop/install/mac-install/) or [Windows](https://docs.docker.com/desktop/install/windows-install/).

#### Linux

We recommend installing the Docker Engine on your Linux system. You can follow the official instructions to install Docker Engine for [Linux](https://docs.docker.com/desktop/install/linux-install/). After the installation, make sure that it can run Docker containers without `sudo`. Please follow the instructions in [this guide](https://docs.docker.com/engine/install/linux-postinstall/) to set that up.

Alternatively, you can install Docker Desktop on your Linux system. You can follow the official instructions to install Docker Desktop for [Linux](https://docs.docker.com/desktop/install/linux-install/).

---

After installing the Docker Desktop or Docker engine, open your terminal, and then verify the installation by running the command:

```bash
docker run hello-world
```

```Output
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### (Mini)conda

There are several ways to install Conda on your system. For this course, we recommend using Miniconda installer. However if you already have Anaconda installed, you can use it as well.

Follow the [official instructions](https://docs.anaconda.com/free/miniconda/) to install Miniconda on Windows, MacOS, or Linux.

After installing Miniconda, open a **new** terminal window and verify the installation by running the command:

```bash
conda --version
```

```Output
conda 24.4.0
```

It's OK if the version number is different as long as you can create a Python environment as shown in the next step.

If you see an error message, you may need to restart your terminal or even your computer.

### Python environment and Python packages

Now build a new Python environment using conda and install the required Python packages.

```bash
# Create a new conda environment
conda create -n v6-workshop python=3.10

# Activate the new environment
conda activate v6-workshop

# Install the required Python packages
pip install jupyterlab vantage6==4.7.1 vantage6-client==4.7.1 vantage6-algorithm-tools==4.7.1
```

1. Verify the installation of `vantage6`:

```bash
v6 --help
```

If the installation is successful, it will print out a message explaining the usage.

```Output
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

2. Verify the installation of `jupyterlab`:

```bash
jupyter lab
```

Make sure JupyterLab opens in your browser.

3. Verify the installation of `vantage6-client` and `vantage6-algorithm-tools`:
Now create a new jupyter notebook in your jupyter lab environment and run a cell
with the following code:

```python
 import vantage6.client
import vantage6.algorithm.tools
```

If there is no output and no error message, the installation is successful.

## Create Dockerhub account

In this course, we will build our own vantage6 algorithms. Part of these exercises will
be to share the algorithm Docker images online. For this, you need a Dockerhub account.
Please create one [here](https://app.docker.com/signup) on the Dockerhub website.
Make sure to remember your username and password!

**Congratulations 🎉** You have successfully set up all required software for this lesson!
