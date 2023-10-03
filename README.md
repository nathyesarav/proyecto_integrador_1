# Api Proyecto Integrador 1 Henry
El presente proyecto presenta el desarrollo de una APP para Steam.
Inicialmente se requirió de un preprocesamiento de los datos proporcionados, que se detalla en el notebook en la carpeta "clean" llamado Proyecto_Integrador_1.ipynb

Se generaron cinco archivos CSV con los datos procesados, que se usaron en la implementación de una API desplegada en Render con la URL:
https://api-2kri.onrender.com/docs

Los métodos implementados son los siguientes:

https://api-2kri.onrender.com/sentiment_analysis/2011

/playtimegenre/{genre}: Devuelve año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

/userforgenre/{genre}: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

/usersrecommend/{year}: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

/usersnotrecommend/{year}: Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

/sentiment_analysis/{year}: Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

/recomendacion_juego/{id}: Un modelo de recomendación con una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la similitud del coseno.
Ejemplo de retorno: [49, 64, 86, 2077, 2164]

## Requisitos

Los requisitos están en el archivo requirements.txt

## Instalación
pip install -r requirements.txt
