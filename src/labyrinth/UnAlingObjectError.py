
class UnAlingObjectError(RuntimeError):
    """
    Represents when a object shoul be parallel 
    or aling with an axis and is not. 
    """

    def __init__(self, messeage):
        super().__init__(messeage)