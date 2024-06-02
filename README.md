This  repository unifies three separate repositories of mine :  

- Spring backend repo : https://github.com/aszilard99/ai-health-backend
- Flask server with a Tensorflow CNN : https://github.com/aszilard99/py_pred_server
- Next.js frontend : https://github.com/aszilard99/ai-health-frontend

This application allows the classification of brain magnetic resonance images into healthy and tumorous categories. It has a Next.js frontend with NextUI and D3 library, a Spring backend and a Python Flask server which serves the Tensorflow CNN that was trained on the augmented version of this dataset: https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection

It can be run by a 'docker compose up' command locally, then the frontend can be accessed on http://localhost:3000
