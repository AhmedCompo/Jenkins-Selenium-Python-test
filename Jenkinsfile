pipeline {
    agent any

    environment {
        // Define the Python version you want to use
        pythonVersion = '3.10.6'
    }

    stages {
       

        stage('Setup Virtual Environment') {
            steps {
                // Create a virtual environment
                sh "python${pythonVersion} -m venv venv"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Activate the virtual environment and install dependencies
                sh ". venv/bin/activate && pip install selenium"
            }
        }

        stage('Version') {
            steps {
                // Check Python version (optional)
                sh "python${pythonVersion} --version"
            }
        }

        stage('Run Tests') {
            steps {
                // Run the script within the virtual environment
                sh ". venv/bin/activate && python${pythonVersion} test_sign_in.py"
            }
        }

        stage('Cleanup') {
            steps {
                // Deactivate the virtual environment and remove it (optional)
                sh "deactivate"
                sh "rm -rf venv"
            }
        }
    }
}
