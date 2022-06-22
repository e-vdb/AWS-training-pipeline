# How to create a continuous deployment pipeline on AWS for a containerised Python web app deployed on Elastic Beanstalk?

## Summary
Tutorial that explains the steps to create a continuous deployment pipeline using AWS Pipeline service.
This tutorial is specifically intended for a Docker containerised Python web app deployed on Elastic Beanstalk.

## Pre-requisite

- Tutorial: Deployment of a Docker containerised Python web app using Elastic Beanstalk.

## Main steps

Steps 1 -> 7 from tutorial on Elastic Beanstalk 
1. Create a git repository to store the project
2. Write the python script in main.py
3. List the dependencies in requirements.txt
4. Write a Dockerfile to build the container
5. Create a container registry on AWS ECR
6. Build and push the Docker image on ECR
7. Deploy the app on Elastic Beanstalk Application
8. Create a Pipeline on AWS

## Detailed instructions for the pipeline creation

## References

- https://aws.amazon.com/fr/getting-started/hands-on/continuous-deployment-pipeline/
- https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
- https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.artifacts.files
- https://stackoverflow.com/questions/41090723/error-in-aws-codepipeline-when-deploying-elasticbeanstalk
- https://avishayil.medium.com/deploy-to-elastic-beanstalk-using-bitbucket-pipelines-189eb75cf052
- https://levelup.gitconnected.com/create-pipeline-to-push-docker-image-to-ecr-deploy-containerised-app-to-elastic-beanstalk-e721af796f33
