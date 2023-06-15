# Python script to install run jenkins as docker container 
import os 
import time 

# Export jenkins user and home directory 
jenkins_user = "jenkins"
home_directory = "/opt/jenkins"

print("Jenkins user is",jenkins_user)
print("Jenkins home directory is", home_directory)

# Add jenkins user 
add_jenkins_user = "useradd -m -d /opt/jenkins jenkins"

# Change jenkins home directory permissions 
home_dir_write_perm = "chmod -vR 777 /opt/jenkins"

os.system(add_jenkins_user)
os.system(home_dir_write_perm)

docker_run = "docker run --name jenkins -it -d -p 8090:8080 -p 50000:50000 -v /opt/jenkins:/var/jenkins_home  jenkins/jenkins:lts-jdk11"
os.system(docker_run)
print("\nPlease note, jenkins is accessible on port 8090\n")

print("Displaying Jenkins admin password in 10 seconds\n")
time.sleep(10)
jenkins_admin_password = "docker exec jenkins  cat /var/jenkins_home/secrets/initialAdminPassword"
os.system(jenkins_admin_password)
print("\n")
