class NotInitialisedException(BaseException):
    def __init__(self, message='Config not initialised.'):
        self.message = message
        super(NotInitialisedException, self).__init__(message)
