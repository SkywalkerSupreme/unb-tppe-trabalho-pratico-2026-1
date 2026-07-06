# src/main.py
import os
import sys
import json
from src.curador import Curador, FormatoInvalidoError, IdInvalidoError

def rodar_curadoria():
    print("=" * 60)
    print("SISTEMA DE CURADORIA E DEDUPLICAÇÃO DE DADOS CIENTÍFICOS")
    print("=" * 60)

    # Resolve o caminho do arquivo JSON de forma relativa e segura
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_base_dados = os.path.join(diretorio_atual, "tests", "data", "dados_curadoria_800.json")

    print(f"[*] Localização da base de dados: {caminho_base_dados}")
    
    curador = Curador()

    try:
        # 1. Carrega os dados reais do arquivo JSON
        if not os.path.exists(caminho_base_dados):
            raise FileNotFoundError(f"Arquivo JSON não encontrado no caminho: {caminho_base_dados}")
            
        with open(caminho_base_dados, "r", encoding="utf-8") as arquivo:
            registros_brutos = json.load(arquivo)
            
        total_originais = len(registros_brutos)
        print(f"[*] Base de dados carregada com sucesso. Total de registros brutos: {total_originais}")

        # 2. Executa a validação estrutural do lote (Método do Curador)
        print("[*] Validando integridade e contratos do dataset...")
        curador.processar_base_dados(registros_brutos)
        
        # 3. Prepara a entrada para a consolidação de IDs (Mapeia id_bruto -> nome_bruto)
        print("[*] Alimentando o motor de deduplicação e gerando assinaturas fonéticas...")
        dicionario_autores = {}
        for reg in registros_brutos:
            # Converte para string pois o método consolidar_ids espera chaves em string como nos testes
            dicionario_autores[str(reg["id"])] = reg["nome"]

        # 4. Executa a consolidação e unificação dos identificadores padrão-ouro
        base_padrao_ouro = curador.consolidar_ids(dicionario_autores)
        
        # Como o retorno de consolidar_ids é um dicionário {id: nome}, o total único são os valores distintos
        total_unicos = len(set(base_padrao_ouro.values()))

        print("\n[+] Curadoria executada com SUCESSO!")
        print(f"[+] Total de registros científicos analisados: {total_originais}")
        print(f"[+] Total de autores unificados (Padrão-Ouro): {total_unicos}")
        print(f"[+] Redução de redundância: {total_originais - total_unicos} registros duplicados eliminados.")
        
        print("\n[*] Amostragem dos primeiros 5 registros consolidados (ID -> Nome Padrão-Ouro):")
        # Pega os primeiros 5 elementos do dicionário final para exibir
        primeiros_pares = list(base_padrao_ouro.items())[:5]
        for id_ouro, nome_ouro in primeiros_pares:
            print(f"  - ID: {id_ouro} -> Autor Consolidado: {nome_ouro}")
            
    except FileNotFoundError as e:
        print(f"[ERR] Erro Crítico de Infraestrutura: {e}")
        sys.exit(1)
    except FormatoInvalidoError:
        print("[ERR] Erro de Formatação: O JSON fornecido possui campos inválidos ou ausentes.")
        sys.exit(1)
    except IdInvalidoError:
        print("[ERR] Erro de Contrato: Identificadores menores ou iguais a zero detectados na base.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("[ERR] Erro de Sintaxe: O arquivo JSON está corrompido.")
        sys.exit(1)

    print("=" * 60)

if __name__ == "__main__":
    rodar_curadoria()