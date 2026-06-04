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
    # Domingos Sequeira (1768-1837)
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
    "Procissão Corpus Christi",
    # Almada Negreiros (1893-1970)
    "Retrato de Fernando Pessoa",
    "Gare Marítima de Alcântara",
    # Mário Eloy (1900-1951)
    "A Fuga",
    # Abel Manta (1888-1982)
    "Retrato de João da Silva",
    # Carlos Botelho (1899-1982)
    "Lisboa",
    # Vieira da Silva (1908-1992)
    "A Cidade",
    # Paula Rego (1935-2022)
    "A Dança",
    # Júlio Pomar (1926-2018)
    "Atelier-Museu Júlio Pomar",
    # Bordalo II (1987-)
    "Half Rabbit",
    # Joana Vasconcelos (1971-)
    "Coração Independente",
]

# Wikimedia Commons filenames — direct painting/artwork images
COMMONS_FILES = {
    "Painéis de São Vicente": "Nuno gonçalves, pannelli di san vincenzo, 1470 ca. 02.jpg",
    "São Pedro": "São Pedro de Grão Vasco, Museu Grão Vasco b.jpg",
    "Pentecostes": "Grão Vasco, Pentecostes, da capela da portaria do mosteiro de Santa Cruz de Coimbra, 1534-35, assinada Velasco.jpg",
    "Calvário": "Calvario GraoVasco.jpg",
    "Natureza-Morta com Doces e Flores": "JosefaObidos4.jpg",
    "A Descida da Cruz": "Descida da Cruz (1827) - Domingos Sequeira.png",
    "O Grupo do Leão": "Grupo do Leão by Columbano Bordalo Pinheiro.jpg",
    "Retrato de Antero de Quental": "Retrato de Antero de Quental (1889) - Columbano Bordalo Pinheiro (MNAC Inv. 1108).png",
    "Concerto de Amadores": "Estudo para Concerto de amadores (1882) by Columbano Bordalo Pinheiro.jpg",
    "O Fado": "Jose malhoa fado.jpg",
    "Os Bêbados": "Jose malhoa bebados.jpg",
    "As Promessas": "Malhoa February 2015-3a.jpg",
    "Conduzindo o Rebanho": "Silva Porto-06.jpg",
    "A Ceifa": "A Ceifa (Lumiar) Silva Porto CMAG Lisboa 01.jpg",
    "Cecília": "Cecilia Henrique Pousão 1882.jpg",
    "Casas Brancas de Capri": "Pousao casas-brancas1.jpg",
    "Canção Popular — a Russa e o Fígaro": "Amadeo de Souza-Cardoso-7.jpg",
    "Procissão Corpus Christi": "Amadeo de Souza-Cardoso, 1913 - Procissão Corpus Christi.JPG",
    "Retrato de Fernando Pessoa": "Orpheu group - Fernando Pessoa (1915) - Almada Negreiros (April 7, 1893 – June 15, 1970) (16762939799).jpg",
    "Gare Marítima de Alcântara": "Alcântara terminal with murals by Almada Negreiros (02).jpg",
    "A Fuga": "A Fuga, 1938-39, Mário Eloy, FCG 01.jpg",
    "Retrato de João da Silva": "ABEL MANTA Joao da Silva 1919.jpg",
    "Lisboa": "Carlos Botelho, Lisboa - Lisbon, 1962, oil on canvas, 54 x 76,5 cm,.jpg",
    "A Cidade": "Philosopher -A replica of a section of the wall covering the Lisbon University City Metro station- (1988) - Maria Helena Vieira da Silva (1908-1992) (49801619896).jpg",
    "A Dança": "Paula Rego's Studio 2007.jpg",
    "Atelier-Museu Júlio Pomar": "Atelier-Museu Júlio Pomar.jpg",
    "Half Rabbit": "Portugal 090716 Street Art Bordalo II 02.jpg",
    "Coração Independente": "2014 Erywań, Park przy Kaskadach (08).jpg",
}

TAGS = {
    "Painéis de São Vicente": "Nuno Gonçalves, c. 1470",
    "São Pedro": "Grão Vasco, c. 1530",
    "Pentecostes": "Grão Vasco, 1535",
    "Calvário": "Grão Vasco, c. 1530",
    "Natureza-Morta com Doces e Flores": "Josefa de Óbidos, c. 1676",
    "A Descida da Cruz": "Domingos Sequeira, 1827",
    "O Grupo do Leão": "Columbano Bordalo Pinheiro, 1885",
    "Retrato de Antero de Quental": "Columbano Bordalo Pinheiro, 1889",
    "Concerto de Amadores": "Columbano Bordalo Pinheiro, 1882",
    "O Fado": "José Malhoa, 1910",
    "Os Bêbados": "José Malhoa, 1907",
    "As Promessas": "José Malhoa, 1890",
    "Conduzindo o Rebanho": "Silva Porto, c. 1880",
    "A Ceifa": "Silva Porto, 1893",
    "Cecília": "Henrique Pousão, 1882",
    "Casas Brancas de Capri": "Henrique Pousão, 1882",
    "Canção Popular — a Russa e o Fígaro": "Amadeo de Souza-Cardoso, 1916",
    "Procissão Corpus Christi": "Amadeo de Souza-Cardoso, 1913",
    "Retrato de Fernando Pessoa": "Almada Negreiros, 1915",
    "Gare Marítima de Alcântara": "Almada Negreiros, 1943-45",
    "A Fuga": "Mário Eloy, 1938-39",
    "Retrato de João da Silva": "Abel Manta, 1919",
    "Lisboa": "Carlos Botelho, 1962",
    "A Cidade": "Vieira da Silva, 1988",
    "A Dança": "Paula Rego, 1988",
    "Atelier-Museu Júlio Pomar": "Júlio Pomar",
    "Half Rabbit": "Bordalo II",
    "Coração Independente": "Joana Vasconcelos",
}

WIKIPEDIA = {}
