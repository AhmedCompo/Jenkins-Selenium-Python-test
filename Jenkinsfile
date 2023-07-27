pipeline {
    agent any

    stages {
        

        stage('Install dependencies') {
            steps {
                // Install the Python dependencies from the requirements.txt file
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Python script') {
            steps {
                // Execute your Python script here
                sh 'python3 test_sign_in.py'
            }
        }
    }
}
