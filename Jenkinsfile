pipeline {
    agent any

    stages {
        stage('Check Docker Version') {
            steps {
                script {
                    // Set the Docker path explicitly
                    def dockerHome = tool name: 'Docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    // Run the 'docker --version' command
                    sh 'docker --version'
                }
            }
        }

        // Add more stages as needed...
    }
}
