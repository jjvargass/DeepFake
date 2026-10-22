# 03 Reenactment / Recreaciones

**Video resultado:**
[https://www.youtube.com/watch?v=SnKEcVQ4m3k](https://www.youtube.com/watch?v=SnKEcVQ4m3k)

![imagen-01.png](03-Reenactment_Recreaciones-img/imagen-01.png)

**Video tutorial Instalación en  linux:** 
[https://www.youtube.com/watch?v=SenfNiDKbCM&t=324s](https://www.youtube.com/watch?v=SenfNiDKbCM&t=324s)

**Video tutorial de instalación en Windows:** [https://www.youtube.com/watch?v=361oR2Yc9EE&t=1481s](https://www.youtube.com/watch?v=361oR2Yc9EE&t=1481s)

# Instalación

Repo GIT:

[https://github.com/KwaiVGI/LivePortrait](https://github.com/KwaiVGI/LivePortrait)

Clonamos repo


```bash
git clone https://github.com/KwaiVGI/LivePortrait
cd LivePortrait
```

Creamos entorno virtual


```bash
# create env using conda
conda create --prefix ./env-livePortrait python=3.10

# **Activamos** env
conda activate .\env-livePortrait\
```

![imagen-02.png](03-Reenactment_Recreaciones-img/imagen-02.png)

Configurar repositorios de conda


```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install ffmpeg
```

![imagen-03.png](03-Reenactment_Recreaciones-img/imagen-03.png)

Validar versión de CUDA


```bash
nvcc -V # example versions: 11.1, 11.8, 12.1, etc.
```

## Instalación para CUDA 11.8

![imagen-04.png](03-Reenactment_Recreaciones-img/imagen-04.png)

**Para CUDA 11.8**


```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```

![imagen-05.png](03-Reenactment_Recreaciones-img/imagen-05.png)

Instalar los requerimientos del repo


```bash
pip install -r requirements.txt
```

Ajustes librerías


```bash
pip uninstall gradio gradio_client -y
pip install gradio==4.44.1 gradio-client==1.3.0
pip install pydantic==2.10.6
```

## Instalación para CUDA 12.8

![imagen-06.png](03-Reenactment_Recreaciones-img/imagen-06.png)

**Para CUDA 12.8**


```bash
pip install torch torchvision torchaudio --index-url https:*//download.pytorch.org/whl/cu128*
```

Ajustes librerías


```bash
pip uninstall gradio gradio_client -y
pip install gradio==4.43.0 gradio_client==1.3.0
pip install --force-reinstall "pydantic==2.10.6"
```

Instalar los requerimientos del repo


```bash
pip install -r requirements.txt
```

## Descargar modelos

Descarga los modelos compartidos desde Google Drive y copia en la carpeta **pretrained_weights **ubicada en el directorio raíz del repositorio.

![imagen-07.png](03-Reenactment_Recreaciones-img/imagen-07.png)

Descargando de Google Drive

![imagen-08.png](03-Reenactment_Recreaciones-img/imagen-08.png)

Pegando en la carpeta

![imagen-09.png](03-Reenactment_Recreaciones-img/imagen-09.png)

# Ejecutar App


```bash
python .\app.py --share
```

# Ejecutar desde Terminal


```bash
# source input is an image
python inference.py -s assets/examples/source/s9.jpg -d assets/examples/driving/d0.mp4
```

![imagen-10.png](03-Reenactment_Recreaciones-img/imagen-10.png)

![imagen-11.png](03-Reenactment_Recreaciones-img/imagen-11.png)
