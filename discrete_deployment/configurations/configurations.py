from discrete_deployment.configurations.config_classes import ConfigClasses


class Configuration:
    def __init__(self):
        self.path = ""
        self.name = ""
        self.config_class: ConfigClasses = ConfigClasses.CONFIG
        self.inherits = ""
        self.command = ""
        self.arguments = []

    def __str__(self):
        return self.name

    def get_key(self):
        return "%s:%s" % (self.config_class.value, self.name)


class LazyConfiguration(Configuration):
    @classmethod
    def from_dict(cls, path: str, config_class: ConfigClasses, dict_values: {}):
        self = cls()
        self.path = path
        self.config_class = config_class
        self.name = dict_values["name"]
        return self
