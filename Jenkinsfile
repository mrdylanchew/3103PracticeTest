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

        stage('Run Tests') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'  // Install project dependencies
                    sh 'python -m unittest testcase.py'  // Run your unit tests
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
