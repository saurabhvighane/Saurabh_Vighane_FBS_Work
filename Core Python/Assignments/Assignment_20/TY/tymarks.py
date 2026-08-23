class TYMARKS:
    def __init__(self,theory,practical):
        self.theory=theory
        self.practical=practical

    def __str__(self):
        return (f'\ntheory:{self.theory}\t'
                f'Practical:{self.practical}')