pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
            }
        }

        stage('Install dependencies') {
            steps {
                // Activate the virtual environment
                sh '. venv/bin/activate'
                // Install the required modules
                sh 'pip install selenium'
            }
        }

        stage('Version') {
            steps {
                // Check Python version (optional)
                sh 'python3 --version'
            }
        }

        stage('Run') {
            steps {
                // Run the script within the virtual environment
                sh '. venv/bin/activate && python3 test_sign_in.py'
            }
        }

        stage('Cleanup') {
            steps {
                // Deactivate the virtual environment and remove it (optional)
                sh 'deactivate'
                sh 'rm -rf venv'
            }
        }
    }
}
