# How to set up a continuous deployment pipeline on AWS for a containerized Python web app deployed on Elastic Beanstalk?

## Abstract
Tutorial that explains the steps to create a continuous deployment pipeline using AWS Pipeline service. 
This tutorial is specifically intended for a Docker containerized Python web app deployed on Elastic Beanstalk.

## Pre-requisites
Prior to set up a CI/CD pipeline, you must

- Create a Bitbucket repository with the Python script of the web app
- Create a Docker image for you web app
- Deploy your web app on Elastic Beanstalk

## Why do we need a continuous deployment pipeline
You successively deployed your web app using Elastic Beanstalk? Congrats 🎉  
Then your manager asks you to add new features. 

So back to work…

Once you’re happy with your local version, you follow theses steps:

- Push the code on remote repository.
- Build the Docker image and push to ECR
- Redeploy your web app using Beanstalk

Could it be easier? Yes 👍 Using a continuous deployment pipeline, the build and deployment stages can be done automatically after you push your code on the remote repository.

## Continuous deployment pipeline architecture
The pipeline can be divided into three steps:

1. Source: git repository that hosts the project
2. Build
3. Deployment

![](figures/pipeline_architecture.png)

