pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }
      stages {
    stage('Setup') {
      steps {
        sh 'python --version'
        sh 'pip install -r requirements.txt'
        sh 'python iris_model.py'
      }
    }

    stage('Test') {
      steps {
        sh 'python3 test_api.py'
      }
    }

    stage('Docker Build') {
      steps {
        sh 'docker build -t iris-fastapi-app .'
      }
    }

    stage('Docker Run') {
      steps {
        sh 'docker run -d -p 8000:8000 iris-fastapi-app'
      }
    }

    // stage('Ping API') {
    //     steps {
    //         sh 'python ping_api.py'
    //     }
    // }
    
    // stage('Cleanup') {
    //     steps {
    //         sh 'ping -n 6 127.0.0.1 >nul'
    //         sh 'for /f %i in (\'docker ps -q\') do docker stop %i || echo Container not running'
    //         sh 'for /f %i in (\'docker ps -aq\') do docker rm %i || echo Container not found'
    //     }
    // }
  }
}
