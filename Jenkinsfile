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

        stage('Verify Tools') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker --version'
                        sh 'git --version'
                    } else {
                        bat 'docker --version'
                        bat 'git --version'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t ${DOCKER_IMAGE} .'
                    } else {
                        bat 'docker build -t %DOCKER_IMAGE% .'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm ${DOCKER_IMAGE} python -m unittest discover -s tests'
                    } else {
                        bat 'docker run --rm %DOCKER_IMAGE% python -m unittest discover -s tests'
                    }
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} ${DOCKER_REGISTRY}'
                        sh 'docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest'
                        sh 'docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest'
                    } else {
                        bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASSWORD% %DOCKER_REGISTRY%'
                        bat 'docker tag %DOCKER_IMAGE% %DOCKER_REGISTRY%/%DOCKER_IMAGE%:latest'
                        bat 'docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE%:latest'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                if (isUnix()) {
                    sh 'docker system prune --filter "until=24h" -f'
                } else {
                    bat 'docker system prune --filter "until=24h" -f'
                }
            }
        }
    }
}
