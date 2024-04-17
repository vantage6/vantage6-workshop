---
title: "Algorithm development"
teaching: 10
exercises: 2
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

The goal of this lesson is to develop a very simple average algorithm, and walk through
all the steps from creating the proper code up until running it in the User Interface
and via the Python client. We will start by explaining how the algorithm
interacts with the vantage6 infrastructure. Then, you will start to build your own
algorithm, then test and run it.

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
- **Data**: the tools provide a way to load the data from the node and provide it
  to the algorithm as a Pandas dataframe.
- **Input**: the tools read the input from the node and provide it to the arguments
  of the algorithm function.
- **Environment variables**: the tools get the environment variables from the node
  and pass them on to the algorithm
- **Token**: the algorithm tools ensure that the algorithm uses the security token
  to be able to get the allowed resources from the server.
- **Output**: the output from the algorithm functions is written to the proper file, so
  that the node will send it back to the server.

Many of these functionalites are handled by using Docker file mounts, which are read
from and written to by the algorithm tools.

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
pip install vantage6
```

Then, create a new boilerplate with:

```bash
v6 algorithm create
```

If you later want to modify your answers, you can do so by running:

```bash
v6 algorithm update --change-answers
```

The update command can also be used to update your algorithm to a new version, even
after you have implemented your functions.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Create a personalized boilerplate

Create a personalized template to start developing your average algorithm

- We need both a central and a partial function.
- The central function should get an algorithm client to communicate with the server,
  but it does not need data.
- The partial function should get one database from the node.
- Both functions should have a `column` argument - the average over this column will
  be calculated.
- (Optional) Use the advanced options to create a Github pipeline that creates and
  pushes your Docker image every time you commit to main.

TODO what do they need to do for central?

:::::::::::::::::::::::: solution

## Output

The personalized boilerplate should be successfully created.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Your personalized boilerplate is now ready to be adapted into a simple algorithm. We
are now going to implement the average algorithm in several steps. Note that the README
file in the boilerplate also provides a checklist that you can follow to implement the
rest of the algorithm; however we are going to guide you through the process in this
lesson.

### Implement the algorithm functions

We are going to implement the central and partial functions. The easiest is to start
with the partial function. Using the Pandas dataframe that is provided by the algorithm
tools, the following should be extracted for the requested column:

- The number of rows that contains a number
- The sum of all these numbers

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
easily test your algorithm functions locally without worrying about the infrastructure.

Your personalized template already contains a `test/test.py` file that contains
most of the code to test your algorithm.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Implement the functions and test them

Implement your partial and central functions. Adapt and run `test.py` to test your
function implementation.

TODO add more details

:::::::::::::::::::::::: solution

## Output

TODO the average reported by `test.py` should be X. It should also provide sum Y and
count Z for each of the partial functions.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Build your algorithm into a docker image

Your algorithm boilerplate contains a `Dockerfile` in the root folder. You can build
your algorithm into a docker image by running:

```bash
docker build -t your-image-name .
```

in the directory where your `Dockerfile` resides.

Note that if you have selected the advanced options when creating your boilerplate,
you had the option to include a Github action pipeline that built the Docker image for
you every time a commit is pushed to main. This is the preferred way of working for
real-world projects with open-source algorithm implementations.

TODO include exercise to build the algorithm image

## Set up a local test environment

When the algorithm image is built, it is recommended to test locally if it also works
with an actual server and nodes - not just using the mock client. The easiest way to
set up a server and a few nodes locally with:

```bash
v6 dev create-demo-network
```

TODO test on linux/mac?
TODO it would be very convenient to add algorithm store and UI to this network

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

In the previous lesson, you have learned how to run an algorithm using the Python
client. Now, you can run your own algorithm using the Python client!

TODO link to lesson 5 where Python client is discussed

TODO exercise to test the algorithm on the local network

## Publish your algorithm in the algorithm store

In previous lessons, we have discussed how to run algorithms from the algorithm store.
Now, it is time to publish your own algorithm in the algorithm store. This is required
if you want to run your algorithm in the user interface: the user interface gathers
information about how to run the algorithm from the algorithm store. For example, this
helps the UI to construct a dropdown of available functions, and to know what arguments
the function expects.

The boilerplate you create should already contain an `algorithm_store.json` file that
contains a JSON description of your algorithm - how many databases each function uses,
for example.

TODO link in first sentence to lesson where algorithm store is discussed (lesson 3)

TODO this lesson is not finished yet as it depends on algorithm store/UI development to
be completed over the next months. It should include:

- whether they should run an algorithm store locally and how?
- how to publish the algorithm in the store. This can at the moment be done via the API
  or Python client, but in future should be easier via the UI.

TODO exercise to publish the algorithm and run it in the UI. What should they adapt the algorithm_store.json?

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
  crash when unexpected input is provided.
  TODO include something about the v6 errors here
- **Documentation**: document your algorithm so that others can understand how to use
  it.

Other next steps could be to extend the algorithm with more functionality, such as
allowing to calculate the average over multiple columns, or to add a `group_by`
argument to compute the average per group.

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

<!-- TODO add reference to function documentation of client so that people know where to look for functions (or help(client)) -->
