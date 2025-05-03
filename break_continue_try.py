
a=0
b=2
while a<4:
    print("----------------------------")
    a+=1
    b-=1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0},{1} - division by zero".format(a,b))
        """continue will excute rest of the code without terminating program even if zerodivisionerro occure"""
        # continue
        
        """break will not excute rest of the code if zerodivisionerro occure"""
        break
    
    finally:
        print("{0},{1}- allways excute".format(a,b))
    
    print("{0},{1} - main loop".format(a,b))

