acl_template = [
    "ip access-list extended TestACL",
    "permit ip ${SRC_NET} ${SRC_WILDCARD} host 8.14.5.1",
    "deny ip any any log"
]

object = {
    "SRC_NET": "1.1.1.1",
    "SRC_WILDCARD": "0.0.0.255"
}

def generate_acl(template, objects):
    acl = []
    for line in template:
        for key, value in objects.items():
            line = line.replace(f"${{{key}}}", value)
        acl.append(line)
    return acl

generated_acl = generate_acl(acl_template, object)

with open(f"acl.txt", "w") as file:
    file.write("\n".join(generated_acl))