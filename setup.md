---
title: Setup
---

Vantage6 has hardware and software requirements in order to run the vantage6 node(s) and/or server. As for the detailed requirements, please refer to the [vantage6 documentation](https://docs.vantage6.ai/en/main/node/requirements.html).

For now, we just need to focus on the software setup.

## Software setup

Vantage6 requires the following software to be installed on your system. In this lesson, we will explain how to install it:

- Recommended operating system: Ubuntu 20.04+ , MacOS Big Sur+, or Windows 10+
- Docker Desktop (always latest version)
- Conda (latest version)
- Python v3.10
- Python packages:
    - jupyterlab
    - vantage6
    - vantage6-client
    - vantage6-algorithm-tools

### Docker

We recommend installing [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your system, which is the easiest way to install Docker.

You can follow the official instructions to install Docker Desktop on [MacOS](https://docs.docker.com/desktop/install/mac-install/), [Windows](https://docs.docker.com/desktop/install/windows-install/), or [Linux](https://docs.docker.com/desktop/install/linux-install/).

::: callout
#### Linux users
If you have Docker Engine installed on your Linux system and want to use it instead of Docker Desktop, you must make sure that it can run Docker containers without `sudo`. For that, please check the [guide](https://docs.docker.com/engine/install/linux-postinstall/) for more information.
:::

After installing the Docker Desktop, open the application, and then verify the installation by running the command in your terminal:

```bash
docker version
```

```Output
Client:
 Version:           26.1.4
 API version:       1.45
 Go version:        go1.21.11
 Git commit:        5650f9b
 Built:             Wed Jun  5 11:26:02 2024
 OS/Arch:           darwin/arm64
 Context:           desktop-linux

Server: Docker Desktop 4.31.0 (153195)
 Engine:
  Version:          26.1.4
  API version:      1.45 (minimum version 1.24)
  Go version:       go1.21.11
  Git commit:       de5c9cf
  Built:            Wed Jun  5 11:29:12 2024
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.6.33
  GitCommit:        d2d58213f83a351ca8f528a95fbd145f5654e957
 runc:
  Version:          1.1.12
  GitCommit:        v1.1.12-0-g51d5e94
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

The above output shows a successful installation and will vary based on your system. Make sure you see versions for both `Client` and `Server`.

If you cannot see the `Server` version, you have to open the Docker Desktop application first, then run the command again.

### Conda

There are several ways to install Conda on your system. For this lesson, we recommend using Miniconda installer.

Follow the [official instructions](https://docs.anaconda.com/free/miniconda/#quick-command-line-install) to install Miniconda on Windows, MacOS, or Linux.

After installing Miniconda, open a **new** terminal window and verify the installation by running the command:

```bash
conda --version
```

```Output
conda 24.4.0
```

It's OK if the version number is different as long as you can create a Python environment as shown in the next step.

If you see an error message, you may need to restart your terminal or computer.


### Python environment and Python packages

Now build a new Python environment using conda and install the required Python packages.

```bash
# Create a new conda environment
conda create -n v6-workshop python=3.10

# Activate the new environment
conda activate v6-workshop

# Install the required Python packages
pip install jupyterlab vantage6 vantage6-client vantage6-algorithm-tools
```

1. Verify the installation of `jupyterlab`:

```bash
jupyter lab
```

Make sure the JupyterLab opens in your browser.


2. Verify the installation of `vantage6`:

```bash
v6 --help
```

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

If the installation is successful, it will print out a message explaining the usage.

3. Verify the installation of `vantage6-client` and `vantage6-algorithm-tools`:

```bash
python -c "import vantage6.client"
python -c "import vantage6.algorithm"
```

If there is no output and no error message, the installation is successful.



**Congratulations 🎉** You have successfully set up all required software for this lesson!
