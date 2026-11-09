from varasto import Varasto


def test_varasto_virheellinen_tilavuus():
    varasto = Varasto(0)
    assert varasto.tilavuus == 0.0

    varasto = Varasto(-10)
    assert varasto.tilavuus == 0.0


def test_varasto_negatiivinen_alkusaldo():
    varasto = Varasto(100, -10)
    assert varasto.saldo == 0.0


def test_varasto_alkusaldo_yli_tilavuuden():
    varasto = Varasto(100, 150)
    assert varasto.saldo == 100


def test_lisaa_negatiivinen_maara():
    varasto = Varasto(100, 50)
    varasto.lisaa_varastoon(-10)
    assert varasto.saldo == 50


def test_lisaa_liikaa():
    varasto = Varasto(100, 90)
    varasto.lisaa_varastoon(20)
    assert varasto.saldo == 100


def test_ota_negatiivinen_maara():
    varasto = Varasto(100, 50)
    tulos = varasto.ota_varastosta(-10)
    assert tulos == 0.0
    assert varasto.saldo == 50


def test_ota_liikaa():
    varasto = Varasto(100, 50)
    tulos = varasto.ota_varastosta(60)
    assert tulos == 50
    assert varasto.saldo == 0.0


def test_str():
    varasto = Varasto(100, 20)
    assert str(varasto) == "saldo = 20, vielä tilaa 80"
