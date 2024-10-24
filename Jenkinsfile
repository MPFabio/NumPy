pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "DataGen"
        DOCKER_REGISTRY = "docker.io/mpfabio"
        DOCKER_USER = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/MPFabio/NumPy', credentialsId: 'github-credentials'
            }
        }
    }

        stage('Verify Tools') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'git --version'
                }
            }
        }

        
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker run --rm ${DOCKER_IMAGE} python -m unittest discover -s tests'
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} ${DOCKER_REGISTRY}'
                    sh 'docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest'
                    sh 'docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest'
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}
