
walk = ['n','e','s','w']
def is_valid_walk(walk):
       for i in range(0,11):
            if len(walk)==10 and walk[0]!= walk[-1] and walk[i] != walk[i+1]:
                return True
            else : 
                return False
       
print(is_valid_walk(walk))   
              



