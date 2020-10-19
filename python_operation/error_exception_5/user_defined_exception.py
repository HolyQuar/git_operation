if __name__=='__main__':
    """
    When creating a module that can raise several distinct errors, 
    a common practice is to create a base class for exceptions defined by that module, 
    and subclass that to create specific exception classes_6 for different error conditions.
    """
    class Error(Exception):
        """Base class for exceptions in this module."""
        pass
    class InputError(Error):
        """Eception raised for errors in the input.

        Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
        """
        def __int__(self,expression, message):
            self.expression = expression
            self.message = message

    class TransitionError(Error):
        """Raised when an operation attemps a state transition that's not
        allowed.

        Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
        """
        def __init__(self,previous, next, message):
            self.previous = previous
            self.next = next
            self.message = message