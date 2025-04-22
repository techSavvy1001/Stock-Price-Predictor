pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        // Set Python version (adjust if needed)
        PYTHON = 'python3'
        VENV_DIR = "${env.WORKSPACE}/venv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm  // Pulls code from your Git repository
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh "${PYTHON} -m venv ${VENV_DIR}"
                    
                    // Install dependencies
                    sh "${VENV_DIR}/bin/pip install -r app/requirements.txt"
                }
            }
        }

        stage('Run Training & Plotting') {
            steps {
                script {
                    // Train the model and generate plots
                    sh "${VENV_DIR}/bin/python app/train_and_plot.py"
                }
            }
        }

        stage('Run Predictions') {
            steps {
                script {
                    // Execute predictions (optional)
                    sh "${VENV_DIR}/bin/python app/predict.py"
                }
            }
        }

        stage('Run Main Script') {
            steps {
                script {
                    // Alternatively, run main.py if it's your entry point
                    sh "${VENV_DIR}/bin/python app/main.py"
                }
            }
        }
    }

    post {
        always {
            // Archive generated plots or logs (if needed)
            archiveArtifacts artifacts: 'app/*.png', allowEmptyArchive: true
        }
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}