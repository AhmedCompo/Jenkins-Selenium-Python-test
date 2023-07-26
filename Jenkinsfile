pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Create a virtual environment using Python 3.8 (or 3.9 if available)
                apt install python3.10-venv
            }
        }

        // The rest of your stages (Install dependencies, Version, Run, Cleanup) remain the same.
    }
}
