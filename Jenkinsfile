pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                // Create a virtual environment named 'venv'
                sh 'python3 -m venv venv'
            }
        }

        

        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run your Python script
                sh '. venv/bin/activate && python test_sign_in.py'
            }
        }
    }
}
