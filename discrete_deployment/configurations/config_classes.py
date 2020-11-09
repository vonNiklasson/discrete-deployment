from enum import Enum
from typing import List


class ConfigClasses(Enum):
    DEPLOY = "deploy"
    TEST = "test"
    DO = "do"
    CONFIG = "config"

    @staticmethod
    def from_str(label: str):
        """
        @rtype: ConfigClasses
        """
        return ConfigClasses(label)

    @staticmethod
    def values() -> List[str]:
        return [config_class.value for config_class in ConfigClasses]
