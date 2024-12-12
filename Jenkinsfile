pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python -m venv venv'
                sh './venv/Scripts/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'results']]
                ])
            }
        }
    }
}