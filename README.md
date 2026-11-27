# jenkins-practice

This is a Jenkins practice lab repo.

## What is Jenkins?

Jenkins is an automation and orchestration tool used in software development. Previously/traditionally in software development, all of the review, testing, deployment, integration, etc., were done manually, which created unnecessary delays in the development and delivery of software.

After CI/CD and Jenkins:

It helps create a workflow for software implementation continuously without any manual human intervention for doing such tedious and repetitive tasks. In production, it acts as a single source of truth for continuous implementation and deployment/delivery. Teams would be using the same Jenkins infrastructure for software deployment.

## What is CI/CD?

CI - Continuous Integration.

CD - Continuous Delivery/Deployment.

In software development, CI/CD is the process of shipping new code and deploying it in a continuous flow. It emphasizes the basics of the SDLC (Software Development Life Cycle), i.e., Testing, Deployment, and Maintenance.

### Delivery vs Deployment?

There isn't any huge difference between either of those. The only difference is in the delivery strategy of software.

In Continuous Delivery - Human intervention is needed, where a Team Lead/Project Manager gives the final green flag after checking all previous workflows and showcasing the product to a client, before giving the final go-ahead to deploy it to production.

Whereas, Deployment doesn't require any human intervention or green flags. It automatically deploys onto a production system after all previous CI/CD workflows and final checks have been successfully completed.

---
## Technologies, Environment & Tools:
- AWS EC2 ***(c7i.large)***
- Python ***(Flask, pysonar, pytest, pytest-cov, coverage.py, unittest)***
- Jenkins ***(Freestyle, Pipeline & Multi-Pipeline w/PollSCM, Webhooks)***
- Git, Github
- SonarQube CE
- PostgreSQL
- Docker (EC2 and Local)
- GitHub Codespace

---
# Work in Progress
## Strategy
- Green/Blue
- Canary
