pipeline {
    agent any

    environment {
        FLASK_APP_IMAGE_NAME = 'flask-app-1'
        NGINX_IMAGE_NAME = 'nginx-1'
        GIT_CONFIG_IMAGE_NAME = 'git-config-1'
        JENKINS_IMAGE_NAME = 'jenkins-1'

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
                    docker.build("${FLASK_APP_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", 'path_to_flask_app_Dockerfile')
                    docker.build("${NGINX_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", 'path_to_nginx_Dockerfile')
                    docker.build("${GIT_CONFIG_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", 'path_to_git_config_Dockerfile')
                    docker.build("${JENKINS_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", 'path_to_jenkins_Dockerfile')
                }
            }
        }

        stage('Start Docker Containers') {
            steps {
                script {
                    docker.run("-d --name ${CONTAINER_NAME}_flask ${FLASK_APP_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                    docker.run("-d --name ${CONTAINER_NAME}_nginx ${NGINX_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                    docker.run("-d --name ${CONTAINER_NAME}_git ${GIT_CONFIG_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                    docker.run("-d --name ${CONTAINER_NAME}_jenkins ${JENKINS_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
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

                docker.stop("${CONTAINER_NAME}_nginx")
                docker.remove("${CONTAINER_NAME}_nginx")

                docker.stop("${CONTAINER_NAME}_git")
                docker.remove("${CONTAINER_NAME}_git")

                docker.stop("${CONTAINER_NAME}_jenkins")
                docker.remove("${CONTAINER_NAME}_jenkins")
            }
            echo 'End of Execution'
        }
        failure {
            script {
                // Stop and remove all containers on failure
                docker.stop("${CONTAINER_NAME}_flask")
                docker.remove("${CONTAINER_NAME}_flask")

                docker.stop("${CONTAINER_NAME}_nginx")
                docker.remove("${CONTAINER_NAME}_nginx")

                docker.stop("${CONTAINER_NAME}_git")
                docker.remove("${CONTAINER_NAME}_git")

                docker.stop("${CONTAINER_NAME}_jenkins")
                docker.remove("${CONTAINER_NAME}_jenkins")
            }
            echo 'Failed'
        }
    }
}
