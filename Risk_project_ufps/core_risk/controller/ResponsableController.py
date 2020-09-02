from Risk_project_ufps.core_risk.dao.ResponsableDao import *
from Risk_project_ufps.core_risk.dto.models import *

class ResponsableController(): 

	def registrar_responsable(self, nombre, descripcion, proyecto):
		responsable_dao = ResponsableDao()
		return responsable_dao.registrar_responsable(nombre, descripcion, proyecto)

	def listar_responsables(self, id):
		responsable_dao = ResponsableDao()
		return responsable_dao.listar_responsables(id)

	def obtener_responsable(self, id):
		responsable_dao = ResponsableDao()
		return responsable_dao.obtener_responsable(id)

	def editar_responsable(self, responsable, nombre, descripcion):
		responsable_dao = ResponsableDao()
		return responsable_dao.editar_responsable(responsable, nombre, descripcion)

	def eliminar_responsable(self, responsable):
		responsable_dao = ResponsableDao()
		return responsable_dao.eliminar_responsable(responsable)

	
