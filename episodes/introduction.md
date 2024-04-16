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
insights from sensitive data while still respecting the privacy Furthermore, researchers are often
more interested in the insights derived from data
rather than the raw data itself. This raises an intriguing question: Can we unlock these valuable
insights in a manner that upholds and respects privacy standards?

## Introducing the landscape of PETs

There are many different technologies in which data can be shared and analyzed while the privacy of
individuals can be protected. It often depends on the exact use case which technology is
appropriate. We will not be able to cover all the techniques that can be used. However, we will list
a number of common technologies that can be used in the context of vantage6.

The main idea of the technologies that we will list is that we select the ones still enable the
*analysis* of the data while shielding the identities of the people in the dataset. 
Common technologies like encryption are incredibly important, and is implemented in vantage6 as well,
however it is not part of our list of PETs because when it is applied (i.e. the data is encrypted), 
it is impossible to perform any form of computation on it.

TODO: Something about aggregation

### Data anonymization and pseudonymization

The first step in the process is often *data anonymization*. Personal identifiable information
will in this case be removed so that individuals stay anonymous. Data *pseudonimization* is a
similar process, but in this case, the records will be assigned an id that will make it
possible to link individuals across datasets.

While data anonymization and pseudonymization is often a good first step, there is no guarantee that
the data will never be reidentified. A famous example of reidentification is the story of the
[Netflix prize](https://en.wikipedia.org/wiki/Netflix_Prize). The Netflix prize was an open
competition to build the best recommender system to predict user ratings for films based on previous
ratings. The data was anonymized, but in 2007 two researchers from The University of Texas at Austin
(Vitaly Shmatikov and Arvind Narayanan) were able to identify a large number of users by matching
the dataset with film ratings on the Internet Movie Database (IMDB).

### Homomorphic encryption
Homomorphic encryption is a form of encryption that allows computations to be performed on
ciphertexts. The result of a computation is a new ciphertext, that, when decrypted, matches the
result of the same operations performed on plaintext. In this way, data scientists can perform
analyses on the data without knowing the underlying data. 

Incomplete list of PETs:

- Data anonymization
- Homomorphic encryption
- Federated learning
- Secure Multiparty Computation
- differential privacy
- synthetic data

See individual PETs as building blocks to craft your analyses.

### Who can you trust?

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
