pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io'  // Replace with your Docker registry URL
        IMAGE_NAME = '3103practicetest-flask-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Building the Docker image
                    docker.withRegistry('https://${DOCKER_REGISTRY}', 'docker-credentials') {
                        def customImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '-f Dockerfile .')
                        customImage.push()
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building the project...'
                    // Add your build commands here
                }
            }
        }
    }

    post {
        success {
            echo 'Build and Docker image build successful!'
        }
        failure {
            echo 'Build or Docker image build failed!'
        }
    }
}
