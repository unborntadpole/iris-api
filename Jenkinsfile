pipeline {
  agent any

  stages {
    stage('Setup') {
      steps {
        bat 'python --version'
        bat 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        bat 'pytest tests/'
      }
    }
  }
}
