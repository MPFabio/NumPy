pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "datagen"
        DOCKER_REGISTRY = "mpfabio/datagen"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/MPFabio/NumPy', credentialsId: 'github-credentials'
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
                    sh 'docker run --rm ${DOCKER_IMAGE} python -m unittest discover -s . -p "test_*.py"'
                }
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh 'echo "${DOCKER_PASSWORD}" | docker login -u ${DOCKER_USER} --password-stdin'
                        sh 'docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}:latest'
                        sh 'docker push ${DOCKER_REGISTRY}:latest'
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker system prune -f'
                }
            }
        }
    }
}