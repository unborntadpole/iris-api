pipeline {
  agent any

  stages {
    stage('Setup') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest tests/'
      }
    }
  }
}
