pipeline {
    agent any

    environment {
        // Define the Python version you want to use
        pythonVersion = '3.8'
    }

    stages {
        stage('Install Python') {
            steps {
                // Install Python using the package manager (Linux) or a script (Windows/macOS)
                script {
                    // For Linux (Debian/Ubuntu-based)
                    sh "apt-get update -qq"
                    sh "apt-get install -y python${pythonVersion} python${pythonVersion}-venv"
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                // Create a virtual environment
                sh "python${pythonVersion} -m venv venv"
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
