pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u root'
    }
  }

  stages {
    stage('Test') {
      steps {
        sh 'python --version'
        sh 'pytest tests/'
      }
    }
  }
}
