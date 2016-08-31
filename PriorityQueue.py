# priority queue implementation with binary tree

class priorityQueue:
    
    def __init__(self):
        self.tree = []
    def insert(self,val):
        if len(self.tree) == 0:
            self.tree.append(val)
        else:
            self.tree.append(None)
            i = -2
            while i >= -len(self.tree):
               if self.tree[i]>= val:
                   self.tree[i+1] = val
                   break
               else:
                  temp = self.tree[i]
                  self.tree[i] = val
                  self.tree[i+1] = temp

               i -= 1
    
    def  getMax(self):
        return self.tree[0]
    
    def  extractMax(self):
        
        if len(self.tree) == 1:
            temp = self.tree[0]
            self.tree = []
            return temp
        elif len(self.tree) == 0:
            return 
        else:       
            tempMin = self.tree[-1]
            tempMax = self.tree[0]
            self.tree[0] = tempMin        
            del self.tree[-1]
            i = 0
            while i< len(self.tree)-2:
                if self.tree[i+1] >= self.tree[i+2]:
                    self.tree[i] = self.tree[i+1]
                    self.tree[i+1] = tempMin
                    i = i+1
                else:
                    self.tree[i] = self.tree[i+2]
                    self.tree[i+2] = tempMin
                    i = i+2
            return tempMax
    
    def changePriority(self,pos,newVal):
        self.tree[pos] = newVal
        i = pos
        if self.tree[(i+1)/2-1] <= newVal:
            while (i+1)/2-1 >= 0:
                if self.tree[(i+1)/2-1] <= newVal:
                    tempMax = newVal
                    tempMin = self.tree[(i+1)/2 - 1]
                    self.tree[(i+1)/2-1] = tempMax
                    self.tree[i] = tempMin
                i = (i+1)/2-1
                if i == 0:
                    break
                print self.tree
        
            
        elif self.tree[i*2+1] > newVal:
            while i*2+1 < len(self.tree):
                if self.tree[i*2+1] > newVal:
                    tempMax = self.tree[i*2+1]
                    tempMin = newVal
                    self.tree[i*2+1] = tempMin
                    self.tree[i] = tempMax
                i = i*2+1
                if i  == len(self.tree)-1:
                    break
                #print self.tree
        
    def remove(self,pos):
        temp = self.tree[pos] 
        temp2 = self.tree[-1]
        
        self.tree[pos] = temp2
        del self.tree[-1]
        
        i = pos 
        newVal = temp2
        while i*2+1 < len(self.tree):
            if self.tree[i*2+1] > newVal:
                tempMax = self.tree[i*2+1]
                tempMin = newVal
                self.tree[i*2+1] = tempMin
                self.tree[i] = tempMax
                i = i*2+1
                if i  == len(self.tree)-1:
                    break            
        

test = priorityQueue()
test.insert(5)
test.insert(6)
test.insert(3)
test.insert(10)
test.insert(2)
test.insert(13)
print test.tree
print test.getMax()
print test.extractMax()
print test.tree
test.changePriority(2,14)
print test.tree

test.changePriority(1,1)
print test.tree
test.remove(2)
print test.tree