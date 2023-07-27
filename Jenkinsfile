pipeline {
    agent any

    stages {
        stage('Install Selenium') {
            steps {
                sh 'apt update'
                sh 'apt install -y python3-selenium'
            }
        }

    }
}
