pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-v $HOME/.cache/pip:/root/.cache/pip'
    }
  }

  environment {
    DOCKER_BUILDKIT = '1'
  }

  stages {
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest tests/ --disable-warnings'
      }
    }
    stage('Docker Build') {
      steps {
        sh 'docker build -t iris-api .'
      }
    }
  }
}