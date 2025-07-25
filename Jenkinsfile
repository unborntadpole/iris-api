pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
    }
  }
  stages {
    stage('Debug') {
      steps {
        sh 'echo $SHELL'
        sh 'python --version'
      }
    }
  }
}
