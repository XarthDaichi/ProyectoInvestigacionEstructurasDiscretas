ALPHABET_SIZE = 256


def bm(pat, txt):
    sizeP = len(pat)
    sizeT = len(txt)
    ocurrences = []
    cont = 0

    # NO CONTADA EN LA INSTRUMENTACION
    # --- 0. SUFFIXES TABLE ---
    suff = [0 for i in range(sizeP)]
    suff[sizeP-1] = sizeP
    g = sizeP - 1
    f = 0
    for i in range(sizeP-2, -1, -1):
        if i > g and suff[i + sizeP - 1 - f] < i-g:
            suff[i] = suff[i + sizeP - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pat[g] == pat[g + sizeP - 1 - f]:
                g -= 1
            suff[i] = f-g

    # --- 1. BAD CHARACTER TABLE ---
    bcT = []
    # This part is changed on the instrumentation section. Here we use List Comprehension.
    bcT = []
    for i in range(ALPHABET_SIZE):
        cont += 1
        bcT.append(sizeP)
    for j in range(sizeP):
        cont += 1
        bcT[ord(pat[j])] = sizeP - j

    # --- 2. GOOD SUFFIX TABLE ---
    gsT = []
    gsT = [sizeP for i in range(sizeP)]
    for i in range(sizeP-1, -1, -1):
        if suff[i] == i+1:
            for j in range(0, sizeP-1-i):
                cont += 1
                if gsT[j] == sizeP:
                    gsT[j] = sizeP - 1 - i
    for i in range(0, sizeP-1):
        cont += 1
        gsT[sizeP-1-suff[i]] = sizeP - 1 - i

    # --- 3. SEARCH STAGE ---
    for i in range(0, sizeT-sizeP+1):
        submatch = 0
        for j in range(sizeP-1, -1, -1):
            cont += 1
            if(pat[j] != txt[i+j]):
                break
            submatch += 1
        if submatch == sizeP:
            ocurrences.append(f"Ocurrence at index {i}!")
        else:
            i += max(bcT[ord(txt[i+j])], gsT[j])
    return cont


print(bm('aa', 'aaaa'))
