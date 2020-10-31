from discrete_deployment.configurations.config_types import ConfigTypes


class Configuration:

    def __init__(self):
        self.name = ''
        self.config_type: ConfigTypes = ConfigTypes.CONFIG
        self.inherits = ''
        self.command = ''
        self.arguments = []

    def __str__(self):
        return self.name


class LazyConfiguration(Configuration):

    @classmethod
    def from_dict(cls, config_type: ConfigTypes, dict_values: {}):
        self = cls()
        self.config_type = config_type
        self.name = dict_values['name']
        return self
