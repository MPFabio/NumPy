pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "datagen"
        DOCKER_REGISTRY = "docker.io/mpfabio/datagen"
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
                        sh 'docker run --rm ${DOCKER_IMAGE} python -m unittest discover -s . -p "test_*.py"'
                    } else {
                        bat 'docker run --rm %DOCKER_IMAGE% python -m unittest discover -s . -p "test_*.py"'
                    }
                }
            }
        }

        stage('Push') {
            steps {
                withCredentials([
                    usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD'),
                    string(credentialsId: 'docker-token', variable: 'DOCKER_TOKEN')
                ]) {
                    script {
                        if (isUnix()) {
                            sh 'echo "${DOCKER_PASSWORD}" | docker login -u ${DOCKER_USER} --password-stdin'
                            sh 'docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}:${DOCKER_IMAGE}'
                            sh 'echo ${DOCKER_TOKEN} | docker login --username ${DOCKER_USER} --password-stdin'
                            sh 'docker push ${DOCKER_REGISTRY}:${DOCKER_IMAGE}'
                        } else {
                            bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USER% --password-stdin'
                            bat 'docker tag %DOCKER_IMAGE% %DOCKER_REGISTRY%:%DOCKER_IMAGE%'
                            bat 'echo %DOCKER_TOKEN% | docker login --username %DOCKER_USER% --password-stdin'
                            bat 'docker push %DOCKER_REGISTRY%:%DOCKER_IMAGE%'
                        }
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