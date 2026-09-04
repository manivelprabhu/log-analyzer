Project Structure
log-analyzer/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── sample.log
├── k8s/
│   ├── deployment.yml
│   └── services.yml
├── ansible/
│   ├── log_analyzer.ini
│   └── setup.yml
├── .gitignore
└── README.md
1. Run the Application Directly
cd app
python3 app.py

The application runs on port 5000.

Test:

curl http://localhost:5000/
curl http://localhost:5000/analyze

Expected response from /:

Prabhu - Log Analyzer App is running!

Expected response from /analyze:

{
  "ERROR": 2,
  "INFO": 3,
  "WARNING": 1,
  "total_logs": 6
}
2. Run with Docker

Build the Docker image:

cd app
docker build -t log-analyzer:1.2 .

Run the container:

docker run -d --name log-analyzer -p 5000:5000 log-analyzer:1.2

Test:

curl http://localhost:5000/
curl http://localhost:5000/analyze

Check the container:

docker ps

Stop and remove the container:

docker stop log-analyzer
docker rm log-analyzer
3. Deploy on Minikube

Check Minikube:

minikube status

Load the Docker image into Minikube:

minikube image load log-analyzer:1.2

Deploy the application:

kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/services.yml

Check the deployment:

kubectl get deployments
kubectl get pods
kubectl get services

Access the application using port forwarding:

kubectl port-forward service/log-analyzer-service 5000:5000 --address 0.0.0.0

Then access:

http://<server-ip>:5000/
http://<server-ip>:5000/analyze
4. Deploy with Ansible

The Ansible playbook automatically:

Installs Python and pip
Installs Flask
Creates the application directory
Copies app.py
Copies sample.log
Creates a systemd service
Enables and starts the application
Inventory

The inventory file is:

ansible/log_analyzer.ini

Example:

[appservers]
localhost ansible_connection=local
Syntax Check
cd ansible
ansible-playbook -i log_analyzer.ini setup.yml --syntax-check
Dry Run
ansible-playbook -i log_analyzer.ini setup.yml --check
Deploy
ansible-playbook -i log_analyzer.ini setup.yml
Verify
systemctl status log-analyzer
curl http://localhost:5000/analyze

Expected response:

{
  "ERROR": 2,
  "INFO": 3,
  "WARNING": 1,
  "total_logs": 6
}
Technologies Used
Python
Flask
Docker
Kubernetes
Minikube
Ansible
Linux
systemd
Learning Objectives

This project demonstrates:

Python application development
Docker containerization
Kubernetes Deployment and Service
Minikube deployment
Ansible automation
Linux systemd service configuration
Basic application testing
