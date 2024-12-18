---
title: "Running a PET analysis using the Python client"
teaching:
exercises:
---

:::::::::::::::::::::::::::::::::::::: questions

In the context of the Python client:

- How to connect to the vantage6 server?
- How to explore the `Client` object?
- How to check details of a collaborations?
- How to start a compute task?
- How to collect the results of a finished computation?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After completing this episode, you will be able to:

- Understand the basic concepts of the vantage6 Python client.

use the Python client to …

- Connect to the vantage6 server.
- Use the Python client to get details of a collaboration.
- Create a task using the Python client.
- Collect the results of a finished computation using the Python client.

::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::: prereq


# Prerequisite
Make sure you completed the [Setup Episode](../index.md) before starting this episode. Some basic knowledge of Python is also required to complete the exercises in this episode.

:::::::::::::::::

# The Python client
The vantage6 Python client is a library designed to facilitate interaction with the vantage6 server, to perform various tasks such as creating computation tasks, managing organizations, collaborations, users, and collecting results. It is a versatile alternative to the web-based user interface we have used in previous lessons.

Data scientists and administrators may use it to manage resources programatically. For example, to automate actions or integrating them on other applications. The Python client communicates with the [REST API (wikipedia.org)](https://en.wikipedia.org/wiki/REST) of the vantage6 server, handling encryption and decryption where applicable.

::: spoiler

## Alternative clients
Besides the Python client, there is also an [R client (github.com)](https://github.com/iknl/vtg) available. This client is more focused on starting federated analysis and does not provide tools to manage the server. Important to note that this client is poorly maintained and lags behind in terms of features. Therefore we do *not* recommend using it. You can find more information in the [documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/user/rclient.html).

If your organization uses a different programming language, you can always create a client in that language by following the [API documentation (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/user/api.html).


**In this workshop, we will only use on the Python client.**

:::


## Connect & authenticate
Creating an instance of the vantage6 Python client is relatively straightforward. The user defines server connection details: server address, login credentials, and the organization's private key in case [encryption (docs.vantage6.ai)](https://docs.vantage6.ai/en/main/features/inter-component/encryption.html) is used in the collaboration. In case the server has [two-factor authentication (docs.vantage6.ai)](https://docs.vantage6.ai/en/stable/technical-documentation/features/server/2fa.html) (2FA) enabled, you should also enter the corresponding time-based 6-digit code accordingly.

To avoid leaking your username and/or password by accident, they can be defined in a separate Python file (e.g., `config.py`), which is then imported into the main script. This way, the main script does not contain any sensitive information.

::::::::::::::::::::::::::::::::::::: instructor

Make sure to use the credentials from the first day. And use the reseacher credentials,
so not the `_admin` credentials!

:::::::::::::::::::::::::::::::::::::

```python
server_url = "https://<vantage6-server-address>"
server_port = 443
server_api = "/api"

username = "MY USERNAME"
password = "MY PASSWORD"

# Path to the private key, if encryption is enabled. Can be None if
# encryption is not used. Note that this key is the organization's
# private key. In case of this workshop we do not use encryption, so
# this can be None.
organization_key = None
```

Once you have created the Python module with the configuration settings, you can import it and create the client instance as follows:

```python
from vantage6.client import Client

# It is assumed here that the `config.py` you just created is in the current
# directory. If it is not, then you need to make sure it can be found on
# your PYTHONPATH
import config

# Initialize the client object, and authenticate
client = Client(config.server_url, config.server_port, config.server_api,
                log_level='info')
client.authenticate(config.username, config.password)
# In the case of 2FA, you should also include the 6-digit code:
# client.authenticate(config.username, config.password, '123456')

# In case encryption is used, this line can be used to set the organizations private
# key.
# client.setup_encryption(config.organization_key)
```

::::::::::::::::::::::::::::::::::::: challenge

## 1. Connect 🌍!

Connect to the vantage6 server using the Python client!

:::::::::::::::::::::::: hint

1. Create the `config.py` with the your credentials and connection details.
2. Create a cell with the `client` script with the code above.
3. Run the `client` cell as defined above to create the client instance.
4. Make sure to use the correct user / password
5. Check the output to see if there are any errors

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

1. Make sure you have created the `config.py` file with your credentials and the
   `client` cell with the code above.
2. Run the `client` cell. If the connection is successful, you should see the
   message `--> Succesfully authenticated`:

    ```
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
| `client.user`         | Manage users including your own user details                           |
| `client.organization` | Manage organizations or the organization that you are part of|
| `client.rule`         | View all available permission rules |
| `client.role`         | Manage roles (are collections of rules) |
| `client.collaboration`| Manage collaborations |
| `client.task`         | Create new tasks and view their run data |
| `client.result`       | Obtain results from the tasks |
| `client.util`         | Provides utility functions for the vantage6 Python client. For example to reset your password             |
| `client.node`         | Manage nodes |
| `client.store`        | Manage algorithm stores |
| `client.algorithm`    | Manage algorithms that can be used for the computations |

### Method and parameter documentation
There are many methods available in each of the resources and each method has its own set
of parameters. To know which parameters are available for a specific method, you can use
the `help()` function in Python. For example, to get the documentation of the
`client.organization.list()` method, you can use the following command:

```python
help(client.organization.list)
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

::::::::::::::::::::::::::::::::::::: spoiler

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

::: tab

### Linux / MacOS

```bash
pip show vantage6-client | grep Version
```

### Windows

```cmd
pip show vantage6-client | findstr Version
```

:::

:::::::::::::::::::::::::::::::::::::


::: callout

### Permissions

Note that the authenticated user may not be allowed to perform all operations or view all
resources. For example, a user may not be allowed to create a new organization, but may
be allowed to list the organizations within all collaboration its organization
participates in. The server will only allow the user to perform operations on the
resources that the user has permission to perform.

:::


### The 5 basic operations

Almost all of the resources provide a [get](#get), [list](#list), [create](#create),
[update](#update) and [delete](#delete) operation. When using the `get` and `list`
methods a dictionary is returned with the requested information. In the case of the
`create` and `update` methods typically the created resource is returned. Finally in the
case of `delete` nothing is returned but a message is printed to confirm the deletion.

::::::::::::::::::::::::::::::::::::: tab


### List
Get all *resource* items that the user is allowed to see with
`client.<resource>.list()`. For example:

```Python
client.organization.list()
```

The output should look similar to the following:
```output
[
    {'id': 1, 'name': 'Huckleberry Holdings', ...}
    {'id': 2, 'name': 'Lychee Labs', ...},
    {'id': 3, 'name': 'Pineapple Paradigm', ...},
    {'id': 4, 'name': 'Huckleberry Hub', ...},
    {'id': 5, 'name': 'Mango Matrix', ...},
    {'id': 6, 'name': 'Apple Innovations', ...},
    {'id': 7, 'name': 'eScience center', ...},
    {'id': 8, 'name': 'Grapefruit Group', ...},
    {'id': 9, 'name': 'Raspberry Revolution', ...},
]
```

The `list()` method returns a paginated result. Pagination divides the complete list of items into smaller parts, called pages. By default, the `list()` method returns the first page of 10 items. The page and the number of items per page can be specified with the `page` and `per_page` parameters.

### Get
Get a specific *resource* with `client.<resource>.get(<id>)`. For example:

```Python
client.organization.get(1)
```
```output
{
    'nodes': '/api/node?organization_id=1',
    'public_key': '',
    'studies': '/api/study?organization_id=1',
    'name': 'Huckleberry Holdings',
    'tasks': '/api/task?init_org_id=1',
    'address2': '',
    'users': '/api/user?organization_id=1',
    'domain': 'huckleberryholdings.mc',
    'country': 'Monaco',
    'zipcode': '98000',
    'runs': '/api/run?organization_id=1',
    'address1': '4747 Huckleberry Ln',
    'id': 1,
    'collaborations': '/api/collaboration?organization_id=1'
}
```

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
--> Organization id=1 was removed from the database
```

:::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### 2. Collect collaboration details

Before starting a task, you need to know the details of the collaboration you are working with. Use the Python client to get the details of the collaboration you have access to. Write down the **name** and **ID** of each collaboration.

:::::::::::::::::::::::: hint

Use the `client.collaboration.list()` method to get the details of the collaborations you have access to.

```python
client.collaboration.list()
```

::::::::::::::::::::::::

:::::::::::::::::::::::: hint

Use `help(client.collaboration.list)` to see which arugments you can use to filter the
collaborations.

::::::::::::::::::::::::

:::::::::::::::::::::::: hint

You can use the `fields` parameter to specify which fields you want to see in the output.

```python
client.collaboration.list(fields=['id', 'name'])
```

::::::::::::::::::::::::


:::::::::::::::::::::::: solution
```python
client.collaboration.list(fields=['id', 'name'])
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

::::::::::::::::::::::::::::::::::::: challenge

### 3. Find documentation

Find the documentation on how to reset your password 🔑 in case you forgot it. You can
use the `help()` to explore the client functions.

::: hint

Have a look at the [client table](#using-the-client), and see if you can find a
resource group that might contain the method you are looking for.

:::

::: hint

Use the `help()` function to find the documentation of the `client.util` resource.

:::

::: solution

To obtain a token:
```python
help(client.util.reset_my_password)
```
Then you can use:

```python
help(client.util.change_my_password)
```

The function `client.util.change_my_password` is used to change the password of the
authenticated user.
:::

::::::::::::::::::::::::::::::::::::::::::::::::

### Identifiers are key
It is important to note that the Python client use identifiers rather than names to
select resources. For example, to filter the organizations that belong to a a given
collaboration, you need to know the collaboration's identifier first.

In a previous challenge, you were asked to get the details of the collaborations you
have access to. This is common practice when working with the vantage6 Python client.

It is also possible to obtain these identifiers through the UI. However, when working
with the UI, identifiers are not as important as the names can be used to identify the
resources. But also for the UI, it is important to know the identifiers of the resources
as names are not always unique.

::: spoiler

#### Why identifiers?

The reason for this is that the UI is designed to more be user-friendly, and it is
expected that users will interact with the resources using their names. Typically
they will select the resources from a list or dropdown. Since names do not always
have to be unique (e.g. task names) it is impossible to identify a resource
uniquely by its name.

:::

Now that we understand the basic concepts of the vantage6 Python client, let us get
some more details about our collaborations. First, as before, we collect the details of
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
As the checklist above indicates, we have not checked the status of the nodes. You can
start an analys when nodes are offline, they will start the analysis once they are
online. In case a node is offline, you might need to inquire with the node owner to get
it back online.

::::::::::::::::::::::::::::::::::::: challenge

##### 4. Check the status of the nodes

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

One of the nodes in our collaboration is offline. In the real world, you would need to
contact the node owner to get the node back online. But for the purpose of this
workshop we have defined a [study](./chap2_introduction_v6.md#project-administration-in-vantage6)
that contains only online nodes. Which has a name that ends with *Subset*. You can find
the study ID by using the `client.study.list()` method. Write down the ID of the study.

```python
client.study.list(fields=("id", "name"))
```

#### Task definition

A task in vantage6 is a request to execute an algorithm on a given organization. When
creating a task, you need to specify the following:

- The collaboration[, study] and organization identifiers.
- The algorithm to be executed.
- The input parameters for the algorithm.

The average algorithm we are going to use is the same as in [Episode 3](./chap3_run_analysis_ui.md#running-a-simple-federated-algorithm).

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
   collaboration=1,
   organizations=[1,2,3,4],
   study=4,
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

This means that in case you want to use the task result in the remainder of your code,
your program needs to wait until the task is completed, so you can get access to the
results (or to the error details, if something goes wrong).

You can use the `client.wait_for_result()` method to make the program execution wait
until the task is completed. For that, you need the ID of the task you just created,
which was included in the dictionary returned by the `client.task.create()` method.
For the task execution request of the code snippet above, this will look like:

```python
task_id = average_task['id']
result = client.wait_for_results(task_id)
```

### Aggregate results

The results contain the output of the algorithm. In the case of the `partial_average()`
function, the output is not yet aggregated. This means that the output of each node is
returned separately. In the case of the `central_average()` function, the output is
aggregated and only the aggregated result is returned.

For now we can aggregate the results ourselfs:

```python
import json
global_sum = 0
global_count = 0
for output in results["data"]:
    output = json.loads(output["result"])
    global_sum += output["sum"]
    global_count += output["count"]

print(global_sum / global_count)
```

### Create a central task

In the previous section you created a task to run the `partial_average()` function. Now,
create a task to run the `central_average()` function.

::::::::::::::::::::::::::::::::::::: challenge

## 5. Run central method

In section [Creating a new task](#creating-a-new-task) it is explained how to create a
task to run the `partial_average()` function. Now, create a task to run the
`central_average()` function. ⚠ Make sure to **only** send the task to a single
organization.

:::::::::::::::::::::::: solution

```python
input_ = {
    'method': 'central_average',
    'args': [],
    'kwargs': {'column_name': 'age'}
}

average_task = client.task.create(
   organizations=[1],
   study=1,
   name="name_for_the_task",
   image="harbor2.vantage6.ai/demo/average",
   description='',
   input_=input_,
   databases=[
      {'label': 'default'}
   ]
)
```

Then you can obtain the results by using the `client.wait_for_results()` method:

```python
task_id = average_task['id']
result = client.wait_for_results(task_id)
print(result)
# '{"average": 48.8}'
```

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

### Inspecting log files

Each task consists of several runs. Each node included in the task execution will at
least have one run. But in case of multi-step algorithms or iterative algorithms, a
node can have multiple runs. Each run has a log file that contains information about
the execution of the algorithm on the node.

::::::::::::::::::::::::::::::::::::: challenge

## 6. Inspect log files

1. Retrieve the log files from the central method from previous challenge.
2. Rerun the central method, but this time use a column name that does not exist in the
   dataset (e.g. `abc123`). Retrieve the log files from this task as well.

:::::::::::::::::::::::: solution

To retrieve the log files from any task, you can use the `client.run.from_task()`
method:
```python
runs = client.run.from_task(task_id)
for run in runs["data"]:
    print(run['log'])
```

In the second case you should be able to find an exception in the log file. Is the error
message clear enough to understand what went wrong?

:::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::::::::::
