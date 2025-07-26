pipeline {
    agent any
    environment {
        PATH = "C:\\\\Windows\\\\System32;${env.PATH}"
    }
      stages {
    stage('Setup') {
      steps {
        bat 'python --version'
        bat 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        bat 'python .\test\test_api.py'
      }
    }
  }
}
