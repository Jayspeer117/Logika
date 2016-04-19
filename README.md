#Liczebniki Church'a:
Liczebniki Church'a są jednym z wielu sposobów reprezentacji liczb naturalnych.
Liczby naturalne są reprezentowane dzięki wykorzystaniu funkcji **f**, która 
wywołana n razy reprezentuje liczbę n, itp.

```
0:= f x = x
1:= f x = f ( f x )
2:= f x = f ( f ( f x ) ) 
:
:
n:= f x = f^n x
```

Liczbę n możemy uzyskiwać dzięki zwiększeniu o 1 liczby n-1. Tworzymy więc 
funkcję **successor**, która dla n wykonuje funkcję n+1 razy.

```
suc:= n f x = f ( n f x )
```

Dodawanie dwóch liczb n i m polega na wykonaniu f n+m razy.

```
add:= n m f x = n f ( m f x ) 
```

Mnożenie, analogicznie jak dodawanie, polega na wykonaniu f n*m razy.

```
mul:= n m f x = n ( m f ) x
```

Potęgowanie równierz polega na ponownej zasadzie: f wykonujemy n<sup>m</sup> razy.

```
exp = n m f x = ( n m ) f x
```
