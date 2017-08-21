"""
This script calls "GET /network-device" API and print out
an easy to read list with device host name,device ip and device type
All simplify REST request functions and get authentication token function are in apicem.py
Controller ip, username and password are defined in apicem_config.py
"""
from  apicem import *

device = []
try:
    # The request and response of "GET /network-device" API
    resp = get(api="PUT API CALL FOR NETWORK DEVICE HERE")
    status = resp.status_code
    # Get the json-encoded content from response
    response_json = resp.json()
    # All network-device detail is in "response"
    device = response_json["response"]

    # Try un-comment the following line to see what we get

    # print(json.dumps(device,indent=4))
except:
    print ("Something wrong, cannot get network device information")
    sys.exit()

if status != 200:
    print (resp.text)
    sys.exit()

if device == [] :   # Response is empty, no network-device is discovered.
    print ("No network device found !")
    sys.exit()

device_list = []
# Now extract host name, ip and type to a list. Also add a sequential number in front
i=0
for item in device:
    i+=1
    device_list.append([i,item["PUT HOSTNAME ATTRIBUTE HERE"],item["PUT MANAGEMENT IP ATTRIBUTE HERE"],item["PUT TYPE ATTRIBUTE HERE"],item["PUT INSTANCE ID ATTRIBUTE HERE"]])

# We use tabulate module here to print a nice table format. You should use "pip" tool to install in your local machine
# For the simplicity we just copy the source code in working directory without  installing it.
# Not showing id to user, it's just a hex string
print (tabulate(device_list, headers=['number','hostname','ip','type'],tablefmt="rst"))
