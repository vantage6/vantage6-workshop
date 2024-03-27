## Target Audience
### Newbies
Want to run basic federated data analyses
#### Prerequisites
- Know how to do data analysis in a centralized setting

### Data scientist
Knows what the newbie knows. Want more control over their analyses. Potentially develop their own
federated algorithms.

#### Prerequisites
- Basic (!) python knowledge
- Experience with command line
- Knows how to do federated analysis using the vantage6 UI

### Sys admin (not targeted)
People who install vantage6. We are probably not going to cover this topic.

#### Prerequisites
- Lots of prerequisites

## Objectives (we need max. 8)
### Newbie objectives
1. Understand the basic concepts of PET
   - Understand PET, FL, MPC, homomorphic encryption, differential privacy
   - Understand how different PET techniques relate
   - Understand scenarios where PET could be applied
   - Understand horizontal vs vertical partitioning
   - Decompose a simple analysis in a federated way 
   - Understand that there is paperwork to be done (DPIA etc.)
2. Understanding v6
   - List the high-level infrastructure components of v6 (server, client, node)
   - Understand the added value of v6
   - Understand that there is different actors in algorithms
   - Understand that the v6 server does not run algorithms
   - Explain how a simple analysis runs on v6
   - Understand the future of vantage6 (policies, etc.)
3. Running PET analysis without programming
   - Find available algorithms in community store
   - Know an algorithm store can be created for their project
   - Run an algorithm in an existing collaboration
   - View partial results in UI
   - Understand privacy limit set by collaboration
4. Be able to manage v6 projects with the UI
   - Understand the relation between the administrative entities of v6 (e.g. users, orgs, collaborations)
   - Understand the permission system of v6
   - be able to manage a collaboration using the UI
        - Be able to register a new organization
        - Ad a user to the new organization
        - Reset an api key
   

### Data scientist objectives
Preparation (might require setup session):
- Install v6 packages
- Install docker

1. Run PET analysis using the python client
   - Log in to v6
   - Find available algorithms in community store
   - Look up your collaboration, organization, nodes
   - Run an algorithm in an existing collaboration
   - View results of a (sub)task
2. Make your data available to a v6 network
   - Understand [IT requirements](https://docs.vantage6.ai/en/main/node/requirements.html) to share data with v6 (python, docker, )
   - Know the basic commands of the v6 cli
   - Configure a new node using the wizard
   - Start and observe the logs
3. Creating basic algorithms
   - Understand the available algorithm tools
   - Create a new personalized boilerplate using the v6 cli
   - Adapt the boilerplate into a simple algorithm
   - Test your algorithm using the mock client
   - Build your algorithm into a docker image
   - Set up a local test environment using the v6 cli (`v6 dev`)
   - Publish your algorithm in the algorithm store
   - Run your algorithm in the UI
4. Understanding advanced future features
   - Understand how to integrate external libraries into v6
   - Know about build service
5. Working on your own v6 projects
   - Know some examples/starting points

### Rejected objectives
- setting up v6 infrastructure (very difficult, requires different prerequisites)
- how to do the paperwork

