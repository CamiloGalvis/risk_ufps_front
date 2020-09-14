from Risk_project_ufps.core_risk.dto.models import *
from contextlib import closing
from django.db import connection


class TareaHasRecursoDao():


	def agregar_recurso_tarea(self, tarea, recurso, cantidad):
		with closing(connection.cursor()) as cursor:
			cursor.execute(
                'INSERT INTO riesgos_bd.`tarea_has_recurso`(`tarea_id`, `recurso_id`, `cantidad` )'
                'VALUES (%s, %s, %s)',
                (tarea.tarea_id, recurso.recurso_id, cantidad),
            )

			return "Se asigno recurso exitosamente."

	def get_recurso_tarea_by_id(self, tarea, recurso):
		tarea_recurso = None
		try:
			tarea_recurso = TareaHasRecurso.objects.get(tarea_id=tarea.tarea_id, recurso_id=recurso.recurso_id)     
		except Exception as e:
			print(e)
		finally:
	 		return tarea_recurso

	def eliminar_recurso_tarea(self, tarea_recurso):
		tarea_recurso = tarea_recurso
		try:
			tarea_recurso.delete() 
		except Exception as e:
			print(e)
		finally:
	 		return "Recurso desvinculado exitosamente"
