import toml
import sys

def check_toml_keys(filename):
    with open(filename, 'r') as f:
        d = toml.load(f)
    for i in range(1, len(d)):
        assert set(d['0'].keys()) == set(d[str(i)].keys()), f'incorrect keys for index {i}'
    return True

if __name__ == '__main__':
    success = check_toml_keys(sys.argv[1])
    if success:
        print('Data keys look good!')