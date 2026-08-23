class SYMARKS:
    def __init__(self,computer_total,maths_total,Electronics_total):
        self.computer_total=computer_total
        self.maths_total=maths_total
        self.Electronics_total=Electronics_total

    def __str__(self):
        return  (f'computer total:{self.computer_total}\t'
                f'maths total:{self.maths_total}\t'
                f'electronics total:{self.Electronics_total}\n')