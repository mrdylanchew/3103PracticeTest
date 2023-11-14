pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'practice-docker-image'
        DOCKER_IMAGE_TAG = 'latest'
        CONTAINER_NAME = 'docker-container-name'
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
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", '.')
                }
            }
        }

        stage('Start Docker Container') {
            steps {
                script {
                    docker.run("-d --name ${CONTAINER_NAME} ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.exec("${CONTAINER_NAME}", 'python3 -m unittest testcase.py')
                }
            }
        }
    }

    post {
        success {
            script {
                docker.stop(CONTAINER_NAME)
                docker.remove(CONTAINER_NAME)
            }
            echo 'End of Execution'
        }
        failure {
            script {
                docker.stop(CONTAINER_NAME)
                docker.remove(CONTAINER_NAME)
            }
            echo 'Failed'
        }
    }
}
