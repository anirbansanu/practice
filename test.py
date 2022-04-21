operations = {
    "(":None,
    "^": lambda a,b: a**b,
    "/": lambda a,b: a/b,
    "*": lambda a,b: a*b,
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b
}
 
class PostFix():
    def __init__(self,exp:'str') -> None:
        self.stack =[]
        self.exp = exp
        self.p_exp = [] 
        self.exe(self.exp)
        self.postfix = "".join(self.p_exp)

    #Operators Precedence
    def op_prd(self,op:'str'):
        d = {"(":1,"^":2,"/":3,"*":4,"+":5,"-":6}
        if op in d.keys():
            return d[op]
        return None

    def stack_append_handler(self,item,prd):
        if len(self.stack)==0:
            self.stack.append(item)
            return self.stack
        prv_prd = self.op_prd(self.stack[-1])
        if prv_prd < prd:
            temp= self.stack.pop()
            self.stack.append(item)
            self.p_exp.append(temp)
        else:
            self.stack.append(item)
        return self.stack

    def exe(self,exp):
        i=0
        while i < len(self.exp):
            prd = self.op_prd(exp[i])
            if prd:
                self.stack_append_handler(exp[i],prd)
            else:
                self.p_exp.append(exp[i])
            i+=1
        if 0 < len(self.stack):
            self.p_exp = self.p_exp + self.stack[::-1]

    def eval(self):
        stack = []
        i=0
        while i < len(self.postfix):
            if self.op_prd(self.postfix[i]) == None:
                stack.append(self.postfix[i])
            else:
                try:
                    _2nd = int(stack.pop())
                    _1st = int(stack.pop())
                    result = operations[self.postfix[i]](_1st,_2nd)
                    stack.append(result)
                except:
                    print('Error : Operand Should be int')
                    return None
            i+=1
        return result


if __name__ == '__main__':
    p = PostFix("2+6/2*5")
    print(p.postfix)
    print(p.eval())