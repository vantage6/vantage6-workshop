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
resource for researchers. However, personal data should be handled with great care and responsibility
because of its sensitive nature. This is why there are privacy regulations in place like 
[GDPR](https://gdpr-info.eu/) to prohibit easy access to this wealth of data. 

However, often researchers are not interested in the personal records that make up the data, but rather
in the *insights* derived from it. This raises an intriguing question: Can we unlock these valuable
insights in a manner that upholds and respects privacy standards?

## Introducing the landscape of PETs

Privacy enhancing technologies (PETs) are a way to gain valuable
insights from sensitive data while still respecting the privacy of the individuals in the raw
datasets.There are many different technologies in which data can be shared and analyzed while the
privacy of
individuals can be protected. It often depends on the exact use case which technology is
appropriate. We will not be able to cover all the techniques that can be used. However, we will list
a number of common technologies that can be used in the context of vantage6.

The main idea of the technologies that we will list is that we select the ones still enable the
*analysis* of the data while shielding the identities of the people in the dataset. An analysis is 
often akin to a form of *aggregation* of the data. This can be in the shape of traditional statistics
like the mean, or it can be more intricate like a machine learning model. Aggregating the data does
not ensure complete protection of person-level information, but it certainly makes
it less likely that this will happen. Usually the final solution consists of a mix of a variety of
technical and non-technical measures to provide multiple layers of security.

### Data anonymization and pseudonymization

The first step in the process is often *data anonymization*. Personal identifiable information
will in this case be removed so that individuals stay anonymous. Data *pseudonimization* is a
similar process, but in this case, the records will be assigned an id that will make it
possible to link individuals across datasets.

While data anonymization and pseudonymization are often a good first step, there is no guarantee that
the data will never be reidentified. A famous example of reidentification is the story of the
[Netflix prize](https://en.wikipedia.org/wiki/Netflix_Prize). The Netflix prize was an open
competition to build the best recommender system to predict user ratings for films based on previous
ratings. The data was anonymized, but in 2007 two researchers from The University of Texas at Austin 
were able to identify a large number of users by matching the dataset with film ratings on the
Internet Movie Database (IMDB).

### Homomorphic encryption

Homomorphic encryption is a form of encryption that allows computations to be performed on
ciphertexts. The result of a computation is a new ciphertext, that, when decrypted, matches the
result of the same operations performed on plaintext. In this way, data scientists can perform
analyses on the data without knowing the underlying data.

One caveat to keep in mind is that the fact that the data cannot be decrypted right now, it might 
still be possible to do so in the future. Therefore it is important that the encrypted data is
deleted from all machines when the analysis is done. This requires a high level of trust with the
other parties that will handle the homomorphically encrypted data.

### Federated Learning
In homomorphic encryption the raw data, albeit encrypted, is passed around to other parties. 
Usually it is preferred to leave the raw data at the original location. A classic example of this
is federated learning. The term federated learning was introduced in 2016 by researchers at Google 
(McMahan et al.) and refers to a "loose federation of participating devices which are coordinated by
a central server". Federated learning generally refers to a situation where multiple devices train
a machine learning model. The resulting collection of models (or rather, weights or gradients) is 
then aggregated at a central server into the final model.

A common caveat with this type of analysis is that the gradients that are shared with the central
server could still be used to reconstruct the original data. This vulnerability is known as
*gradient leakage*.

### Secure Multiparty Computation
Secure Multiparty Computation (MPC) is a subset of techniques where computations are performed 
collaboratively by multiple parties. Data is encrypted in such a way that other parties cannot see
the original values, but values of multiple parties can still be combined (e.g. added or multiplied).
A classic technique from the field of MPC is secret sharing. With this technique data is encrypted, after
which pieces of the encryption are sent to the other parties. No single party will be able to
reconstruct the original value. Only when all parties work together, the original value can be retrieved.

When combining multiple values using secret sharing, this will result in the parties owning new 
puzzle pieces that when put together will reveal the result of the computation.

TODO: picture

TODO: Exercise with secret sharing where data is leaked.


### Differential privacy
As mentioned before, aggregation of data will not always prevent leaks of sensitive information.
Differential privacy deals with techniques to prevent this from happening. This is often done by
making small random changes to the individual data so that the statistical properties stay intact.

An algorithm is differentially private if it cannot be proven with certainty that a specific individual
was part of the analysis. An individual has *plausible deniability* with regards to whether it was 
part of the dataset.

### Synthetic data


No solution is perfect.
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
