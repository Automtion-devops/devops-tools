package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

var repositories = []string{}

func showBanner() {
	banner := `
    ____             ____        _            
   / __ \____  _____/ __ \____  (_)___  ____ _
  / / / / __ \/ ___/ /_/ / __ \/ / __ \/ __ ` + "`" + `/
 / /_/ / /_/ / /  / _, _/ /_/ / / / / / /_/ / 
/_____/\____/_/  /_/ |_|\____/_/_/ /_/\__, /  
                                     /____/   
    ____             _                 
   / __ \____  _____(_)___  ____  _____
  / / / / __ \/ ___/ / __ \/ __ \/ ___/
 / /_/ / /_/ / /  / / /_/ / / / (__  ) 
/_____/\____/_/  /_/\____/_/ /_/____/  
    ____        __                     
   / __ \____  / /_  __  ______________
  / / / / __ \/ __ \/ / / / ___/ ___/ _ \
 / /_/ / /_/ / /_/ / /_/ (__  |__  )  __/
/_____/\____/_.___/\__,_/____/____/\___/ 
                                        
                by Andres Henao
    `
	fmt.Println(banner)
}

func showMainMenu() {
	fmt.Println("DevOps Tools Main Menu:")
	fmt.Println("1. Check System")
	fmt.Println("2. Tools DevOps")
	fmt.Println("3. Exit")
}

func showSystemMenu() {
	fmt.Println("Check System Menu:")
	fmt.Println("1. Check Disk Usage")
	fmt.Println("2. Check Memory Usage")
	fmt.Println("3. Check CPU Usage")
	fmt.Println("4. Check Network Usage")
	fmt.Println("5. Check Running Processes")
	fmt.Println("6. Check System Uptime")
	fmt.Println("7. Back to Main Menu")
}

func showToolsMenu() {
	fmt.Println("Tools DevOps Menu:")
	fmt.Println("1. Install Tools")
	fmt.Println("2. Check Version and Update")
	fmt.Println("3. GitHub")
	fmt.Println("4. Back to Main Menu")
}

func showInstallToolsMenu() {
	fmt.Println("Install Tools Menu:")
	fmt.Println("1. Install Minikube")
	fmt.Println("2. Install kubectl")
	fmt.Println("3. Install Terraform")
	fmt.Println("4. Install Helm")
	fmt.Println("5. Install GitHub CLI")
	fmt.Println("6. Install Docker")
	fmt.Println("7. Install Ansible")
	fmt.Println("8. Back to Tools DevOps Menu")
}

func showGitHubMenu() {
	fmt.Println("GitHub Menu:")
	fmt.Println("1. Authenticate with GitHub")
	fmt.Println("2. Clone GitHub Repository")
	fmt.Println("3. Create GitHub Repository")
	fmt.Println("4. List GitHub Repositories")
	fmt.Println("5. Back to Tools DevOps Menu")
}

func showCheckVersionMenu() {
	fmt.Println("Check Version and Update Menu:")
	fmt.Println("1. Check Minikube Version")
	fmt.Println("2. Check kubectl Version")
	fmt.Println("3. Check Terraform Version")
	fmt.Println("4. Check Helm Version")
	fmt.Println("5. Check GitHub CLI Version")
	fmt.Println("6. Check Docker Version")
	fmt.Println("7. Check Ansible Version")
	fmt.Println("8. Back to Tools DevOps Menu")
}

func runCommand(command string) error {
	cmd := exec.Command("bash", "-c", command)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

func authenticateGitHub() {
	fmt.Println("Authenticating with GitHub...")
	err := runCommand("gh auth login")
	if err != nil {
		fmt.Println("Error authenticating with GitHub:", err)
	} else {
		fmt.Println("Successfully authenticated with GitHub.")
	}
}

func checkVersion(command, toolName string) {
	cmd := exec.Command("bash", "-c", command)
	output, err := cmd.Output()
	if err != nil {
		fmt.Printf("Error checking %s version: %s\n", toolName, err)
		return
	}
	fmt.Printf("%s Version: %s\n", toolName, strings.TrimSpace(string(output)))
	fmt.Printf("Do you want to update %s? (y/n): ", toolName)
	reader := bufio.NewReader(os.Stdin)
	update, _ := reader.ReadString('\n')
	update = strings.TrimSpace(update)
	if update == "y" {
		switch toolName {
		case "Minikube":
			installMinikube()
		case "kubectl":
			installKubectl()
		case "Terraform":
			installTerraform()
		case "Helm":
			installHelm()
		case "GitHub CLI":
			installGitHubCLI()
		case "Docker":
			installDocker()
		case "Ansible":
			installAnsible()
		}
	}
}

func checkMinikubeVersion() {
	checkVersion("minikube version --short", "Minikube")
}

func checkKubectlVersion() {
	checkVersion("kubectl version --client --short", "kubectl")
}

func checkTerraformVersion() {
	checkVersion("terraform version", "Terraform")
}

func checkHelmVersion() {
	checkVersion("helm version --short", "Helm")
}

func checkGitHubCLIVersion() {
	checkVersion("gh --version", "GitHub CLI")
}

func checkDockerVersion() {
	checkVersion("docker --version", "Docker")
}

func checkAnsibleVersion() {
	checkVersion("ansible --version", "Ansible")
}

func checkDiskUsage() {
	runCommand("df -h")
}

func checkMemoryUsage() {
	runCommand("free -h")
}

func checkCPUUsage() {
	runCommand("top -bn1 | grep 'Cpu(s)'")
}

func checkNetworkUsage() {
	runCommand("ifconfig")
}

func checkRunningProcesses() {
	runCommand("ps aux")
}

func checkSystemUptime() {
	runCommand("uptime")
}

func cloneGitHubRepo() {
	fmt.Print("Enter the GitHub repository URL to clone: ")
	reader := bufio.NewReader(os.Stdin)
	repoURL, _ := reader.ReadString('\n')
	repoURL = strings.TrimSpace(repoURL)
	runCommand(fmt.Sprintf("git clone %s", repoURL))
}

func createGitHubRepo() {
	fmt.Print("Enter the name of the new GitHub repository: ")
	reader := bufio.NewReader(os.Stdin)
	repoName, _ := reader.ReadString('\n')
	repoName = strings.TrimSpace(repoName)
	runCommand(fmt.Sprintf("gh repo create %s --public", repoName))
}

func listGitHubRepos() {
	fmt.Print("Enter the GitHub username: ")
	reader := bufio.NewReader(os.Stdin)
	username, _ := reader.ReadString('\n')
	username = strings.TrimSpace(username)
	runCommand(fmt.Sprintf("gh repo list %s", username))
}

func installMinikube() {
	if err := runCommand("minikube version"); err == nil {
		fmt.Println("Minikube is already installed.")
	} else {
		runCommand("curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64")
		runCommand("sudo install minikube-linux-arm64 /usr/local/bin/minikube")
	}
}

func installKubectl() {
	if err := runCommand("kubectl version --client"); err == nil {
		fmt.Println("kubectl is already installed.")
	} else {
		runCommand("curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl")
		runCommand("sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl")
	}
}

func installTerraform() {
	if err := runCommand("terraform version"); err == nil {
		fmt.Println("Terraform is already installed.")
	} else {
		runCommand("sudo apt update && sudo apt upgrade -y")
		version := "1.5.0"
		terraformZip := fmt.Sprintf("terraform_%s_linux_arm.zip", version)
		terraformURL := fmt.Sprintf("https://releases.hashicorp.com/terraform/%s/%s", version, terraformZip)
		runCommand(fmt.Sprintf("wget %s", terraformURL))
		runCommand(fmt.Sprintf("unzip %s", terraformZip))
		runCommand("sudo mv terraform /usr/local/bin/")
		runCommand("terraform -version")
		runCommand(fmt.Sprintf("rm %s", terraformZip))
		fmt.Println("Terraform instalado correctamente.")
	}
}

func installHelm() {
	runCommand("curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash")
}

func installGitHubCLI() {
	if err := runCommand("gh --version"); err == nil {
		fmt.Println("GitHub CLI is already installed.")
	} else {
		runCommand("type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)")
		runCommand("curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg")
		runCommand("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C99B11DEB97541F0")
		runCommand("sudo apt-add-repository \"deb [arch=arm64] https://cli.github.com/packages stable main\"")
		runCommand("sudo apt update && sudo apt install gh")
	}
}

func installDocker() {
	if err := runCommand("docker --version"); err == nil {
		fmt.Println("Docker is already installed.")
	} else {
		fmt.Println("Updating package list...")
		if err := runCommand("sudo apt update"); err != nil {
			fmt.Println("Error updating package list:", err)
			return
		}

		fmt.Println("Installing prerequisite packages...")
		if err := runCommand("sudo apt install -y apt-transport-https ca-certificates curl software-properties-common"); err != nil {
			fmt.Println("Error installing prerequisite packages:", err)
			return
		}

		fmt.Println("Adding Docker GPG key...")
		if err := runCommand("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"); err != nil {
			fmt.Println("Error adding Docker GPG key:", err)
			return
		}

		fmt.Println("Adding Docker repository to APT sources...")
		if err := runCommand(`echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`); err != nil {
			fmt.Println("Error adding Docker repository:", err)
			return
		}

		fmt.Println("Updating package list again...")
		if err := runCommand("sudo apt update"); err != nil {
			fmt.Println("Error updating package list:", err)
			return
		}

		fmt.Println("Installing Docker...")
		if err := runCommand("sudo apt install -y docker-ce"); err != nil {
			fmt.Println("Error installing Docker:", err)
			return
		}

		fmt.Println("Checking Docker status...")
		if err := runCommand("sudo systemctl status docker"); err != nil {
			fmt.Println("Error checking Docker status:", err)
			return
		}

		fmt.Println("Adding user to Docker group...")
		if err := runCommand("sudo usermod -aG docker ${USER}"); err != nil {
			fmt.Println("Error adding user to Docker group:", err)
			return
		}

		fmt.Println("Applying new group membership...")
		if err := runCommand("su - ${USER}"); err != nil {
			fmt.Println("Error applying new group membership:", err)
			return
		}

		fmt.Println("Docker installation and configuration complete.")
	}
}

func installAnsible() {
	runCommand("sudo apt update")
	runCommand("sudo apt install ansible -y")
}

func main() {
	showBanner()
	reader := bufio.NewReader(os.Stdin)
	for {
		showMainMenu()
		fmt.Print("Enter your choice: ")
		choice, _ := reader.ReadString('\n')
		choice = strings.TrimSpace(choice)
		switch choice {
		case "1":
			for {
				showSystemMenu()
				fmt.Print("Enter your choice: ")
				systemChoice, _ := reader.ReadString('\n')
				systemChoice = strings.TrimSpace(systemChoice)
				if systemChoice == "7" {
					break
				}
				switch systemChoice {
				case "1":
					checkDiskUsage()
				case "2":
					checkMemoryUsage()
				case "3":
					checkCPUUsage()
				case "4":
					checkNetworkUsage()
				case "5":
					checkRunningProcesses()
				case "6":
					checkSystemUptime()
				default:
					fmt.Println("Invalid choice. Please try again.")
				}
			}
		case "2":
			for {
				showToolsMenu()
				fmt.Print("Enter your choice: ")
				toolsChoice, _ := reader.ReadString('\n')
				toolsChoice = strings.TrimSpace(toolsChoice)
				if toolsChoice == "4" {
					break
				}
				switch toolsChoice {
				case "1":
					for {
						showInstallToolsMenu()
						fmt.Print("Enter your choice: ")
						installChoice, _ := reader.ReadString('\n')
						installChoice = strings.TrimSpace(installChoice)
						if installChoice == "8" {
							break
						}
						switch installChoice {
						case "1":
							installMinikube()
						case "2":
							installKubectl()
						case "3":
							installTerraform()
						case "4":
							installHelm()
						case "5":
							installGitHubCLI()
						case "6":
							installDocker()
						case "7":
							installAnsible()
						default:
							fmt.Println("Invalid choice. Please try again.")
						}
					}
				case "2":
					for {
						showCheckVersionMenu()
						fmt.Print("Enter your choice: ")
						versionChoice, _ := reader.ReadString('\n')
						versionChoice = strings.TrimSpace(versionChoice)
						if versionChoice == "8" {
							break
						}
						switch versionChoice {
						case "1":
							checkMinikubeVersion()
						case "2":
							checkKubectlVersion()
						case "3":
							checkTerraformVersion()
						case "4":
							checkHelmVersion()
						case "5":
							checkGitHubCLIVersion()
						case "6":
							checkDockerVersion()
						case "7":
							checkAnsibleVersion()
						default:
							fmt.Println("Invalid choice. Please try again.")
						}
					}
				case "3":
					for {
						showGitHubMenu()
						fmt.Print("Enter your choice: ")
						githubChoice, _ := reader.ReadString('\n')
						githubChoice = strings.TrimSpace(githubChoice)
						if githubChoice == "5" {
							break
						}
						switch githubChoice {
						case "1":
							authenticateGitHub()
						case "2":
							cloneGitHubRepo()
						case "3":
							createGitHubRepo()
						case "4":
							listGitHubRepos()
						default:
							fmt.Println("Invalid choice. Please try again.")
						}
					}
				default:
					fmt.Println("Invalid choice. Please try again.")
				}
			}
		case "3":
			fmt.Println("Exiting...")
			return
		default:
			fmt.Println("Invalid choice. Please try again.")
		}
	}
}
