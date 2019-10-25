## Changonition! Una api rest para face recognition

para correr: \
     ./manage.py runserver \
\
modelos (JSON): \
        person: \
        { \
          "id" : "ID DE PESONA" \
          "face" : "Cara en base64" (max 500000 caracteres) \
        } \
\ 
        get_index: \
        { \
          "face" : "Cara en base64" cara a encontrar \
        } \
\
endpoints: \

	http://127.0.0.1:8000/changonition/api/v1/person/ (GET, POST, DELETE, PUT) ABM Persona \
	http://127.0.0.1:8000/changonition/api/v1/person/get_index/ (POST) devuelve el ID de la cara si se encontro o -1 si no \ 

