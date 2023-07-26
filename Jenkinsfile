pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Create a virtual environment using Python 3.8 (or 3.9 if available)
                sh 'python3.10 -m venv venv'
            }
        }

        // The rest of your stages (Install dependencies, Version, Run, Cleanup) remain the same.
    }
}
