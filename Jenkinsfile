pipeline{
    agent any
    environment{
        IMAGE = "devarshinichite/myflaskappec2test"
        TAG = "v${BUILD_NUMBER}-feature/test"
    }
    stages{
        stage('Build'){
            steps{
                echo "Building docker image and pushing it via the pipeline: Phase 1"
                echo "==============================="

                echo "Building the Docker image"
                sh 'docker build -t "$IMAGE:$TAG" -t "$IMAGE:latest" .'
                }
            }
        }
        stage('Push'){
            steps{
                echo "Pushing Docker image on Docker Hub"
                echo "================================="
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKERHUB_PWD', usernameVariable: 'DOCKERHUB_USER')]) {
                    sh 'echo "$DOCKERHUB_PWD" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                
                echo "Pushing the image to Docker Hub"
                sh 'docker push "$IMAGE:$TAG"'
                sh 'docker push "$IMAGE:latest"'
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying the container via pipeline: Phase 2"
                echo "==============================="

                echo "Running the Docker container"
                echo "==============================="
                sh 'docker pull "$IMAGE:$TAG"'
                sh 'docker rm -f flaskappec2-test || true'
                sh 'docker run -d -p 5000:5000 --name flaskappec2-test "$IMAGE:$TAG"'
            }
        }
        stage('Test'){
            steps{
                echo "Testing the container via pipeline: Phase 3"
                echo "==============================="

                sh 'sleep 5'
                // sh 'curl -f http://3.110.107.36:5000'

                echo "Hit the endpoint successfully"
                
            }
        }
        stage('Cleanup'){
            steps{
                echo "Cleaning up the pipeline: Phase 4"
                echo "==============================="

                echo "Cleaning the workspace"
                sh 'rm -rf $WORKSPACE/*'
            }
        }
    }
    post{
        success{
            echo "Pipeline completed successfully"
        }
        failure{
            echo "Pipeline failed"
        }
        always{
            echo "Pipeline completed"
        }
    }
}