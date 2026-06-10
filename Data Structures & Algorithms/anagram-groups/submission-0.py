class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        palavra_sorted = []
    
        for palavra in strs:
            if sorted(palavra) not in palavra_sorted:
                palavra_sorted.append(sorted(palavra))

        dicionario = {}
        for p in palavra_sorted:
            lista = []
            for n in strs:
                if p == sorted(n):
                    lista.append(n)
                dicionario[tuple(p)] = lista

        return list(dicionario.values())