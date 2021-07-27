# -*- coding: utf-8 -*-

"""
https://svt.ac-versailles.fr/spip.php?article1050
Dans ce programme la variable "transcrit" est un ARN qui va être traduit.
"""



def get_init_codon(transcrit):
    # **** Boucle pour trouver le codon initiateur (s'il y en a un) ****
    numero = 0
    numbis = 0
    while numero < len(transcrit)-2:
        if transcrit[numero:numero+3] == "AUG":
            numbis = numero
            break
        numero += 1
    return numbis

# Code génétique
ala = ["GCU", "GCC", "GCA", "GCG"]
arg = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]
asn = ["AAU", "AAC"]
asp = ["GAU", "GAC"]
cys = ["UGU", "UGC"]
gln = ["CAA", "CAG"]
glu = ["GAA", "GAG"]
gly = ["GGU", "GGC", "GGA", "GGG"]
his = ["CAU", "CAC"]
ile = ["AUU", "AUC", "AUA"]
leu = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]
lys = ["AAA", "AAG"]
met = ["AUG"]                  # codon initiateur
phe = ["UUU", "UUC"]
pro = ["CCU", "CCC", "CCA", "CCG"]
ser = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
thr = ["ACU", "ACC", "ACA", "ACG"]
trp = ["UGG"]
tyr = ["UAU", "UAC"]
val = ["GUU", "GUC", "GUA", "GUG"]
stop = ["UAG", "UGA", "UAA"]

def main(transcrit):    
    traduit = ""
    numbis = get_init_codon(transcrit)
    # **** Boucle pour traduire la séquence après le codon initiateur ****
    print(numbis)
    seq_lu = ''
    if numbis:
        while numbis < len(transcrit)-2:
            seq = transcrit[numbis:numbis+3]
            if seq in ala:
                traduit += "Ala"
            elif seq in arg:
                traduit += "Arg"
            elif seq in asn:
                traduit += "Asn"
            elif seq in cys:
                traduit += "Cys"
            elif seq in gln:
                traduit += "Gln"
            elif seq in glu:
                traduit += "Glu"
            elif seq in gly:
                traduit += "Gly"
            elif seq in his:
                traduit += "His"
            elif seq in ile:
                traduit += "Ile"
            elif seq in leu:
                traduit += "Leu"
            elif seq in lys:
                traduit += "Lys"
            elif seq in met:
                traduit += "Met"
            elif seq in phe:
                traduit += "Phe"
            elif seq in pro:
                traduit += "Pro"
            elif seq in ser:
                traduit += "Ser"
            elif seq in thr:
                traduit += "Thr"
            elif seq in trp:
                traduit += "Trp"
            elif seq in tyr:
                traduit += "Tyr"
            elif seq in val:
                traduit += "Val"
            elif seq in stop:
                traduit += "Stop"
                seq_lu += seq
                break
            numbis += 3
            seq_lu += seq+'-'
        print("Séquence lue :", seq_lu)
        print("Séquence traduite :", traduit)

    else:
        print("Il n'y a pas de codon initiateur")


if __name__ == '__main__':
    transcrit = "UAACGGAAUGUUCAUAUGCCCAAUGAUUUAGUU"
    #transcrit = 'AGCUAUGACGACAUUCUGGUGAGAAAAUCUGUAUCUGCAACCGCGUG'
    #transcrit = 'CGAUGAGCUAUGACGUCUGUCGGUACCCAACUAUGAGGACUCCCUCGGAUUC'
    main(transcrit)
