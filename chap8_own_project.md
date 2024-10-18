---
title: "Work on your own project"
teaching: 10
exercises: 1
---

:::::::::::::::::::::::::::::::::::::: questions

- How can you use vantage6 in your own project?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Start working on your own research project

OR

- Complete some advanced challenges

::::::::::::::::::::::::::::::::::::::::::::::::

# Working on your own project

In this chapter, we will give you the opportunity to work on your own project. Feel free
to ask questions and discuss your project with the instructors. We are here to help you!

If you prefer, you can also complete some advanced challenges that we have prepared for
you. Note that these challenges don't have one solution - discuss your solutions with
the workshop instructors!

# Advanced challenges

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Add privacy filters to your algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. Now, you can add privacy filters to your algorithm.

- Create an algorithm that does not return the results unless there are more than 10
  data points.
- Make this value configurable by the node administrator. Hint: look up the node
  configuration options in the [documentation](https://docs.vantage6.ai) to provide
  environment variables to your algorithm.
- When the privacy filters are triggered, use one of the [vantage6
  exceptions](https://docs.vantage6.ai/en/main/function-docs/_autosummary/vantage6.algorithm.tools.exceptions.html)
  to return an error message.
- What else could you do to protect the privacy of the data?

:::::::::::::::: hint

The [contingency table algorithm](https://github.com/vantage6/v6-crosstab-py/blob/main/v6-crosstab-py/partial.py#L64)
already has a few privacy filters implemented. You can use this algorithm as an example.

::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Use your own data the v6 dev network

The algorithm that you created in the [previous lesson](./chap7_algo_dev.md) uses
dummy data. In this challenge, you will use your own data in the `v6 dev` network.
If you don't have any data, you can use the
[Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

Locate and modify the node configuration files. Before starting the algorithm, how can
you make sure that the data is available to the nodes?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: Document your algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. For this challenge, learn how to document your algorithm.

- Make sure a documentation template is available in the algorithm repository. If it is
  not, you can generate it using the `v6 algorithm update --change-answers` command.
- Install the dependencies required to run the documentation locally. You can find the
  dependencies in the `requirements.txt` file in `docs` folder.
- Run the documentation locally in your browser. Use `docs/README.md` to find out how to
  do this.

For more details, learn about restructured text (rst) files online!

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: Visualize the results of your algorithm in the UI

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. In this challenge, modify the algorithm in the algorithm store to include
a table visualization. You can do this in the UI by modifying your algorithm
in the algorithm store.

Then, check that your algorithm's results are displayed in a table!

:::::::::::::::::: hint

### Hint: What do the docs say?

Check the [documentation](https://docs.vantage6.ai/en/main/algorithm_store/processes.html#algorithm-submission)

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 5: Expand your average algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
average algorithm. In this challenge, expand your algorithm to calculate the one or
more of the following:

- Standard deviation
- Minimum
- Maximum

Consider which data you share in the partial results and how you can minimize this
to protect the privacy of the data.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 6: Make your dev environment more secure

In the [previous lesson](./chap7_algo_dev.md), you have created a simple algorithm
with the `v6 dev` command. In this challenge, make your development environment more
secure.

Use the documentation to find configuration options that can help you to:

- Enable two-factor authentication in the vantage6 server.
- Change your node configuration to only allow running algorithms from the local
  algorithm store. Verify that it then no longer allows running the algorithms from the
  community store. Note that you can both whitelist single algorithms or entire
  algorithm stores.
- The `v6 dev` algorithm store has a specific setting that turns off the need for
  review of algorithms - they are automatically accepted. Change this setting to require
  review of algorithms. Feel free to explore the review process in the Algorithm Store
  section of the UI!

Are there any other security measures you can take to make your development environment
more secure?

:::::::::::::::::: hint

### Hint: Ajdusting configuration

To complete this challenge, locate the configuration files of the `v6 dev` network and
modify them. You may need to use the `--user` flag to locate the server and algorithm
store configuration files.

::::::::::::::::::::::::

::::::::::::::::::: hint

### Hint: Configuration changes don't take effect

Try restarting the `v6 dev` network after changing the configuration files.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::
