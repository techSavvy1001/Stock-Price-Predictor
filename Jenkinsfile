pipeline {
    agent any

    stages {
        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Installing pip (if missing)') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3-pip
                '''
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
