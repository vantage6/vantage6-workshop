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

The following diagram illustrates what a collaboration between two organizations would look like. In this scenario, users from both organizations -with the right roles- would be able to request the execution of multiple **tasks** on `Collaboration A`, based on one of the **algorithms** registered on a given **algorithm store**.

![](fig/chapter3/v6-task-and-user-concepts-illustrated.drawio.png)


The following diagram expand the previous scenario further: what if `Organization 1` needs to participate on an additional **collaboration** with another **organization** (e.g., `Organization 2`)? In this case, `Organization 1` will have two running nodes, one for each collaboration. Moreover, as also depicted on the diagram below, each **collaboration** can make use of one or more **algorithm stores**:

![](fig/chapter3/v6-core-concepts-illustrated.drawio.png)


Finally, the concept of **study** is an important one to be considered when using vantage6 for data analysis. A **study** is a subset of organizations from a given collaboration that are involved in a specific research question. By setting up studies, it can be easier to send tasks to a subset of the organizations in a collaboration and to keep track of the results of these analyses. For example, in the `Collaboration W` below there are six organizations involved. It may happen that in this particular collaboration there are two different research questions. One involves data from organizations 1, 2, 3 and 4; wheras the other is based on data from organizations 4, 5 and 6. Upon setting up the studies `Study Alpha` and `Study Beta`, as a resarcher you can choose three different targets for your data analysis tasks: the whole `Collaboration W` organization (hence, on nodes `A` to `F`), the `Study Alpha` (nodes `A` to `D`) or the `Study Beta` (nodes `D` to `F`).

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

|  User     |  Roles        |
|-----------|---------------|
|PhY24-rs1  | Researcher    |


::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution

![User-entity - edit option](fig/chapter3/user-edit.png)

:::::::::::::::::::::::::::::::::




## From theory to practice: a hypothetical case study using vantage6 collaborations


gender	age	height	weight	isOverweight	ageGroup





As previously discussed, in vantage6 a collaboration refers to an agreement between two or more parties to participate in a study or to answer a research question together. This concept is central to the Privacy Enhancing Technologies (PETs) that vantage6 supports. Each party involved in a collaboration remains autonomous, meaning they retain control over their data and can decide how much of their data to contribute to the collaboration's global model and which algorithms are allowed for execution.

To illustrate this, let's analyze a hypothetical scenario: an international collaboration project of multiple health research institutes, working together on two studies:

- _Age-Related Variations in Overweight Prevalence: A Comparative Study Across Gender and Age Groups_ **(AGOT2024)** .

- _The Effect of Gender on Height Development Across Various Age Groups_  **(GGA2024)**.

The first study, **AGOT2024**, involves the analysis of age and weight-related data available on a subset of the institutions participating on the collaboration. Likewise, **GGA2024** involves the analysis of age and height related data from a different (and potentially overlapping) subset of the collaboration's participants. The diagram below illustrates the kind of configuration you will be working with. Keep in mind that your configuration may have different node and collaboration names, an different study subsets.


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
- Analyze and discuss the potential outcomes if a Task to execute `central_average` is initiated within a collaboration where one of the nodes is offline.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: exploring the status of the collaboration and the studies configured on a vantage6 server

The instructors will provide you credentials for accessing as a researcher of one of the institutions from the collaboration.

Using these credentials see which institutions were asigned to the two studies. Also check the status of the corresponding nodes. Given this and your algorithm analysis from Challenge #2 answer the following:

1. Which study is ready for creating a Task for the **federated average** algorithm?
2. If one of the studies is not ready, which organization you would need to contact in order to make it ready for executing the algorithm too?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution steps

To check the status of the nodes of each collaboration:

1. Log in to each one with the given credentials
2. Click on 'Administration' on the top of the UI
3. select 'Collaborations' on the left panel, and then select the corresponding collaboration.
4. If there are 'offline' nodes, click on the 'Nodes' panel on the left and check when these were seen for the last time.

![Collaboration status](fig/chapter3/collab-status-offline.png)

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 4: adding an algorithm store to an organization

In order to execute the **average algorithm** on a given collaboration, considering the previous discussion on algorithm trustwortiness, you need to first register an algorithm store on it first. Use the credentials given for Challenge #4 to register the 'community store', which contains the said algorithm: `https://store.cotopaxi.vantage6.ai`

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Solution steps

You will now link the 'community-store' to the collaboration whose nodes are ready for it.

1. Login into the organization using the corresponding credentials from above.
2. Click on 'Administration' on the top of the UI, select 'Collaborations' on the left panel, and then select the corresponding collaboration.
3. Click on '+ Add algorithm store'
4. Add the vantage6's community store. Use any descrption as name, and provide community store URL: `https://store.cotopaxi.vantage6.ai`
5. Make sure the store is now shown on the collaboration details:
   ![Community store entry on the collaboration details](fig/chapter3/community-store-entry.png)

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 5: your first algorithm execution as a researcher

Now, you'll take on the role of the researcher within the collaboration for which you've just established the algorithm store. With this role, you will finally request the execution of the algorithm.

1. log in as a researcher using the corresponding credentials below:

   | User      | Roles      | Collaboration |
   | --------- | ---------- | ------------- |
   | PhY24-rs1 | Researcher | PhY24         |
   | GHT-rs1   | Researcher | GHT           |

2. Select the collaboration given on the front page, and select 'Tasks' from the panel on the left.
   ![Collaboration researcher view](fig/chapter3/collab-researcher-view.png)

3. If you have set up everything correctly, the 'Average' algorithm should be now listed under the '_Select which algorithm you want to run_' dropdown menu. Select it, and provide a name and a description.

   ![Algorithm selection](fig/chapter3/task-alg-selection.png)

4. Now the UI will let you choose between the two functions you explored in Challenge #1. First, try to run the `partial_average` on all the nodes individually.

   ![Running a function on all nodes](fig/chapter3/task-partial-on-individial-orgs.png)

5. Select the 'default' database, choose any numerical column as a parameter, and then click on 'Submit'.

6. The task you just requested should be listed with a 'pending' status. Once finished, explore and download the provided results:
   ![alt text](fig/chapter3/task-results.png)

Based on these results, answer the following:

1. If you repeat the same exercise but with the `central_average` function (refer to Challenge #2 if needed), which organization nodes should you choose this time to actually calculate the overall (across all the datasets) average? Experiment with this and discuss the results with the instructors.

2. What would happen if you select an alpha-numerical column (e.g., 'participant_pseudo_id')? Do this experiment and explore the generated error logs. Discuss with the instructors how these logs can be used to diagnose any task execution issues.

::::::::::::::::::::::::::::::::::::::::::::::::
