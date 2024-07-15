import os
import json
import re

PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG = json.load(open(f"{PATH}/main_config.json", "r"))


def user_has_perm_for(user, command):
    """
    checks if a user has the Permission for the command.
    The ranks are stored in the config.json

    Args:
        user (Discord User): user to check
        command (string): command string

    Returns:
        boolean: user has permission
    """
    for _ in user.roles:
        for role in CONFIG["perm"][command]:
            if re.findall(role, _.name, re.IGNORECASE):
                return True

    return False

