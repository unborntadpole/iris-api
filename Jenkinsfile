pipeline {
    agent any
    stages {
        stage('Debug Env') {
            steps {
                bat 'echo %PATH%'
                bat 'python --version'
            }
        }
        stage('Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest tests/'
            }
        }
        stage('Docker Build') {
            steps {
                bat 'docker build -t iris-api .'
            }
        }
    }
}