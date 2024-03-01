import os, sys

def app_path(self):    
    # print(sys.path[0])
    # print(os.getcwd())
    # print(os.path.realpath(__file__))
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(__file__))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # print(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))    
    print(os.path.dirname(os.path.realpath(sys.argv[0])))
    return os.path.dirname(os.path.realpath(sys.argv[0]))