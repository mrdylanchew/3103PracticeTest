pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io'
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
                    docker.withRegistry('https://${DOCKER_REGISTRY}', 'docker-credentials') {
                        def customImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '-f Dockerfile .')
                        customImage.push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add deployment steps here (e.g., deploy to a server, Kubernetes, etc.)
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").remove()
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
