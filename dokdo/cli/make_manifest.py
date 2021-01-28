import os
from pathlib import Path

def make_manifest(fastq_dir, output_file):
    _fastq_dir = Path(fastq_dir).resolve()

    files = {}

    for r, d, f in os.walk(_fastq_dir):
        for x in f:
            name = '_'.join(x.split('_')[:-3])

            if '_R1_001.fastq' in x:
                if name not in files:
                    files[name] = ['', '']
                files[name][0] = f'{r}/{x}'
            elif '_R2_001.fastq' in x:
                if name not in files:
                    files[name] = ['', '']
                files[name][1] = f'{r}/{x}'
            else:
                pass

    with open(output_file, 'w') as f:
        headers = ['sample-id', 'forward-absolute-filepath',
                   'reverse-absolute-filepath']
        f.write('\t'.join(headers) + '\n')

        for name in sorted(files):
            fields = [name, files[name][0], files[name][1]]
            f.write('\t'.join(fields) + '\n')
