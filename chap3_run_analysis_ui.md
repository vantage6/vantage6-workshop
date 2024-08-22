---
title: "Running a PET analysis without programming on vantage6"
teaching: 2
exercises: 3
---

:::::::::::::::::::::::::::::::::::::: questions

- How does a vantage6 collaboration work?
- How to check the status of a given collaboration within vantage6?
- How to link an algorithm store to a given collaboration?
- How to run a task through vantage6's UI?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explore specific data analysis scenarios that further illustrate the concept of collaboration
- Understand the concept of 'algorithm trustworthiness' in the context of a vantage6 collaboration
- Understand vantagee6's algorithm-store current and envisioned features
- Understand the UI-based approach for performing a data analysis through the given scenarios

::::::::::::::::::::::::::::::::::::::::::::::::

## Vantage6 user interface basics

To navigate vantage6's UI seamlessly, it's essential to grasp the platform's fundamental concepts and their interconnections, as the UI design reflects these relationships. These fundamental concepts are defined as follows:

- An **Organization** is a group of users that share a common goal or interest (e.g., a consortium, an institute, etc.). 
- A **Collaboration** involves one or more **organizations** working together towards a shared objective. 
- A **Node** is a vantage6 component with access to the **organization** data, which is capable of executes algorithms on it. It represents the organization's contributions to the network.
- A **Task** is a request for the execution of a given analysis **algorithm** on one or more **organizations** within a **collaboration**. These execution requests are handled by the corresponding organizations' **nodes**.
- An **user** is a person that belongs to one **organization** who can create **tasks** for one or more **organizations** within a **collaboration**.
- An **algorithm** is a computational model or process -that adhere to the vantage6 framework-, which can be securely distributed to **nodes** for execution on the corresponding organization's data.
- An **algorithm store** is a centralized platform for managing pre-registered **algorithms**. This serves as an alternative to using algorithms from unknown authors or those lacking transparency regarding their development process and status.

The diagram below illustrates a collaboration between two organizations. In this scenario, users from `Organization 1` and `Organization 3` — with the appropriate credentials — can request the execution of **tasks** within *Collaboration A*. In this case, a user from `Organization 1` might request the execution of an **algorithm** (previously registered in an **algorithm store** trusted by the collaboration) across all participating organization nodes. In response, each node from the involved organizations executes the **algorithm** on its local data. The resulting (aggregated) data is then sent back to the server, where it can be accessed by the requesting user.


![](fig/chapter3/collaboration_animated_exp.gif)


The following diagram expand the previous scenario further: what if `Organization 1` needs to participate on an additional **collaboration** with another **organization** (e.g., `Organization 2`)? In this case, `Organization 1` will have two running nodes, one for each collaboration. Moreover, as also depicted on the diagram below, each **collaboration** can make use of one or more **algorithm stores**:

![](fig/chapter3/v6-core-concepts-illustrated.drawio.png)


Finally, the concept of **study** is an important one when using vantage6 for data analysis. A **study** represents a subset of organizations within a given collaboration that are engaged in a specific research question. By setting up studies, you can more efficiently assign tasks to a specific group of organizations within a collaboration and better manage the results of these analyses. 

For example, consider the `Collaboration W` below, which includes six organizations. This collaboration might involve two distinct research questions: one that requires data from organizations 1, 2, 3, and 4, and another that focuses on data from organizations 4, 5, and 6. By establishing `Study Alpha` and `Study Beta`, you, as a researcher, can target your data analysis tasks in three different ways: you can address the entire `Collaboration W` (including nodes `A` to `F`), focus on `Study Alpha` (nodes `A` to `D`), or concentrate on `Study Beta` (nodes `D` to `F`).


![](fig/chapter3/v6-concepts-study.png)



::::::::::::::::::::::::::::::::::::: challenge

## Mapping vantage6 to "real life"

Let's consider a scenario where you, on behalf of your research institute, want to conduct a new study on a particular illness across three major academic hospitals in the Netherlands: VUmc in Amsterdam, Maastricht UMC+, and UMC Utrecht, as these have valuable data related to the illness. Consider the following:

- Your research institute has an existing collaboration (with a different purpose, not related with yours) with UMC Utrecht and UMC Groningen. Hence, there is a vantage6 node already running on your institution for the said collaboration.
- You will be conducting this study with a colleague from your institute named Daphne. Both of you are already registered on the organization but without access to the existing collaborations.

How would the concepts described above map to your potential use case?

1. Which organizations will you need to add to your collaboration?
2. How many new nodes would you need to set up and on which organizations?
3. How many users would be created?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution

1. In this case the organizations would be the academic hospitals as well as your own organization: VUmc, Maastricht UMC+, UMC Utrecht *and* your research institue. Note that UMC Utrecht must be added to the new collaboration despite being already part of an existing one.
2. One node for every academic hospital, so 3. Note that UMC Utrecht needs a new node despite already having one, as the existing one is for a different collaboration.
3. There is no need to create new users, as these are already registered on the organization. Note that the users are linked only to the organization, not to the nodes.

:::::::::::::::::::::::::::::::::


### Where are these concepts in the UI?

After logging in to the vantage6 UI, you will see the start page.

![vantage6 UI start page](fig/chapter3/ui_start_page.png)

There are some collaborations displayed on the start page. Clicking one of the collaborations will show the tasks of that collaboration.

![vantage6 UI tasks page](fig/chapter3/ui_task_page.png)

The start page also contains a button `Administration` in the top right corner. Clicking on this button will redirect you to the administration page.

On the administration page, you can manage the entities of vantage6. The entities are divided into tabs: `Organizations`, `Collaborations`, `Roles`, `Users`, and `Nodes`. You can click on an entity to see more details or to edit the entity. We will get back to this later in more detail.

![vantage6 UI administration page](fig/chapter3/ui_admin_page.png)

::::::::::::::::::::::::::::::::::::: challenge

## Get familiar with the vantage6 UI

Log in to the Vantage6 UI using the credentials below (the password will be given by the instructors). Once logged in, navigate to the administration page to familiarize yourself with the entities there. Then, try to update your email, first name, and last name, but do not change your username, as it will be needed for some of the follow-up challenges.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution

![User-entity - edit option](fig/chapter3/user-edit.png)

:::::::::::::::::::::::::::::::::




## From theory to practice: a hypothetical case study using vantage6 collaborations

As previously discussed, in vantage6 a collaboration refers to an agreement between two or more parties to participate in a study or to answer a research question together. This concept is central to the Privacy Enhancing Technologies (PETs) that vantage6 supports. Each party involved in a collaboration remains autonomous, meaning they retain control over their data and can decide how much of their data to contribute to the collaboration's global model and which algorithms are allowed for execution.

To illustrate this, let's analyze a hypothetical scenario: an international collaboration project of multiple health research institutes, working together on two studies:

- _Age-Related Variations in Overweight Prevalence: A Comparative Study Across Gender and Age Groups_ **(AGOT2024)** .

- _The Effect of Gender on Height Development Across Various Age Groups_  **(GGA2024)**.

The first study, **AGOT2024**, involves the analysis of age and weight-related data available on a subset of the institutions participating in the collaboration. Likewise, **GGA2024** involves the analysis of age and height-related data from a different (and potentially overlapping) subset of the collaboration's participants. The diagram below illustrates the kind of configuration you will be working with. Keep in mind that your configuration may have different node and collaboration names, an different study subsets.


![Hypothetical collaborations scenario](fig/chapter3/case-study-example.drawio.png)

### Algorithms trustworthiness in a federated setting

While a vantage6-supported research infrastructure like the one described above offers a strong defense against many data privacy risks, there remains one crucial security aspect that falls outside the platform's scope: the validation of the code that will run on this infrastructure. For instance, the administrators of the nodes running within each organization are responsible for defining which algorithms (i.e., [which container images](https://docs.vantage6.ai/en/main/node/configure.html#all-configuration-options)) will be allowed for execution on the respective collaborations. As this is a critical and complex task that entails activities like code analysis and verification, working with algorithms from trusted sources is the primary line of defense against potential threats.

Vantage6's algorithm store aims to enhance trustworthiness by offering a centralized platform for managing pre-registered algorithms. This serves as an alternative to using algorithms from unknown authors or those lacking transparency regarding their development process and status. The algorithm store currently allows researchers to explore which algorithms are available and how to run them. This, along with its integration with vantage6's UI, streamlines task execution requests within collaborations. Also, the algorithm store integrates additional information to the algorithm metadata such who developed and reviewed the algorithm. Only after complying with the review policies of a store, a new algorithmn will be published in the store.

### Running a PET (privacy-enhancing technology) analysis without programming!

In this episode, you will perform a PET analysis on an existing vantage6 collaboration (based on 'dummy' nodes) that resembles the two described above. For reference, the datasets of each organization can be seen here (TODO).

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: understanding a simple federated algorithm

First, let's take a look at one of the federated algorithms -available on the vantage6's community store- that will be used in this episode: [a federated average](https://github.com/IKNL/v6-average-py/blob/master/v6-average-py/__init__.py).

Analyze the algorithm based on the code and its comments and answer the following questions:

- How are the `central_average` and `partial_average` functions related?
- Why does the `central_average` function, unlike `partial_average`, **not** get any data as an input?
- Analyze and discuss the potential outcomes if a Task to execute `central_average` is initiated within a collaboration or study where one of the nodes is offline.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: exploring the status of the collaboration its related studies

The instructors will provide you credentials for accessing as a researcher of one of the institutions from the collaboration.

Using these credentials see which institutions were asigned to the two studies. Also check the status of the corresponding nodes. Given this and your algorithm analysis from Challenge #2 answer the following:

1. Which study is ready for creating a Task for the **federated average** algorithm?
2. If one of the studies is not ready, which organization you would need to contact in order to make it ready for executing the algorithm too?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution steps

To check the status of the nodes of each collaboration:

1. Log in to each one with the given credentials
2. Click on 'Administration' on the left panel of the UI
3. select 'Collaborations', and then select the corresponding collaboration.
4. If there are 'offline' nodes, click on the 'Nodes' panel on the left and check when these were seen for the last time.

![Collaboration status](fig/chapter3/collab-status-offline.png)

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: your first algorithm execution as a researcher

Now, you'll play the role of the researcher within the collaboration you have just examined. With this role, you will finally request the execution of the algorithm.

1. Log in with the credentials provided by the instructors.

2. Select `Analyze` on the Administration option from the panel on the left, and then select your collaboration.

3. Select `+ Create task` to create a new task on your collaboration.

   ![](fig/chapter3/create-task.png)

4. As the first step, you can choose between running the task on the entire collaboration, or on one particular study (i.e., on a subset of the collaboration's institutions). Choose the study that, according to your analysis on Challenge #3, is still NOT ready to execute a _federated average_ task.

   ![](fig/chapter3/select-study.png)

5. The 'Average' algorithm should be listed under the '_Select which algorithm you want to run_' dropdown menu. Select it, and provide a name and a description.

   ![](fig/chapter3/alg-selection.png)

6. Now the UI will let you choose between the two functions you explored in Challenge #2. For now try to run the `partial_average`, selecting ALL the organizations.

   ![](fig/chapter3/selecting-alg-and-nodes.png)

7. Select the 'default' database, choose any numerical column relevant for the study you selected, and then click on 'Submit'.

8.  The task you just requested should be listed with a 'pending' status. Once finished, explore and download the provided results.
   
Based on these results, answer the following:

1. What just happened? Did the `partial_average` function fail or not?

2. If you do the same process, this time on the study that is ready for new task, and using the `central_average` function (refer to Challenge #2 if needed), which organization or organizations should you choose this time? Experiment with this and discuss the results with the instructors.

3. What would happen if you select an alpha-numerical column (e.g., 'gender')? Do this experiment and explore the generated error logs. Discuss with the instructors how these logs can be used to diagnose any task execution issues.

::::::::::::::::::::::::::::::::::::::::::::::::