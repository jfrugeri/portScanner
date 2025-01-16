# Port Scanner

Este projeto é um scanner de portas escrito em Python. Ele permite que você verifique quais portas em um determinado host estão abertas ou fechadas.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/jfrugeri/portScanner.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd portScanner
   ```
3. (Opcional) Crie um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Para usar o scanner de portas, execute o script `portScanner.py` com o endereço IP ou nome do host que você deseja verificar. Por exemplo:

```sh
python portScanner.py 192.168.1.1
```

Você também pode especificar um intervalo de portas:

```sh
python portScanner.py 192.168.1.1 20-80
```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
