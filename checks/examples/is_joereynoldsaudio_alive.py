import subprocess

def check():

    # Note in this example we're using curl instead of urllib.
    # This is because CloudFlare seems to block the urllib
    # agent, lame.
    result = subprocess.run(
        ['curl', '-s', 'https://joereynoldsaudio.com'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    if 'OpenGameArt' not in result.stdout.decode('utf-8'):
        raise Exception('Failed to find string "OpenGameArt"')
