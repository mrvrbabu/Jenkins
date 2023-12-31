# Python script to install run jenkins as docker container
import os
import time

# Export jenkins user and home directory
jenkins_user = "jenkins"
home_directory = "/opt/jenkins"

print("Jenkins user is", jenkins_user)
print("Jenkins home directory is", home_directory)

# Add jenkins user
add_jenkins_user = "useradd -m -d /opt/jenkins jenkins"

# Change jenkins home directory permissions
home_dir_write_perm = "chmod -vR 777 /opt/jenkins"

os.system(add_jenkins_user)
os.system(home_dir_write_perm)


# Note : - Enable port -p 50000:50000 to configure jenkins as master slave
docker_run = "docker run --name jenkins -it -d --restart unless-stopped -p 8090:8080 -v /opt/jenkins:/var/jenkins_home  jenkins/jenkins:lts-jdk11"
os.system(docker_run)
print("\nPlease note, jenkins is accessible on port 8090\n")

print("Displaying Jenkins admin password in 10 seconds\n")
# time.sleep(10)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

        # print("Sto")
        print(time_sec)


# num = int(input("Set Your Timer in sec : "))

countdown(10)

jenkins_admin_password = "docker exec jenkins  cat /var/jenkins_home/secrets/initialAdminPassword"
os.system(jenkins_admin_password)
print("\n")
