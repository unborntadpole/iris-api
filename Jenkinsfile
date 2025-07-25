pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                bat '"C:\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat '"C:\\Python311\\python.exe" -m pytest tests/'
            }
        }
        stage('Docker Build') {
            steps {
                bat 'docker build -t iris-api .'
            }
        }
    }
}