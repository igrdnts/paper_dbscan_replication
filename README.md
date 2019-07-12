# paper_dbscan_replication
Repositório contendo o código e instruções de replicação dos paper 'A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise' de Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu.

## Instalando bibliotecas
O arquivo `requirements.txt` contém todas as bibliotecas necessárias para execução do processo de replicação, e eles podem ser facilmente instalados utiliando:

```
pip install -r requirements.txt
```

## Procedimento de replicação
- Substituir o arquivo `pyclustering/samples/definitions.py` da biblioteca PyClustering pelo arquivo deste repositório. Isto facilitará a utilização do benchmark SEQUOIA 2000 no processo de replicação.
- Adicionar a pasta `sequoia` dentro do diretório `pyclustering/samples/samples`
- Todas as funções utilizadas para o DBSCAN e o CLARANS estão contidas nos seguintes arquivos, respectivamente: `dbscan_rep.py` e `clarans_rep.py`.