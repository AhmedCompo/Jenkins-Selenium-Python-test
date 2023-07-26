pipeline {
    agent {
        dockerContainer image: 'python:3.10'
    }

     stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
            }
        }

    }
}
