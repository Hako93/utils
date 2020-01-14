from datetime import datetime
 
__all__ = ['proclamer']
 
 
def proclamer():
    print ("Sam et Max, c'est bien",datetime.now())
 
 
if __name__ == "__main__":
    proclamer()
