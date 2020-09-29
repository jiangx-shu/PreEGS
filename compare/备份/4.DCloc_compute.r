#weighted DCloc Test 
library(igraph)
dictionary = "D:/COML/Network flow/4_single_cell_rna_seq_datasets_comparison"
setwd(dictionary)

c.test <- function(n, x, y) {
  stan.dev <- sqrt(2/(n - 3))
  dist <- x-y
  z <- abs(dist/stan.dev)
  p <- 2*(1 - pnorm(z))
  return(c(p,z))
}

### Fisher transformation
fisherr2z <- function(r) {
  z <- log((1 + r)/(1 - r)) / 2
  return(z)
}

### Inverse Fisher transformation
fisherz2r <- function(z) {
  r <- (exp(2 * z) - 1)/(1 + exp(2 * z))
  return(r)
}

DCloc  <- function(Mat.A, Mat.B, n.supp=100, r.min=0, r.max=fisherz2r(2.5), min.neigh=3) {
  
  cat("Computing correlation matrices ...\n")
  ngenes <- nrow(Mat.A)
  #cor.A <- cor(t(Mat.A))
  #cor.B <- cor(t(Mat.B))
  #for(i in 1:ngenes){
  #    cor.A[i,i]<-0
  #    cor.B[i,i]<-0
  #}
  #cor.A <- fisherr2z(cor.A)
  #cor.B <- fisherr2z(cor.B)
  cor.A = Mat.A
  cor.B = Mat.B
  inter = intersect(colnames(cor.A),colnames(cor.B))
  z.min <- fisherr2z(r.min)
  z.max <- fisherr2z(r.max)
  z <- seq(z.min, z.max, length.out=n.supp)
  
  #Computing the topological dissimilarity
  result <- list()
  for (x in c("nA", "nB", "one", "both", "d")) {
    result[[x]] <- matrix(nrow=length(inter), ncol=n.supp, 0)
    rownames(result[[x]]) <- inter
    colnames(result[[x]]) <- z
  }
  
  for (j in 1:n.supp) {
    z.thres <- z[j]
    cat(j, ". threshold r >= ", fisherz2r(z.thres), "\n", sep="")
    network.A <- (cor.A >= z.thres)
    network.B <- (cor.B >= z.thres)
    for (i in inter) {
      index.A <- which(network.A[i, ]==1)
      index.B <- which(network.B[i, ]==1)
      result$nA[i, j] <- length(index.A)
      result$nB[i, j] <- length(index.B)
      result$both[i, j] <- length(intersect(index.A, index.B))
      result$one[i, j] <- length(union(index.A, index.B))
      
      if( result$one[i, j] >= min.neigh ) {
        result$d[i, j] <-(( 1 - result$both[i, j]/result$one[i, j] )* sign(result$nA[i, j] - result$nB[i, j]))
      }
      
    }
  }
  
  cat("Averaging of the results... \n")
  ret <- matrix(ncol=4,nrow=length(inter),0)
  colnames(ret) <- c("abs.top.dissim", "top.dissim", "mean.neigh.A", "mean.neigh.B")
  rownames(ret) <- inter
  ret[ ,1] <- apply(result$d, 1, function(x){mean(abs(x))})
  ret[ ,2] <- apply(result$d, 1, mean)
  ret[ ,3] <- apply(result$nA, 1, mean)
  ret[ ,4] <- apply(result$nB, 1, mean)
  return(ret)
}


important = read.table("gold_list/GOC_GO0045595_regulation_of_cell_differentiation.txt")

### GSE59114
data_fold = "GSE59114/compute_all_again"
network1 = read.table(paste(data_fold,"edgelist_HSC.txt",sep = "/"))
g1 = graph.data.frame(network1,directed = F)
#or another writing version
MAT1 = abs(as.matrix(get.adjacency(g1,attr = "V3")))
#E(g1)$weight = network1$V3
#MAT1 = abs(as.matrix(get.adjacency(g1,attr = "weight")))
network2 = read.table(paste(data_fold,"edgelist_MPP.txt",sep = "/"))
g2 = graph.data.frame(network2,directed = F)
MAT2 = abs(as.matrix(get.adjacency(g2,attr = "V3")))
result = DCloc(MAT1,MAT2)
result = result[,2]
inter = intersect(colnames(MAT1),colnames(MAT2))
g1_degree = degree(g1,inter)
g2_degree = degree(g2,inter)
diff_degree = abs(g1_degree-g2_degree)
#closeness_centrality
g1_closeness = closeness(g1,inter)
g2_closeness = closeness(g2,inter)
diff_closeness = abs(g1_closeness-g2_closeness)
#pageRank_centrality
g1_pageRank = page_rank(g1,vids = inter)
g1_pageRank = g1_pageRank$vector
g2_pageRank = page_rank(g2,vids = inter)
g2_pageRank = g2_pageRank$vector
diff_pageRank = abs(g1_pageRank-g2_pageRank)

diff = data.frame(result,names(result)%in%important$V2,
                  g1_degree,g2_degree,diff_degree,
                  g1_closeness,g2_closeness,diff_closeness,
                  g1_pageRank,g2_pageRank,diff_pageRank
)
diff = diff[order(diff$result,decreasing = T),]
diff$rank = c(1:length(inter))
write.csv(diff,paste(data_fold,"DCloc_result.csv",sep = "/"))



### GSE76381
data_fold = "GSE76381/compute_all_again"
network1 = read.table(paste(data_fold,"edgelist_NPC.txt",sep = "/"))
g1 = graph.data.frame(network1,directed = F)
#or another writing version
MAT1 = abs(as.matrix(get.adjacency(g1,attr = "V3")))
#E(g1)$weight = network1$V3
#MAT1 = abs(as.matrix(get.adjacency(g1,attr = "weight")))
network2 = read.table(paste(data_fold,"edgelist_RGL.txt",sep = "/"))
g2 = graph.data.frame(network2,directed = F)
MAT2 = abs(as.matrix(get.adjacency(g2,attr = "V3")))
result = DCloc(MAT1,MAT2)
result = result[,2]
inter = intersect(colnames(MAT1),colnames(MAT2))
g1_degree = degree(g1,inter)
g2_degree = degree(g2,inter)
diff_degree = abs(g1_degree-g2_degree)
#closeness_centrality
g1_closeness = closeness(g1,inter)
g2_closeness = closeness(g2,inter)
diff_closeness = abs(g1_closeness-g2_closeness)
#pageRank_centrality
g1_pageRank = page_rank(g1,vids = inter)
g1_pageRank = g1_pageRank$vector
g2_pageRank = page_rank(g2,vids = inter)
g2_pageRank = g2_pageRank$vector
diff_pageRank = abs(g1_pageRank-g2_pageRank)

diff = data.frame(result,names(result)%in%important$V2,
                  g1_degree,g2_degree,diff_degree,
                  g1_closeness,g2_closeness,diff_closeness,
                  g1_pageRank,g2_pageRank,diff_pageRank
)
diff = diff[order(diff$result,decreasing = T),]
diff$rank = c(1:length(inter))
write.csv(diff,paste(data_fold,"DCloc_result.csv",sep = "/"))



### PRJNA324289
data_fold = "PRJNA324289/compute_all_again"
network1 = read.table(paste(data_fold,"edgelist_NSC.txt",sep = "/"))
g1 = graph.data.frame(network1,directed = F)
#or another writing version
MAT1 = abs(as.matrix(get.adjacency(g1,attr = "V3")))
#E(g1)$weight = network1$V3
#MAT1 = abs(as.matrix(get.adjacency(g1,attr = "weight")))
network2 = read.table(paste(data_fold,"edgelist_NPC.txt",sep = "/"))
g2 = graph.data.frame(network2,directed = F)
MAT2 = abs(as.matrix(get.adjacency(g2,attr = "V3")))
result = DCloc(MAT1,MAT2)
result = result[,2]
inter = intersect(colnames(MAT1),colnames(MAT2))
g1_degree = degree(g1,inter)
g2_degree = degree(g2,inter)
diff_degree = abs(g1_degree-g2_degree)
#closeness_centrality
g1_closeness = closeness(g1,inter)
g2_closeness = closeness(g2,inter)
diff_closeness = abs(g1_closeness-g2_closeness)
#pageRank_centrality
g1_pageRank = page_rank(g1,vids = inter)
g1_pageRank = g1_pageRank$vector
g2_pageRank = page_rank(g2,vids = inter)
g2_pageRank = g2_pageRank$vector
diff_pageRank = abs(g1_pageRank-g2_pageRank)

diff = data.frame(result,names(result)%in%important$V2,
                  g1_degree,g2_degree,diff_degree,
                  g1_closeness,g2_closeness,diff_closeness,
                  g1_pageRank,g2_pageRank,diff_pageRank
)
diff = diff[order(diff$result,decreasing = T),]
diff$rank = c(1:length(inter))
write.csv(diff,paste(data_fold,"DCloc_result.csv",sep = "/"))