pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Report') {
            steps {
                allure([
                    includeProperties: true,
                    jdk: '',
                    results: [[path: 'report']]
                ])
            }
        }
    }
}