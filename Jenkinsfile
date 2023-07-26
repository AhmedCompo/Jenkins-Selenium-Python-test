pipeline {
    agent {
        docker {
            image 'python:3.10.6' // Choose the appropriate Python version
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install selenium'
            }
        }

        // Rest of your stages here...
    }
}
