# Auth Module MicroService
This repository contains the codebase for the authentication project.
When setting up a pipeline for a new project, it's important to follow these steps:

1. Create an EC2 server with Docker and Docker Compose installed.
2. Clone the repository and save the Git credentials on the server.
3. Copy the public key of the Jenkins server (specifically the Jenkins user) to the newly created server and restart the SSHD service.
4. Establish an SSH connection from Jenkins to the server.
5. Ensure that the Dockerfile is optimized for the project's needs.
6. Use a bash script to build and run the Docker container.
7. Configure the proxy path in the Nginx site-available default file.
8. Add a DNS entry in Route 53 to map the project's domain to the server's IP address.
9. Implement SSL certificate for secure communication.

Following these steps will help streamline the process of setting up a pipeline for new projects.

