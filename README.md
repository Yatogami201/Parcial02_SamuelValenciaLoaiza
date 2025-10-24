# Análisis: Comunicación con otro microservicio de historial

Si este microservicio necesitara almacenar el historial de cálculos en una base de datos externa mediante otro servicio, el diseño se modificaría para permitir la comunicación entre ambos microservicios de forma desacoplada y escalable.

1. **Separación de responsabilidades:** 
   El microservicio actual seguiría calculando el factorial y generando la respuesta JSON, mientras que un segundo microservicio, por ejemplo `historial-service`, se encargaría de registrar cada cálculo en una base de datos externa.

2. **Comunicación entre servicios:** 
   El servicio de factorial enviaría una solicitud **HTTP POST** al servicio de historial con los datos del cálculo, por ejemplo:
   ```json
   {
     "numero": 5,
     "factorial": 120,
     "etiqueta": "impar",
     "timestamp": "2025-10-24T07:30:00Z"
   }
   ```
   Esto podría implementarse con la librería `requests` en Python.

3. **Desacoplamiento:** 
   Ambos servicios serían independientes, lo que permitiría que el microservicio factorial continúe funcionando aunque el de historial no esté disponible. Para mejorar la tolerancia a fallos, se podría usar una cola de mensajes (RabbitMQ, Kafka) o un sistema de reintentos.

4. **Beneficios del diseño distribuido:** 
   - Permite escalar cada servicio de forma separada. 
   - Facilita la reutilización del servicio de historial por otras aplicaciones. 
   - Mejora la mantenibilidad y evolución del sistema.

**Ejemplo de flujo:**

```
[Cliente] → (GET) /factorial/5 → [Servicio Factorial]
                                   ↓
                           (POST) /historial → [Servicio Historial + Base de Datos]
```
