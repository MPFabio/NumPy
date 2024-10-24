pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "datagen"
        DOCKER_REGISTRY = "mpfabio/datagen"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code from GitHub...'
                git branch: 'master', url: 'https://github.com/MPFabio/NumPy', credentialsId: 'github-credentials'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests inside the Docker container...'
                bat 'docker run --rm %DOCKER_IMAGE% python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-pat', variable: 'DOCKER_PAT')]) {
                    echo 'Using Docker PAT to login...'
                    bat "echo %DOCKER_PAT% | docker login -u mpfabio --password-stdin"
                    bat 'docker tag %DOCKER_IMAGE% %DOCKER_REGISTRY%:latest'
                    bat 'docker push %DOCKER_REGISTRY%:latest'
                }
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up Docker images...'
                bat 'docker system prune -f'
            }
        }
    }
}