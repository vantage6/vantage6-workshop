---
title: "Running a PET analysis using the python client"
teaching: 
exercises: 
---

:::::::::::::::::::::::::::::::::::::: questions
- What is a common collaboration scenario where the same institution is involved in multiple collaborations?
- How to check the status of a given collaboration within vantage6?
- How to link an algorithm store to a given collaboration?
- How to request a task based on a given algorithm through vantage6's UI?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explore specific data analysis scenarios that further illustrate the concept of collaboration
- Understand the concept of 'algorithm trustworthiness' in the context of a vantage6 collaboration
- Understand v6's algorithm-store current and envisioned features
- Understand the UI-based approach for performing a data analysis through the given scenarios 

::::::::::::::::::::::::::::::::::::::::::::::::


## Python client

The Vantage6 Python client is a library designed to facilitate interaction with the Vantage6 server, enabling automation of various tasks such as creating computation tasks, managing organizations, collaborations, users, and collecting results. It communicates with the server through its API, handling encryption and decryption of data for secure operations. The client aims to comprehensively support all aspects of server communication, making it a crucial tool for users looking to leverage the full capabilities of the Vantage6 platform programmatically.

We provide four ways in which you can interact with the server to manage your vantage6 resources: the User interface (UI), the Python client, the R client, and the server API. Below are installation instructions for each of them.

For most use cases, we recommend to use the UI (for anything except creating tasks - this is coming soon) and/or the Python Client. The latter covers the server functionality completely, but is more convenient for most users than sending HTTP requests directly to the API.

The following groups (related to the Components) of methods are available, most of them have a list(), create(), delete() and get() method attached.

- `client.user`
- `client.organization`
- `client.rule`
- `client.role`
- `client.collaboration`
- `client.task`
- `client.result`
- `client.util`
- `client.node`



The client allows to do the same as the UI

Creating organizations, collaborations, etc

## Requirements

You need Python to use the Python client. We recommend using Python
3.10, as the client has been tested with this version. For higher
versions, it may be difficult to install the dependencies.


::::::::::::::::::::::::::::::::::::: challenge
## Challenge 1 - Check the server's API version and installing the right client

It is important to install the Python client with the same version as the vantage6 server you are talking to.
Check your server version by going to `https://SERVER_DOMAIN_NAME/api/version`. 

Create a python environment (conda or venv)

Then you can install the `vantage6-client` with:

    pip install vantage6==<version>

where you add the version you want to install. You may also leave out
the version to install the most recent version.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge
## Challenge 2 - Setting up authentication

This section and the following sections introduce some minimal examples for administrative tasks that you can perform with our. We start by authenticating.
Look for one of the users with researcher privileges given on episode #3.

``` python
# config.py

server_url = "https://MY VANTAGE6 SERVER" # e.g. https://cotopaxi.vantage6.ai or
                                          # http://localhost for a local dev server
server_port = 443 
server_api = "/api" 

username = "MY USERNAME"
password = "MY PASSWORD"

organization_key = "" # Path to the encryption key, if encryption is enabled
```

Now, a basic client that uses the authentication data


``` python
from vantage6.client import UserClient as Client

# Note: we assume here the config.py you just created is in the current directory.
# If it is not, then you need to make sure it can be found on your PYTHONPATH
import config

# Initialize the client object, and run the authentication
client = Client(config.server_url, config.server_port, config.server_api,
                log_level='debug')
client.authenticate(config.username, config.password)

# Optional: setup the encryption, if you have an organization_key
client.setup_encryption(config.organization_key)
```
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution
![alt text](fig/chapter5/auth-screenshot.png)
:::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::: challenge

### Challenge 3: use the client to find the identifiers of your collaboration and its organizations

. Given the collaborations scenarion from episode three, 
![Hypothetical collaborations scenario](fig/chapter3/orgs_n_collabs_scenario.png)

Extend the previous code where the a client object was successfully created. You need to run the federated algorithm 'algx' on the collaboration PhY-project, using only the data from the Lifelines and Cantabria nodes. Use the API to get this information:


````
 python -i client.py 
````


````python
client.collaboration.list(fields=['id', 'name', 'organizations'])
client.organization.list(fields=['id', 'name'])
````



-   you have a Python session with an authenticated Client object, as created in `authentication`.
-   you already have the algorithm you want to run available as a container in a docker registry (see
    [here](https://vantage6.discourse.group/t/developing-a-new-algorithm/31) for more details on developing your own algorithm)
-   the nodes are configured to look at the right database - ** they have the same label and database

In this manual, we\'ll use the averaging algorithm from `harbor2.vantage6.ai/demo/average`, so the second requirement is met.
We\'ll assume the nodes in your collaboration have been configured to look as something like:

``` yaml
databases:
   - label: default
     uri: /path/to/my/example.csv
     type: csv
   - label: my_other_database
     uri: /path/to/my/example2.csv
     type: excel
```

The third requirement is met when all nodes have the same labels in their configuration. As an end-user running the algorithm, you\'ll need
to align with the node owner about which database name is used for the
database you are interested in. For more details, see `how to configure <configure-node>`{.interpreted-text role="ref"} your node.

**Determining which collaboration / organizations to create a task for**

First, you\'ll want to determine which collaboration to submit this task
to, and which organizations from this collaboration you want to be
involved in the analysis

``` python
>>> client.collaboration.list(fields=['id', 'name', 'organizations'])


[
    {'id': 4, 'name': 'PhY-research', 'organizations': '/api/organization?collaboration_id=4'}, 
    {'id': 5, 'name': 'GHT_consortium', 'organizations': '/api/organization?collaboration_id=5'}
]

>>> client.collaboration.list(0)
[
{'organizations': '/api/organization?collaboration_id=4', 'algorithm_stores': '/api/algorithmstore?collaboration_id=4', 'name': 'PhY-research', 'id': 4, 'tasks': '/api/task?collaboration_id=4', 'studies': '/api/study?collaboration_id=4', 'nodes': '/api/node?collaboration_id=4', 'encrypted': False}, {'organizations': '/api/organization?collaboration_id=5', 'algorithm_stores': '/api/algorithmstore?collaboration_id=5', 'name': 'GHT_consortium', 'id': 5, 'tasks': '/api/task?collaboration_id=5', 'studies': '/api/study?collaboration_id=5', 'nodes': '/api/node?collaboration_id=5', 'encrypted': False}
]


*** THIS OUTPUT IS OUTDATED
[
 {'id': 1, 'name': 'example_collab1',
 'organizations': [
     {'id': 2, 'link': '/api/organization/2', 'methods': ['GET', 'PATCH']},
     {'id': 3, 'link': '/api/organization/3', 'methods': ['GET', 'PATCH']},
     {'id': 4, 'link': '/api/organization/4', 'methods': ['GET', 'PATCH']}
 ]}
]
```

CLIENT.ORGANIZATION.LIST

{'data': [{'address1': '', 'name': 'CANTABRIA_organization', 'id': 3, 'zipcode': '', 'tasks': '/api/task?init_org_id=3', 'country': 'Spain', 'users': '/api/user?organization_id=3', 'studies': '/api/study?organization_id=3', 'public_key': '', 'nodes': '/api/node?organization_id=3', 'collaborations': '/api/collaboration?organization_id=3', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=3'}, {'address1': '', 'name': 'LIFELINES_organization', 'id': 4, 'zipcode': '', 'tasks': '/api/task?init_org_id=4', 'country': 'The Netherlands', 'users': '/api/user?organization_id=4', 'studies': '/api/study?organization_id=4', 'public_key': '', 'nodes': '/api/node?organization_id=4', 'collaborations': '/api/collaboration?organization_id=4', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=4'}, {'address1': '', 'name': 'GAZEL_organization', 'id': 5, 'zipcode': '', 'tasks': '/api/task?init_org_id=5', 'country': 'France', 'users': '/api/user?organization_id=5', 'studies': '/api/study?organization_id=5', 'public_key': '', 'nodes': '/api/node?organization_id=5', 'collaborations': '/api/collaboration?organization_id=5', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=5'}, {'address1': '', 'name': 'GNC_organization', 'id': 6, 'zipcode': '', 'tasks': '/api/task?init_org_id=6', 'country': 'Germany', 'users': '/api/user?organization_id=6', 'studies': '/api/study?organization_id=6', 'public_key': '', 'nodes': '/api/node?organization_id=6', 'collaborations': '/api/collaboration?organization_id=6', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=6'}, {'address1': '', 'name': 'PhY24-consortium', 'id': 7, 'zipcode': '', 'tasks': '/api/task?init_org_id=7', 'country': '', 'users': '/api/user?organization_id=7', 'studies': '/api/study?organization_id=7', 'public_key': '', 'nodes': '/api/node?organization_id=7', 'collaborations': '/api/collaboration?organization_id=7', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=7'}, {'address1': '', 'name': 'GHT-Consortium', 'id': 8, 'zipcode': '', 'tasks': '/api/task?init_org_id=8', 'country': '', 'users': '/api/user?organization_id=8', 'studies': '/api/study?organization_id=8', 'public_key': '', 'nodes': '/api/node?organization_id=8', 'collaborations': '/api/collaboration?organization_id=8', 'domain': '', 'address2': '', 'runs': '/api/run?organization_id=8'}], 'links': {'first': '/api/organization?page=1', 'self': '/api/organization?page=1', 'last': '/api/organization?page=1'}}




In this example, we see that the collaboration called `example_collab1` has three organizations associated with it, of which the organization id\'s are `2`, `3` and `4`. To figure out the names of these organizations, we run:

``` python
>>> client.organization.list(fields=['id', 'name'])
[{'id': 1, 'name': 'root'}, {'id': 2, 'name': 'example_org1'},
 {'id': 3, 'name': 'example_org2'}, {'id': 4, 'name': 'example_org3'}]
```

i.e. this collaboration consists of the organizations `example_org1`
(with id `2`), `example_org2` (with id `3`) and `example_org3` (with id
`4`).

::::::::::::::::::::::::::::::::::::::::::::::::






::::::::::::::::::::::::::::::::::::: challenge
## Challenge 4: Creating a task that runs the central algorithm**

Now, we have two options: create a task that will run the central part of an algorithm (which runs on one node and may spawns subtasks on other
nodes), or create a task that will (only) run the partial methods (which are run on each node). Typically, the partial methods only run the node
local analysis (e.g. compute the averages per node), whereas the central methods performs aggregation of those results as well (e.g. starts the partial analyses and then computes the overall average). First, let us create a task that runs the central part of the `harbor2.vantage6.ai/demo/average` algorithm:

``` python
input_ = {
    'method': 'central_average',
    'kwargs': {'column_name': 'age'}
}

average_task = client.task.create(
   collaboration=1,
   organizations=[2,3],
   name="an-awesome-task",
   image="harbor2.vantage6.ai/demo/average",
   description='',
   input_=input_,
   databases=[
      {'label': 'default'}
   ]
)
```


Note that the `kwargs` we specified in the `input_` are specific to this algorithm: this algorithm expects an argument `column_name` to be
defined, and will compute the average over the column with that name.
Furthermore, note that here we created a task for collaboration with id `1` (i.e. our `example_collab1`) and the organizations with id `2` and `3` (i.e. `example_org1` and `example_org2`). I.e. the algorithm need not necessarily be run on *all* the organizations involved in the collaboration.

Finally, note that you should provide any databases that you want to use via the `databases` argument. In the example above, we use the `default`
database; using the `my_other_database` database can be done by simply specifying that label in the dictionary. If you have a SQL or SPARQL
database, you should also provide a `query` argument, e.g.

``` python
databases=[
   {'label': 'default', 'query': 'SELECT * FROM my_table'}
]
```

Similarly, you can define a `sheet_name` for Excel databases if you want
to read data from a specific worksheet. Check `help(client.task.create)`
for more information.




**Creating a task that runs the partial algorithm**

You might be interested to know output of the partial algorithm (in this
example: the averages for the \'age\' column for each node). In that
case, you can run only the partial algorithm, omitting the aggregation
that the central part of the algorithm will normally do:

``` python
input_ = {
    'method': 'partial_average',
    'kwargs': {'column_name': 'age'},
}

average_task = client.task.create(collaboration=1,
                                  organizations=[2,3],
                                  name="an-awesome-task",
                                  image="harbor2.vantage6.ai/demo/average",
                                  description='',
                                  input_=input_)
```

**Inspecting the results**

Of course, it will take a little while to run your algorithm. You can
use the following code snippet to run a loop that checks the server
every 3 seconds to see if the task has been completed:

``` python
print("Waiting for results")
task_id = average_task['id']
result = client.wait_for_results(task_id)
```

You can also check the status of the task using:

``` python
task_info = client.task.get(task_id, include_results=True)
```

and then retrieve the results

``` python
result_info = client.result.from_task(task_id=task_id)
```

The number of results may be different depending on what you run, but
for the central average algorithm in this example, the results would be:

``` python
>>> result_info
[{'average': 53.25}]
```

while for the partial algorithms, dispatched to two nodes, the results
would be:

``` python
>>> result_info
[{'sum': 253, 'count': 4}, {'sum': 173, 'count': 4}]
```
::::::::::::::::::::::::::::::::::::::::::::::::