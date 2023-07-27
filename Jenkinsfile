pipeline {
    agent any

    tools {
        // Define the 'docker' tool to ensure Docker is available in the pipeline
        // Set the 'Docker' label to match the name configured in Jenkins Global Tool Configuration
        docker 'Docker'
    }

    stages {
        stage('Check Docker Version') {
            steps {
                // Run the 'docker --version' command
                sh 'docker --version'
            }
        }

        // Add more stages as needed...
    }
}
