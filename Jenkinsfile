pipeline {
    agent any
    stages {
        stage('Checkout Source') {
            steps {
                git ''
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build name + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.withRegistry( "" ) {
                        dockerImage.inside() {
                            parallel {
                                stage("Unit Test") {
                                    steps {
                                        sh 'pytest -vvv'
                                    }
                                }
                                stage("Functional Test") {
                                    steps {
                                        sh 'pytest -vvv'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

    }

}