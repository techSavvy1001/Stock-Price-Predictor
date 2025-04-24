pipeline {
    agent any

    stages {
        stage('Verify Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Scripts') {
            steps {
                bat 'python app\\main.py'
            }
        }
    }
}
