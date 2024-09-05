---
title: "Algorithm development"
teaching: 10
exercises: 5
---

:::::::::::::::::::::::::::::::::::::: questions

- What do the algorithm tools in vantage6 provide?
- How do you create a personalized boilerplate using the v6 cli?
- What is the process for adapting the boilerplate into a simple algorithm?
- How can you test your algorithm using the mock client?
- How do you build your algorithm into a docker image?
- How do you set up a local test environment using the v6 cli (`v6 dev`)?
- How can you publish your algorithm in the algorithm store?
- How can you run your algorithm?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the available algorithm tools
- Create a personalized boilerplate using the v6 cli
- Adapt the boilerplate into a simple algorithm
- Test your algorithm using the mock client
- Build your algorithm into a docker image
- Set up a local test environment using the v6 cli (`v6 dev`)
- Publish your algorithm in the algorithm store
- Run your algorithm in the UI
- Run your algorithm with the Python client

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

The goal of this lesson is to develop a simple average algorithm, and walk through
all the steps from creating the proper code up until running it in the User Interface
and via the Python client. We will start by explaining how the algorithm
interacts with the vantage6 infrastructure. Then, you will start to build, test and run
your own algorithm.

## Algorithm tools

The vantage6 infrastructure provides a set of tools to help you develop your
algorithm. You can install the algorithm tools with:

```bash
pip install vantage6-algorithm-tools
```

The algorithm tools provide the following for you:

- **Algorithm client**: this client can be used to interact with the server, e.g.
  to create a subtask, retrieve results, or get the organizations participating in the
  collaboration.
- **Data loading**: the tools provide a way to load the data from the node and provide it
  to the algorithm as a Pandas dataframe.
- **Input**: the tools read the input from the node and provide it to the arguments
  of the algorithm function.
- **Environment variables**: the tools get the environment variables from the node
  and pass them on to the algorithm
- **Token**: the algorithm tools ensure that the algorithm uses the security token
  to be able to get the allowed resources from the server.
- **Output handling**: the output from the algorithm functions is written to a file such
  that the node will send back to the server.

For more information about the algorithm tools, please check out the relevant
[documentation][algo-concepts].

## Create a simple algorithm

Vantage6 requires the functions in the algorithm to be at the base level of a Python
package that is defined within the Docker image. These requirements can be cumbersome to
get right if you have to write all the code yourself. Fortunately, vantage6 provides
tools to create a boilerplate for you, so that you can focus on the development of your
algorithm functions rather than worry about the infrastructure.

To create a personalized boilerplate, use the vantage6 CLI. If you haven't done so yet,
install it with:

```bash
conda create -n v6-workshop python=3.10
conda activate v6-workshop
pip install vantage6
```

Then, create a new algorithm boilerplate repository with:

```bash
v6 algorithm create
```

If you later want to modify your answers, you can do so by running:

```bash
v6 algorithm update --change-answers
```

This is recommended to do whenever you want to change something like the name of the
function, as it will ensure that it will be updated in all places it was mentioned.

The update command can also be used to update your algorithm to a new version, even
after you have implemented your functions. This is helpful when there is new
functionality or changes in vantage6 that require algorithms to update.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Create a personalized boilerplate

Create a personalized template to start developing your average algorithm

- We need both a central and a partial function.
- The central function should get an algorithm client to communicate with the server,
  but it does not need data.
- The partial function does not need an algorithm client, but it should get one database
  from the node.
- Both functions should have a `column` argument - the average over this column will
  be calculated.
- (Optional) Use the advanced options to create a Github pipeline that creates and
  pushes your Docker image every time you commit to main.

:::::::::::::::::::::::: solution

## Solution

The personalized boilerplate should be successfully created.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Your personalized boilerplate is now ready to be adapted into a simple algorithm. We
are now going to implement the average algorithm in several steps. Note that the README
file in the boilerplate also provides a checklist that you can follow to implement the
rest of the algorithm - however, in this lesson we are going to guide you through these
steps.

### Implement the algorithm functions

We are going to implement the central and partial functions. The easiest is to start
with the partial function. Using the Pandas dataframe that is provided by the algorithm
tools, the following should be extracted for the requested column:

- The number of rows that contains a number
- The sum of all these numbers

The boilerplate code for the central function already a large part of the code that will
be required to gather the results from the partial functions. To compute the final
average, we will need to:

- Modify how the subtasks are created - we need to provide the column to the partial
  functions
- Combine the results from the partial functions to compute the average

Remember that both functions should return the results as valid JSON serializable
objects - we recommend returning a Python dictionary.

### Test your algorithm using the mock client

As discussed before, the algorithm tools contain an algorithm client that helps the
algorithm container to communicate with the server. When testing your algorithm,
it would be cumbersome to test your algorithm in the real infrastructure on every code
change, as this requires you to build your algorithm image, ensure all nodes in your
collaboration are online, etc. To facilitate the testing phase, the algorithm tools
also provide a mock client. This client can be used to test your algorithm locally
without having to start up the server and nodes. The mock client provides the same
functions as the algorithm client, but instead of communicating with the server, it
simply returns a smart mock response. The mock client does **not** mock the output
of the algorithm functions, but actually calls them with test data. This way, you can
easily test locally if your algorithm functions give the answer you expect without
worrying about the infrastructure.

Your personalized template already contains a `test/test.py` file that contains
most of the code to test your algorithm.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Implement the functions and test them

Implement your partial and central functions as described above.

Adapt and run `test.py` to test your function implementation:

- Create a Python environment and run `pip install -e .`. This installs the local Python
  package and also the algorithm tools (which contain the mock client).
- Adjust `test.py` to compute the average over the **age** column. Do this both
  for the test of the central and of the partial function
- Run `test.py` to test your functions.

:::::::::::::::::::::::: solution

## Solution

You output of `test.py` should look something like:

```
[{'id': 0, 'name': 'mock-0', 'domain': 'mock-0.org', 'address1': 'mock', 'address2': 'mock', 'zipcode': 'mock', 'country': 'mock', 'public_key': 'mock', 'collaborations': '/api/collaboration?organization_id=0', 'users': '/api/user?organization_id=0', 'tasks': '/api/task?init_org_id=0', 'nodes': '/api/node?organization_id=0', 'runs': '/api/run?organization_id=0'}, {'id': 1, 'name': 'mock-1', 'domain': 'mock-1.org', 'address1': 'mock', 'address2': 'mock', 'zipcode': 'mock', 'country': 'mock', 'public_key': 'mock', 'collaborations': '/api/collaboration?organization_id=1', 'users': '/api/user?organization_id=1', 'tasks': '/api/task?init_org_id=1', 'nodes': '/api/node?organization_id=1', 'runs': '/api/run?organization_id=1'}]
info > Defining input parameters
info > Creating subtask for all organizations in the collaboration
info > Waiting for results
info > Mocking waiting for results
info > Results obtained!
info > Mocking waiting for results
[{'average': 34.666666666666664}]
{'id': 2, 'runs': '/api/run?task_id=2', 'results': '/api/results?task_id=2', 'status': 'completed', 'name': 'mock', 'databases': ['mock'], 'description': 'mock', 'image': 'mock_image', 'init_user': {'id': 1, 'link': '/api/user/1', 'methods': ['GET', 'DELETE', 'PATCH']}, 'init_org': {'id': 0, 'link': '/api/organization/0', 'methods': ['GET', 'PATCH']}, 'parent': None, 'collaboration': {'id': 1, 'link': '/api/collaboration/1', 'methods': ['DELETE', 'PATCH', 'GET']}, 'job_id': 1, 'children': None}
info > Mocking waiting for results
[{'sum': 624.0, 'count': 18}, {'sum': 624.0, 'count': 18}]
```

Hence, the average age is 34.666!

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Build your algorithm into a docker image

Your algorithm boilerplate contains a `Dockerfile` in the root folder. You can build
your algorithm into a docker image by running something like:

```bash
cd /go/to/directory/with/dockerfile
docker build -t your-image-name .
```

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: Implement the functions and test them

Build an algorithm image with the name: `harbor2.vantage6.ai/workshop/average:<myname>`.
Replace `myname` with the first letter of your first name and your last name (e.g.
`lmessi` for Lionel Messi). Push it to the repository.

:::::::::::::::::::::::: solution

## Solution

If your name is Jane Smith, you may have done the following in the base directory of
your algorithm (where the Dockerfile is):

```bash
docker build -t harbor2.vantage6.ai/workshop/average:jsmith .
docker push harbor2.vantage6.ai/workshop/average:jsmith
```

Both commands should execute without errors.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Set up a local test environment

When the algorithm image is built, it is recommended to test locally if it also works
with an actual server and nodes - not just using the mock client. The easiest way to
set up a server and a few nodes locally with:

```bash
v6 dev create-demo-network
```

This command creates a vantage6 server configuration, and then registers a
collaboration with 3 organizations in it. It registers a node for each organization and
finally, it creates the vantage6 node configuration for each node with the correct API
key.

The other available commands are:

```bash
# Start the server and nodes
v6 dev start-demo-network

# Stop the server and nodes
v6 dev stop-demo-network

# Remove the server and nodes
v6 dev remove-demo-network
```

In [Chapter 5](./chap5_python_client.md), you have learned how to run an algorithm using the Python
client. Now, you can run your own algorithm using the Python client!

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: Test your algorithm on a local vantage6 network

Create and start a local vantage6 network with the `v6 dev` commands. Then, run your
algorithm using the Python client. You can find the command to run your algorithm in
the `test.py` file, since the mock client has exactly the same syntax as the real client.

<!-- TODO an alternative is to do this all locally, but that only works if vdev has UI + algorithm store -->

:::::::::::::::::::::::: solution

## Solution

Your algorithm should give the same results as when you tested it with the mock client.

::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::

## Publish your algorithm in the algorithm store

[Previously](./chap3_run_analysis_ui.md), we have discussed how to run algorithms from the algorithm store.
Now, it is time to publish your own algorithm in the algorithm store. This is required
if you want to run your algorithm in the user interface: the user interface gathers
information about how to run the algorithm from the algorithm store. For example, this
helps the UI to construct a dropdown of available functions, and to know what arguments
the function expects.

The boilerplate you create should already contain an `algorithm_store.json` file that
contains a JSON description of your algorithm - how many databases each function uses,
for example.

You can put the algorithm in the store by selecting the algorithm store in the UI, then
clicking on the "Add algorithm" button. You can then upload the `algorithm_store.json`
file in the top. After uploading it, you can change the details of the algorithm before
submitting it.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 5: Add your algorithm to the algorithm store

Upload your algorithm to the algorithm store. Submit the `algorithm_store.json`, check
the filled in details, and submit the algorithm.

Then, can you download the revised JSON file so you can update it in your algorithm
repository?

:::::::::::::::::::::::: solution

## Solution

You can find the revised JSON file on the page with the algorithm details

::::::::::::::::::::::::::::::::::::::::::::::::
::::::::

## Next steps

Congratulations! You have successfully developed your first algorithm. You have learned
how to create a personalized boilerplate, implement the algorithm functions, and run the
algorithm using the Python client and the UI. The resulting algorithm, however, is not
suitable yet for real-world use. For instance, if a node contains only a single data
point for a given column, there are no guards implemented that prevent that such
sensitive data is shared with the server. Here, we describe a few next steps that are
usually important to take before your algorithm is ready for real-world use:

- **Privacy filters**: implement privacy filters to ensure that sensitive data is not
  shared with the server.
- **Error handling**: implement error handling to ensure that the algorithm does not
  crash when unexpected input is provided. Note that there are [custom vantage6 errors][v6-errors]
  that you can raise to provide more information about what went wrong.
- **Documentation**: document your algorithm so that others can understand how to use
  it.

Other next steps could be to extend the algorithm with more functionality, such as
allowing to calculate the average over multiple columns, or to add a `group_by`
argument to compute the average per group. Alternatively, you can have a look at other
algorithms in the algorithm store to see if you can understand and/or improve them.

In the final lesson of this course, you will have the opportunity to work on your own
projects. Maybe you can also use that opportunity to further develop your algorithm!

::::::::::::::::::::::::::::::::::::: keypoints

- Use `v6 algorithm create` to create a personalized boilerplate
- Implement the central and partial functions
- Build your algorithm into a docker image
- Test it with the mock client and generate a local test environment with `v6 dev`
- Publish your algorithm in the algorithm store to run it in the UI

::::::::::::::::::::::::::::::::::::::::::::::::

[algo-concepts]: https://docs.vantage6.ai/en/main/algorithms/concepts.html
[v6-errors]: https://docs.vantage6.ai/en/main/function-docs/_autosummary/vantage6.algorithm.tools.exceptions.html#module-vantage6.algorithm.tools.exceptions
