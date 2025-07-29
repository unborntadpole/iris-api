pipeline {
    agent any
      stages {
    stage('Setup') {
      steps {
        sh 'export PATH="/opt/homebrew/bin:$PATH" && python3 --version'
        sh 'python3 --version'
        sh 'python3 -m pip install -r requirements.txt'
        sh 'python3 iris_model.py'
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
        sh 'export PATH="/opt/homebrew/bin:$PATH" && docker build -t iris-fastapi-app .'
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
