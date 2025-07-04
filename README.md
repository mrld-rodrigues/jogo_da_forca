# Jogo da Forca Profissional com Pygame

![screenshot](assets/forca_screenshot.png)

## Descrição

Este é um projeto modular e profissional do clássico Jogo da Forca, desenvolvido em Python com Pygame. O código foi refatorado para ser limpo, seguro, escalável e fácil de manter, seguindo boas práticas de engenharia de software.

## Estrutura do Projeto

```
projeto_string_forca/
├── assets/                # Recursos visuais/sonoros (imagens, sons, fontes)
├── tests/                 # Testes unitários
├── ui/                    # Componentes de interface (telas, popups, efeitos, desenho da forca)
│   ├── telas.py
│   ├── popup.py
│   ├── efeitos.py
│   └── forca.py
├── config.py              # Configurações centralizadas (cores, fontes, dimensões)
├── forca_pygame.py        # Interface principal e loop do jogo
├── jogo_forca.py          # Lógica do jogo (core)
├── palavras.py            # Listas de palavras
├── LICENSE                # Licença MIT
└── README.md              # Este arquivo
```

## Como Executar

1. Instale as dependências:
   ```bash
   pip install pygame
   ```
2. Execute o jogo:
   ```bash
   python forca_pygame.py
   ```

## Testes

Os testes unitários estão na pasta `tests/` e cobrem a lógica do jogo:

```bash
python -m unittest discover tests
```

## Contribuição

- Siga o padrão de modularização e documentação do projeto.
- Use linter (recomendado: `flake8` e `black`) para padronização:
  ```bash
  pip install flake8 black
  flake8 .
  black .
  ```
- Sugestões, issues e pull requests são bem-vindos!

## Licença

MIT. Veja o arquivo `LICENSE`.

---

Sinta-se à vontade para modificar, experimentar e compartilhar!
