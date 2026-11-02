# Vendored from molecule-docker 2.1.0
# (molecule_docker/playbooks/filter_plugins/get_docker_networks.py, verbatim
# except this header).
# Reason: the bundled destroy.yml lives next to that filter_plugins dir, so
# Ansible auto-loads the molecule_get_docker_networks filter for bundled
# playbook runs. This scenario-local destroy.yml override does NOT inherit
# that adjacent dir, and molecule sets no filter_plugins path of its own, so
# without this copy the "Delete docker networks(s)" loop fails with
# "No filter named 'molecule_get_docker_networks'". Remove this file together
# with the scenario-local destroy.yml override when upstream fixes the
# string conditional that forced the override.
"""Embedded ansible filter used by Molecule Docker driver create playbook."""


def get_docker_networks(data, labels={}):
    """Get list of docker networks."""
    network_list = []
    network_names = []
    for platform in data:
        if "docker_networks" in platform:
            for docker_network in platform["docker_networks"]:
                if "labels" not in docker_network:
                    docker_network["labels"] = {}
                for key in labels:
                    docker_network["labels"][key] = labels[key]

                if "name" in docker_network:
                    network_list.append(docker_network)
                    network_names.append(docker_network["name"])

        # If a network name is defined for a platform but is not defined in
        # docker_networks, add it to the network list.
        if "networks" in platform:
            for network in platform["networks"]:
                if "name" in network:
                    name = network["name"]
                    if name not in network_names:
                        network_list.append({"name": name, "labels": labels})
    return network_list


class FilterModule(object):
    """Core Molecule filter plugins."""

    def filters(self):
        return {
            "molecule_get_docker_networks": get_docker_networks,
        }
