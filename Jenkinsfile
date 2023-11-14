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

        stage('Run Python') {
            steps {
                script {
                    sh 'python3 --version'  // Install project dependencies
                }
            }
        }

        stage('hello') {
            steps {
                sh 'python3 app.py'
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
