class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for palavra in strs:
            encoded += f"{len(palavra)}#{palavra}"
        return encoded

    def decode(self, s: str) -> List[str]:
        lista = list()
        count = 0
        while count < len(s):
            i = s.index("#", count)
            tamanho = int(s[count:i])
            palavra = s[i+1:i+1+tamanho]
            lista.append(palavra)
            count = i + 1 + tamanho
        return lista
