# PreEGS
Prediction of differential essential genes is an important field to research cell development and differentiation, drug discovery and disease causes. The goal of this work is to extract gene expression and topological changes in biomolecular networks for identifying the essential nodes or modules. Based on the random forests model, this paper proposes an essen-tial node prediction algorithm for biomolecular networks called Differential Network Analysis method based on Random Forests (DNARF). The algorithm has two main points. First, the 5-dimension eigenvector construc-tion method is put forward to extract the differential information of nodes in networks. Second, a positive sample expansion method based on the Pearson correlation coefficient is present to solve the problem that positive and negative samples may be unbalanced. In the simulated data experiments, the DNARF algorithm is compared with three other algorithms. The results prove that the DNARF has a good performance on the prediction of essential genes. In the real data experiments, four real gene regulatory networks are used as datasets. DNARF algorithm predicts five essential genes related to leukemia: HES1, STAT1, TAL1, SPI1 and RFXANK, which has been proved by literatures. Also, DNARF can be applied to other biological networks to identify new essential genes.