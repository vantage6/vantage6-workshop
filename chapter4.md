---
title: "Managing vantage6 server via the user interface"
teaching: 2
exercises: 3
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the administrative entities in vantage6?
- What is the relation between the entities in vantage6?
- What is the permission system in vantage6?
- What are the default roles in vantage6?
- How to create a new organization using vantage6 user interface (UI)?
- How to create a new user using vantage6 UI?
- How to create a new collaboration using vantage6 UI?

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the types of administrative entities in vantage6
- Understand the relation between the administrative entities of vantage6
- Understand the permission system of vantage6
- Understand the default roles in vantage6
- Be able to create a new organization using the vantage6 UI
- Be able to create a new user using the vantage6 UI
- Be able to create a new collaboration using the vantage6 UI
- Be able to reset an api key for a node

::::::::::::::::::::::::::::::::::::::::::::::::


## Vantage6 entities and their relations

There are several entities in vantage6, such as users, organizations, tasks, etc. These entities are created by users that have sufficient permission to do so and are stored in a database that is managed by the central server.

The administrative entities in vantage6 are:

- **User**: a person who can perform certain actions in vantage6.
    - A user can only belong to one **organization**.
    - A user can have multiple **roles** and can be assigned with extra permissions not covered by the roles.
    - A user can create **tasks** for one or more **organizations** within a **collaboration**.
- **Organization**: an orgarnization to which users belong
    - An organization can have zero and more **users**.
    - An organization can have multiple **nodes**.
- **Collaboration**: a collection of one or more **organizations**.
    - In a specific **collaboration**, each participating **organization** needs one **node** to compute **tasks**; In another **collaboration**, the same **organization** must have a separate **node** for this **collaboration**.
    - A collaboration can contain zero or more **studies**.
    - A **study** is a subset of organizations from the collaboration that are involved in a specific research question. By setting up studies, it can be easier to send tasks to a subset of the organizations in a collaboration and to keep track of the results of these analyses.
- **Role**: a collection of rules that define the permissions of a user.
    - A user can have multiple roles.
    - The permissions of the user are defined by the assigned **rules**.
    - **Rules** define what each entity is allowed to do, based on the operation (view, create, edit, delete, send, receive), the scope (own,  organization, collaboration, global), and the resource (e.g. users, orgarnizations).
- **Node**: an application that can execute **tasks**.
- **Task**: a task that is executed by one or more **nodes**.
    - A task should use an algorithm run for each organization involved in the task. The results are part of such an algorithm run.
    - A task can be part of a **study** or a **collaboration**.

The following diagram is simplified relations between these entities. A `1-n` relationship means that the entity on the left side of the relationship can have multiple entities on the right side. For instance, a single organization can have multiple vantage6 users, but a single user always belongs to one organization. There is one `0-n` relationship between roles and organizations, since a role can be coupled to an organization, but it doesn’t have to be. An `n-n` relationship is a many-to-many relationship: for instance, a collaboration can contain multiple organizations, and an organization can participate in multiple collaborations.

![vantage6 relations between entities](fig/v6_entities.png)

### Where are the entities in the UI?

After logging in to the vantage6 UI, you will see the start page.

![vantage6 UI start page](fig/ui_start_page.png)

There are some collbarations displayed on the start page. Clicking one of the collaborations will show the tasks of that collaboration.

![vantage6 UI tasks page](fig/ui_task_page.png)

The start page also contains a button `Administration` in the top right corner. Clicking on this button will redirect you to the administration page.

In the administration page, you can manage the entities of vantage6. The entities are divided into tabs: `Organizations`, `Collaborations`, `Roles`, `Users`, and `Nodes`. You can click on an entity to see more details or to edit the entity. We will get back to this later in more detail.

![vantage6 UI administration page](fig/ui_admin_page.png)

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Get familiar with the vantage6 UI

Log in to the vantage6 UI and navigate to the `Administration` page. Familiarize yourself with the entities in the administration page.

Can you find the `Organizations`, `Collaborations`, `Roles`, `Users`, and `Nodes` tabs?

::::::::::::::::::::::::::::::::::::::::::::::::


## Vantage6 permission system

vantage6 uses a permission system to control who can do what in the system. The permission system is based on **roles**, which are collections of rules that define the permissions of a user. A user can have multiple roles, and the permissions of the user are defined by the assigned **rules**.

The permission rules define what each entity is allowed to do, based on the operation (view, create, edit, delete, send, receive), the scope (own,  organization, collaboration, global), and the resource (e.g. users, orgarnizations). Users can be assigned anywhere between zero and all of these permission rules. For example, having the rules with `create` in the scope `organization` for the resource `users` means that the user can create users for the organization they belong to.

To make it easier to assign permissions, there are also predefined roles:

- Root: has all permissions (👉 see image below)
- Collaboration Admin: can do almost everything for all organizations in collaborations they are a member of
- Organization Admin: can do everything for their own organization
- Researcher: can view the organization's resources and create tasks (👉 see image below)
- Viewer: can only view the organization's resources

The permissions are set up in the `Roles` tab in the administration page. You can click on a role to see the permissions of that role. You can also create a new role by clicking the `Create role` button.

The permission structure allows for a lot of flexibility, but it can be complex for beginners to set up. The default roles provide a quick way to set up permissions, but it is recommended to review them before using them in a project.

![vantage6 permissions for the role Root](fig/permissions_root.png)

![vantage6 permissions for the role Researcher](fig/permissions_researcher.png)

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: What can you do in vantage6?

Go the administration page in the vantage6 UI, check the permissions that you have, and answer the following questions:

1. What is your role in vantage6?
2. Do you have the permissions to create a new organization, a new user or a new collaboration?
3. Do you have the permission to remove an existing organization, a user, or a collboration?

:::::::::::::::::::::::: solution

## Output

1. Check it with your instructor.
2. Yes, you should be able to create a new organization, a new user, and a new collaboration. If not, ask your instructor to give you the necessary permissions.
3. Check it with your instructor.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::


## Manage vantage6 project using the UI

::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

Before starting this section, make sure that the participants have enough permissions to create a new organization, a new user, and a new collaboration. If not, give them the necessary permissions.
Note that the role `Collaboration Admin` does not have the permission to create a new organization.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In this section, we will go through the steps to create a new organization, a new user, a new collaboration and reset an api key for a node using the vantage6 UI.

First you need to log in to the vantage6 UI, and then go to the `Administration` page. You can find the `Administration` button in the top right corner of the start page.

![vantage6 UI administration page](fig/ui_admin_page.png)

### Create a new organization
It's quite straightforward to create a new organization in vantage6. Here are the steps:

1. Click on the `Organizations` tab in the administration page.
2. Click on the `Create organization` button.
3. Fill in the details of the new organization.
    * The `Upload public key` field is optional. You can upload a public key for the organization if you want to use encryption in the collaboration.
4. Click on the `Submit` button to create the new organization.

![Create a new organization](fig/create_org.png)

### Create a new user
Now let's create a new user for the organization we just created. Here are the steps:

1. Click on the `Users` tab in the administration page.
2. Click on the `Create user` button.
3. Fill in the details of the new user.
    * You can assign the user to an organization by selecting it from the `Organization` dropdown. Only one organization can be selected.
    * You can assign roles to the user by selecting them from the `Roles` dropdown. Here we assign the `Researcher` role to the new user. You can give the user more permissions by assigning multiple roles or select the operation boxes in the `Permissions` section.
4. Click on the `Submit` button to create the new user.

![Create a new user](fig/create_user.png)

### Create a new collaboration
A collaboration is a collection of one or more organizations. Let's create a new collaboration between two organizations. Here are the steps:

1. Click on the `Collaborations` tab in the administration page.
2. Click on the `Create collaboration` button.
3. Fill in the details of the new collaboration.
    * For `Encrypted` box, you can select whether the collaboration should be encrypted or not.
    * You can select the organizations that will participate in the collaboration by selecting them from the `Organizations` dropdown.
    * By default, we select the `Register nodes` box. This will ensure the nodes of the organizations are registered in the collaboration. If you don't select this box, you will have to register the nodes manually later.

![Create a new collaboration](fig/create_collab_01.png)

4. Click on the `Submit` button to create the new collaboration.
    * After submitting the form, you may see a dialog box to ask you to download the API key (on MacOS) or a dialog points out that the API key has been downloaded (on Windows). The API key is used to authenticate the nodes in the collaboration. Later we will see how to reset the API key for a node.

![Download API keys](fig/create_collab_02.png)

You will see a message:

> API key download
>
> The API keys have been downloaded.
>
> Please distribute each of these keys privately to each of the organizations. Note that they may reset their API key so that no-one but them knows it.

5. After creating the collaboration, you can see the details of the collaboration by clicking on the specific collaboration listed in the `Collaborations` tab.
    * You will see what organizations are participating in the collaboration.
    * You will see the nodes of the organizations that are registered in the collaboration. If no nodes are registered, you can register them manually by clicking the `Register missing nodes` button.
    * You can also see the algorithm store available for the collaboration. You can add a algorithm store for the collaboration by clicking the `Add algorithm store` button.
    * You can also see the studies of the collaboration. You can add a study by clicking the `Add study` button.

![Collaboration details](fig/create_collab_03.png)

### Reset API key for a node
If you want to reset the API key for a node, you can do so by following these steps:

1. Click on the `Nodes` tab in the administration page.
2. Click on the tab of the node you want to reset the API key for in the list of nodes.

![Reset API key for a node](fig/reset_api_key_01.png)

3. Click on the `Reset API key` button.
    * You will see a dialog box to ask you to download the new API key.

![Download new API key](fig/reset_api_key_02.png)

You will see a message:

> API key download
>
> Your API key has been reset. Please read your new key in the file that has been downloaded.

At this point, put the new API key in your node configuration file and restart the node to connect to the server again.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 3: Manage vantage6 project using the UI

Go the administration page in the vantage6 UI and try to create a new organization, a new user, and a new collaboration. Also, try to reset the API key for a node.

1. Can you create a new organization, a new user, and a new collaboration?
2. Can you reset the API key for a node?
3. Which steps are challenging for you?

::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::: keypoints

- Vantage6 entities are `Users`, `Organizations`, `Collaborations`, `Roles`, `Nodes`, and `Tasks`.
- Vantage6 uses a permission system to control who can do what in the system.
- Vantage6 has default roles like  `Root`, `Collaboration Admin`, `Organization Admin`, `Researcher`, and `Viewer`.
- Vantage6 UI can be used to manage the entities of vantage6, like creating a new organization, a new user, a new collaboration, and resetting an api key for a node.

::::::::::::::::::::::::::::::::::::::::::::::::