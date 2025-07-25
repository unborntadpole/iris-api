pipeline {
    agent {
        docker {
            image 'python:3.11-slim'       // Choose your base image
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Optional: allows building containers from within
        }
    }

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t iris-api .'
            }
        }
    }
}