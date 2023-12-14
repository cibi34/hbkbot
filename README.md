# hbkbot

hbkbot is a toolkit which lets you
* create embeddings and vector databases
* using a offline and local chatbot in browser
* using open source models and llms

## Installation (Windows PowerShell)

Make sure you have installed Python 3.11 and "Python" is in your environment variables

1. Clone the repository 
2. Navigate to the root folder 'hbkbot/'
3. Create virtual env  
    ```powershell 
    python -m venv venv
    ```
4. Windows PS only to get authorization for venv
    ```powershell
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```
5. Activate venv
   ```powershell
    .\venv\Scripts\Activate.ps1
    ```
    Make sure "(venv)" is now your scope and shows at the beginning of the line
6. Upgrade pip
    ```powershell 
    python.exe -m pip install --upgrade pip
    ```
7. Install requirements
    ```powershell 
    pip install -r .\requirements.txt
    ```
8. Download your models (eg. [cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer))
    ```powershell 
    cd .\models\transformer\ 
    git lfs install

    git clone https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer

    ```

9. Start GUI (go back to hbkbot/)
    ```powershell 
    streamlit run .\web\prep_files.py 
    ```