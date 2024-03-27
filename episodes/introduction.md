---
title: "Introduction to privacy enhancing technologies (PET)"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions

- TODO

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand PET, FL, MPC, homomorphic encryption, differential privacy
- Understand how different PET techniques relate
- Understand scenarios where PET could be applied
- Understand horizontal vs vertical partitioning
- Decompose a simple analysis in a federated way
- Understand that there is paperwork to be done (DPIA etc.)
::::::::::::::::::::::::::::::::::::::::::::::::

## Problem statement

The amount of data being generated nowadays is absolutely mind-boggling. This data can be a valuable
resource for researchers. However, privacy regulations will prevent easy access to this wealth of
data, and this is a good thing. Privacy enhancing technologies (PETs) are a way to gain valuable
insights from sensitive data while still respecting the privacy Furthermore, researchers are often more interested in the insights derived from data
rather than the raw data itself. This raises an intriguing question: Can we unlock these valuable
insights in a manner that upholds and respects privacy standards?

## Introducing the landscape of PETs
Incomplete list of PETs:
- Homomorphic encryption
- Federated learning
- Secure Multiparty Computation
- differential privacy
- synthetic data

See individual PETs as building blocks to craft your analyses.

## Data partitioning
Data sharing challenges come in many different shapes and sizes, but in the end, the goal of the
researchers is often to analyze data *as if* it were available in one big table in one place. 
There are 2 main ways in which the dataset can be separated over different sources: **horizontal**
and **vertical** partioning. In horizontal partitioning, this giant table has been snipped in pieces
by making horizontal cuts. The result is that information of an individual record will stay in one
place, but the records themselves have been scattered around in different locations.

In vertical partitioning, the cuts have been made vertically. Columns have now been divided over
different locations. This type of partitioning is usually more challenging because often a way needs
to be found to link identities accross datasources.

In reality, data can be horizontally and vertically partitioned at the same time. It might be
necessary to combine multiple techniques in order to overcome your problems.

## Example: federated average

## Technology doesn't solve everything

Paperwork, trust, etc.
::::::::::::::::::::::::::::::::::::: keypoints

- TODO

::::::::::::::::::::::::::::::::::::::::::::::::

[r-markdown]: https://rmarkdown.rstudio.com/
