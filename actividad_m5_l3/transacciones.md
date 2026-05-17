#
##
###

## 4. Consultas SQL
# En el archivo transacciones.md, responde: 
**• ¿Qué es una transacción en bases de datos y por qué es importante?**

R: Una transacción es un conjunto de operaciones en una base de datos (como INSERT, UPDATE o DELETE) que se ejecutan como una única unidad lógica de trabajo. Es importante porque garantiza la integridad de los datos ante errores del sistema o fallos en el proceso, asegurando que la base de datos nunca quede en un estado a medias o corrupto.

**• Describe brevemente qué significa:** 

**• Atomicidad:** Representa el principio de "todo o nada". Si una de las operaciones dentro de la transacción falla, se deshacen todos los cambios y la transacción completa falla, dejando los datos como estaban al principio.

**• Consistencia:** Asegura que cualquier transacción solo lleve la base de datos de un estado válido a otro, respetando siempre todas las reglas, esquemas y restricciones definidas.

**• Aislamiento:** Garantiza que múltiples transacciones que se ejecutan de manera concurrente (al mismo tiempo) no interfieran entre sí. Una transacción no puede ver los datos "a medias" de otra transacción que aún no ha terminado.

**• Durabilidad:** Significa que una vez que la transacción ha finalizado con éxito (hace "commit"), los cambios guardados son totalmente permanentes y no se perderán, incluso si ocurre un corte de energía o fallo en el sistema.


**Comenta qué diferencia notaste entre ROLLBACK y COMMIT.**

BEGIN;
UPDATE pedidos SET total = 0 WHERE id = 1;  -- cambia total a 0
ROLLBACK;                                    -- ← deshace el UPDATE
SELECT * FROM pedidos;                       -- el pedido id=1 sigue con su total original

BEGIN;
DELETE FROM pedidos WHERE id = 2;  -- elimina el pedido
COMMIT;                            -- ← confirma y guarda el DELETE
SELECT * FROM pedidos;             -- el pedido id=2 ya no existe

COMMIT = Confirma y guuardar en un documento
ROLLBACK = Deshacer antes de guardar — vuelve al estado anterior al BEGIN