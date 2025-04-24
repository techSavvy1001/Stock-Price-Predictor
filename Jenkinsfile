pipeline {
    agent any

    stages {
        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Scripts') {
            steps {
                sh 'python3 app/main.py'
            }
        }
    }
}
