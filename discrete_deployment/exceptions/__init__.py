class NotInitialisedException(BaseException):
    def __init__(self):
        self.message = 'Config not initialised.'
        super(NotInitialisedException, self).__init__(self.message)


class ConfigurationAlreadyExistsException(BaseException):
    def __init__(self, config_name=''):
        self.message = 'Configuration "%s" already exists.' % config_name
        super(ConfigurationAlreadyExistsException, self).__init__(self.message)


__all__ = [
    NotInitialisedException,
    ConfigurationAlreadyExistsException,
]
