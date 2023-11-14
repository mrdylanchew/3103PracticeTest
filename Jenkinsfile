pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Build Docker Image for Python Flask'
                sh 'docker build -t docker.io/3103practicetest-flask-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker Image to Registry'
                sh 'docker push docker.io/3103practicetest-flask-app:latest'
            }
        }
    }

    post {
        success {
            echo 'End of Exeuction'
        }
        failure {
            echo 'Failed'
        }
    }
}
