pipeline {
    agent any

    environment {
        // Use 'python' if added to PATH, else full path (e.g., 'C:\\Python39\\python.exe')
        PYTHON = 'python'  
        VENV_DIR = "${env.WORKSPACE}\\venv"
    }

    stages {
        stage('Check Python') {
            steps {
                script {
                    bat """
                        ${PYTHON} --version || echo ERROR: Python not found. Install it and add to PATH.
                    """
                }
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    bat """
                        ${PYTHON} -m venv "${VENV_DIR}"
                        call "${VENV_DIR}\\Scripts\\activate.bat" && pip install -r app\\requirements.txt
                    """
                }
            }
        }

        stage('Run Scripts') {
            steps {
                script {
                    bat """
                        call "${VENV_DIR}\\Scripts\\activate.bat" && ${PYTHON} app\\train_and_plot.py
                    """
                }
            }
        }
    }
}