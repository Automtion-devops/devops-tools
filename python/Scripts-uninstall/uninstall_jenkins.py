import subprocess

def uninstall_jenkins():
    try:
        subprocess.run(['sudo', 'docker', 'stop', 'jenkins'], check=True)
        subprocess.run(['sudo', 'docker', 'rm', 'jenkins'], check=True)
        subprocess.run(['sudo', 'docker', 'rmi', 'jenkins/jenkins:lts'], check=True)
        subprocess.run(['sudo', 'rm', '-rf', 'jenkins_home'], check=True)
        print("Jenkins uninstalled successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to uninstall Jenkins.")

if __name__ == "__main__":
    uninstall_jenkins()