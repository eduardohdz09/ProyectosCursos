# Tarea 1 de la clase 2 - Archivo .gitignore

  

## Introducción 🚀

  

> En la clase 2 del curso de revisó la funcionalidad del archivo .gitignore con la finalidad de ignorar archivos no relevantes o demasiado pesados en nuestro repositorio.

## Desarrollo de la actividad 🔧
> Realizar un archivo .gitignore con la finalidad de ignorar los archivos dentro del repositorio **venv** y la extensión **.mp3**.
> 
> 1. Indagamos dentro de la documentación del archivo .gitignore las sintaxis para ignorar directorios y extensión de archivos.
> 
>| Pattern |Example Matches  |Explanation|
>|--|--|--|
>|  logs/| logs/debug.log | Appending a slash indicates the pattern is a directory. The entire contents of any directory in the repository matching that name – including all of its files and subdirectories – will be ignored|
>|*.log|debug.log|An asterisk is a wildcard that matches zero or more characters.| 
>
>Para mayor detalle, consultar el [siguiente enlace](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)
>
>2. Realizamos el archivo .gitignore (se creó en la raiz) y escirbimos las siguientes líneas:
>*venv/* - ignorar los archivos dentro del directorio **venv**.
>**.mp3* - ignorar los archivos con extensión .mp3.
## Autores ✒️


>  - Eduardo Hernández
