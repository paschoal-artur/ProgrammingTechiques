import conversores as cvs

def teste(valor):
    print(cvs.celsius_para_fahrenheit(valor))
    print(cvs.fahrenheit_para_celsius(valor))
    print(cvs.metro_para_pes(valor))
    print(cvs.pes_para_metros(valor))
    print(cvs.quilometro_para_milhas(valor))
    print(cvs.dia_para_hora(valor))

teste(25)