pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'pytest tests/'
            }
        }
        stage('Docker Build') {
            steps {
                bat 'docker build -t iris-api .'
            }
        }
    }
}
