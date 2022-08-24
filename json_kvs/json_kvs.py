import json
import os

class KVS:
    basicJson = {"general": {} }
    kvsData = {}


    def __read_kvs_file(self,path):
        try:
            fileObj = open(path, 'r')
            data = json.load(fileObj)
            fileObj.close()
            #print('KVS file uploaded successfully')
            return data
        except Exception as e:
            print("Can't read KVS file")
            print(e)
            exit()

    def __upload_kvs_content(self, path):
        if os.path.exists(path):
            self.kvsData = self.__read_kvs_file(path)
        else:
            print('KVS file not exists and will be created')
            basicJson = '{"general": {} }'
            try:
                with open(path, 'w') as fileObj:
                    fileObj.write(basicJson)
                    fileObj.close()
                self.kvsData = self.basicJson
            except Exception as e:
                print("Can't create KVS file")
                print(e)
                exit()


    def __write_down_kvs_content(self, path):
        self.__compare_and_merge_json_delta(path)
        try:
            fileObj = open(path, 'w')
            json.dump(self.kvsData, fileObj)
            fileObj.close()
        except Exception as e:
            print(e)


    def __verify_scope_and_cereate_if_not_exists(self):
        #print(self.scope, type(self.kvsData), self.kvsData, type(self.basicJson), self.basicJson)
        if self.scope not in self.kvsData.keys():
            self.kvsData[self.scope] = {}
    
    
    def __compare_and_merge_json_delta(self, path):
        fileData = self.__read_kvs_file(path)
        for key in fileData.keys():
            if key in self.kvsData.keys():
                for key2 in fileData[key].keys():
                    if key2 not in self.kvsData[key].keys():
                        self.kvsData[key][key2] = fileData[key][key2]
                        
            else:
                self.kvsData[key] = fileData[key]


    def __init__(self, path, scope = None):
        self.kvsPath = path
        if not scope:
            self.scope = 'general'
        else:
            self.scope = scope
        self.__upload_kvs_content(self.kvsPath)


    def __set_key(self, key):
        self.__verify_scope_and_cereate_if_not_exists()
        #print(self.kvsData)
        if key not in self.kvsData[self.scope].keys():
            self.kvsData[self.scope][key] = ""
            self.__write_down_kvs_content(self.kvsPath)


    def set_value(self, key, value):
        self.__verify_scope_and_cereate_if_not_exists()
        self.__set_key(key)
        self.kvsData[self.scope][key] = value
        self.__write_down_kvs_content(self.kvsPath)
        return True
    

    def get_value(self, key):
        return self.kvsData[self.scope][key]


    def test(self):
        print(self.scope)
        print(self.kvsData)

