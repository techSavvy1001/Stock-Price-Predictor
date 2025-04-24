pipeline {
    agent any

    stages {
        stage('Verify Python') {
            steps {
                sh 'python --version'
            }
        }

        stage('Run Scripts') {
            steps {
                sh 'python app\\main.py'
            }
        }
    }
}
