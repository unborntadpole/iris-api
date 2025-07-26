    pipeline {
        agent any
        environment {
            PATH = "C:\\\\Windows\\\\System32;${env.PATH}"
        }
        stages {
            stage('Run Command') {
                steps {
                    bat 'echo Hello from cmd!'
                }
            }
        }
    }
