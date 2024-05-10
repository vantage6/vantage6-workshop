---
title: "Running a PET analysis without programming"
teaching: 0
exercises: 0
---

   - Find available algorithms in community store
   - Know an algorithm store can be created for their project
   - Run an algorithm in an existing collaboration
   - View partial results in UI
   - Understand privacy limit set by collaboration

Understand privacy limit set by collaboration: does this mean, for instance, that only people from organizations that belong to a collaboration will be able to see the results?

We define a collaboration as an agreement between two or more parties to participate in a study (i.e., to answer a research question). Moreover, there are a three fundamental functional aspects of FL infrastructures that are worth describing (and that are often overlooked8):


:::::::::::::::::::::::::::::::::::::: questions


:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explore in more depth an specific data analysis scenarios that further illustrates the concept of collaboration
- Understand the concept of 'algorithm trustworthiness' in the context of a collaboration
- Understand v6's algorithm-store current and envisioned features
- Understand the UI-based approach for performing a data analysis through the given scenarios 

::::::::::::::::::::::::::::::::::::::::::::::::


## Vantage6 collaborations illustrated

In the context of Vantage6, a collaboration refers to an agreement between two or more parties to participate in a study or to answer a research question together. This concept is central to the federated learning and multi-party computation (FL/MPC) infrastructures that Vantage6 supports. Each party involved in a collaboration remains independent and autonomous, meaning they retain control over their own data and can decide how much of their data to contribute to the collaboration's global model and which algorithms are allowed to be executed. 

To illustrate this, let's analize an hypotetical scenario: two international research projects relying on vantage6 technology on the same server. The first one, __PhY2024__ (Prevalence of hypertension and its association with lifestyle), requires to determine mean blood pressure levels of population across France, Spain and The Netherlands. The second, __GHT__ (Global Health Trends), requires to determine the Average BMI across The Netherlands, Spain and Germany. Although both projects are independent from each other, the data from Spain and The Netherlands -required by both- will be provided by the same national-level, large-scale cohort studies, namely CANTABRIA (Spain) and LIFELINES (The Netherlands). However, in both cases there are legal agreements that constraint each project to access only the data it actually needs (gaining access to the whole set of variables study increases risks of inference attacks). Data from French and German population (for __PhY2024__ and __GHT__ studies), on the other hand, will be provided by the GAZEL and GNC prospective cohort studies.

Following vantage6's concepts, this scenario would involve two collaborations, one for each research project. As described on the previous sections, a vantage6 node is needed for each collaboration. For this resason, as illustrated in the diagram below, CANTABRIA and LIFELINES organizations would require two vantage6-data node instances each one. As each data node define its own data access and algorithms usage rules, this ensures that analysis from different collaborations, with common organizations/datasets will not cause conflict with each other.

![alt text](fig/chapter3/orgs_n_collabs_scenario.png)


## Algorithms trustworthiness on a federated setting

Although a technical infrastructure like the described on the previous sections provide a good measure against most data privacy risks, there is one key security element that scapes from the platform's realm: the validation of the code that will be running on this infrastructure. For instance, the administrators of the nodes running within each organization are responsibles for defining which algorithms (i.e., [which the docker images](https://docs.vantage6.ai/en/main/node/configure.html#all-configuration-options)) will be allowed for execution on their running nodes. As this is a critical and complex task that entails activities like code analysis, working with algorithms from trusted sources is the first measure for preventing potential threats. 

Vantage6's algorithm store feature is aimed at enabling this trustworthiness by providing a centralized way of managing pre-registered algorithms. It is an alternative to the use of algorithms from unkown authors or lacking details about its development process and status. The algorithm store currently allow researchers to explore which algorithms are available and how to run them, which, along with its integration with the UI, simplifies the request of a task execution within a collaboration. At the time of writing this document, the integration of information such as who created the algorithm or who reviewed the code is a work in progress. Furthermore, the algorithm-review process is planned to be itegrated on the publication process on any algorithm store.



::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: 


::::::::::::::::::::::::::::::::::::::::::::::::



::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: 


:::::::::::::::::::::::: solution

## Output

1. Check it with your instructor.
2. Yes, you should be able to create a new organization, a new user, and a new collaboration. If not, ask your instructor to give you the necessary permissions.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::





Running PET analysis without programming

Find available algorithms in community store

Know an algorithm store can be created for their project

Run an algorithm in an existing collaboration

View partial results in UI

Understand privacy limit set by collaboration
