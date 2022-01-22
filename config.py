import json

with open('config.json') as f:
    config = json.loads(f.read())

if __name__ == '__main__':
    print(config)