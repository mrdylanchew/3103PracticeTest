pipeline {
    agent {
        docker {
            // Specify the Docker image that has both Jenkins and Docker installed
            image 'jenkins/jenkins:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        FLASK_APP_IMAGE_NAME = 'flask-app-1'
        DOCKER_IMAGE_TAG = 'latest'
        CONTAINER_NAME = '3103practicetest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${FLASK_APP_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", '.')
                }
            }
        }

        stage('Start Docker Containers') {
            steps {
                script {
                    // Start the Flask app container
                    docker.run("-d --name ${CONTAINER_NAME}_flask ${FLASK_APP_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests in the flask-app-1 container
                    docker.exec("${CONTAINER_NAME}_flask", 'python3 -m unittest testcase.py')
                }
            }
        }
    }

    post {
        success {
            script {
                // Stop and remove all containers
                docker.stop("${CONTAINER_NAME}_flask")
                docker.remove("${CONTAINER_NAME}_flask")
            }
            echo 'End of Execution'
        }
        failure {
            script {
                // Stop and remove all containers on failure
                docker.stop("${CONTAINER_NAME}_flask")
                docker.remove("${CONTAINER_NAME}_flask") 
            }
            echo 'Failed'
        }
    }
}
