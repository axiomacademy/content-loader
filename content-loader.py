import argparse
import yaml
from yamlinclude import YamlIncludeConstructor

YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir='.')

# Building the argument parser
parser = argparse.ArgumentParser(description='Upload content into the knowledge graph')
parser.add_argument('--commit', dest='commit', action='store_const',
        const=True, default=False, help='Commit changes to the database')
parser.add_argument("config_file")

args = parser.parse_args()
print(args.commit)
print(args.config_file)

# Open up the config file
with open(args.config_file, 'r') as cf:
    parsed_yaml = yaml.load(cf, Loader=yaml.FullLoader)
    print(parsed_yaml)

