---
title: "vantage6 basics"
---

::: questions
-   Why to use vantage6?
-   How does vantage6 work?
-   How do federated algorithms run in vantage6?
-   What will be available in vantage6 in the future?
:::

::: objectives
-   List the high-level infrastructure components of vantage6 (server, client, node)
-   Understand the added value of vantage6
-   Understand that there are different actors in the vantage6 network
-   Understand that the vantage6 server does not run algorithms
-   Explain how a simple analysis runs on vantage6
-   Understand the future of vantage6 (policies, etc.)
:::

# Unique selling points of vantage6

vantage6 is a platform to execute  privacy enhancing techniques (PETs). Several alternative platforms for PETS are available, but vantage6 provides some unique features:

-   Open source.
-   Container orchestration for privacy enhancing techniques.
-   Easily extensible to different types of data sources.
-   Algorithms can be developed in any language.
-   Other applications can connect to vantage6 using the API.
- Managing and enforcing collaboration policies
- Minimal network requirements at data stations

# The vantage6 infrastructure

In vantage6, a **client** can pose a question to the central **server**. Each organization with sensitive data contributes one **node** to the network. The nodes collect the computation request from the server and fetches the **algorithm** to answer it. When the algorithm completes, the node sends the aggregated results back to the server.

![High level overview of the vantage6 infrastructure. Client(s) and Node(s) communicate through the Server. Nodes are able to communicate directly with each other when the optional VPN feature is enabled.](fig/vantage6_basic_schema.svg)

On a technical level, vantage6 may be seen as a container orchestration tool for privacy preserving analyses. It deploys a network of containerized applications that together ensure insights can be exchanged without sharing record-level data.

Lets explain in some more detail what these network actors are responsible for, and which subcomponents they contain.

### Server

The A (central) **server** that acts as communication hub between clients and nodes. The server tracks the status of the computation requests and handles administrative functions such as authentication and authorization.It consists of multiple applications:

-   **Vantage6 server**: Contains the users, organizations, collaborations, tasks and their results. It handles authentication and authorization to the system and acts as the communication hub for clients and nodes.

-   **Docker registry**: Contains algorithms stored in images which can be used by clients to request a computation. The node will retrieve the algorithm from this registry and execute it. It is possible to use public registries for this purpose like [Docker hub](https://hub.docker.com/) or [Github Containers](https://ghcr.io). However it is also possible to host your own registry, for example a [Harbor](https://goharbor.io/) instance.

-   **Algorithm store**: Is intended to be used as a repository for trusted algorithms within a certain project. Algorithm stores can be coupled to specific collaborations or to all collaborations on a given server.

- **EduVPN instance**: If algorithms need to be able to engage in peer-to-peer communication, a VPN server can be set up to help them do so.

- **RabbitMQ**: Is used to synchronize the messages between multiple vantage6 server instances.

### Data Station

The data station hosts the node (vantage6-node), that have access to the local data and execute algorithms, and a database.

-   **Vantage6 node** The node is responsible for executing the algorithms on the local data. It protects the data by allowing only specified algorithms to be executed after verifying their origin. The node is responsible for picking up the task, executing the algorithm and sending the results back to the server. The node needs access to local data. For more details see the technical documentation of the node.

-   **Database** The database may be in any format that the algorithms relevant to your use case support. The currently supported database types are listed here.

### Client

A user or application who interacts with the vantage6-server. They create tasks, retrieve their results, or manage entities at the server (i.e. creating or editing users, organizations and collaborations).

The vantage6 server is an API, which means that there are many ways to interact with it programatically. There are however a number of applications available that make is easier for users to interact with the vantage6 server:

-   **User interface** The user interface is a web application (hosted at the server) that allows users to interact with the server. It is used to create and manage organizations, collaborations, users, tasks and algorithms. It also allows users to view and download the results of tasks. Use of the user interface recommended for ease of use.

-   **Python client** The vantage6 python client <python-client> is a Python package that allows users to interact with the server from a Python environment. This is especially usefull for data scientists who want to integrate vantage6 into their existing Python workflow.

-   **API** It is also possible to interact with the vantage6-server using the API directly.


## How algorithms run in vantage6

Federated algorithms can be split in a **federated** and a **central** part:

-   **Central**: The central part of the algorithm is responsible for orchestration and aggregation of the partial results.

-   **Federated**: The partial tasks are executing computations on the local privacy sensitive data.

![vantage6 central and federated tasks.](fig/algorithm_central_and_subtasks.png)

Now, let’s see how this works in vantage6. The user creates a task for the central part of the algorithm. This is registered at the server, and leads to the creation of a central algorithm container on one of the nodes. The central algorithm then creates subtasks for the federated parts of the algorithm, which again are registered at the server. All nodes for which the subtask is intended start their work by executing the federated part of the algorithm. The nodes send the results back to the server, from where they are picked up by the central algorithm. The central algorithm then computes the final result and sends it to the server, where the user can retrieve it


::: callout

## vantage6-server vs central part of an algorithm

It is easy to confuse the central server with the central part of the algorithm: the server is the central part of the infrastructure but not the place where the central part of the algorithm is executed. The central part is actually executed at one of the nodes, because it gives more flexibility: for instance, an algorithm may need heavy compute resources to do the aggregation, and it is better to do this at a node that has these resources rather than having to upgrade the server whenever a new algorithm needs more resources.
:::
::: challenge

Two centers $a$ and $b$ have data regarding the age of a set of patients. Each center has a data station and We want to compute the overall average age of the patients.

![Architecture.](fig/schema_exercise.png)

Given that we that the the central average can be computed using the following equation:

$\overline{x} =\dfrac{1}n \sum_{i=1}^{n} x_i$

It can be written as follow, to make it ready for a federate computation:

$\overline{x} =\dfrac{1}{n_a+n_b} (\sum_{i=1}^{n_a} a_i+\sum_{i=1}^{n_b} b_i)$

Can you determine which part of the infrastructure will execute each part of the computation?

::: solution

The Server starts the central task on one of the two nodes (e.g. Data station A).

The node A starts two subtasks, one per node. Node A will run the following computation:

$S_a =\sum_{i=1}^{n_a} a_i$

Node B will run the following computation:

$S_b =\sum_{i=1}^{n_b} a_i$

The central task receives $S_a$ and $n_a$ from node A and $S_b$ and $n_b$ from node B, and will run the following computation:

$\overline{x} =\dfrac{S_a+S_b}{n_a+n_b}$

![vantage6 algorithm workflow.](fig/algorithm_workflow.png)

:::

:::

# Future developments of vantage6
Back in 2018 when the development of vantage6 started, the focus was on Federated Learning. Since then, vantage6 has been extended to support different types of data sources, different types of algorithms and improved its usability. Privacy Enhancing Technologies (PET) are a rapidly evolving field. To keep up with the latest developments, the vantage6 platform is designed to be flexible and to adapt to new developments in the field.

From the development team we are working towards making vantage6 the PETOps platform for all your (distributed) analysis needs.

[Image of the PETOps cycle]

We identified a number of areas where we want to improve and extend vantage6 in order to achieve this goal:

## Policies
Currently, vantage6 lets you set several policies, such as the organizations that are allowed to participate in a collaboration, the algorithms that are allowed to run on the nodes, and the data that is allowed to be used in a collaboration. We want to extend this to a more generic policy framework in which any aspect of the vantage6 platform can be controlled by policies. This will maximize the flexibility of the platform and make it easier to adapt to new use cases.

For example, it would be possible:

* Define the version of vantage6 that is allowed to be used in a collaboration
* Which users is allowed to run a certain algorithm
* Which algorithms are allowed in a collaboration/study
* Define privacy guards at algorithm level

In order to avoid that policies need to be set manually at the nodes, we envision a distributed policy system (possibly using Blocakchain) in which policies are distributed to the nodes by the server.

## Model Repository
Currently vantage6 is focused on privacy enhancing techniques. Some of these techniques result in a model that can be used to make predictions. We want to extend vantage6 with a model repository in which these models can be stored, shared and used. This will make it easier to reuse models and to compare the performance of different models.


## Build Services
Algorithms in vantage6 are shipped as container images. Currently, this image can be build by the user or some external process. We want to extend vantage6 with a build service that can build the container image for you. This will make it easier to develop and deploy algorithms in vantage6 but more importantly, it will enhance the security of the platform as they are build in a controlled environment.


::: keypoints
These are the keypoints
:::
