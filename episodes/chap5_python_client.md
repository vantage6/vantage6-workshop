---
title: "Running a PET analysis using the Python client"
teaching:
exercises:
---

:::::::::::::::::::::::::::::::::::::: questions

With the Python client:

- How to connect to the vantage6 server?
- How to use the `Client` object?
- How to check details of a collaboration?
- How to start a task?
- How to collect the results of a finished computation?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After completing this episode, participants should be able to…

- Connect to the vantage6 server using the Python client.
- Understand the basic concepts of the vantage6 Python client.
- Use the Python client to get details of a collaboration.
- Create a task using the Python client.
- Collect the results of a finished computation using the Python client.

::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::: prereq


# Prerequisite
 Make sure you completed the [Setup Episode](../index.md) before starting this episode.

:::::::::::::::::

# The Python client
The vantage6 Python client is a library designed to facilitate interaction with the vantage6 server, to perform various tasks such as creating computation tasks, managing organizations, collaborations, users, and collecting results. It is a versatile alternative to the web-based user interface we have used in previous lessons.

Data scientists and administrators may use it to manage resources programatically. For example, to automate actions or integrating them on other applications. The Python client communicates with the REST API of the vantage6 server, handling encryption and decryption where applicable.

::: spoiler

## Alternative clients
Besides the Python client, there is also an [R client (github.com)](https://github.com/iknl/vtg) available. This client is more focused on starting federated analysis and does not provide tools to manage the server. It typically also lags behind the Python client in terms of features and updates. You can find more information in the [official documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/user/rclient.html).

If your organization uses a different programming language, you can always create a client in that language by following the [API documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/user/api.html).


**In this workshop, we will only use on the Python client.**

:::


## Connect & authenticate
Creating an instance of the vantage6 Python client is relatively straightforward. The user defines server connection details: server URL, login credentials, and the organization's private key in case encryption is used in the collaboration. In case the server has [two-factor authentication (docs.vantage6.ai)](https://docs.vantage6.ai/en/stable/technical-documentation/features/server/2fa.html) (2FA) enabled you should also enter the corresponding time-based 6-digit code accordingly.

To avoid leaking your username and/or password by accident, they can be defined in a separate Python file (e.g., `config.py`), which is then imported into the main script.

```python
# config.py

server_url = "https://<vantage6-server-address>"
server_port = 443
server_api = "/api"

username = "MY USERNAME"
password = "MY PASSWORD"

# Path to the private key, if encryption is enabled. Can be None if
# not used. Note that this key is the organization's private key.
organization_key = None
```

Once you have created the Python module with the configuration settings, you can import it and create the client instance as follows:

```python
# client.py

from vantage6.client import Client

# It is assumed here that the `config.py` you just created is in the current
# directory. If it is not, then you need to make sure it can be found on
# your PYTHONPATH
import config

# Initialize the client object, and authenticate
client = Client(config.server_url, config.server_port, config.server_api,
                log_level='debug')
client.authenticate(config.username, config.password)
# In the case of 2FA, you should also include the 6-digit code:
# client.authenticate(config.username, config.password, '123456')

# Setup the encryption, in case not encryption is used, this line can be
# omitted or `config.organization_key` should be set to None
client.setup_encryption(config.organization_key)
```


::::::::::::::::::::::::::::::::::::: challenge

## Connect 🌍!

Connect to the vantage6 server using the Python client!

:::::::::::::::::::::::: hint

1. Activate the conda environment with the vantage6 client installed: `conda activate v6-workshop`.
2. Create the `config.py` with the your credentials and connection details.
3. Create the `client.py` script with the code above.
4. Run the `client.py` script as defined above to create the client instance.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

1. Make sure you have activated the conda environment with the vantage6 client
   installed: `conda activate v6-workshop`.
2. Make sure you have created the `config.py` file with your credentials and the
   `client.py` file with the code above.
3. Run the `client.py` script: `python client.py`. If the connection is successful,
    you should see the message `--> Succesfully authenticated`:

    ```bash
    (v6-workshop) $ python client.py
    Welcome to
                      _                     __
                     | |                   / /
    __   ____ _ _ __ | |_ __ _  __ _  ___ / /_
    \ \ / / _` | '_ \| __/ _` |/ _` |/ _ \ '_ \
     \ V / (_| | | | | || (_| | (_| |  __/ (_) |
      \_/ \__,_|_| |_|\__\__,_|\__, |\___|\___/
                                __/ |
                               |___/

    --> Join us on Discord! https://discord.gg/rwRvwyK
    --> Docs: https://docs.vantage6.ai
    --> Blog: https://vantage6.ai
    ------------------------------------------------------------
    Cite us!
    If you publish your findings obtained using vantage6,
    please cite the proper sources as mentioned in:
    https://vantage6.ai/vantage6/references
    ------------------------------------------------------------

    ...

    --> Succesfully authenticated
    ```

:::::::::::::::::::::::::::::::::

## Using the client

The `Client` instance offers a set of attributes that correspond to the
[vantage6 server resources (Episode 3)](./chap3_run_analysis_ui.md#vantage6-user-interface-basics)
also described in the [official documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/introduction/introduction.html#vantage6-resources). The available attributes are:

| Resource              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `client.user`         | Manage users including your own details                           |
| `client.organization` | Manage organizations                  |
| `client.rule`         | View all available rules                          |
| `client.role`         | Manage roles that are collections of rules                           |
| `client.collaboration`| Manage collaborations                  |
| `client.task`         | Create new tasks and view their run data |
| `client.result`       | Obtain results from the tasks |
| `client.util`         | Provides utility functions for the vantage6 Python client. For example to reset your password.             |
| `client.node`         | Manage nodes |
| `client.store`        | Manage an algorithm store |
| `client.algorithm`    | Manage algorithms that can be used for the computations |

Almost all of these attributes provide a [get](#get), [list](#list), [create](#create),
[update](#update) and [delete](#delete) operation. All of the functions that interact
with the server return a dictionary with the requested information.


::: callout

### Permissions

Note that the logged-in user may not be allowed to perform all operations or view all
resources. The server will only allow the user to perform operations on the resources
that the user has permission to perform.

For example, a user may not be allowed to create a new organization, but may be allowed
to list the organizations within all collaboration its organization participates in.

:::


### The 5 basic operations

Most resources provide five basic operations: get, list, create, update, and delete.

::::::::::::::::::::::::::::::::::::: tab

### Get
Get a specific *resource* with `client.<resource>.get(<id>)`. For example:

```Python
client.organization.get(166)
```
```output
{
    'nodes': '/api/node?organization_id=166',
    'public_key': '',
    'studies': '/api/study?organization_id=166',
    'name': 'Huckleberry Holdings',
    'tasks': '/api/task?init_org_id=166',
    'address2': '',
    'users': '/api/user?organization_id=166',
    'domain': 'huckleberryholdings.mc',
    'country': 'Monaco',
    'zipcode': '98000',
    'runs': '/api/run?organization_id=166',
    'address1': '4747 Huckleberry Ln',
    'id': 166,
    'collaborations': '/api/collaboration?organization_id=166'
}
```

### List
Get all *resource* items that the user is allowed to see with
`client.<resource>.list()`. For example:

```Python
client.organization.list()
```
```output
[
    {'id': 168, 'name': 'Lychee Labs', ...},
    {'id': 158, 'name': 'Pineapple Paradigm', ...},
    {'id': 155, 'name': 'Huckleberry Hub', ...},
    {'id': 140, 'name': 'Mango Matrix', ...},
    {'id': 128, 'name': 'Apple Innovations', ...},
    {'id': 170, 'name': 'eScience center', ...},
    {'id': 165, 'name': 'Grapefruit Group', ...},
    {'id': 145, 'name': 'Raspberry Revolution', ...},
    {'id': 136, 'name': 'Ivy Berry Solutions', ...},
    {'id': 166, 'name': 'Huckleberry Holdings', ...}
]
```

Typically, the `list()` method returns a paginated result.

### Create
Register a new *resource* at the server with `client.<resource>.create(...)`. For
example, let's create a new organization:

```Python
client.organization.create(
    name='new_organization',
    address1='street 1',
    address2='',
    zipcode='1234AB',
    country='NL',
    domain='example.com',
)
```
```output
{
    'nodes': '/api/node?organization_id=172',
    'public_key': '',
    'studies': '/api/study?organization_id=172',
    'name': 'new_organization',
    'tasks': '/api/task?init_org_id=172',
    'address2': '',
    'users': '/api/user?organization_id=172',
    'domain': 'example.com',
    'country': 'NL',
    'zipcode': '1234AB',
    'runs': '/api/run?organization_id=172',
    'address1': 'street 1',
    'id': 172,
    'collaborations': '/api/collaboration?organization_id=172'
}
```

### Update
Update an specific *resource*. For example:

```Python
client.organization.update(id_, name='new_name')
```
```output
{
    'nodes': '/api/node?organization_id=173',
    'public_key': '',
    'studies': '/api/study?organization_id=173',
    'name': 'new_name',
    'tasks': '/api/task?init_org_id=173',
    'address2': '',
    'users': '/api/user?organization_id=173',
    'domain': 'example.com',
    'country': 'NL',
    'zipcode': '1234AB',
    'runs': '/api/run?organization_id=173',
    'address1': 'street 1',
    'id': 173,
    'collaborations': '/api/collaboration?organization_id=173'
}
```

### Delete
To delete an specific instance of the given *resource* you can use
`client.<resource>.delete(id_)` . Sometimes you need to also delete all the related
instances of the given *resource* as well.
```Python
client.organization.delete(1)
```
```output
TODO: output, as this is not implemented in the current version
```

:::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Collect collaboration details

Before starting a task, you need to know the details of the collaboration you are working with. Use the Python client to get the details of the collaboration you have access to. Write down the **name** and and **ID** of each collaboration.

:::::::::::::::::::::::: hint

Use the client script you created in the previous challenge to connect to the server.
Make sure you use the `-i` flag to start an interactive Python session after running
the script.

```bash
python -i client.py
```

Now you have a variable `client` that you can use to interact with the server.

::::::::::::::::::::::::
:::::::::::::::::::::::: hint

Use the `client.collaboration.list()` method to get the details of the collaborations you have access to.

```python
client.collaboration.list()
```

::::::::::::::::::::::::


:::::::::::::::::::::::: solution

```output
[
    {'id': 168, 'name': 'Lychee Labs', ...},
    {'id': 158, 'name': 'Pineapple Paradigm', ...},
    {'id': 155, 'name': 'Huckleberry Hub', ...},
    {'id': 140, 'name': 'Mango Matrix', ...},
    {'id': 128, 'name': 'Apple Innovations', ...},
    {'id': 170, 'name': 'eScience center', ...},
    {'id': 165, 'name': 'Grapefruit Group', ...},
    {'id': 145, 'name': 'Raspberry Revolution', ...},
    {'id': 136, 'name': 'Ivy Berry Solutions', ...},
    {'id': 166, 'name': 'Huckleberry Holdings', ...}
]
```

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

### Additional operations

Some resources do not provide all five operations and some resource provide additional
operations. For example:

- it is not possible to create new rules. In other words: `client.rule.create` does not
  exist.
- the `client.task` has a `client.task.kill` method which is able to stop a task that
  currently is running.


### Top level methods
Up untill now we only discussed `Client` methods that are bound to an resource. There
are also some methods that are not bound to a specific resource. Examples are:

- `client.authenticate()` to authenticate the user. You have already used this method
  when you authenticated to the server.
- `client.setup_encryption()` to setup the encryption.
- `client.wait_for_results()` to wait for the results of a task.


### Method and parameter documentation
We have shown the basic methods of the client, however there are many methods available
in the `Client` object. Each method has its own set of parameters and in order to know
which parameters are available for a specific method, you can use the `help()` function
in Python. For example, to get the documentation of the `client.organization.list()`
method, you can use the following command:

```bash
python -i client.py
>>> help(client.organization.list)
```
```output
list(self, name: 'str' = None, country: 'int' = None, collaboration: 'int' = None, study: 'int' = None, page: 'int' = None, per_page: 'int' = None) -> 'list[dict]'
    List organizations

    Parameters
    ----------
    name: str, optional
        Filter by name (with LIKE operator)
    country: str, optional
        Filter by country
    collaboration: int, optional
        Filter by collaboration id. If client.setup_collaboration() was called,
        the previously setup collaboration is used. Default value is None

```
This shows you that you can filter the list of organizations (among others) by name,
country, and collaboration.  It is also possible to request documentation of a higher
level method, for example `help(client.organization)` or even `help(client)`.:

::: spoiler

#### Online documentation

To view all `Client` functions and their arguments without using `help()` you can use
the [official documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/function-docs/_autosummary/vantage6.client.Client.html#vantage6-client-client). Which is the same as the Python client's docstring.

Make sure you are viewing the documentation of the version of the client you are using.
You can find the version of the client by one of the following commands:

```Python
import vantage6.client
print(vantage6.client.__version__)
```

or by running the following command in the terminal:

```bash
pip show vantage6-client | grep Version
```

:::

::::::::::::::::::::::::::::::::::::: challenge

### Find documentation

Find the documentation on how to reset your password 🔑 using the `help()` function.

::: hint

Have a look at the [client table](#using-the-client), and see if you can find a
resource group that might contain the method you are looking for.

:::

::: hint

Use the `help()` function to find the documentation of the `client.util` resource.

:::

::: solution

```python
help(client.util.change_my_password)
```
:::

::::::::::::::::::::::::::::::::::::::::::::::::

### Identifiers are key
From parameters like the ones described in this episode, it is important to note that
the client methods use identifiers rather than names. This implies that, for example,
to filter the organizations that belong to a a given collaboration, you need to know
the collaboration's identifier first.

In a previous challenge, you were asked to get the details of the collaborations you
have access to. This is common practice when working with the vantage6 Python client.

It is also possible to obtain these identifiers through the UI. But note that when
working with the UI, identifiers are not as important as the names are used to identify
the resources.

::: spoiler

#### Why identifiers?

The reason for this is that the UI is designed to more be user-friendly, and it is
expected that users will interact with the resources using their names. Typically
they will select the resources from a list or dropdown. Since names do not always
have to be unique (e.g. task names) it is impossible to identify a resource
uniquely by its name.

:::

Now that we understand the basic concepts of the vantage6 Python client, let us get
some more details about our collaborations. First, as bevore, we collect the details of
the collaborations we have access to. We do so by specifying an additional parameter
`fields` to the `list()` method. This parameter allows us to specify which fields we
want to see in the output. This makes it more readable and easier to find the
information we are looking for.

```Python
client.collaboration.list(fields=['id', 'name'])
```
```output
[
    {'id': 12, 'name': 'Birch Brotherhood'},
    {'id': 9, 'name': 'Pine Partners'},
    {'id': 11, 'name': 'Cedar Coalition'},
    {'id': 10, 'name': 'Maple Consortium'},
    {'id': 15, 'name': 'demo'},
    {'id': 8, 'name': 'Oak Alliance'},
    {'id': 14, 'name': 'Redwood Union'},
    {'id': 13, 'name': 'Willow Network'}
]
```

Then, we are interested in all the organizations that participate in one of the
collaborations. Lets assume that the collaboration ID is 1. We then can get the
organizations that are part of this collaboration by using the
`client.organization.list()` method with the `collaboration` parameter set to 1.

```Python
client.organization.list(collaboration=1, fields=['id', 'name'])
```
```output
[
    {'id': 171, 'name': 'IKNL'},
    {'id': 172, 'name': 'new_organization'}
]
```

Write down the **ID** of each organization and collaboration. You will need them in the
next challenges.


### Creating a new task

Before starting an analysis we need several details about the collaboration and the
analysis to be performed. This includes the organization and collaboration identifiers,
we have just collected.

Before we start the analysis, let us check if everything is in place:

::: checklist

**Network**

- ✔ Connect to the vantage6 server using the Python client.
- ✔ Use the Python client to get the details of the collaboration and its organizations
  you have access to.
- ⚠ Check the status of the nodes


**Average Algorithm**

- ✔ published at: `harbor2.vantage6.ai/demo/average`.
- ✔ We are going to use the `partial_average()` function.
- ✔ The function requires a `column_name` parameter, we are setting this to 'age'.

:::

#### Node status
Ok so we have not checked the status of the nodes. You can start an analys when nodes
are offline, they will start the analysis once they are online. In case one is offline,
you might need to inquire with the node owner to get it back online.

::::::::::::::::::::::::::::::::::::: challenge

##### Check the status of the nodes

Use the Python client to check the status of the nodes that are part of the
collaboration you are interested in.


::: hint

To check the status of the nodes, you can use the `client.node` resource.

:::

::: hint

See `help(client.node.list)` to see how to get the details of the nodes of a given
collaboration. You can also use the `fields` parameter to get only the information you
are interested in.

:::

:::::: solution

You can obtain node details by using the `client.node.list()` method. To filter the
nodes you are interested in, you can use the `collaboration` parameter in the
`client.node.list()` method:

```python
client.node.list(collaboration=1)
```

You can also specify the `fields` parameter to get only the information you are
interested in:

```python
client.node.list(collaboration=1, fields=['id', 'name', 'status'])
```

You can also use the `is_online` parameter to filter the nodes that are online. But for
now it would be good to see both online and offline nodes.

```output
[
    {
        'id': 155,
        'name': 'IKNL demo node',
        'status': None
    }
]
```

::::::


::::::::::::::::::::::::::::::::::::::::::::::::

#### Task definition

A task in vantage6 is a request to execute an algorithm on a given organization. When
creating a task, you need to specify the following:

- The collaboration and organization identifiers.
- The algorithm to be executed.
- The input parameters for the algorithm.

The algorithm we are going to use is the
[federated average algorithm (Github.com)](https://github.com/IKNL/v6-average-py/blob/master/v6-average-py/__init__.py),
which we commonly use for demonstrations. Typically, you want to run a more complex
algorithm, but for the sake of this workshop, we will use this simple algorithm.

This algorithm has two functions: `partial_average()` and `central_average()`. If you
do not know the difference between *partial* and *central* function, you should read
[How algorithms run in vantage6 (Episode 2)](./chap2_introduction_v6.md#how-algorithms-run-in-vantage6)
again.

We can use the `client.task.create()` method to create a new task to be executed by the
nodes.

::: spoiler

#### Documentation of client.task.create()

```python
help(client.task.create)
```
```output
create(organizations: 'list', name: 'str', image: 'str', description: 'str', input_: 'dict', collaboration: 'int' = None, study: 'int' = None, store: 'int' = None, databases: 'list[dict]' = None) -> 'dict' method of vantage6.client.Task instance
    Create a new task

    Parameters
    ----------
    organizations : list
        Organization ids (within the collaboration) which need
        to execute this task
    name : str
        Human readable name
    image : str
        Docker image name which contains the algorithm
    description : str
        Human readable description
    input_ : dict
        Algorithm input
    collaboration : int, optional
        ID of the collaboration to which this task belongs. Should be set if
        the study is not set
    study : int, optional
        ID of the study to which this task belongs. Should be set if the
        collaboration is not set
    store : int, optional
        ID of the algorithm store to retrieve the algorithm from
    databases: list[dict], optional
        Databases to be used at the node. Each dict should contain
        at least a 'label' key. Additional keys are 'query' (if using
        SQL/SPARQL databases), 'sheet_name' (if using Excel databases),
        and 'preprocessing' information.

    Returns
    -------
    dict
        A dictionairy containing data on the created task, or a message
        from the server if the task could not be created
```

:::


Lets start by defining the input for the task. The `partial_average()` function requires
a `column_name` parameter. We can define the input as follows:

```python
input_ = {
    'method': 'partial_average',
    'args': [],
    'kwargs': {'column_name': 'age'}
}
```

Basically we are defining the method to be executed, the arguments and keyword arguments
for the method. In other words, we just created a function call in Python that would
look like this: `partial_average(column_name=age)`. If you are not familiar with
Python's args and kwargs, you can read more about them at W3C Schools:
[args (w3schools.com)](https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp)
and [kwargs (w3schools.com)](https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp).

Now that you have defined the task input, you can create and start it by also specifying
(using the IDs we collected earlier) which organizations and for which collaboration,
it will be executed:

```Python
average_task = client.task.create(
   collaboration=45,
   organizations=[12,23],
   name="name_for_the_task",
   image="harbor2.vantage6.ai/demo/average",
   description='',
   input_=input_,
   databases=[
      {'label': 'default'}
   ]
)
```

#### Database parameter
We have not yet explained the `databases` parameter. This parameter is used to
specify the database that the nodes will use to execute the algorithm. Each node can
have multiple databases, and you can specify them in the `databases` parameter. We will
go into more detail about this in
[Seting up a vantage6 node (Episode 6)](./chap6_setup_node.md).

### Obtaining results

A client's task execution request is asynchronous. This means that once the
`client.task.create()` method is invoked, the task will begin running in the background,
returning the control to the Python program immediately (i.e., without waiting for the
task to complete).

This means that your client program needs to wait until the task is completed, so you
can get access to the results (or to the error details, if something goes wrong).

You can use the `client.wait_for_result()` method to make the program execution wait
until the task is completed. For that, you need the ID of the task you just created,
which was included in the dictionary returned by the `client.task.create()` method.
For the task execution request of the code snippet above, this will look like:

```python
task_id = average_task['id']
result = client.wait_for_results(task_id)
```

Since the above will pause the execution of the program until the task is completed,
you can include instructions for retrieving the results immediately afterward:

```python
result_info = client.result.from_task(task_id=task_id)
```


# Advanced Exercises


:::::::::::::::::::::::::::::::::::::::::::::::: challenge


Use the researcher credentials from [Running analysis from the UI (Episode 3)](./chap3_run_analysis_ui.md), to get the identifiers of the two collaborations from this episode's scenario. Use this information to get the identifiers of the organizations that belong to each collaboration.

Refer to the **Python client - basic concepts** section above to do this.

| User      | Roles      | Collaboration |
| --------- | ---------- | ------------- |
| PhY24-rs1 | Researcher | PhY24         |
| GHT-rs1   | Researcher | GHT           |

Now, try to identify which nodes are active on each collaboration. Hint: use the `client.node` resource. Remember that you can use the `help()` function to see how to get the details of the nodes of a given organization.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

```python
>>> client.collaboration.list(fields=['id', 'name', 'organizations'])

[
    {'id': 4, 'name': 'PhY-research', 'organizations': '/api/organization?collaboration_id=4'},
    {'id': 5, 'name': 'GHT_consortium', 'organizations': '/api/organization?collaboration_id=5'}
]

```

By knowing the ID of the collaboration, you can find the identifiers of the organizations that are participating on it:

```python

>>> client.organization.list(collaboration=4)

[
    {'address1': '', 'studies': '/api/study?organization_id=3', 'users': '/api/user?organization_id=3', 'zipcode': '', 'domain': '', 'tasks': '/api/task?init_org_id=3', 'public_key': '', 'name': 'CANTABRIA_organization', 'address2': '', 'nodes': '/api/node?organization_id=3', 'country': 'Spain', 'collaborations': '/api/collaboration?organization_id=3', 'runs': '/api/run?organization_id=3', 'id': 3},
    {'address1': '', 'studies': '/api/study?organization_id=4', 'users': '/api/user?organization_id=4', 'zipcode': '', 'domain': '', 'tasks': '/api/task?init_org_id=4', 'public_key': '', 'name': 'LIFELINES_organization', 'address2': '', 'nodes': '/api/node?organization_id=4', 'country': 'The Netherlands', 'collaborations': '/api/collaboration?organization_id=4', 'runs': '/api/run?organization_id=4', 'id': 4},
    {'address1': '', 'studies': '/api/study?organization_id=5', 'users': '/api/user?organization_id=5', 'zipcode': '', 'domain': '', 'tasks': '/api/task?init_org_id=5', 'public_key': '', 'name': 'GAZEL_organization', 'address2': '', 'nodes': '/api/node?organization_id=5', 'country': 'France', 'collaborations': '/api/collaboration?organization_id=5', 'runs': '/api/run?organization_id=5', 'id': 5},
    {'address1': '', 'studies': '/api/study?organization_id=7', 'users': '/api/user?organization_id=7', 'zipcode': '', 'domain': '', 'tasks': '/api/task?init_org_id=7', 'public_key': '', 'name': 'PhY24-consortium', 'address2': '', 'nodes': '/api/node?organization_id=7', 'country': '', 'collaborations': '/api/collaboration?organization_id=7', 'runs': '/api/run?organization_id=7', 'id': 7}
]
```

Getting the status of an organization node for a given collaboration: The following returns the nodes (there is a node for each collaboration the organization contributes to).

```python
>>> client.node.list(organization=4)

[
    {'config': [], 'last_seen': '2024-06-18T06:57:48.114072',
    'organization': {'id': 4, 'link': '/api/organization/4',
    'methods': ['PATCH', 'GET']},
    'collaboration': {'id': 4, 'link': '/api/collaboration/4',
    'methods': ['GET', 'PATCH', 'DELETE']},
    'name': 'PhY-research - LIFELINES_organization', 'status': 'offline',
    'type': 'node', 'ip': None, 'id': 13},
    {'config': [], 'last_seen': None,
    'organization': {'id': 4, 'link': '/api/organization/4',
    'methods': ['PATCH', 'GET']},
    'collaboration': {'id': 5, 'link': '/api/collaboration/5',
    'methods': ['GET', 'PATCH', 'DELETE']},
    'name': 'GHT_consortium - LIFELINES_organization', 'status': None,
    'type': 'node', 'ip': None, 'id': 18}
]
```

:::::::::::::::::::::::::::::::::



::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: Creating a task that runs a partial algorithm\*\*

The following is the information of a new algorithm **(TODO a new algorithm should be created for this)**, that you need to use on the collaboration whose 100% of its nodes are active:

- Image: harbor2.vantage6.ai/**TODO**alg_xxyy
- Functions: central(), partial()
- Algorithm source code: github.com/**TODO**/repo/alg_xxyy

Using the guidelines given in the **Python client - basic concepts** section above, use the client to create a task for executing the `partial()` function on all the nodes. Check in the source code what the parameters of this function are, and define their input accordingly. For the database selection, all the nodes use the one labeled as 'default'.

Include the necessary code to wait until the new task is completed, and to get and print the results. Discuss the output with the instructors.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: Create a task that runs a central function, and figure out why it failed\*\*

Using the Python client, create a new task with the same algorithm from Challenge #3. This time, launch the `central()` function. As you will see, this time the task failed. Using the client, try to find out which of the nodes involved on the task execution failed and the error message. Discuss with the instructors, based on the algorithm source code and the error message the cause of the error, and what should be done to fix it.
**(TODO This requires the new algorithm or the data on one of the nodes to cause an error)**
::::::::::::::::::::::::::::::::::::::::::::::::
