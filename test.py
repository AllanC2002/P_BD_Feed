import redis
import json

# Conexión al servidor Redis (ajusta IP y contraseña si es necesario)
r = redis.Redis(
    host='18.209.242.168',  # tu IP pública del servidor
    port=6379,
    password='1716983349',  # si le pusiste contraseña
    decode_responses=True  # para trabajar con strings
)

# Supongamos que este usuario sigue a otros y ve este feed
user_id = 12
feed_key = f"feed:user:{user_id}"

# Publicaciones de ejemplo
post1 = {
    "Id_publication": "68576f513ac5b69dd669e328",
    "Text": "Primera publicación de ejemplo.",
    "Multimedia": "",
    "Datepublish": "2025-06-22T02:49:53.342+00:00"
}
post2 = {
    "Id_publication": "685770e13ac5b69dd669e44b",
    "Text": "Otra publicación de prueba.",
    "Multimedia": "",
    "Datepublish": "2025-06-22T05:00:00.000+00:00"
}

# Insertamos en una lista para simular un timeline
r.rpush(feed_key, json.dumps(post1))
r.rpush(feed_key, json.dumps(post2))

print("Feed inicializado en Redis")
