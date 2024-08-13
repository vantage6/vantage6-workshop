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
you.

# Advanced challenges

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Add privacy filters to your algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. Now, you can add privacy filters to your algorithm.

- Create an algorithm that does not return the results unless there are more than 10
  data points.
- Make this value configurable by the node administrator. Hint: look up the node
  configuration options in the [documentation](https://docs.vantage6.ai) to provide
  environment variables to your algorithm.
- What else could you do to protect the privacy of the data?
- When the privacy filters are triggered, use one of the [vantage6
  exceptions](https://docs.vantage6.ai/en/main/function-docs/_autosummary/vantage6.algorithm.tools.exceptions.html)
  to return an error message.

:::::::::::::::: hint

The [contingency table algorithm](https://github.com/vantage6/v6-crosstab-py)
already has a few privacy filters implemented. You can use this algorithm as an example.

::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Use your own data the v6 dev network

The algorithm that you created in the [previous lesson](./chap7_algo_dev.md) uses
dummy data. In this challenge, you will use your own data in the `v6 dev` network.

Locate and modify the node configuration files. Before starting the algorithm, how can
you make sure that the data is available to the nodes?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Document your algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. For this challenge, learn how to document your algorithm.

- Make sure a documentation template is available in the algorithm repository. If it is
  not, you can generate it using the `v6 algorithm` command.
- Try out how you can run the documentation locally in your browser, and adapt it to
  your needs.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Visualize the results of your algorithm in the UI

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
algorithm. In this challenge, modify the algorithm in the algorithm store to include
a visualization of the results. You can do this in the UI by modifying your algorithm
in the algorithm store.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Expand your average algorithm

In the [previous lesson](./chap7_algo_dev.md), you have created a simple
average algorithm. In this challenge, expand your algorithm to calculate the one or
more of the following:

- Standard deviation
- Minimum
- Maximum

Consider which data you share in the partial results and how you can minimize this
to protect the privacy of the data.

::::::::::::::::::::::::::::::::::::::::::::::::
