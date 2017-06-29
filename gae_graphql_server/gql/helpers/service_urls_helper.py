
class Helpers:

	@staticmethod
	def get_service_urls(context):
	    service_urls = {}
	    service_urls['core_server_url'] = context['core_server_url']
	    service_urls['pls_server_url'] = context['pls_server_url']
	    return service_urls