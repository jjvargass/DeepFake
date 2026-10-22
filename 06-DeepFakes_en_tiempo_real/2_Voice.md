# 2.Voice

# 1) Instalación cambiador de voz

Ingresando al repositorio  [https://github.com/w-okada/voice-changer](https://github.com/w-okada/voice-changer)

![imagen-01.png](2_Voice-img/imagen-01.png)

Encontramos el link para descargamos el vccliente

![imagen-02.png](2_Voice-img/imagen-02.png)

Nos direcciona a este sitio [https://huggingface.co/wok000/vcclient000/tree/main](https://huggingface.co/wok000/vcclient000/tree/main)

Descargamos la versión más alta.

![imagen-03.png](2_Voice-img/imagen-03.png)

Este link nos direcciona a [https://huggingface.co/wok000/vcclient000/blob/main/MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.18a.zip](https://huggingface.co/wok000/vcclient000/blob/main/MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.18a.zip)  para descargar

![imagen-04.png](2_Voice-img/imagen-04.png)

1 Descargamos en el escritorio

2 Descomprimimos

3 Ejecutamos como administrador el programa

![imagen-05.png](2_Voice-img/imagen-05.png)

Se abren 2 ventanas las cuales no se deben cerrar, trabajaremos con la ventana número 2

![imagen-06.png](2_Voice-img/imagen-06.png)

## 1.1 Configurar entradas y salidas de audio

En la **input **seleccionamos el micrófono, con el que se cuenta.

**Output **debemos seleccionar el cable virtual “*que debe estar instalado*”.

Para fines de pruebas en **monitor **seleccionamos los audífonos o parlantes para escuchar la voz del personaje.

Pero para los ejercicios una vez testeado, dejar en none.

![imagen-07.png](2_Voice-img/imagen-07.png)

![imagen-08.png](2_Voice-img/imagen-08.png)

## 1.2 Configurar Ganancia de entrada y salida

La **GAIN  “ganancia” de entradas “in”**  si el micrófono suena muy suave se le puede subir para ganar audio de entrada.

para **GAIN OUT se recomienda en 2. **

![imagen-09.png](2_Voice-img/imagen-09.png)

## 1.3 Configurar Tune

Modifica el tono de la voz

Voz femenina o de niños de 10 en adelante.  10 a 18

voz masculinas y gruesas -10 a -18

![imagen-10.png](2_Voice-img/imagen-10.png)

## 1.4 Configurar INDEX

Es la terminación vocal de los personajes, no todos los modelos tiene

0,5 es ideal para que no suene robótico

![imagen-11.png](2_Voice-img/imagen-11.png)

## 1.5 Configurar supresores de ruido

![imagen-12.png](2_Voice-img/imagen-12.png)

Echo : suprime el eco

Sup1: suprime el ruido

Sup2: suprime los pop

## 1.6 Configura Método de conversión

Se recomienda el **creve** y si no funciona bien como segunda opción **harvest**

![imagen-13.png](2_Voice-img/imagen-13.png)

![imagen-14.png](2_Voice-img/imagen-14.png)

## 1.7 Configura delay compuerta de ruido

Lo que hace es que cuando dejamos de hablar, cierra el micrófono y deja un retardo, lo recomendado es dejarlo en** 0.**

![imagen-15.png](2_Voice-img/imagen-15.png)

## 1.8 Configura Fragmentos CHUNK

Son los fragmentos de información que le enviamos a la IA, depende de las capacidades de la tarjeta gráfica con la que cuente el pc.

Con 6 GB se puede dejar en **320**

![imagen-16.png](2_Voice-img/imagen-16.png)

## 1.9 Configura EXTRA

Si tienes una buena PC podría ser 131072

pero en el tuto 32768

![imagen-17.png](2_Voice-img/imagen-17.png)

## 1.10 Configura GPU

Debe salir su tarjeta gráfica, en mi caso este pc no tiene tarjeta grafica por eso sale cpu.

![imagen-18.png](2_Voice-img/imagen-18.png)

# 2) Repositorio de Voces

[https://voice-models.com/](https://voice-models.com/)

![imagen-19.png](2_Voice-img/imagen-19.png)

![imagen-20.png](2_Voice-img/imagen-20.png)

![imagen-21.png](2_Voice-img/imagen-21.png)

Servidor de discor

[https://discord.com/invite/aihub](https://discord.com/invite/aihub)

Un **epoch **implica un ciclo completo del conjunto de datos de entrenamiento que se compone de lotes e iteraciones del conjunto de datos, y el número de epoch necesarios para que un modelo se ejecute de manera eficiente se basa en los datos en sí y en el objetivo del modelo.

# 3) Instalación Cable virtual

![imagen-22.png](2_Voice-img/imagen-22.png)

Ingresamos a la pagina [https://vb-audio.com/Cable/](https://vb-audio.com/Cable/)

![imagen-23.png](2_Voice-img/imagen-23.png)

Ejecutamos como administrador.

![imagen-24.png](2_Voice-img/imagen-24.png)

![imagen-25.png](2_Voice-img/imagen-25.png)

![imagen-26.png](2_Voice-img/imagen-26.png)

## 3.1 Configurar output en cambiador de voces

Como ya tenemos instalado el cable virtual, en el voice change en la sección de AUDIO en la opción output seleccionamos el cable virtual

![imagen-27.png](2_Voice-img/imagen-27.png)

![imagen-28.png](2_Voice-img/imagen-28.png)

# Fuentes

[https://www.youtube.com/watch?v=M8FzJlKSHTQ](https://www.youtube.com/watch?v=M8FzJlKSHTQ)

[https://www.youtube.com/watch?v=iDbqspsWqZc](https://www.youtube.com/watch?v=iDbqspsWqZc)

# Alternativas

[https://www.youtube.com/watch?v=hcOMsLuOoCc](https://www.youtube.com/watch?v=hcOMsLuOoCc)

![imagen-29.png](2_Voice-img/imagen-29.png)

## Puesto #3

![imagen-30.png](2_Voice-img/imagen-30.png)

[https://www.youtube.com/watch?v=q4i68Uxcv8E](https://www.youtube.com/watch?v=q4i68Uxcv8E)

El principal problema es configurar la entrada y salida de audio si no son las misma el programa no inicia.

![imagen-31.png](2_Voice-img/imagen-31.png)

Ejemplo algunos dispositivos no tiene la misma terminación

![imagen-32.png](2_Voice-img/imagen-32.png)

Repo github

[https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

Video tutorial

[https://www.youtube.com/watch?v=TZ2odHFHOp0](https://www.youtube.com/watch?v=TZ2odHFHOp0)

![imagen-33.png](2_Voice-img/imagen-33.png)

Configuración Inicial

![imagen-34.png](2_Voice-img/imagen-34.png)
