pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python --version' // Corrected the Python version check
            }
        }

        // Add more stages as needed...
    }
}
