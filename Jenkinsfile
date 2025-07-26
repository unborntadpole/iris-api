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
        bat 'python app/iris_model.py'
      }
    }

    stage('Test') {
      steps {
        bat 'python test/test_api.py'
      }
    }
  }
}
