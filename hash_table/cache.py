cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]  # retorna os dados do cache
    else:
        data = get_server_data(url)
        cache[url] = data  # antes de retornar os dados, eles serao armazenados no cache
        return data
