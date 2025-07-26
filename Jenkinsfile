pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
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

    stage('Ping API') {
        steps {
            bat 'python ping_api.py'
        }
    }
    
    stage('Cleanup') {
        steps {
            bat 'timeout /t 5'
            bat 'for /f %i in (\'docker ps -q\') do docker stop %i || echo Container not running'
            bat 'for /f %i in (\'docker ps -aq\') do docker rm %i || echo Container not found'
        }
    }
  }
}
