pipeline {
    agent any

    stages {
        stage('Check Docker Version') {
            steps {
                script {
                    // Use Docker directly in the pipeline
                    docker.image('docker:latest').inside {
                        sh 'docker --version'
                    }
                }
            }
        }

        // Add more stages as needed...
    }
}
