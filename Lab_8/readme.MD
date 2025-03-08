# Laboratory Assignment 8

## Problem Statement 
This assignment focuses on data collection from social media platforms using APIs, text preprocessing, semantic vector embeddings, and clustering algorithms. You'll learn how to securely connect to external platforms, process unstructured text data, and apply advanced NLP techniques to identify similar content clusters.

## Video Demo Link
  TBD

## Technologies Used
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![PRAW](https://img.shields.io/badge/PRAW-FF4500?style=for-the-badge&logo=reddit&logoColor=white)](https://praw.readthedocs.io/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=fff)](https://www.mysql.com/)
[![NLTK](https://img.shields.io/badge/NLTK-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.nltk.org/)
[![Gensim](https://img.shields.io/badge/Gensim-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://radimrehurek.com/gensim/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

## How to run Application Locally
1. Clone the GitHub Project
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install python and the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your credentials (see `secrets_import.py` for format)
   ```ini
   [mysql]
   host=localhost
   user=YOUR_USERNAME
   password=YOUR_PASSWORD
   database=YOUR_DATABASE

   [reddit]
   client_id=YOUR_REDDIT_CLIENT_ID
   client_secret=YOUR_REDDIT_CLIENT_SECRET
   user_agent=YOUR_APP_NAME/1.0
   ```
4. Run the Jupyter notebook to analyze data
   ```sh
   jupyter notebook DSCI560_Lab8.ipynb
   ```

## Code details
1. **Data Collection from Reddit**: The `fetch_and_store_reddit_posts` function in the notebook collects posts from specified subreddits using the PRAW API.
2. **Text Preprocessing**: The `clean_text` function removes HTML, special characters, and stopwords from the collected text.
3. **Vector Embeddings**: Both Doc2Vec and Word2Vec models are implemented for generating semantic embeddings.
4. **Clustering Algorithms**: K-means clustering is applied to group similar posts based on their vector representations.
5. **Evaluation Metrics**: Silhouette scores and Davies-Bouldin indices are calculated to evaluate clustering quality.
6. **Visualization**: PCA and t-SNE techniques are used to visualize the clustering results.

## File Structure
- `DSCI560_Lab8.ipynb`: Main Jupyter notebook containing the code for data collection, processing, and analysis
- `config_setup_helper.py`: Helper functions to set up the database and Reddit API connection
- `secrets_import.py`: Handles secure loading of credentials
- `requirements.txt`: Python package dependencies
- `readme.MD`: This documentation file

## References

- [PRAW Documentation](https://praw.readthedocs.io/)
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [NLTK Documentation](https://www.nltk.org/)
- [Gensim Documentation](https://radimrehurek.com/gensim/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Lab 6 README](../Lab_6/README.md)
- [t-SNE Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
- [PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [K-means Clustering](https://scikit-learn.org/stable/modules/clustering.html#k-means)
