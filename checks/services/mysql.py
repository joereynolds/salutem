import subprocess

def check():
    result = subprocess.run(
        ['sudo', 'service', 'mysql', 'status'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    if result.returncode != 0:
        raise Exception(result.stdout)

