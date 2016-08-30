# Priority Queue Naive Implementation

class priorityQueue:
    
    def __init__(self):
        self.bag = []
        
    def insert(self,val):
        self.bag.append(val)
    
    def extractMax(self):
        result = max(self.bag)
        self.bag.remove(result)
        return result
    
    def getMax(self):
        return max(self.bag)
    

test = priorityQueue()
test.insert(5)
test.insert(8)
test.insert(13)
test.insert(32)
test.insert(1)
print test.extractMax()
print test.extractMax()