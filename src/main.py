import os
import sys
from curador import Curador, FormatoInvalidoError, IdInvalidoError

def rodar_curadoria():
    print("=" * 60)
    print("SISTEMA DE CURADORIA E DEDUPLICAÇÃO DE DADOS CIENTÍFICOS")
    print("=" * 60)

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_base_dados = os.path.join(diretorio_atual, "tests", "data", "dados_curadoria_800.json")

    print(f"[*] Localização da base de dados: {caminho_base_dados}")
    
    curador = Curador()

    try:
        print("[*] Início do processamento do motor (Fase GREEN)...")
        base_padrao_ouro = curador.processar_base_dados(caminho_base_dados)
        
        print("\n[+] Curadoria executada com SUCESSO!")
        print(f"[+] Total de registros originais analisados: {len(curador.dados)}")
        print(f"[+] Total de autores unificados (Padrão-Ouro): {len(base_padrao_ouro)}")
        print(f"[+] Redução de duplicidade: {len(curador.dados) - len(base_padrao_ouro)} registros limpos.")
        
        print("\n[*] Amostragem dos primeiros 5 registros do Padrão-Ouro:")
        for registro in base_padrao_ouro[:5]:
            print(f"  - ID: {registro['id']} | Autor: {registro['nome']} | Área: {registro.get('area_pesquisa', 'N/A')}")
            
    except FileNotFoundError as e:
        print(f"[ERR] Erro Crítico: {e}")
        sys.exit(1)
    except FormatoInvalidoError as e:
        print(f"[ERR] Erro de Formatação do JSON: {e}")
        sys.exit(1)
    except IdInvalidoError as e:
        print(f"[ERR] Erro de Contrato (ID Inválido): {e}")
        sys.exit(1)

    print("=" * 60)

if __name__ == "__main__":
    rodar_curadoria()