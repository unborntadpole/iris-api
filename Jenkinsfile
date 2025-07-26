pipeline {
    agent any
    environment {
        PATH = "C:\\\\Windows\\\\System32;${env.PATH}"
        PATH = "C:\\\\Program Files\\\\Docker\\\\Docker\\\\resources\\\\bin;${env.PATH}"
    }
      stages {
    stage('Setup') {
      steps {
        bat 'python --version'
        bat 'pip install -r requirements.txt'
        bat 'python iris_model.py'
      }
    }

    stage('Test') {
      steps {
        bat 'python test_api.py'
      }
    }

    stage('Docker Build') {
      steps {
        bat 'docker build -t iris-fastapi-app .'
      }
    }

    stage('Docker Run') {
      steps {
        bat 'docker run -d -p 8000:8000 iris-fastapi-app'
      }
    }
  }
}
