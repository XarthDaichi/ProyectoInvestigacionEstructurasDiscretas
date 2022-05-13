
def fuerza_bruta_instrumentado(txt, patron):
    N = len(txt)
    M = len(patron)
    i = 0
    cont = 0
    while i <= (N - M):
        j = 0
        while j < M:
            cont += 3
            if txt[i+j] != patron[j]:
                break
            j += 1
        if j == M:
            return cont
        i += 1
    return cont

def test_maxima_in_matrix_instrumentado(filename):
    file = open(filename, 'w')
    file.write('txt_const;pat_var;time;txt_var;pat_const;time\n')
    for i in range(2, 21, 1):
        txt = "aaaaaaaaaaaaaaaaaaah"
        pat = "a" * i
        l = list(pat)
        l[len(pat) - 1] = 'h'
        pat = "".join(l)

        txt2 = "aaa" * i
        pat2 = "ah"
        l2 = list(txt2)
        l2[len(txt2) - 1] = 'h'
        txt2 = "".join(l)

        file.write(f"{20};{len(pat)};{fuerza_bruta_instrumentado(txt, pat)};{len(txt2)};{2};{fuerza_bruta_instrumentado(txt2, pat2)}\n")
    file.close

test_maxima_in_matrix_instrumentado('/Users/derekrm/Documents/UNA/Discretas/Python/fuerza_bruta_instrumentado.csv')

#https://programmerclick.com/article/21021656414/