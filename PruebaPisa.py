#Sección de Matemáticas- test de preparación para prueba PISA 
#En este archivo se pegarán las demás partes del programa para completar el test.

def menu_p():
    def menu_p2():
        print('''Menú principal: Test para prueba PISA
        
        Con el fin de mejorar su desempeño en la prueba PISA, este test realizará preguntas sobre los temas que
        este examen contiene. Por favor, seleccione una opción: ''')

        opcion=input('''
        a) Sección de Español/Lectura
        b) Sección de Matemáticas
        c) Sección de Ciencias
        d) Salir
        Respuesta: ''')
        opcion=opcion.lower()
        opcion=opcion.strip()
        return opcion
    opcion=menu_p2()
    while opcion!='a' and opcion!='b' and opcion!='c' and opcion!='d':
        print ('Opcion invalida')
        print ('Porfavor intente de nuevo')
        opcion=menu_p2()

    if opcion=="b":
        puntaje=0
        def pr1():
            print('''\n\nProblema 1:
            Mark (de Sydney, Australia) y Hans (de Berlín, Alemania) se comunican a menudo utilizando el 'chat' de Internet.
            Ambos tienen que conectarse a Internet simultáneamente para poder 'chatear'.
            Para encontrar una hora apropiada para chatear, Mark buscó un mapa horario mundial y halló lo siguiente:
            Berlín: 1:00 am         Sydney: 10:00am
            
            Cuando son las 7:00 de la tarde en Sydney, ¿qué hora es en Berlín? ''')

            respuesta=input("\na) 10:00\nb) 9:00\nc) 17:00\n\n Respuesta: ")
            respuesta=respuesta.lower()

            if respuesta== "a":
                print("Respuesta correcta.")
                puntaje=+ 1

            elif respuesta== "b":
                print("Respuesta incorrecta")

            elif respuesta== "c":
                print("Respuesta incorrecta")
            
          
        def pr2():
            print('''\n\nProblema 2:
            Mark y Hans no pueden chatear entre las 9:00 de la mañana y las 4:30 de la tarde, de sus respectivas horas locales, porque tienen que ir al colegio.
            Tampoco pueden desde las 11:00 de la noche hasta las 7:00 de la mañana, de sus respectivas horas locales, porque estarán durmiendo.
            ¿A qué horas podrían chatear Mark y Hans?
            Escoge las respectivas horas locales correctas:''')

            respuesta=input('''\na) Mark: 16:00  Hans:7:00
                               b) Mark:5:00  Hans:12:00
                               c) Mark: 17:00  Hans:8:00
                               Respuesta: ''')
            respuesta=respuesta.lower()
            if respuesta== "a":
                print("Respuesta incorrecta.")

            elif respuesta== "b":
                print("Respuesta incorrecta")

            elif respuesta== "c":
                print("Respuesta correcta")
                puntaje=+ 1
            print("Tu puntaje actual es de: ",puntaje)     
            
        def pr3():
            print('''\n\nProblema 3:
            Normalmente, una pareja de pingüinos pone dos huevos al año. 
            Por lo general, el polluelo del mayor de los dos huevos es el único que sobrevive.
            En el caso de los pingüinos de penacho amarillo, el primer huevo pesa aproximadamente 78 g y el segundo huevo pesa aproximadamente 110 g.
            Aproximadamente, ¿en qué porcentaje es más pesado el segundo huevo que el primer huevo?''')

            respuesta=input("\na) 29%\nb) 32%\nc) 41%\nd) 71%\n\n Respuesta: ")
            respuesta=respuesta.lower()
            if respuesta== "a":
                print("Respuesta incorrecta.")

            elif respuesta== "b":
                print("Respuesta incorrecta")

            elif respuesta== "c":
                print("Respuesta correcta")
                puntaje=+ 1

            elif respuesta== "d":
                print("Respuesta incorrecta")
            print("Tu puntaje actual es de: ",puntaje)  
        def pr4():           
            print('''\n\nProblema 4.
            Una pizzería sirve dos pizzas redondas del mismo grosor y de diferente tamaño.
            La más pequeña tiene un diámetro de 30 cm y cuesta 30 euros. La mayor tiene un diámetro de 40 cm y cuesta 40 euros.
            ¿Qué pizza tiene mejor precio?
            ''')
            respuesta=input("\na) Pizza de 30 cm\nb) Pizza de 40 cm\nc) Ambas \nd) No se puede determinar\n\n Respuesta: ")
            respuesta=respuesta.lower()
            if respuesta== "a":
                print("Respuesta incorrecta.")

            elif respuesta== "b":
                print("Respuesta correcta")
                puntaje=+ 1

            elif respuesta== "c":
                print("Respuesta incorrecta")

            elif respuesta== "d":
                print("Respuesta incorrecta")

        def pr5():
            print('''\n\nProblema 5.
            Nicolás quiere pavimentar el patio rectangular de su nueva casa.
            El patio mide 5,25 metros de largo y 3,00 metros de ancho.
            Nicolás necesita 81 ladrillos por metro cuadrado.
            Calcula cuántos ladrillos necesita Nicolás para pavimentar todo el patio.
            ''')
            respuesta=input("\na) 1276\nb) 1330\nc) 1277\nd) 980\n\n Respuesta: ")
            respuesta=respuesta.lower()

            if respuesta== "a":
                print("Respuesta correcta.")
                puntaje=+ 1

            elif respuesta== "b":
                print("Respuesta incorrecta")

            elif respuesta== "c":
                print("Respuesta incorrecta")

            elif respuesta== "d":
                print("Respuesta incorrecta")

        def pr6():
            print('''\n\nProblema 6.
            En el colegio de Irene, su profesora de ciencias les hace exámenes que se puntúan de 0 a 100.
            Irene tiene una media de 60 puntos de sus primeros cuatro exámenes de ciencias.
            En el quinto examen sacó 80 puntos. 
            ¿Cuál es la media de las notas de Irene en ciencias después de los cinco exámenes? ''')

            respuesta=input("\na) 60\nb) 65\nc) 64\nd) 72\n\n Respuesta: ")
            respuesta=respuesta.lower()

            if respuesta== "a":
                print("Respuesta incorrecta.")

            elif respuesta== "b":
                print("Respuesta incorrecta")

            elif respuesta== "c":
                print("Respuesta correcta")
                puntaje=+ 1

            elif respuesta== "d":
                print("Respuesta incorrecta")

        def pr7():
            print('''\n\n Problema 7.
            La madre de Roberto le deja coger un caramelo de una bolsa. 
            Él no puede ver los caramelos. El número de caramelos de cada color que hay en la bolsa son los siguientes:
            Rojo:6
            Naranja:5
            Amarillo:3
            Verde:3
            Azul:2
            Rosa:4
            Violeta:2
            Marrón:5
            ''')
            respuesta=input('''¿Cuál es la probabilidad de que Roberto extraiga un caramelo rojo? 
            a) 10% 
            b) 20% 
            c) 25% 
            d) 50%
            Respuesta: ''')
            respuesta=respuesta.lower()

            if respuesta== "a":
                print("Respuesta incorrecta.")

            elif respuesta== "b":
                print("Respuesta correcta")
                puntaje=+ 1

            elif respuesta== "c":
                print("Respuesta incorrecta")

            elif respuesta== "d":
                print("Respuesta incorrecta")
                
        def salida_programa():
            print(" Has salido del programa. ")

        def seccion_m():
            access=""
            while access!="h":
                print('''Menú:  Sección de matemáticas.
                Para poder lograr una buena calificación en su prueba PISA, en la sección de matemáticas, es necesario practicar''')

                access=input('''\n\nSe harán preguntas de diferentes áreas de matemáticas.
                                Selecciona alguna letra/opción del siguiente menú:
                                a) Ir a Problema 1
                                b) Ir a Problema 2
                                c) Ir a Problema 3
                                d) Ir a Problema 4
                                e) Ir a Problema 5
                                f) Ir a Problema 6
                                g) Ir a Problema 7
                                h) Regresar al Menú principal
                                Respuesta: ''')

                access=access.lower()

                if access== "a":
                    print("Comenzamos")
                    pr1() 
               
                elif access=="b":
                    pr2()

                elif access=="c":
                    pr3()

                elif access=="d":
                    pr4()

                elif access=="e":
                    pr5()

                elif access=="f":
                    pr6()

                elif access=="g":
                    pr7()

                elif access=="h":
                    menu_p()
                else:
                    access=input("Error. Por favor, selecciona una opción del menú: ")
        seccion_m()

    #Español
    elif opcion=="a":

        def problema1():
            print("Problema 1: Leer el siguiente texto sobre la gripe y responder las preguntas:\nComo usted probablemente ya sabe, la gripe se propaga rápida y extensamente durante el invierno. Los que la sufren pueden estar enfermos durante semanas. La mejor manera de vencer a este virus es cuidar lo más posible la salud de nuestro cuerpo. El ejercicio diario y una dieta rica en frutas y vegetales es lo más recomendable para contribuir a que nuestro sistema inmunitario esté en buenas condiciones para luchar contra el virus invasor.")
            print("\n")
            print("ACOL ha decidido ofrecer a su personal la oportunidad de vacunarse contra la gripe, como recurso adicional para evitar que este insidioso virus se extienda entre nosotros. ACOL ha previsto que una enfermera lleve a cabo el programa de vacunación dentro de la empresa en horas de trabajo, durante la mitad de la jornada laboral de la semana del 17 de mayo. Este programa se ofrece gratuitamente a todos los empleados de la empresa.")
            print("\n")
            print("La participación es voluntaria. Los empleados que decidan utilizar esta oportunidad deben firmar un impreso manifestando su consentimiento e indicando que no padecen ningún tipo de alergia y que comprenden que pueden experimentar algunos efectos secundarios sin importancia.")
            print("\n")
            print("El asesoramiento médico indica que la inmunización no produce la gripe. No obstante, puede originar algunos efectos secundarios como cansancio, fiebre ligera y molestias en el brazo.")
            print("\n")
            print("¿QUIEN DEBE VACUNARSE? Cualquiera que esté interesado en protegerse del virus. Esta vacunación está especialmente recomendada para las personas mayores de 65 años y, al margen de la edad, para CUALQUIERA que padezca alguna enfermedad crónica, especialmente si es de tipo cardíaco, pulmonar, bronquial o diabético. En el entorno de una oficina, TODAS LAS PERSONAS corren el riesgo de contraer la enfermedad. En el entorno de una oficina, TODAS LAS PERSONAS corren el riesgo de contraer la enfermedad.")
            print("\n")
            print("¿QUIEN NO DEBE VACUNARSE? Las personas que sean hipersensibles a los huevos, las que padezcan alguna enfermedad que produzca fiebres altas y las mujeres embarazadas. Consulte con su doctor si está tomando alguna medicación o si anteriormente ha sufrido reacciones adversas a la vacuna contra la gripe.Las personas que sean hipersensibles a los huevos, las que padezcan alguna enfermedad que produzca fiebres altas y las mujeres embarazadas. Consulte con su doctor si está tomando alguna medicación o si anteriormente ha sufrido reacciones adversas a la vacuna contra la gripe.")
            print("\n")
            print("Si usted quiere vacunarse durante la semana del 17 de mayo, por favor, avise a la jefa de personal, Raquel Escribano, antes del viernes 7 de mayo. La fecha y la hora se fijarán conforme a la disponibilidad de la enfermera, el número de participantes en la campaña y el horario más conveniente para la mayoría de los empleados. Si quiere vacunarse para este invierno pero no puede hacerlo en las fechas establecidas, por favor, comuníqueselo a Raquel. Quizá pueda fijarse una sesión de vacunación alternativa si el número de personas es suficiente. Para más información, contacte con Raquel en la extensión 5577. Si usted quiere vacunarse durante la semana del 17 de mayo, por favor, avise a la jefa de personal, Raquel Escribano, antes del viernes 7 de mayo. La fecha y la hora se fijarán conforme a la disponibilidad de la enfermera, el número de participantes en la campaña y el horario más conveniente para la mayoría de los empleados. Si quiere vacunarse para este invierno pero no puede hacerlo en las fechas establecidas, por favor, comuníqueselo a Raquel. Quizá pueda fijarse una sesión de vacunación alternativa si el número de personas es suficiente. Para más información, contacte con Raquel en la extensión 5577.")
            print("\n")
            print("Raquel Escribano, directora del departamento de recursos humanos de una empresa llamada ACOL, preparó la información que se presenta en esta página y en la anterior para distribuirla entre el personal de la empresa ACOL.Raquel Escribano, directora del departamento de recursos humanos de una empresa llamada ACOL, preparó la información que se presenta en esta página y en la anterior para distribuirla entre el personal de la empresa ACOL.")
        problema1()
        print("\n")
        def preg1():  
            print("1. ¿Cuál de las siguientes afirmaciones describe una característica del programa de inmunización de ACOL contra la gripe?")
            respuesta=input("a) Se darán clases de ejercicio físico durante el invierno. \nb) Se ofrecerá un pequeño bono a los participantes.\nc) La vacunación se llevará a cabo durante las horas de trabajo.\nd) Un médico pondrá las inyecciones.\n\n Respuesta: ")  
            if respuesta == "a":
                print ("Respuesta incorrecta.")
            elif respuesta == "b":
                print ("Respuesta incorrecta")
            elif respuesta == "c":
                print ("Respuesta correcta")
            elif respuesta == "d":
                print("Respuesta incorrecta")        
        preg1()
        print("\n")
        def preg2():
            print("2. Podemos hablar sobre el contenido de un escrito (lo que dice). Podemos hablar sobre su estilo (el modo en el que se presenta). Raquel quería que esta hoja informativa tuviera un estilo cordial y que animase a vacunarse. En tu opinion, ¿crees que lo consiguió? ¿describe como?") 
            respuesta=input("a) Sí, las imágenes rompen el texto y lo hacen más fácil de leer\nb) El dibujo de tipo tebeo es cordial [Se refiere a un aspecto concreto (“dibujo tipo tebeo”) de una ilustración.\nc) No, las ilustraciones son infantiles y poco relevantes\nd) Todas las respuestas anteriores son correctas\n\n Respuesta: ")  
            if respuesta == "a":
                print ("Respuesta incorrecta.")
            elif respuesta == "b":
                print ("Respuesta incorrecta")
            elif respuesta == "c":
                print ("Respuesta incorrecta")
            elif respuesta == "d":
                print("Respuesta correcta")
        preg2()
        print("\n")
        def preg3():  
            print("3. Esta hoja informativa sugiere que si uno quiere protegerse del virus de la gripe, la inyección de una vacuna de la gripe es... ")
            respuesta=input("a) Más eficaz que el ejercicio y una dieta saludable, pero más arriesgada.\nb) Una buena idea, pero no un sustituto del ejercicio y la dieta saludable.\nc) Tan eficaz como el ejercicio y una dieta saludable y menos problemática.\nd) No es necesaria si se hace ejercicio y se sigue una dieta sana.\n\n Respuesta: ")  
            if respuesta == "a":
                print ("Respuesta incorrecta.")
            elif respuesta == "b":
                print ("Respuesta correcta")
            elif respuesta == "c":
                print ("Respuesta incorrecta")
            elif respuesta == "d":
                print("Respuesta incorrecta")        
        preg3()
        print("\n")
        def preg4():  
            print("4. Parte de la información de la hoja dice:\n¿QUIÉN DEBE VACUNARSE? Cualquiera que esté interesado en protegerse del virus.\nDespués de que Raquel distribuyera la hoja informativa, un colega le dijo que debería no haber escrito las palabras “cualquiera que esté interesado en protegerse del virus” porque podían malinterpretarse.\n¿Lo que Raquel argumenta esta en lo correcto?")
            respuesta=input("a) Sí, porque la vacuna sería peligrosa para ciertas personas(ej.las mujeres embarazadas)\nb) No, porque hace que el mensaje destaque \nc) Si, porque no tiene mucha informacion y muchas personas pueden confundirse por solo esa hoja informativa\nd) No, porque todos deberian de estar inmunes al virus.\n\n Respuesta: ")  
            if respuesta == "a":
                print ("Respuesta correcta.")
            elif respuesta == "b":
                print ("Respuesta incorrecta")
            elif respuesta == "c":
                print ("Respuesta incorrecta")
            elif respuesta == "d":
                print("Respuesta incorrecta")        
        preg4()
        print("\n")
        def preg5():  
            print("5. Según la hoja informativa, ¿cuál de estos empleados de la empresa debería contactar con Raquel?")
            respuesta=input("a) Ramón, del almacén, que no quiere vacunarse porque prefiere confiar en su sistema inmunológico natural.\nb) Julia, de ventas, que quiere saber si el programa de vacunación es obligatorio.\nc) Alicia, de recepción, que querría vacunarse este invierno pero dará a luz dentro de dos meses.\nd) Miguel, de contabilidad, al que le gustaría vacunarse pero tiene que salir de viaje la semana del 17 de mayo.\n\n Respuesta: ")  
            if respuesta == "a":
                print ("Respuesta incorrecta.")
            elif respuesta == "b":
                print ("Respuesta incorrecta")
            elif respuesta == "c":
                print ("Respuesta incorrecta")
            elif respuesta == "d":
                print("Respuesta correcta")       
        preg5()



    #Ciencias
    elif opcion=="c":
        # Definimos una funcion que nos prepare las opciones y nos diga si esta correcta o no
        def ask_question(Pregunta, Opciones, Respuesta):
            # Definimos el numero de veces que se puede preguntar una pregunta y usamos un while para no pasarnos
            attempts = 0
            while attempts < 2:
                # Aqui ya con las opciones nadamas las imprimimos y acomodamos para que el usuario las tenga como opciones
                print(Pregunta)
                print('A)', Opciones[0])
                print('B)', Opciones[1])
                print('C)', Opciones[2])
                # El usuario pone su input
                user_answer = input("Ingresa la respuesta (A, B, o C): ")
                # Aqui se checa si la respuesta esta mal le agrega al attemp 1 punto para que no se repita la pregunta como ya haviamos dicho antes
                if user_answer.upper() != Respuesta:
                    attempts += 1
                    if attempts<=1:
                        print("Incorrecto, intenta de nuevo.")
                # Aqui si la respuesta es correcta nos imprime correcto
                else:
                    print("Correcto!")
                    return user_answer.upper()
            # Si el usuario obtuvo 2 veces la respuesta incorrecta el while lo saca y manda imprimir lo siguiente
            print("La respuesta correcta es " + Respuesta)
            # Esto regresa la respuesta para que se cheque si puee tener un punto
            return
        # Definimos una lista que contiene adentro un diccionario con todo (Preguntas, opciones y respuestas).
        Preguntas = [
            {"Pregunta": "¿Qué es el ADN?", "Opciones": ["Una sustancia presente en las membranas celulares que impide que se salga el contenido de la célula.", "Una molécula que contiene las instrucciones para la fabricación de nuestros cuerpos.", "Una proteína presente en la sangre que ayuda a transportar oxígeno a los tejidos."],"Respuesta": "B"},
            {"Pregunta": "Muchas enfermedades pueden curarse utilizando antibióticos. Sin embargo, el éxito de algunos antibióticos frente a la fiebre puerperal ha disminuido en los últimos años. ¿Cuál es la razón de este hecho?", "Opciones": ["Una vez fabricados, los antibióticos pierden gradualmente su actividad.", "Las bacterias se hacen resistentes a los antibióticos", "Esos antibióticos sólo ayudan frente a la fiebre puerperal, pero no frente a otras enfermedades."],"Respuesta":"B"},
            {"Pregunta": "¿Cuál de las siguientes funciones es propia del pulmón?","Opciones": ["Bombear sangre oxigenada a todas las partes del cuerpo.", "Purificar la sangre reduciendo a cero su contenido en dióxido de carbono.", "Transferir el oxígeno del aire que respiras a la sangre."],"Respuesta":"C"},
            {"Pregunta": "¿Cuál de las siguientes preguntas no puede ser respondida mediante pruebas científicas?", "Opciones": ["¿En quién pensaba la víctima cuando murió?", "¿Cuál fue la causa médica o fisiológica del fallecimiento de la víctima?", "¿Constituye el raspado de la mejilla una forma segura de recoger muestras de ADN?"],"Respuesta": "A"},
            {"Pregunta": "¿Cuál es el proceso de la fotosíntesis en las plantas?","Opciones": ["Las plantas toman dióxido de carbono y producen oxígeno","Las plantas toman oxígeno y producen dióxido de carbono","Las plantas toman luz solar y producen glucosa"],"Respuesta": "C"},
            {"Pregunta": "¿Cuántas cámaras tiene el corazón humano?","Opciones": ["1","2","3"],"Respuesta": "B"},
            {"Pregunta": "¿Cuál es la función principal del sistema digestivo en nuestro cuerpo?","Opciones": ["Producir hormonas","Almacenar comida","Descomponer la comida en nutrientes utilizables"],"Respuesta": "C"},
            {"Pregunta": "¿Cómo se llaman las unidades básicas de la vida?","Opciones": ["Átomos","Células","Tejidos"], "Respuesta": "B"},
            {"Pregunta": "¿Cómo obtienen los nutrientes las plantas?","Opciones": ["A través de sus raíces del suelo","A través de sus hojas del aire","A través de su tallo del agua"],"Respuesta": "A"},
            {"Pregunta": "¿Cuál es la función principal del esqueleto en nuestro cuerpo?","Opciones": ["Proteger nuestros órganos","Almacenar minerales","Apoyar nuestro cuerpo y permitir el movimiento"],"Respuesta": "A"}
        ]
        # Definimos una puntuacion
        score = 0
        # Hacemos un loop for para tomas en cuenta en que pregunta esta y cuantas le querdan
        for Pregunta in Preguntas:
            # Aqui le preguntamos a el diccionario que si nos da una pregunta, opciones y respuesta para poderla poner nosotros
            answer = ask_question(Pregunta['Pregunta'], Pregunta['Opciones'], Pregunta['Respuesta'])
            # Esto nadamas si te la sacaste la pregunta bien le agrega un punto al puntaje
            if answer == Pregunta['Respuesta']:
                score += 1
        # Aqui imprimimos la puntuacion y el numero de preguntas en total
        print(f"Tuviste una puntuacion de {score} de {len(Preguntas)}.")
        
menu_p()

def Repetir():
    def Repetir_otra():
        Repetir=input("Gusta regresar al menu? (escriba 'Si' O 'No')")
        Repetir=Repetir.upper()
        Repetir=Repetir.strip()
        while Repetir=="SI" or Repetir=="SÍ":
            menu_p()
            Repetir=input("Gusta regresar al menu? (escriba 'Si' O 'No')")
            Repetir=Repetir.upper()
            Repetir=Repetir.strip()
        return Repetir
    Repetir=Repetir_otra()
    while (Repetir!='SI' or Repetir!='SÍ') and Repetir!='NO':
        print ('Respuesta invalida')
        print ('Porfavor intente de nuevo')
        Repetir=Repetir_otra()
    if Repetir=="NO":
        print ('Gracias por usar nuestro programa!!')
Repetir()
