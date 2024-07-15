import os
import json
import logging
from pathlib import Path

from typing import Dict


class ConfigManager:
    def __init__(self, storage_path: Path) -> None:
        self.storage_path = storage_path
        self._configs = {}
        number = 0
        for _, file in enumerate(os.listdir(storage_path)):
            with open(f"{storage_path}/{file}", encoding="utf-8") as _file:
                self._configs |= {
                    file.rstrip(".json"): json.loads(_file.read())
                }
            number += 1
        logging.info(f"Loaded: {number} configs")

    def get_config_from(self, guild_id: int) -> Dict:
        config = self._configs.get(guild_id, None)
        if config is None:
            logging.critical(
                "Tried to load config from unkown guildID %i", guild_id)
        return config

    def store_config(self, guild_id: int, config: Dict) -> bool:
        with open(f"{self.storage_path}/{guild_id}.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(config, indent=4))

        return os.path.exists(f"{self.storage_path}/{guild_id}.json")

    def shutdown(self):
        for guild_id in self._configs:
            self.store_config(guild_id, self.get_config_from(guild_id))
