#Tema Interval_scheduling in cursuri

def interval_scheduling(cursuri):
    cursuri.sort(key=lambda x: x[1])
    rezultat = []
    end_time = 0
    for inceput , sfarsit in cursuri:
        if inceput >= end_time:
            rezultat.append((inceput, sfarsit))
            end_time = sfarsit
    return rezultat

cursuri = [(9, 11), (10 , 12) , (13,14) , (11, 13), (12,14)]
print(interval_scheduling(cursuri))



########################################################################################

import heapq

class NodHuffman:
    def __init__(self, simbol, frecventa):
        self.simbol = simbol
        self.frecventa = frecventa
        self.st = None
        self.dr = None
    def __lt__(self, alt):
        return self.frecventa < alt.frecventa

def huffman(frecvente):
    heap = [NodHuffman(symb, freq) for symb, freq in frecvente.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        st = heapq.heappop(heap)
        dr = heapq.heappop(heap)
        intermediar = NodHuffman(None, st.frecventa + dr.frecventa)
        intermediar.st = st
        intermediar.dr = dr
        heapq.heappush(heap, intermediar)
    return heap[0]

def genereaza_coduri(nod, cod="", coduri={}):
    if nod is None:
        return
    if nod.simbol is not None:
        coduri[nod.simbol] = cod
    genereaza_coduri(nod.st, cod + "0", coduri)
    genereaza_coduri(nod.dr, cod + "1", coduri)
    return coduri


freq = {'a':5 ,'b':2,'c':1,'d':1}
arbore = huffman(freq)
coduri = genereaza_coduri(arbore)
print("Coduri Huffman:", coduri)
