pipeline{
    agent {label "master"}
    environment {
        SHELL="/bin/bash"
    }
    stages{
        stage("Debug Docker") {
            steps {
                sh "whoami"
                sh "id"
                sh "env"
                sh "which docker || echo 'Docker not found'"
                sh "docker --version || echo 'Docker command not available'"
            }
        }    
         stage('init environment') {
            steps {
                echo "initializing the environment"
                sh 'export PATH=$PATH:/usr/bin'
            }
        }
        stage("SCM"){
            steps{
                git branch: 'main', url: 'https://github.com/pranaygupta1988/python-server-demo.git'
            }
        }
        stage("Build Docker Image"){
            steps{
                sh "/usr/bin/docker image build -t pranaygupta1988/server10 ."
            }
        }
        stage("Docker Login"){
            steps{
                withCredentials([string(credentialsId: 'DOCKER_HUB_TOKEN', variable: 'DOCKER_HUB_TOKEN')]) {
                sh "echo $DOCKER_HUB_TOKEN | /usr/bin/docker login -u pranaygupta1988 --password-stdin"
                 }
            }
        }
        stage("Push Docker Image "){
            steps{
                sh "/usr/bin/docker image push pranaygupta1988/server10"
            } 
        }
        stage("Remove Existing Docker Service"){
            steps{
                sh "/usr/bin/docker service rm server10"
            }
        }
        stage("Create Docker Service"){
            steps{
                sh "/usr/bin/docker service create --name server10 --replicas 2 -p 5000:5000 pranaygupta1988/server10"
            }
        }
    }
}
