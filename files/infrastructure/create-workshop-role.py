url = "https://server.workshop.vantage6.ai"
port = 443
api_path = "/api"

# When running this, create a file config.py with the following content:
from config import username, password

from vantage6.client import Client

client = Client(url, port, api_path, log_level="debug")

client.authenticate(username, password)
client.setup_encryption(None)

# get collab admin role's rules
rules = client.rule.list(role=7, field="id", per_page=9999)
rules = [r["id"] for r in rules]

# add rules for viewing everything globally
view_rules = client.rule.list(operation="v", scope="glo", field="id")
for rule in view_rules:
    rules.append(rule["id"])

# add rules to create orgs and collabs
create_org_rule = client.rule.list(
    operation="c", scope="glo", name="organization", field="id"
)[0]
rules.append(create_org_rule["id"])
create_collab_rule = client.rule.list(
    operation="c", scope="glo", name="collaboration", field="id"
)[0]
rules.append(create_collab_rule["id"])

# discard doubles
rules = list(set(rules))

# create the role
client.role.create(
    name="workshop-user-admin",
    description="Role for workshop participants to practise administration",
    rules=rules,
)
