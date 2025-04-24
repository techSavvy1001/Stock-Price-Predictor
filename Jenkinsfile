pipeline {
    agent any

    stages {
        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 app/main.py'
            }
        }
    }
}
