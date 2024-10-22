
class LCG:
    def __init__(self,seed,mul,inc,mod):
     self.cur=seed
     self.mul=mul
     self.inc=inc
     self.mod=mod

    def next(self):
        self.cur=(self.mul*self.cur+self.inc)%self.mod
        return self.cur



seed=27
mul=17
inc=43
mod=100
lcg = LCG(seed,mul,inc,mod)
random_nums=[lcg.next()for _ in range(10)]
print("Generated sequence of random numbers:")
print(random_nums)
