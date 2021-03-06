#weighted DBC Test 
library(igraph)

dictionary = "/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/m3_0.05"
setwd(dictionary)
for (filename in 1:100) {
network1=read.table(paste("rho3_0.1_",filename,"/edgelist_network1.txt",sep=""))
network2=read.table(paste("rho3_0.1_",filename,"/edgelist_network2.txt",sep=""))
important = read.table(paste("rho3_0.1_",filename,"/important.txt",sep=""))

#filename = "GSE59114"
#network1 = read.table(paste(filename,"edgelist_HSC_560_3429.txt",sep = "/"))
#network2 = read.table(paste(filename,"edgelist_MPP_576_3572.txt",sep = "/"))
#important = read.table("gold_list/GOC_GO0045595_regulation_of_cell_differentiation.txt")

g1 = graph.data.frame(network1,directed = F)
g2 = graph.data.frame(network2,directed = F)
re1 = betweenness(g1,directed = F)
re2 = betweenness(g2,directed = F)
inter = intersect(names(re1),names(re2))
result1 = abs(re1[inter]-re2[inter])
diff1 = degree(g1)/max(degree(g1))
diff2 = degree(g2)/max(degree(g2))
inter = intersect(names(diff1),names(diff2))
result2 = abs(diff1[inter]-diff2[inter])
result = 0.25*result2 + 0.75*result1
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
write.csv(diff,paste("rho3_0.1_",filename,"/DiffRank_result.csv",sep=""))
}


