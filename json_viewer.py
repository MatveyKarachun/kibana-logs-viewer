import argparse
import json

parser = argparse.ArgumentParser(description='Filter log JSON file.')
parser.add_argument('filename', type=str, help='The path to the JSON file.')

args = parser.parse_args()

with open(args.filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

for hit in data['hits']['hits']:
    source = hit['_source']
    log_text = source.get('text', 'N/A')

    if "FreeMarker" in log_text:
        continue
    print(f"{source.get('localTime', 'N/A')}")
    print(f"{source.get('text', 'N/A')}")

    print()

    print(f"{source.get('podName', 'N/A')}", end=' ')
    print(f"{source.get('level', 'N/A')}", end=' ')
    print(f"{source.get('callerClass', 'N/A')}", end=' ')
    print(f"{source.get('callerMethod', 'N/A')}", end=' ')
    print(f"{source.get('callerLine', 'N/A')}")
    print(f"{source.get('traceId', 'N/A')}")
    print(f"{source.get('stack', 'N/A')}")

    print()
    print("----")
    print()