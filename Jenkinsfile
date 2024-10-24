pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "datagen"
        DOCKER_REGISTRY = "mpfabio/datagen"
        WORKSPACE_UNIX = convertPathToUnixStyle(env.WORKSPACE)
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
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside("-w ${WORKSPACE_UNIX} -v ${WORKSPACE_UNIX}:${WORKSPACE_UNIX}") {
                        sh 'python -m unittest discover -s . -p "test_*.py"'
                    }
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}").push('latest')
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

def convertPathToUnixStyle(String path) {
    return path.replaceAll('C:', '/c').replaceAll('\\\\', '/')
}