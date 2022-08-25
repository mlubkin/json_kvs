json_kvs is dependency free library for key/value storage, based on json file

json_kvs can receive optional 'scope' parameter, what allows to use same file in multiple scripts simultaneously  

## Installation
```
pip install json_kvs
```

## Usage

kvsObj = KVS('path_to_json_file', scope='scope_name'(OPTIONAL))

kvsObj.set_value('key', 'value')  -- write value

kvsObj.get_value('key')           -- reade value

## Example

```python
from json_kvs import KVS
key = 'key1'
value = 'val1'
scope = 'test_scope1'
pathToJson = '/tmp/kvs.json'

kvsObj = KVS(pathToJson, scope=scope)

kvsObj.set_value(key, value)

print(kvsObj.get_value(key))

```
## License

MIT