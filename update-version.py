import yaml
import argparse

parser = argparse.ArgumentParser("version modifier")
parser.add_argument("filename", help="the filename to be modified as yaml", type=str)
parser.add_argument("key", help="key to modify", type=str)
parser.add_argument("value", help="value to modify", type=str)
args = parser.parse_args()

def updateYML(filename,key,value):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
        print("before ")
        print(data)
        data[key] = value
    with open(filename, 'w') as file:
        yaml.dump(data,file,sort_keys=False)
        print ("after ")
        print(data)
    print('done!') 
    
updateYML(args.filename,args.key,args.value)