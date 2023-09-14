class DuplicateUserException(Exception):
    def __init__(self, message="User with given credentials already exists"):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self, message="User with given credentials not found"):
        self.message = message
        super().__init__(self.message)


class InvalidUserCredentialsException(Exception):
    def __init__(self, message="User with given credentials are incorrect"):
        self.message = message
        super().__init__(self.message)
