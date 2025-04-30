"""
code inside __name=="__main__ will not excute when currect file is imported in other file and function is called. but if we run currect file it will excute code inside __name=="__main__
"""

def hello():
    print("Hello from my_script!")

if __name__ == "__main__":
    print("This runs only when executed directly")
    hello()