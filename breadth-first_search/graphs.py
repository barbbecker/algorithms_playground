# -*- coding: utf-8 -*-
from collections import deque

# se o nome estiver no array da Claire, retorne True -> todos os amigos de Claire são vendedores de manga
def sales_person(name):
    if name in graph["Claire"]:
        return True


graph = {}
graph["You"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []   # esse vetor vc mantem o registro das pessoas que já foram verificadas
    while search_queue:
        person = search_queue.popleft()
        if not person in verified:   # verifica essa pessoa somente se ela nao tiver sido verificada
            if sales_person(person):
                print('{0} é um vendedor de mangas'.format(person))
                return True
            else:
                search_queue += graph[person]
                verified.append(person)   # marca a pessoa como verificada
    return False

search("You")