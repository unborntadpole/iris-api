pipeline {
  agent any

  stages {
    stage('Setup') {
      steps {
        powershell 'python --version'
        powershell 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        powershell 'pytest tests/'
      }
    }
  }
}
