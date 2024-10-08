## Creating resources for the workshop

### Goal of the scripts in this directory

The scripts in this directory add resources such as users, organizations, nodes, and
collaborations for the workshop to the vantage6 server. Also, node configuration files
are created, together with the necessary database files.

What these scripts do not do, is deployment of the workshop vantage6 server and the
nodes. The server was manually deployed on an Azure App Service, and the nodes were
deployed on Azure Virtual Machines.

### Script to create resources

1. Make sure that the server is deployed before running the scripts and that you have a
   user account with root permissions.
1. Clone this repo and go to the directory where this README is located.
1. Activate your python env where the vantage6-client is installed (v4.6+)
1. **Modify the participants.csv in the `workshop_resources` directory**. You should update the
   workshop participants list to include the names of the participants of the workshop.
   _Do not commit this_ for privacy reasons.
   The other resources do not need to be modified - but you can if you e.g. prefer
   other names for organizations and collaborations. At present, the scripts work
   for **up to 35 participants**. If you have more participants, you will need to
   modify the scripts to include more participants (probably only add more resources
   to the `workshop_resources` directory but this has not been tested).
1. Create a file `config.py` with the following content

   ```
   username = "my-username"
   password = "my-password"
   ```

1. Run the cells in `create-resources.ipynb` to create the resources on the server. This
   notebook will create the resources for the workshop participants, and also create
   the node configuration files and attach the data files to them.
1. Deploy the nodes on the VMs. The node configuration files are created in the `output`
   directory.

### What the script creates

For exercises to create tasks:

- One user per participant
  - username is `jdoe` if participant is called John Doe
  - password is always `Password123!`
- One organizations per participant
- One collaboration per 5 participants, composed of the 5 organizations that the
  participants belong to
- A node for each of the organizations
- Each collaboration also contains an extra dummy organization where this organization has
  no node deployed. This node _is_ registered but no config file is created.
- A study is created for each collaboration that excludes the dummy organization
- A node configuration file for each of the nodes, with two datafiles attached to it:
  one with data based on the SEER data, and one with random test data (both in CSV format).

For exercises to manage resources:

- One user per participant
  - username is `jdoe_admin` if participant is called John Doe
  - password is always `Password123!`
- Three organizations per participant, one of them they are member of
- Two collaborations, both containing the organization of the partipipant and one of
  the two other dummy organizations

### Cleanup

Run the `workshop-delete-resources` script to delete everything that was created.

### Node Management

Where and how the node and server are deployed is not part of this public documentation.
To manage the nodes, login to the VM where they are deployed and use the following
commands to manage them:

```bash
source .bashrc
conda activate vantage6

# start all nodes
node_names=$(v6 node list | sed '1,3d' | sed '$ d' | awk '{print $1}')
for node_name in $node_names; do
  v6 node start -n $node_name;
done

# stop all nodes
v6 node stop --all
```

Ensure that the node config files and data files are in the appropriate directory:

```bash
# copy data files to VM
username=X
ip=W.X.Y.Z
scp infrastructure/data_files/* ${username}@${ip}:/data

# After creating node config files
scp infrastructure/output/node_configs/* ${username}@${ip}:~/.config/vantage6/node
```

### Just before workshop

- Reallocate the node VM
- Scale the node VM
- Start the nodes
