import sys
import re
import subprocess

NUMBER_OF_LINES_TO_READ = 2

if len(sys.argv) != 2:
    print('Usage: python test.py <filename>')
    sys.exit(1)

file_name = sys.argv[1]
file_content = ''
expectedValues = {}

with open(file_name, 'r') as file:
    for i in range(NUMBER_OF_LINES_TO_READ):
        file_content += file.readline()

    pattern = re.compile(r'# status: (.+)\n# stdout: (.+)')
    match = pattern.search(file_content)

    if match:
        expectedValues = {'status': match.group(1), 'stdout': match.group(2)}
    else:
        print('Usage: file does not have tests in a valid format')
        sys.exit(1)

    result = subprocess.run(f'python3 {file_name}', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    # print(expectedValues['status'])
    # print(result.returncode)

    if expectedValues['status'] == 'success' and result.returncode != 0:
        print(f'{file_name}: <failure>')
        sys.exit(1)


    if expectedValues['status'] == 'error' and result.returncode == 0:
        print(f'{file_name}: <failure>')
        sys.exit(1)

    # print(expectedValues['stdout'].strip())
    # print(result.stdout.strip())

    if expectedValues['stdout'].strip() != result.stdout.strip():
        print(f'{file_name}: <failure>')
        sys.exit(1)

    print(f'{file_name}: <success>')

