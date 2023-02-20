#Isivedam tikrinamo ir istikrinto failo locations, cia jei atnaujintas neegzistuoja - jis bus sukurtas, o jei egzistuoja - perrasytas
failas = "E:/AAILABS/srt_pakeitimo_autamatizavimo_programa/milda_teka_upe_pro_sali_22_40000_poliarinis-ratas-6.srt"
atnaujintas = "E:/AAILABS/srt_pakeitimo_autamatizavimo_programa/milda_teka_upe_pro_sali_NAUJAS.srt"

def zodzio_pakeitimas(file,oldword,newword,newplace):
    updatedword = "*" + newword
    import pysrt
    subs = pysrt.open(file)
    for sub in subs:
        lowers = sub.text.lower()
        if lowers.__contains__(oldword):
            sub.text = sub.text.replace(oldword,updatedword)
            print(sub.text)
                        
    subs.save(newplace)

def pazymejimas_raides(file,letter,newplace):
    import pysrt
    subs = pysrt.open(file)
    for sub in subs:
        if sub.text.__contains__(letter.lower()) or sub.text.__contains__(letter.upper()):
            sentence = sub.text.split()
            for word in sentence:
                if word.__contains__(letter.lower()) or word.__contains__(letter.upper()):
                    if word[0] != "*":
                        newword = "*" + word
                        sub.text = sub.text.replace(word,newword)
                        print(sub.text)
    subs.save(newplace)

def raides_pakeitimas(file,oldletter,newletter,newplace):
    import pysrt
    subs = pysrt.open(file)
    for sub in subs:
        if sub.text.__contains__(oldletter.lower()) or sub.text.__contains__(oldletter.upper()):
            sentence = sub.text.split()
            for word in sentence:
                if word.__contains__(oldletter.lower()) or word.__contains__(oldletter.upper()):
                    if word[0] != "*":
                        oldword = word.lower()
                        newword = "*" + oldword.replace(oldletter,newletter)
                        sub.text = sub.text.replace(word,newword)
                        print(sub.text)
                    else:
                        oldword = word.lower()
                        newword = oldword.replace(oldletter,newletter)
                        sub.text = sub.text.replace(word,newword)
                        print(sub.text)
    subs.save(newplace)

#Populiariausios klaidos galetu buti pataisytos taip
#raides_pakeitimas(failas,"h","hhh",atnaujintas)
#raides_pakeitimas(atnaujintas,"f","ff",atnaujintas)

#Cia yra visu zodziu su tam tikra raide pazymejimas zvaigzdute pries zodi
#pazymejimas_raides(failas,"h",atnaujintas)

#Cia galima pakeisti tam tikra raide i raidziu derini arba kita raide ir pazymeti pakeitima zvaigzdute
#raides_pakeitimas(failas,"h","hhh",atnaujintas)

#Apacioje yra jau iskart su galimybe pakeisti zodi i kita zodi, blogas/geras yra pavyzdys kaip galetu atrodyti pakeitimas
blogas = "sėdė́jo "
geras = "ssėdė́jo "
#zodzio_pakeitimas(failas,blogas,geras,atnaujintas)

#Cia galima butu padaryti blogu zodziu sarasa is karto su pakeitimais
geri = []
blogi = []
if len(geri) != len(blogi):
    print("Unequal lists of changeable words")
#i = 0
#while i < len(geri):
#    zodzio_pakeitimas(failas,blogi[i],geri[i],atnaujintas)
#    i = i + 1


