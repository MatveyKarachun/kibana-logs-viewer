import argparse
import json

parser = argparse.ArgumentParser(description='Filter log JSON file.')
parser.add_argument('filename', type=str, help='The path to the JSON file.')
parser.add_argument('output', type=str, help='The path to the output file.')
parser.add_argument('--skip_stack', action='store_true', default=False, help='Show stack (default: True)')

args = parser.parse_args()

with open(args.filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(args.output, 'w', encoding='utf-8') as f_out:
    for hit in data['hits']['hits']:
        source = hit['_source']
        log_text = source.get('text', 'N/A')

        output = [
            f"{source.get('localTime', 'N/A')}\n",
            f"{source.get('text', 'N/A')}\n\n",
            f"{source.get('podName', 'N/A')} {source.get('level', 'N/A')} {source.get('callerClass', 'N/A')} {source.get('callerMethod', 'N/A')} {source.get('callerLine', 'N/A')}\n",
            f"{source.get('traceId', 'N/A')}\n",
        ]

        if not args.skip_stack:
            output.append(f"{source.get('stack', 'N/A')}\n")

        output.append("----\n\n\n")

        f_out.writelines(output)
