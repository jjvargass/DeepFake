# Pestaña 1

# FACE

# 1) Instalación de Chocolatey

Correr como administrador consola de powerShell

![imagen-01.png](1_Face-img/imagen-01.png)

![imagen-02.png](1_Face-img/imagen-02.png)

Ingresamos a la página [https://chocolatey.org/](https://chocolatey.org/)  y click en instalar

![imagen-03.png](1_Face-img/imagen-03.png)

![imagen-04.png](1_Face-img/imagen-04.png)

Pegamos el comando en la terminal que se abrió como administrador

![imagen-05.png](1_Face-img/imagen-05.png)

Verificados la versión de chocolatey


```bash
choco -v
```

![imagen-06.png](1_Face-img/imagen-06.png)

# 2) Instalación de python

Está versión está conforme a la documentacion en deep live can en github en su tiempo

ahora es 3.11


```bash
PS **C**:\WINDOWS\system32> choco install python --version=3.10.0
```

![imagen-07.png](1_Face-img/imagen-07.png)

![imagen-08.png](1_Face-img/imagen-08.png)

cerrar la terminal y volver abrir como admin para validar la instalación de python


```bash
python --version
```

![imagen-09.png](1_Face-img/imagen-09.png)

# 3) Instalación de pip


```bash
python -m pip install --upgrade pip
```

![imagen-10.png](1_Face-img/imagen-10.png)


```bash
pip --version
```

# 4) Instalación de git


```bash
choco install git
```

![imagen-11.png](1_Face-img/imagen-11.png)

comprobamos la instalación, cerrando la terminal y abriendo de nuevo como admin


```bash
git --version
```

![imagen-12.png](1_Face-img/imagen-12.png)

# 5) Instalación ffmpeg


```bash
choco install ffmpeg
```

![imagen-13.png](1_Face-img/imagen-13.png)


```bash
ffmpeg -version
```

# 6) Instalación Visual Studio 2022 Runtimes (Windows)

En la documentación del github se encuentra el link para descargar el instalador de visual studio 2022 Runtimes [https://visualstudio.microsoft.com/es/visual-cpp-build-tools/](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/)

![imagen-14.png](1_Face-img/imagen-14.png)

Descargamos el instalador.

![imagen-15.png](1_Face-img/imagen-15.png)

Ejecutamos como administrador

![imagen-16.png](1_Face-img/imagen-16.png)

Click en continuar

![imagen-17.png](1_Face-img/imagen-17.png)

Esperamos que se descargue el instalador

![imagen-18.png](1_Face-img/imagen-18.png)

Luego tenemos este panel con distintas opciones.

![imagen-19.png](1_Face-img/imagen-19.png)

Seleccionamos Desarrollo para el escritorio C++ y luego click en instalar

![imagen-20.png](1_Face-img/imagen-20.png)

![imagen-21.png](1_Face-img/imagen-21.png)

![imagen-22.png](1_Face-img/imagen-22.png)

Cerramos pestaña y continuamos con  los siguientes pasos.

# 7) Instalación CUDA

Siguiendo las indicaciones de la siguiente página [https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html#install-windows](https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html#install-windows)

![imagen-23.png](1_Face-img/imagen-23.png)

## Paso 6.1: Tener los driver Actualizados

Para no tener que ir a buscarlos por la referencia y todo eso, se instala la **NVIDIA APP** en el siguiente link.  Se descarga e instala.

[https://www.nvidia.com/es-la/software/nvidia-app/](https://www.nvidia.com/es-la/software/nvidia-app/)

![imagen-24.png](1_Face-img/imagen-24.png)

Ejecutamos el instalador y saldrá está pantalla, seleccionamos los controladores para Studio ya que el propósito no es Jugar, si fuera este el caso, seleccionamos la otra opción.

![imagen-25.png](1_Face-img/imagen-25.png)

Click en descargar, para proceder a instalar.

![imagen-26.png](1_Face-img/imagen-26.png)

Este es el avance de la descarga

![imagen-27.png](1_Face-img/imagen-27.png)

luego cambia el botón en instalar

![imagen-28.png](1_Face-img/imagen-28.png)

![imagen-29.png](1_Face-img/imagen-29.png)

![imagen-30.png](1_Face-img/imagen-30.png)

![imagen-31.png](1_Face-img/imagen-31.png)

![imagen-32.png](1_Face-img/imagen-32.png)

## Paso 6.2: Seleccionar el CUDA  y cuDNN versiones específicas

Una vez instalada en la parte de Controladores, Podemos consultar qué versión se instaló. Está aplicación instala los driver y los mantiene actualizados.

![imagen-33.png](1_Face-img/imagen-33.png)

Una vez instalados los drivers, debemos seleccionar la versión de CUDA y el cuDNN en sus versiones compatibles . Según el repo de deep live cam se debe utilizar la versión de CUDA 11.8.0

![imagen-34.png](1_Face-img/imagen-34.png)

En el link de  indicaciones de la siguiente página  [https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html#install-windows](https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html#install-windows)  tenemos un link con la matrix de soporte de versiones de CUDA y cuDNN

![imagen-35.png](1_Face-img/imagen-35.png)

[https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/support-matrix.html](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/support-matrix.html)

![imagen-36.png](1_Face-img/imagen-36.png)

![imagen-37.png](1_Face-img/imagen-37.png)

Entonces CUDA 11.8 y cuDNN 9.8.0

## Paso 6.3: Instalar CUDA

descargamos CUDA Toolkit 11.8.0

[https://developer.nvidia.com/cuda-11-8-0-download-archive](https://developer.nvidia.com/cuda-11-8-0-download-archive)

![imagen-38.png](1_Face-img/imagen-38.png)

Ejecutamos el instalador.

![imagen-39.png](1_Face-img/imagen-39.png)

![imagen-40.png](1_Face-img/imagen-40.png)

![imagen-41.png](1_Face-img/imagen-41.png)

**Desmarcamos **las opciones **NVIDIA Geforce** y **Driver Compenents** porque ya se tienen instaladas con la** NVIDIA APP**, clic en siguiente.

![imagen-42.png](1_Face-img/imagen-42.png)

![imagen-43.png](1_Face-img/imagen-43.png)

El programa recomienda tener instalado Visual Studio, es importante tenerlo instalado y luego si realizar la instalación de CUDA. Pero nosotros ya realizamos este proceso.

![imagen-44.png](1_Face-img/imagen-44.png)

![imagen-45.png](1_Face-img/imagen-45.png)

![imagen-46.png](1_Face-img/imagen-46.png)

## Paso 6.4: Instalar cuNND

Descargamos el cuDNN formato zip de la versión específica para el CUDA.

Se debe contar con una cuenta o iniciar sesión con un correo para poder descargar

[https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive)

![imagen-47.png](1_Face-img/imagen-47.png)

Una vez que se haya descargado el archivo cuDNN (archivo .zip), extraiga su contenido en una ubicación conveniente en su sistema. Encontrará varios archivos y directorios dentro del paquete cuDNN, incluidos los directorios bin, include y lib. Navegue hasta el directorio donde instaló CUDA Toolkit (por ejemplo, C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8).

Copie el contenido del directorio bin desde el archivo cuDNN al directorio bin correspondiente en la ruta de instalación de CUDA Toolkit.

De manera similar, copie el contenido del directorio include al directorio include en la ruta de instalación de CUDA Toolkit.

Finalmente, copie el contenido del directorio lib al directorio lib en la ruta de instalación de CUDA Toolkit.

![imagen-48.png](1_Face-img/imagen-48.png)

Las variables se encuentra de está manera

![imagen-49.png](1_Face-img/imagen-49.png)

Creamos la variable CUDNN

**Actualización: solo se configurará en variables del sistema **

![imagen-50.png](1_Face-img/imagen-50.png)

Ahora agregamos CUDA_PATH como variable de para el admin.

![imagen-51.png](1_Face-img/imagen-51.png)

Agregamos a la variable Path del administrador  y también al path del sistema  las siguiente rutas:

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib\x64

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp

Variable Path del ADMIN original

![imagen-52.png](1_Face-img/imagen-52.png)

Quedando de la siguiente manera

![imagen-53.png](1_Face-img/imagen-53.png)

Variable Path del SISTEMA

![imagen-54.png](1_Face-img/imagen-54.png)

Revisar información de instalación


```bash
nvidia-smi
```

Muestra la **versión del driver de NVIDIA** que está instalada, y además indica la **versión máxima de CUDA** que ese driver **soporta**.

![imagen-55.png](1_Face-img/imagen-55.png)

Este comando viene del **CUDA Toolkit**, y muestra la **versión del compilador nvcc**, es decir, la **versión real del toolkit** que tienes instalado.


```bash
nvcc -V
```

![imagen-56.png](1_Face-img/imagen-56.png)

![imagen-57.png](1_Face-img/imagen-57.png)

# 8) Clonar Repositorio


```bash
mkdir git 

cd git

git clone https://github.com/hacksider/Deep-Live-Cam.git
```

![imagen-58.png](1_Face-img/imagen-58.png)

## 8.1) Descargar los Modelos

![imagen-59.png](1_Face-img/imagen-59.png)

[https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth](https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth)

[https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx)

Descargamos los modelos y los pegamos la carpeta models del repositorio Deep-Live-Cam

![imagen-60.png](1_Face-img/imagen-60.png)

Pegado

![imagen-61.png](1_Face-img/imagen-61.png)

## 8.2) Instalar Dependencias python

Entramos a la página del repositorio


```bash
PS C:\Users\virtual\git> cd .\Deep-Live-Cam\
```

![imagen-62.png](1_Face-img/imagen-62.png)

### Creamos entorno virtual


```bash
PS C:\Users\virtual\git\Deep-Live-Cam> py -m venv env-livecam
```

![imagen-63.png](1_Face-img/imagen-63.png)

### Activamos en env.


```bash
PS C:\Users\virtual\git\Deep-Live-Cam> .\env-livecam\Scripts\activate
```

![imagen-64.png](1_Face-img/imagen-64.png)

### Actualizamos en el env las librerías


```bash
(env-livecam) PS C:\Users\virtual\git\Deep-Live-Cam> pip install --upgrade pip setuptools wheel
```

![imagen-65.png](1_Face-img/imagen-65.png)

Si se obtiene este error,

![imagen-66.png](1_Face-img/imagen-66.png)

Cerramos la terminal y la volvemos abrir como admin ejecutamos el env

![imagen-67.png](1_Face-img/imagen-67.png)

El error indica que se debe habilitar la ejecución de script en la terminal, para habilitar:


```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Actualizamos la librerías

![imagen-68.png](1_Face-img/imagen-68.png)

Finalmente se instalan las librerías python


```bash
(env-livecam) PS C:\Users\virtual\git\Deep-Live-Cam> pip install -r requirements.txt
```

### GPU Acceleration


```bash
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.16.3
```

# 9) Ejecutar Deep live cam


```bash
python run.py --execution-provider cuda
```

# 10) Configurar Camara virtual

![imagen-69.png](1_Face-img/imagen-69.png)

![imagen-70.png](1_Face-img/imagen-70.png)

![imagen-71.png](1_Face-img/imagen-71.png)

![imagen-72.png](1_Face-img/imagen-72.png)

![imagen-73.png](1_Face-img/imagen-73.png)

![imagen-74.png](1_Face-img/imagen-74.png)

Organizamos para todo el tamaño de la ventana

![imagen-75.png](1_Face-img/imagen-75.png)

![imagen-76.png](1_Face-img/imagen-76.png)

Configuración en aplicación objetivo. “teams”

![imagen-77.png](1_Face-img/imagen-77.png)

# [Actualización] Instalar la última versión

Descargar nuevo modelo

[https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view)

![imagen-78.png](1_Face-img/imagen-78.png)

y ajustar un script para poder ejecutar

![imagen-79.png](1_Face-img/imagen-79.png)

![imagen-80.png](1_Face-img/imagen-80.png)

![imagen-81.png](1_Face-img/imagen-81.png)



# 11) Fuentes

Chocolatey

[https://www.youtube.com/watch?v=HdPGGhM1C0A&t=630s](https://www.youtube.com/watch?v=HdPGGhM1C0A&t=630s)

Instalar Deep Live Cam

[https://www.youtube.com/watch?v=py4Tc-Y8BcY](https://www.youtube.com/watch?v=py4Tc-Y8BcY)

Instalar CUDA y cuDNN

[https://medium.com/@gokulprasath100702/a-guide-to-enabling-cuda-and-cudnn-for-tensorflow-on-windows-11-a89ce11863f1](https://medium.com/@gokulprasath100702/a-guide-to-enabling-cuda-and-cudnn-for-tensorflow-on-windows-11-a89ce11863f1)

[https://builtin.com/articles/cudnn-download](https://builtin.com/articles/cudnn-download)

[https://www.youtube.com/watch?v=DrEuKFnv8K0&t=149s](https://www.youtube.com/watch?v=DrEuKFnv8K0&t=149s)

