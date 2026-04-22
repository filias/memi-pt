"""Paintings by Portuguese painters."""

PAINTINGS = [
    # Nuno Gonçalves (c. 1450-1491)
    "Painéis de São Vicente",
    # Vasco Fernandes (Grão Vasco, c. 1475-1542)
    "São Pedro",
    "Pentecostes",
    "Calvário",
    # Josefa de Óbidos (1630-1684)
    "Natureza-Morta com Doces e Flores",
    "O Cordeiro Pascal",
    "Menino Jesus Salvador do Mundo",
    # Domingos Sequeira (1768-1837)
    "Adoração dos Magos",
    "Alegoria da Junot",
    "A Descida da Cruz",
    # Columbano Bordalo Pinheiro (1857-1929)
    "O Grupo do Leão",
    "Retrato de Antero de Quental",
    "Concerto de Amadores",
    # José Malhoa (1855-1933)
    "O Fado",
    "Os Bêbados",
    "As Promessas",
    # Silva Porto (1850-1893)
    "Conduzindo o Rebanho",
    "A Ceifa",
    # Henrique Pousão (1859-1884)
    "Cecília",
    "Casas Brancas de Capri",
    # Amadeo de Souza-Cardoso (1887-1918)
    "Canção Popular — a Russa e o Fígaro",
    "Entrada",
    "Procissão Corpus Christi",
    # Almada Negreiros (1893-1970)
    "Retrato de Fernando Pessoa",
    "Maternidade",
    "Começar",
    # Maria Helena Vieira da Silva (1908-1992)
    "A Biblioteca",
    "A Cidade",
    "O Jogo de Xadrez",
    # Paula Rego (1935-2022)
    "A Dança",
    "O Mestre",
    "A Família",
    # Júlio Pomar (1926-2018)
    "O Almoço do Trolha",
    "Encontro de D. Sebastião e Camões",
    # Noronha da Costa (1942-2020)
    "Sem Título (Reflexos)",
    # Graça Morais (1948-)
    "Terra Transmontana",
]

# Map to English Wikipedia articles (where available)
WIKIPEDIA = {
    "Painéis de São Vicente": "Panels of Saint Vincent",
    "São Pedro": "Vasco Fernandes",
    "Pentecostes": "Vasco Fernandes",
    "Calvário": "Vasco Fernandes",
    "Natureza-Morta com Doces e Flores": "Josefa de Óbidos",
    "O Cordeiro Pascal": "Josefa de Óbidos",
    "Menino Jesus Salvador do Mundo": "Josefa de Óbidos",
    "Adoração dos Magos": "Domingos Sequeira",
    "Alegoria da Junot": "Domingos Sequeira",
    "A Descida da Cruz": "Domingos Sequeira",
    "O Grupo do Leão": "O Grupo do Leão",
    "Retrato de Antero de Quental": "Columbano Bordalo Pinheiro",
    "Concerto de Amadores": "Columbano Bordalo Pinheiro",
    "O Fado": "O Fado (painting)",
    "Os Bêbados": "José Malhoa",
    "As Promessas": "José Malhoa",
    "Conduzindo o Rebanho": "Silva Porto",
    "A Ceifa": "Silva Porto",
    "Cecília": "Henrique Pousão",
    "Casas Brancas de Capri": "Henrique Pousão",
    "Canção Popular — a Russa e o Fígaro": "Amadeo de Souza-Cardoso",
    "Entrada": "Amadeo de Souza-Cardoso",
    "Procissão Corpus Christi": "Amadeo de Souza-Cardoso",
    "Retrato de Fernando Pessoa": "Almada Negreiros",
    "Maternidade": "Almada Negreiros",
    "Começar": "Almada Negreiros",
    "A Biblioteca": "Maria Helena Vieira da Silva",
    "A Cidade": "Maria Helena Vieira da Silva",
    "O Jogo de Xadrez": "Maria Helena Vieira da Silva",
    "A Dança": "Paula Rego",
    "O Mestre": "Paula Rego",
    "A Família": "Paula Rego",
    "O Almoço do Trolha": "Júlio Pomar",
    "Encontro de D. Sebastião e Camões": "Júlio Pomar",
    "Sem Título (Reflexos)": "Noronha da Costa",
    "Terra Transmontana": "Graça Morais",
}

# Artist and date
TAGS = {
    "Painéis de São Vicente": "Nuno Gonçalves, c. 1470",
    "São Pedro": "Grão Vasco, c. 1530",
    "Pentecostes": "Grão Vasco, c. 1535",
    "Calvário": "Grão Vasco, c. 1530",
    "Natureza-Morta com Doces e Flores": "Josefa de Óbidos, c. 1676",
    "O Cordeiro Pascal": "Josefa de Óbidos, c. 1670",
    "Menino Jesus Salvador do Mundo": "Josefa de Óbidos, c. 1680",
    "Adoração dos Magos": "Domingos Sequeira, 1828",
    "Alegoria da Junot": "Domingos Sequeira, 1808",
    "A Descida da Cruz": "Domingos Sequeira, 1830",
    "O Grupo do Leão": "Columbano Bordalo Pinheiro, 1885",
    "Retrato de Antero de Quental": "Columbano Bordalo Pinheiro, 1889",
    "Concerto de Amadores": "Columbano Bordalo Pinheiro, 1882",
    "O Fado": "José Malhoa, 1910",
    "Os Bêbados": "José Malhoa, 1907",
    "As Promessas": "José Malhoa, 1933",
    "Conduzindo o Rebanho": "Silva Porto, 1893",
    "A Ceifa": "Silva Porto, 1882",
    "Cecília": "Henrique Pousão, 1882",
    "Casas Brancas de Capri": "Henrique Pousão, 1882",
    "Canção Popular — a Russa e o Fígaro": "Amadeo de Souza-Cardoso, 1916",
    "Entrada": "Amadeo de Souza-Cardoso, 1917",
    "Procissão Corpus Christi": "Amadeo de Souza-Cardoso, 1913",
    "Retrato de Fernando Pessoa": "Almada Negreiros, 1954",
    "Maternidade": "Almada Negreiros, 1935",
    "Começar": "Almada Negreiros, 1968-1969",
    "A Biblioteca": "Maria Helena Vieira da Silva, 1949",
    "A Cidade": "Maria Helena Vieira da Silva, 1951",
    "O Jogo de Xadrez": "Maria Helena Vieira da Silva, 1943",
    "A Dança": "Paula Rego, 1988",
    "O Mestre": "Paula Rego, 1984",
    "A Família": "Paula Rego, 1988",
    "O Almoço do Trolha": "Júlio Pomar, 1946-1950",
    "Encontro de D. Sebastião e Camões": "Júlio Pomar, 2003",
    "Sem Título (Reflexos)": "Noronha da Costa, 1965",
    "Terra Transmontana": "Graça Morais, 1984",
}
