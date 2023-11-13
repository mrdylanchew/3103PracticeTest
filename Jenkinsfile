pipeline {
    agent any

    environment {
        // Define environment variables if needed
        VIRTUAL_ENV = 'venv'
        PATH = "${3103Practice}/${VIRTUAL_ENV}/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create and activate a virtual environment
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'

                // Install necessary dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python tests using a testing framework like pytest
                sh 'source venv/bin/activate && python -m pytest'
            }
        }

        stage('Run Flask Application') {
            steps {
                // Start your Flask application
                sh 'source venv/bin/activate && python your_flask_app.py'
            }
        }
    }

    post {
        success {
            // Additional actions to take on successful build
            echo 'Build successful!'
            // You may consider deploying your application, sending notifications, etc.
        }
        failure {
            // Additional actions to take on failed build
            echo 'Build failed!'
            // You may consider sending notifications, logging, or other actions.
        }
    }
}
