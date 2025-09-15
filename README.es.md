<font color='purple' size=2.5><i>Actualizado en agosto de 2024</i></font>
![Presentation1](https://user-images.githubusercontent.com/59842360/159695863-678be5bc-d146-4340-9592-003ad93241e1.jpg)
# Clases de Álgebra Lineal

Estas notas de clase están destinadas a cursos introductorios de álgebra lineal, adecuadas para estudiantes universitarios, programadores, analistas de datos, traders algorítmicos, etc.

Las notas de clase se basan libremente en varios libros de texto:

1. <b><i>Linear Algebra and Its Applications</i></b> por Gilbert Strang
2. <b><i>Linear Algebra and Its Applications</i></b> por David Lay
3. <b><i>Introduction to Linear Algebra With Applications</i></b> por DeFranza & Gagliardi
4. <b><i>Linear Algebra With Applications</i></b> por Gareth Williams

![cover-min](https://user-images.githubusercontent.com/59842360/83939172-64df6c00-a7e3-11ea-80b1-058af696d5a3.png)

Sin embargo, el objetivo principal del curso no es demostrar teoremas, sino mostrar las prácticas y la visualización de los conceptos. Por lo tanto, no nos involucraremos en deducciones o notaciones precisas, sino que nuestro objetivo es aclarar los conceptos esquivos y, gracias a Python/MATLAB, la tarea es mucho más fácil ahora.

## Requisitos previos
Aunque las clases son para principiantes, es beneficioso que los asistentes tengan cierta exposición al álgebra lineal y al cálculo.

Y también se espera que el asistente tenga conocimientos básicos (3 días de capacitación serían suficientes) de
- [x] Python
- [x] NumPy
- [x] Matplotlib
- [x] SymPy

Todos los códigos están escritos de una manera <b>intuitiva</b> en lugar de un estilo de codificación eficiente o profesional, por lo tanto, los códigos son extremadamente sencillos, supongo que casi nadie tendrá dificultades para entender los códigos.

## Configuración del entorno
Uso poetry para la gestión del entorno, si usas VS Code como yo, sigue los pasos a continuación:
1. En Windows Powershell e instala poetry ``` (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -p```
2. Navega a ```cd $env:APPDATA\Python\Scripts```, verifica si poetry está instalado.
3. Abre un bloc de notas ```notepad $profile``` y establece un alias para poetry ```Set-Alias poetry "C:\Users\user\AppData\Roaming\Python\Scripts\poetry.exe"``` en el bloc de notas, prefiero esta forma, porque a veces la configuración de la ruta del entorno no funciona en Windows.
4. Recarga el perfil con ```. $profile```.
5. Si estás en tu computadora personal ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser``` para relajar tu política de ejecución y elige Y.
6. Restaura la política restringida predeterminada por seguridad ```Set-ExecutionPolicy Restricted -Scope CurrentUser```.
7. Ahora verifica ```poetry --version```, si ves la versión impresa, todo listo.
8. Puedes elegir usar ```poetry update```, o simplemente gestionar la versión a tu conveniencia.

## Qué esperar de las notas
Estas notas te proporcionarán los conocimientos más necesarios y básicos para otras materias, como Ciencia de Datos, Econometría, Estadística Matemática, Ingeniería Financiera, Teoría de Control, etc., que dependen en gran medida del álgebra lineal. Por favor, sigue el tutorial con paciencia, sin duda comprenderás mejor los conceptos fundamentales del álgebra lineal. El siguiente paso es estudiar las matrices especiales y su aplicación con tu conocimiento de dominio.

## Contenidos
Por favor, accede a mi sitio web para una mejor experiencia de lectura: [Álgebra Lineal para Python](https://www.weijiechen.com/linear-algebra-with-python-book/linear-algebra-index.html)<br>
[Capítulo 1 - Sistema de Ecuaciones Lineales](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%201%20-%20Linear%20Equation%20System.html)<br>
[Capítulo 2 - Álgebra Matricial Básica](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%202%20-%20Basic%20Matrix%20Algebra.html)<br>
[Capítulo 3 - Determinante](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%203%20-%20Determinant.html)<br>
[Capítulo 4 - Factorización LU](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%204%20-%20LU%20Factorization.html)<br>
[Capítulo 5 - Suma, Resta y Multiplicación Escalar de Vectores](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%205%20-%20Vector%20Addition%2C%20Subtraction%20and%20Scalar%20Multiplication.html)<br>
[Capítulo 6 - Combinación Lineal](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%206%20-%20Linear%20Combination.html)<br>
[Capítulo 7 - Independencia Lineal](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%207%20-%20Linear%20Independence.html)<br>
[Capítulo 8 - Espacio Vectorial y Subespacio](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%208%20-%20Vector%20Space%20and%20Subspace.html)<br>
[Capítulo 9 - Base y Dimensión](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%209%20-%20Basis%20and%20Dimension.html)<br>
[Capítulo 10 - Espacio Nulo vs Espacio Columna, Espacio Fila y Rango](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2010%20-Null%20Space%20vs%20Col%20Space%2C%20Row%20Space%20and%20Rank.html)<br>
[Capítulo 11 - Transformación Lineal](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2011%20-%20Linear%20Transformation.html)<br>
[Capítulo 12 - Valores Propios y Vectores Propios](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2012%20-%20Eigenvalues%20and%20Eigenvectors.html)<br>
[Capítulo 13b - Análisis de Componentes Principales](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2013b%20-%20Principal%20Component%20Analysis.html)<br>
[Capítulo 13a - Diagonalización](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2013a%20-%20Diagonalization.html)<br>
[Capítulo 14 - Aplicaciones a Sistemas Dinámicos](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2014%20-%20Applications%20to%20Dynamic%20System.html)<br>
[Capítulo 15 - Producto Interno y Ortogonalidad](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2015%20-%20Innear%20Product%20and%20Orthogonality.html)<br>
[Capítulo 16 - Proceso de Gram-Schmidt y Descomposición QR](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2016%20-%20Gram-Schmidt%20Process%20and%20QR%20Decomposition.html)<br>
[Capítulo 17 - Matrices Simétricas, Forma Cuadrática y Descomposición de Cholesky](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2017%20-%20Symmetric%20Matrices%20%2C%20Quadratic%20Form%20and%20Cholesky%20Decomposition.html)<br>
[Capítulo 18 - La Descomposición en Valores Singulares](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2018%20-%20The%20Singular%20Value%20Decomposition.html)<br>
[Capítulo 19 - Distribución Normal Multivariada](https://www.weijiechen.com/linear-algebra-with-python-book/qmd/Chapter%2019%20-%20Multivariate%20Normal%20Distribution.html)<br>

## Ejemplos de Capturas de Pantalla
![截图01](https://user-images.githubusercontent.com/59842360/122352881-6b043e80-cf47-11eb-9ca4-8f52c93c0efa.jpg)
![截图03](https://user-images.githubusercontent.com/59842360/122352926-78212d80-cf47-11eb-9bb4-c33e03b7f085.jpg)
![截图00](https://user-images.githubusercontent.com/59842360/122352940-7b1c1e00-cf47-11eb-9f80-e26454d4baaf.jpg)
![截图00](https://user-images.githubusercontent.com/59842360/126001287-9f8de290-3940-4000-b5db-7b12d8b70005.jpg)
![截图01](https://user-images.githubusercontent.com/59842360/126001290-d342db9f-76eb-41ce-98b2-208075bd4640.jpg)
![截图02](https://user-images.githubusercontent.com/59842360/126001291-5cee0e1b-d02b-4912-9d27-65eaaff13178.jpg)
![截图03](https://user-images.githubusercontent.com/59842360/126001463-0b262316-0032-482e-bb0f-1ccbbd3a2835.jpg)