# MNIST Classifier CI & CD

| Github Action + ArgoCD


CI (Github Action)

- `trigger`: Source Code Push
- Train Code Dockerize
- Ed
- 학습 코드 Dockerize
- training Job (model 파일을 저장)

CD (Github Action + ArgoCD)

- `trigger`: CI Success
- BentoML Dockerize (Inference code & load model)
- 서빙용 Deployment & 서비스 실행
