class FieldElement :
    def __init__(self, num,prime):
        if num >= prime or num < 0:
            error = 'Num {} not in Field range 0 to {}'.format(num , prime -1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime,self.num)

    def __eq__(self,other):
        if other is None :
            return False
        return self.num == other.num and self.prime == other.prime


    def __ne__(self,other):
        if other is None :
            return False
        return self.num != other.num or self.prime != other.prime


    def __add__(self,other):
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different fields")
        num = (self.num + other.num)%self.prime
        return self.__class__(num,self.prime) # Note that we could use FieldElement instead of self.__class__, but this would not make the method easily inheritable.
        # We will be subclassing FieldElement later, so making the method inheritable is important here.
