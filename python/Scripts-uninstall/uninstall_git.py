import subprocess

def uninstall_git():
    try:
        subprocess.run(['sudo', 'apt-get', 'remove', '-y', 'git'], check=True)
        subprocess.run(['sudo', 'apt-get', 'purge', '-y', 'git'], check=True)
        subprocess.run(['sudo', 'apt-get', 'autoremove', '-y'], check=True)
        print("Git uninstalled successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to uninstall Git.")

if __name__ == "__main__":
    uninstall_git()