pipeline {
  agent any

  stages {
    stage('Setup') {
      steps {
        bat 'python3 --version'
        bat 'pip3 install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        bat 'pytest tests/'
      }
    }
  }
}
