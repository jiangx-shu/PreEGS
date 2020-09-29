#weighted DBC Test 
library(igraph)

dictionary = "/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/m3_0.05"
setwd(dictionary)
for (filename in 1:100){ 
  network1=read.table(paste("rho3_0.1_",filename,"/edgelist_network1.txt",sep=""))
  network2=read.table(paste("rho3_0.1_",filename,"/edgelist_network2.txt",sep=""))
  important = read.table(paste("rho3_0.1_",filename,"/important.txt",sep=""))

g1 = graph.data.frame(network1,directed = F)
g2 = graph.data.frame(network2,directed = F)
re1 = eigen_centrality(g1,directed = F)
re2 = eigen_centrality(g2,directed = F)
re1 = re1$vector
re2 = re2$vector
inter = intersect(names(re1),names(re2))
new_re1 = re1[match(inter,names(re1))]
new_re2 = re2[match(inter,names(re2))]
result = abs(new_re1-new_re2)
#result = result[order(result,decreasing = T)]
#table(names(result)%in%important$V2)
#degree
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
write.csv(diff,paste("rho3_0.1_",filename,"/DEC_result.csv",sep=""))
}
