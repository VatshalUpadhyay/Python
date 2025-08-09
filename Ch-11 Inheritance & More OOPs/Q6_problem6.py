class Vector:
    def __init__(self,l):
        self.l=l # here i o;y take l becz i take list here which is only one

    def __len__(self):
        return len(self.l)

v1=Vector([1,2,3]) # here i make list so if i dont konw ki kitne dimension h vo batayega yaha to pta h ki 3 h(1,2,3)
print(f"The length of v1 is:{len(v1)}")