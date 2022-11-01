class CustomStack:
    
    def __init__ (self, maxSize):
        self.maxSize = maxSize
        self.list = []
        

    def push(self, x):
        if len(self.list) < self.maxSize:
            self.list.append(x)
        else:
            print('the stack is full')
        

    def pop(self):
        if self.list:
            return self.list.pop()
        else:
            return -1
        

    def increment(self, k, val):
        rang = min(k,len(self.list))
        for i in range (rang):
            self.list[i] += val
            
    
            
            


def main():
    stack = CustomStack(4)
    print(stack.list)
    stack.push(1)
    print(stack.list)
    stack.push(2)
    print(stack.list)
    stack.push(3)
    print(stack.list)
    stack.push(4)
    print(stack.list)
    stack.push(5)
    print(stack.list)
    stack.pop()
    print(stack.list)
    stack.increment(2, 5)
    print(stack.list)
    

    
    

        

if __name__ == "__main__":
    main()