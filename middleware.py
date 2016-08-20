
class ReferMiddleware():
	def process_request(self, request):
		ref_id = request.GET.get("ref",)
		try:
			obj = Join.object.get(ref_id = ref_id)
		except:
			obj = None
		if obj:
			request.session['join_id_refer'] =obj.id

 