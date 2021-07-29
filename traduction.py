# -*- coding: utf-8 -*-

"""
https://svt.ac-versailles.fr/spip.php?article1050
https://www.supagro.fr/ress-tice/ue1-ue2_auto/Bases_Biologie_Moleculaire_v2/co/_gc_principe_traduction.html
https://fr.wikipedia.org/wiki/Code_génétique

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

dct = {}
# Code génétique
ala = ["GCU", "GCC", "GCA", "GCG"]
dct['ala'] = 'alanine'
arg = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]
dct['arg'] = 'arginine'
asn = ["AAU", "AAC"]
dct['asn'] = 'asparagine'
asp = ["GAU", "GAC"]
dct['asp'] = 'acide aspartique'
cys = ["UGU", "UGC"]
dct['cys'] = 'cystéine'
gln = ["CAA", "CAG"]
dct['gln'] = 'glutamine'
glu = ["GAA", "GAG"]
dct['glu'] = 'acide glutamique'
gly = ["GGU", "GGC", "GGA", "GGG"]
dct['gly'] = 'glycine'
his = ["CAU", "CAC"]
dct['his'] = 'histidine'
ile = ["AUU", "AUC", "AUA"]
dct['ile'] = 'isoleucine'
leu = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]
dct['leu'] = 'leucine'
lys = ["AAA", "AAG"]
dct['lys'] = 'lysine'
met = ["AUG"]                  # codon initiateur
dct['met'] = 'méthionine'
phe = ["UUU", "UUC"]
dct['phe'] = 'phényllalanine'
pro = ["CCU", "CCC", "CCA", "CCG"]
dct['pro'] = 'proline'

ser = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
dct['ser'] = 'serine'
thr = ["ACU", "ACC", "ACA", "ACG"]
dct['thr'] = 'thréonine'
trp = ["UGG"]
dct['trp'] = 'tryptophane'
tyr = ["UAU", "UAC"]
dct['tyr'] = 'tyrosine'
val = ["GUU", "GUC", "GUA", "GUG"]
dct['val'] = 'valine'
stop = ["UAG", "UGA", "UAA"]
dct['stop'] = 'terminaison'

pyl = ['UAG avec PYLIS']
dct['pyl'] = 'pyrrolysine'
sec = ['UGA avec SECIS']
dct['sec'] = 'sélénocystéine'

def main(transcrit):    
    traduit = ""
    numbis = get_init_codon(transcrit)
    # **** Boucle pour traduire la séquence après le codon initiateur ****
    print(numbis)
    seq_lu = ''
    aa_list=[]
    if numbis:
        while numbis < len(transcrit)-2:
            seq = transcrit[numbis:numbis+3]
            if seq in ala:
                traduit += "Ala"
                aa_list.append(dct['ala'])
            elif seq in arg:
                traduit += "Arg"
                aa_list.append(dct['arg'])
            elif seq in asn:
                traduit += "Asn"
                aa_list.append(dct['asn'])
            elif seq in cys:
                traduit += "Cys"
                aa_list.append(dct['cys'])
            elif seq in gln:
                traduit += "Gln"
                aa_list.append(dct['gln'])
            elif seq in glu:
                traduit += "Glu"
                aa_list.append(dct['glu'])
            elif seq in gly:
                traduit += "Gly"
                aa_list.append(dct['gly'])
            elif seq in his:
                traduit += "His"
                aa_list.append(dct['his'])
            elif seq in ile:
                traduit += "Ile"
                aa_list.append(dct['ile'])
            elif seq in leu:
                traduit += "Leu"
                aa_list.append(dct['leu'])
            elif seq in lys:
                traduit += "Lys"
                aa_list.append(dct['lys'])
            elif seq in met:
                traduit += "Met"
                aa_list.append(dct['met'])
            elif seq in phe:
                traduit += "Phe"
                aa_list.append(dct['phe'])
            elif seq in pro:
                traduit += "Pro"
                aa_list.append(dct['pro'])
            elif seq in ser:
                traduit += "Ser"
                aa_list.append(dct['ser'])
            elif seq in thr:
                traduit += "Thr"
                aa_list.append(dct['thr'])
            elif seq in trp:
                traduit += "Trp"
                aa_list.append(dct['trp'])
            elif seq in tyr:
                traduit += "Tyr"
                aa_list.append(dct['tyr'])
            elif seq in val:
                traduit += "Val"
                aa_list.append(dct['val'])
            elif seq in stop:
                traduit += "Stop"
                aa_list.append(dct['stop'])
                seq_lu += seq
                break
            numbis += 3
            seq_lu += seq+'-'
        print("Séquence lue :", seq_lu)
        print("Séquence traduite :", traduit)
        print('Liste d\'acides aminés décodés :', aa_list)

    else:
        print("Il n'y a pas de codon initiateur")


if __name__ == '__main__':
    transcrit = "UAACGGAAUGUUCAUAUGCCCAAUGAUUUAGUU"
    #transcrit = 'AGCUAUGACGACAUUCUGGUGAGAAAAUCUGUAUCUGCAACCGCGUG'
    #transcrit = 'CGAUGAGCUAUGACGUCUGUCGGUACCCAACUAUGAGGACUCCCUCGGAUUC'
    main(transcrit)
