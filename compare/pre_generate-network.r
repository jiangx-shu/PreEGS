#weighted DBC Test 
library(igraph)

dictionary = "/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/m3_0.05"
setwd(dictionary)
filepath="rho3_0.1_"
for (filename in 1:100) {
network1=read.table(paste(filepath,filename,"/matrix1.txt",sep=""),sep=",")
colnames(network1) = c(0:(ncol(network1)-1))
network1 = as.matrix(abs(network1))
g1 = graph.adjacency(network1,mode = "undirected",weighted = T)
edgelist1 = get.edgelist(g1)
write.table(edgelist1,paste(filepath,filename,"/edgelist_network1.txt",sep=""),quote = FALSE,row.names = FALSE, col.names = FALSE)

network1=read.table(paste(filepath,filename,"/matrix2.txt",sep=""),sep=",")
colnames(network1) = c(0:(ncol(network1)-1))
network1 = as.matrix(abs(network1))
g1 = graph.adjacency(network1,mode = "undirected",weighted = T)
edgelist1 = get.edgelist(g1)
write.table(edgelist1,paste(filepath,filename,"/edgelist_network2.txt",sep=""),quote = FALSE,row.names = FALSE, col.names = FALSE)
}

