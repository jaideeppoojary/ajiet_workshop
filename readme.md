## Setup 
1. Download docker https://www.docker.com/products/docker-desktop/

2. Install mini conda https://www.anaconda.com/download/success#miniconda

3. `conda env create --prefix ./venv -f environment.yml`

4. `conda activate ./venv`

5. `pip install -r requirements.txt`

## Other commands
* Run Streamlit app using `streamlit run app.py`
* Ollama 
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```


* `docker exec -it ollama bash`

* `ollama run qwen2.5:0.5b`


* Open web UI
```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```