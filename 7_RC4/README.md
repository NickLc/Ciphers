# RC4

RC4 es un método de cifrado de flujo que fue diseñado por Ron Rivest de RSA Security en 1987, estuvo como un secreto comercial por aproximadamente 7 años, luego fue filtrado.

## Caracteristicas

- Simple de implementar.
- Rapidez en la ejecución.
- Es un cifrado de flujo.
- Criptosistema simetrico, utiliza la misma clave para cifrar y descifrar.
- No es muy recomendado en los nuevos sistemas.
- Clave restringida de 1 a 256 caracteres.

## Implemetación

Se implementa el algoritmo RC4 en el lenguaje python definiendo una clase llamada Rc4, el cifrado se divide en dos partes:

### Key-scheduling algorithm (KSA)

Definimos la función KSA en la clase Rc4 que recibe como input una clave

```py
def KSA(self, key):
```

Se inicializa el vector de estados o caja S de tamaño 8x8 con los valores de 0 a 255.

```py
i=0
S = [i for i in range(256)]
```

Luego convertimos la clave, repitiendo y contanetando hasta que tenga 256 cifras.

```py
newkey = key * int(math.ceil(256/len(key)))
newkey = newkey[:256]
```

Se define un K_ord que contiene un entero representando el unicode de cada letra.

```py
K_ord = [ord(i) for i in newkey]
```

Finalmente realizamos la mezcla del vector S, intercambiando uno a uno en toda la longitud del vector S y retornamos el nuevo S.

```py
j = 0
for i in range(256):
    j = (j + S[i]+ K_ord[i]) % 256
    S[i], S[j] = S[j] , S[i]

return(S)
```

### Pseudo-random generation algorithm (PRGA)

En esta parte se genera la clave de flujo(KeyStream), se define una funcion PRGA que recibe el S de la funcion KSA y la longitud del mensaje que se va cifrar.

```py
def PRGA(self, S, len_text):
```

Luego definimos el KeyStream, que realizamos un recorrido en todo la longitud de texto a cifrar.

```py
for m in range(len_text):
```

Asignamos los valores a dos índices i y j que nos ayudarán a recorrer en la tomar valores de S.

```py
i = (m+1) % 256
j = (j+S[i]) % 256
```

Intercambiamos los valores en S y asignamos el valor en la clave de flujo sumando los valores de S con los índices i y j.

```py
S[i], S[j] = S[j], S[i]
t = (S[i] + S[j]) % 256
Key_Stream.append(S[t])
```

![Proceso de RGCA](E:/UNI/9-CICLO/Topicos III - Seguridad/Ciphers/7_RC4/img/RC4.png)

Finalmente retornamos KeyStream.

```py
return Key_Stream
```

### Metodos Extras

Adicinal a KSA y PRGA definimos los siguientes metodos.

- strToOrd: pasar un string a un array de enteros unicode.
- srtToHex: pasar un string a un string con los valores en hexadecimal.
- xor: realizar un xor entre dos arrays con la cual se encripta el mensaje.

```py
def strToOrd(self, text):
        num = [ord(i) for i in text]
        return num

def strToHex(self, text):
    text_hex = ''.join(format(ord(i), "x") for i in text)
    return str.upper(text_hex)

def xor(self, arr_a, arr_b):
    result = [a^b for a,b in zip(arr_a, arr_b)]
    return result

```

## Demo

Se realiza una demo simple con la libreria tkinter de python.

### Encriptar

En la demo selecciomos el metodo encriptar, ingresamos la clave, ingresamos el texto de encriptar y ejecutamos el boton start.

![Proceso de RGCA](E:/UNI/9-CICLO/Topicos III - Seguridad/Ciphers/7_RC4/img/test_encriptar_wikipedia.png)

### Desencriptar

En la demo selecciomos el metodo desencriptar, ingresamos la clave, ingresamos el texto de desencriptar (copiamos el texto encriptado) y ejecutamos el boton start.

![Proceso de RGCA](E:/UNI/9-CICLO/Topicos III - Seguridad/Ciphers/7_RC4/img/test_desencriptar_wikipedia.png)

