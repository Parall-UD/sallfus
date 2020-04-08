# sallfus
## Descripción

La fusión de imágenes satelitales es un proceso digital que permite reunir en una imagen procesada la riqueza espectral de una imagen multiespectral y la resolución espacial de una imagen pancromática. Para llevar esto a cabo se cuenta con algunas transformaciones ya establecidas previamente, como lo son la Transformada de Brovey, Transformada Multiplicative, Transformada por análisis de componentes principales y la Transformada Á Trous, entre otras. 

Cada una de las distintas técnicas empleadas en la fusión de imágenes satelitales, presentan un conjunto distinto y variado de paso a seguir. No obstante, presentan dos similitudes. La primera de ellas, hace referencia a su propósito, es decir, estas técnicas buscan enriquecer espacialmente una imagen que contenga información espectral. El segundo aspecto, está relacionado con el tipo de operaciones que se realizan, puesto que, en la mayoría de casos son operaciones matriciales, donde a medida que aumenta el tamaño de dicha matriz se eleva es costo computacional.

Al implementar los algoritmos de fusión de imágenes satelitales en forma serial, es decir, realizando su ejecución exclusivamente en CPU, se presentan tiempos elevados al utilizar imágenes de dimensiones superiores, es por esto que este proyecto busca realizar la implementación de las transformadas mencionadas anteriormente mediante procesamiento heterogéneo CPU/GPU con el fin de optimizar los tiempos de ejecución para este algoritmo. Así mismo, se tiene como objetivo proporcionar herramientas para la comparación en términos de tiempos de ejecución y evaluación de la calidad de la imagen obtenida. 


## Manual de Usuario

El manual de usuario realizado para esta librería, tiene como finalidad presentar la interacción paso a paso entre el usuario y sus distintas funcionalidades. El manual de usuario se encuentra disponible en la siguiente dirección : https://github.com/Parall-UD/sallfus/blob/master/documentation/ManualUsuarioSallfus.pdf

## Manual Técnico

El manual técnico realizado para esta aplicación, tiene como finalidad presentar el proceso de instalación para la librería y sus distintas dependencias. El manual técnico se encuentra disponible en la siguiente dirección : https://github.com/Parall-UD/sallfus/blob/master/documentation/ManualTecnicoSallfus.pdf

## Especificación de Requisitos de Software
Este documento es una Especificación de Requisitos Software (ERS) para la librería llamado “Sallfus”. Esta especificación se ha estructurado basándose en las directrices dadas por el estándar IEEE Práctica Recomendada para Especificaciones de Requisitos Software ANSI/IEEE 830, 1998. Este documento se encuentra disponible en la siguiente dirección : https://github.com/Parall-UD/sallfus/blob/master/documentation/IEEE-830Sallfus.pdf

## Video Tutorial
Con el fin de presentar detalladamente el funcionamiento de la librería, se realizó un video tutorial donde se presenta la interacción entre el usuario y cada una de las funciones que pertencen a esta. El video tutorial se encuentra disponible en la siguiente dirección: 
