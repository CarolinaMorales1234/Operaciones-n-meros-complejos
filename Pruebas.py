import LibreriaNúmerosComplejos as c
def test_suma():    
    assert "4+3i"==c.sumar([3,-1],[1,4]),"La respuesta debe ser 4+3i"
    assert "-1-3i"==c.sumar([-3,1],[2,-4]),"La respuesta debe ser -1-3i"
    assert "-321 + 136i"==c.sumar([-321,100],[0,36]),"La respuesta debe ser -321 + 136i"

def test_restar():
    assert "2-5i"==c.restar([3,-1][1,4]),"La respuesta debe ser 2-5i"
    assert "-5+5i"==c.restar([-3,1],[2,-4]),"La respuesta debe ser -5+5i"

def test_multiplicar():
    assert "7+11i"==c.multiplicar([3,-1],[1,4]),"La respuesta debe ser 7+11i"
    assert "7+4i"==c.multiplicar([3,-2],[1,2]),"La respuesta debe ser 7+4i"

def test_dividir():
    assert "(7-11i)/17"==c.dividir([3,1][1,4]),"La respuesta debe ser (7-11i)/17"
    assert "(-1-8i)/5"==c.dividir([3,-2][1,2]),"La respuesta debe ser (-1-8i)/5"

def test_modulo():
    assert "1.4142135623730951"==c.modulo([1,-1]),"La respuesta debe ser 1.4142135623730951"

def test_conjugado():
    assert "3-2i"==c.conjugado([3,2]),"La respuesta debe ser 3-2i"

def test_polarC():
    assert "-0.9999999999999996+1.7320508075688774i"==c.polarC([2,120]),"La respuesta debe ser -0.9999999999999996+1.7320508075688774i"

def test_cartesianoP():
    assert "1.9999999999999998e^i119.99999999999999"==c.carterianoP([-0.9999999999999996,1.7320508075688774]),"La respuesta debe ser1.9999999999999998e^i119.99999999999999"
    
