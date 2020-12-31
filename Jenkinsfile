pipeline {
    environment {
        registry = 'https://registry.hub.docker.com/'
        name = 'chitrankdixit/sideeffect'
        dockerImage = 'chitrankdixit/sideeffect'
    }
    agent any
    stages {
        stage('Checkout Source') {
            steps {
                git 'https://github.com/Chitrank-Dixit/comedian.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build name + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Code Analysis') {
            parallel {
                stage("Flake8") {
                    steps {
                        script {
                            docker.withRegistry( "" ) {
                                dockerImage.inside() {
                                    sh 'flake8 .'
                                }
                            }
                        }
                    }
                }

                stage("black") {
                    steps {
                        script {
                            docker.withRegistry( "" ) {
                                dockerImage.inside() {
                                    sh 'black --check --diff .'
                                }
                            }
                        }
                    }
                }
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Test') {
                  steps {
                    script {
                      docker.withRegistry( "" ) {
                        dockerImage.inside() {
                          sh 'pytest tests/unit/ -vvv'
                        }
                      }
                    }
                  }
                }

                stage('Functional Test') {
                  steps {
                    script {
                      docker.withRegistry( "" ) {
                        dockerImage.inside() {
                          sh 'pytest tests/functional -vvv'
                        }
                      }
                    }
                  }
                }
            }
        }
    }

}