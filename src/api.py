import sys, requests, json, config, os.path
from clint.textui import progress

class ApkDownApi:
    
    def get_app_metadata(self, name):

        url = config.app['metadata']['url']

        payload = {
            'package_name': name
        }

        response = requests.get(url, params=payload)
        return json.dumps(response.json(), sort_keys=True, indent=2)
    

    def get_store_apps(self, name, limit):

        url = config.app['store']['url']

        payload = {
            'store_name': name,
            'limit': limit
        }

        response = requests.get(url, params=payload)
        return json.dumps(response.json(), sort_keys=True, indent=2)
        
    
    def get_search_apps(self, name, limit):
        url = config.app['search']['url']
        
        payload = {
            'query': name,
            'limit': limit
        }

        response = requests.get(url, params=payload)
        return json.dumps(response.json(), sort_keys=True, indent=2)

    def get_download_app(self, name):
        
        url = config.app['search']['url']
        downPath = ""

        payload = {
            'query': name,
            'limit': 1
        }

        response = requests.get(url, params=payload)

        for x in response.json()['datalist']['list']:
            
            print "\n"
            print "------------------- [ APP ] -------------------"
            print "| ID: " + str(x['id'])       + "     |"
            print "| Name: " + str(x['name'])   + "     |"
            print "| Size: " + str(x['size'])   + "     |"
            print "-----------------------------------------------"
            print "Package: " + str(x['package'])
            print "-> Version Name: " + str(x['file']['vername']) 
            print "-> Version Code: " + str(x['file']['vercode'])
            print "-> MD5: " + str(x['file']['md5sum']) 
            print "-> Path: " + str(x['file']['path']) + "\n"

            dowSize = str(x['size'])
            downPath = str(x['file']['path'])

        
        promt = raw_input("[ Download y/n ] ")

        if promt == "y":
            # filename
            local_filename = name + ".apk"
            
            if os.path.exists(local_filename):
                print "File Exists\n"
                return False
            else:
                
                r = requests.get(downPath, stream=True)
                with open(local_filename, 'wb') as f:
                    total_length = int(r.headers.get('content-length'))
                    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                            f.write(chunk)
                            f.flush()
            
            print "\nSuccess!"
            
        else:
            print "Cancelled\n"
