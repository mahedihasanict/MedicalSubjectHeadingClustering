# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:56:54 2017

@author: Mahedi Hasan
"""
from __future__ import division
from ete2 import Tree
import math
import pyodbc
import ast
import re
import json
from sklearn.cluster import SpectralClustering



#**********Global variales*************
accuracy_dictionary={}
#*********************************

def MESHimplementForDatasets():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=MAHEDIHASAN;DATABASE=Medline;UID=sa;PWD=0000')
    cursor1=cnxn.cursor()
    cursor3=cnxn.cursor()
    cursor4=cnxn.cursor()
    
    tA=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeA.txt", format=8);
    tB=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeB.txt", format=8);
    tC=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeC.txt", format=8);
    tD=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeD.txt", format=8);
    tE=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeE.txt", format=8);
    tF=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeF.txt", format=8);
    tG=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeG.txt", format=8);
    tH=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeH.txt", format=8);
    tI=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeI.txt", format=8);
    tJ=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeJ.txt", format=8);
    tK=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeK.txt", format=8);
    tL=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeL.txt", format=8);
    tM=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeM.txt", format=8);
    tN=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeN.txt", format=8);
    tV=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeV.txt", format=8);
    tZ=Tree("F:\\Masters SPBSU\\3rd semester\\information retrieval\\MeshTreeNewickFormat\\TreeZ.txt", format=8);
    
    distance={'A':tA,'B': tB,'C': tC,'D': tD,'E': tE,'F': tF,'G': tG,'H': tH,'I': tI,'J': tJ,'K': tK,'L': tL,
    'M': tM,'N': tN,'V': tV,'Z': tZ}
    

    mesh_headinglist1=[]
    mesh_headinglist2=[]
    mesh_headingTreelist1=[]
    mesh_headingTreelist2=[]
    finalSimilarityList=[]
    AsciiDescriptor={}
    finalSimilarityListIndexer=-1
    
    
    cursor3.execute("SELECT [MESH_HEADING],[MESH_TREE_NUMBER] FROM [Medline].[dbo].[AsciiDescriptor];")
    #mesh_headingTreelist1=[]
    for row3 in cursor3.fetchall():
        AsciiDescriptor[row3.MESH_HEADING.strip()]=row3.MESH_TREE_NUMBER.replace(" ","")    
    #print AsciiDescriptor['Drosophila Proteins']
    with open('F:\\publication work\\Data\\temp\\sample_dataset.txt', 'r') as f2:
            s2 = f2.read()
            all_dataset = ast.literal_eval(s2)
    
    for key,value in all_dataset.items():
        dataset_name=key
        stri='where'
        j=0
        for i in value:
            if (j==0):
                stri=stri+' '+'TOPIC_NO='+str(i)
                j=j+1
            else:
                stri=stri+' or '+'TOPIC_NO='+str(i)
    # Declare list to create a list of the whole document set
        doc_set = list()
        pubmed_identifier_list=list()
        topic_doc_dictionary={}
        cursor1.execute("SELECT [TOPIC_NO],[PUBMED_IDENTIFIER],[MESH_MEJOR_TERMS] FROM [Medline].[dbo].[OnlyDeeplyRelaGeno2005]"+stri+";")
        for row1 in cursor1.fetchall():
            meshMejorTerms= row1.MESH_MEJOR_TERMS.strip()
            #serial_no= row1.SERIAL_NO
            topic_no=row1.TOPIC_NO
            pubmed_identifier=row1.PUBMED_IDENTIFIER
            pubmed_identifier_list.append(pubmed_identifier)
            if topic_no in topic_doc_dictionary.keys():
                topic_doc_dictionary[topic_no].append(pubmed_identifier)
            else:
                topic_doc_dictionary[topic_no]= list()
                topic_doc_dictionary[topic_no].append(pubmed_identifier)
            number_of_topics_in_a_dataset=len(topic_doc_dictionary.keys())
            doc_set.append(meshMejorTerms)
        print len(doc_set)
        for ij in range(0,len(doc_set)):
            #print ij
            finalSimilarityList.append([])
            finalSimilarityListIndexer+=1
            #mesh_headinglist1=[]
            st1=doc_set[ij]
            st1=st1.replace('[','/')
            st1=st1.replace(']','/')
            st1=st1.replace('][','/')
            mesh_headinglist1= filter(None,re.split('/',st1))
            
            for jk in range(0,len(doc_set)):
                print ij,jk
                similarity_of_MESH_sets=0
                #mesh_headinglist2=[]
                st2=doc_set[jk]
                st2=st2.replace('[','/')
                st2=st2.replace(']','/')
                st2=st2.replace('][','/')
                mesh_headinglist2= filter(None,re.split('/',st2))
    
                if(ij==jk or mesh_headinglist1==mesh_headinglist2):
                    similarity_of_MESH_sets=1
                    finalSimilarityList[finalSimilarityListIndexer].append(similarity_of_MESH_sets)
                    continue
                #y=str(jk)
                #cursor.execute("SELECT [MESH_TERMS] FROM [Medline].[dbo].[Ohsumed_20_02_16_1] where SERIAL_NO='"+y+"';")
                simMatrix=[]
                maximumSet=0
                simMatrixIndexer=-1
                similarity_of_MESH_sets=0
    
                for i in range(0,len(mesh_headinglist1)):
                    #simMatrix.append([])
                    heading1=mesh_headinglist1[i]
                    if heading1 in AsciiDescriptor.keys():
                        st3=AsciiDescriptor[heading1]
                        mesh_headingTreelist1=filter(None,re.split('also',st3))
                    if not mesh_headingTreelist1:
                        continue
                    simMatrix.append([])
                    simMatrixIndexer+=1
                    for j in range (0,len(mesh_headinglist2)):
                        maximum=0
                        simvar=0
                        valuelist=[]
                        heading2= mesh_headinglist2[j]
                        if heading1==heading2:
                            simMatrix[simMatrixIndexer].append(1)
                            continue

                        if heading2 in AsciiDescriptor.keys():
                            st4=AsciiDescriptor[heading2]
                            mesh_headingTreelist2=filter(None,re.split('also',st4))

                        if not mesh_headingTreelist2:
                            continue
                        for l in range(0,len(mesh_headingTreelist1)):
                            valuelist.append([])
                            for n in range (0,len(mesh_headingTreelist2)):
                                meshTree1=mesh_headingTreelist1[l]
                                meshTree2=mesh_headingTreelist2[n]
        
                                if(mesh_headingTreelist1[l]==mesh_headingTreelist2[n]):
                                    valuelist[l].append(1)
                                elif (meshTree1[0]==meshTree2[0]):
                                    #valuelist[l].append(1-math.log(distance[meshTree1[0]].get_distance(mesh_headingTreelist1[l],mesh_headingTreelist2[n])+1)/math.log(25))
                                    valuelist[l].append(1-math.log(distance[meshTree1[0]].get_distance(mesh_headingTreelist1[l],mesh_headingTreelist2[n])+1)/math.log(25))
                                else:
                                    valuelist[l].append(0)
                                    
                            maximum = maximum+max(valuelist[l])
            
                        for k in range(0,len(valuelist[0])):
                            maximum=maximum+max(m[k] for m in valuelist)                    
                        simvar= maximum/(len(mesh_headingTreelist1)+len(mesh_headingTreelist2))
                        simMatrix[simMatrixIndexer].append(simvar)
                        del mesh_headingTreelist2[:]
                    del mesh_headingTreelist1[:]

                for q in range (0,len(simMatrix)):
                    if not simMatrix[q]:
                        continue
                    maximumSet = maximumSet+max(simMatrix[q])
                if simMatrix:
                    for p in range(0,len(simMatrix[0])):
                        maximumSet=maximumSet+max(temp[p] for temp in simMatrix)
                if mesh_headinglist1 or mesh_headinglist2:
                    similarity_of_MESH_sets= maximumSet/(len(mesh_headinglist1)+len(mesh_headinglist2))
                finalSimilarityList[finalSimilarityListIndexer].append(similarity_of_MESH_sets)
                
                del mesh_headinglist2[:]
            del mesh_headinglist1[:]
        
        with open('F:\\publication work\\Data\\temp\\MESH_similarity.txt', 'w') as f1:
            f1.write(str(finalSimilarityList))



        with open('F:\\publication work\\Data\\temp\\8.pubmed_identifier.txt', 'w') as f3:
            f3.write(str(pubmed_identifier_list))
        
        #with open('F:\\publication work\\Data\\temp\\9.topics_list.txt', 'w') as f1:
         #   f1.write(str(list_of_topics))
        
        #print dist_of_new_docs_over_topics
        #with open('F:\\publication work\\Data\\temp\\10.distribution_of_topics_in_docs.txt', 'w') as f5:
         #   f5.write(str(dist_of_docs_over_topics))
        
        with open('F:\\publication work\\Data\\temp\\17.topic_doc_dictionary.txt','w') as f4:
            f4.write(str(topic_doc_dictionary))
        
        del doc_set
        del pubmed_identifier_list
        del topic_doc_dictionary
        

        
        
        #replaceBrackets()
        #print 'Bracket replacing completed'
        
        #keepingOnlyProbability(number_of_topics_produced)
        #print 'Keeping only probability completed'
        
        #distanceFromJSD()
        #print 'Measuring distance completed'
        
        #similarityFromJSD()
        #print 'Measuring similarity completed'
        
        spectralClustering(number_of_topics_in_a_dataset,finalSimilarityList)
        print 'Spectral clustering completed'
        
        combiningClusterResult(dataset_name)
        print 'Combining clustering result completed'
        
        accuracyMeasure(dataset_name)
        print 'Measuring accuracy completed'
        
    with open('F:\\publication work\\Data\\temp\\18.NMI_dictionary.txt','w') as f6:
        f6.write(str(accuracy_dictionary))
        
        
    #f1.close()
    f2.close()
    f3.close()
    f4.close()
    #f5.close()
    f6.close()
    cursor1.close()
    cursor3.close()
    cursor4.close()
    cnxn.close()


def spectralClustering(number_of_topics_in_a_dataset,similarity_list): 
    spectral = SpectralClustering(n_clusters=number_of_topics_in_a_dataset,affinity="precomputed")
    spectral.fit(similarity_list)
    
    spectral_label=list()
    
    for lab2 in spectral.labels_:
        spectral_label.append(lab2)
    with open('F:\\publication work\\Data\\temp\\15.spectral_labels.txt','w') as f7:
        f7.write(str(spectral_label))
    
    del spectral_label
    del spectral
    f7.close()



def keepingOnlyProbability(number_of_topics_produced):
    dist_of_new_docs_over_topics_OnlyProb=list()
    dist_of_new_docs_indexer=-1
    f8 = open('F:\\publication work\\Data\\temp\\11.distribution_of_topics_in_docs_bracket_replaced.txt','r')
    #f2 = open('F:\\Masters SPBSU\\4th semester\\Information retrival\\Output\\dist_of_docs_over_topics200OnlyProb.txt','w')
    
    df=json.load(f8)
    for i in df:
        dist_of_new_docs_over_topics_OnlyProb.append([])
        dist_of_new_docs_indexer+=1
        #print(i)
        for j in range(0,number_of_topics_produced):
            dist_of_new_docs_over_topics_OnlyProb[dist_of_new_docs_indexer].append(0)
        for x in i:
            dist_of_new_docs_over_topics_OnlyProb[dist_of_new_docs_indexer][x[0]]=x[1];
            
    with open('F:\\publication work\\Data\\temp\\12.distribution_of_topics_in_docs_bracket_replaced_only_prob.txt','w') as f9:
        f9.write(str(dist_of_new_docs_over_topics_OnlyProb))
    
    del dist_of_new_docs_over_topics_OnlyProb
    del df
    f8.close
    f9.close




def accuracyMeasure(dataset_name):
    number_of_documents_in_dataset=0
    number_of_documents_in_cluster={}
    number_of_documents_in_class={}
    number_of_documents_common_in_class_and_cluster={}
    sum_class=0
    sum_cluster=0
    sum_common=0
    
    with open('F:\\publication work\\Data\\temp\\17.topic_doc_dictionary.txt', 'r') as f2:
            s2 = f2.read()
            class_dictionary = ast.literal_eval(s2)
    for key, value in class_dictionary.items():
         number_of_documents_in_class[key]=len(value)
    number_of_documents_in_dataset=sum(number_of_documents_in_class.values())
    for i in number_of_documents_in_class.values():
        sum_class=sum_class+i*(math.log(i)-math.log(number_of_documents_in_dataset))
        
    
    with open('F:\\publication work\\Data\\temp\\16.spectral_clustering_results'+dataset_name+'.txt', 'r') as f1:
            s1 = f1.read()
            cluster_dictionary = ast.literal_eval(s1)
    for key, value in cluster_dictionary.items():
         number_of_documents_in_cluster[key]=len(value)
    for i in number_of_documents_in_cluster.values():
        sum_cluster=sum_cluster+i*(math.log(i)-math.log(number_of_documents_in_dataset))
    
    for key_class,value_class in class_dictionary.items():
        for key_cluster,value_cluster in cluster_dictionary.items():
          common_doc_counter=0
          for i in value_class:
              if i in value_cluster:
                  common_doc_counter=common_doc_counter+1
          number_of_documents_common_in_class_and_cluster[key_class,key_cluster]=common_doc_counter
          a=math.log(number_of_documents_in_dataset)
          b=0.000000000000000000
          if common_doc_counter:
              b=math.log(common_doc_counter)
          c=math.log(number_of_documents_in_class[key_class])
          d=math.log(number_of_documents_in_cluster[key_cluster])
          sum_common=sum_common+common_doc_counter*(a+b-c-d)
    
    NMI=sum_common/math.sqrt(sum_class*sum_cluster)
    accuracy_dictionary[dataset_name]=NMI
    print 'The NMI is: '+str(NMI)
    
    
    with open('F:\\publication work\\Data\\temp\\19.(Extra)number_of_documents_common_in_class_and_cluster.txt','w') as f4:
        f4.write(str(number_of_documents_common_in_class_and_cluster))
    
    del number_of_documents_in_cluster
    del number_of_documents_in_class
    #del number_of_documents_common_in_class_and_cluster
    del class_dictionary
    del cluster_dictionary
    
    f1.close()
    f2.close()
    #f3.close()
    f4.close()



def combiningClusterResult(dataset_name):
    clusterResult={}
    with open('F:\\publication work\\Data\\temp\\8.pubmed_identifier.txt', 'r') as f:
            s = f.read()
            whip = ast.literal_eval(s)
    
    with open('F:\\publication work\\Data\\temp\\15.spectral_labels.txt', 'r') as f1:
            s1 = f1.read()
            df = ast.literal_eval(s1)
    
    for index, items in enumerate(df):
        if items in clusterResult:
            clusterResult[items].append(whip[index])
        else:
            clusterResult[items]= list()
            clusterResult[items].append(whip[index])
    
    with open('F:\\publication work\\Data\\temp\\16.spectral_clustering_results'+dataset_name+'.txt','w') as f2:
        f2.write(str(clusterResult))
    
    del clusterResult
    del whip
    del df
    f.close()
    f1.close()
    f2.close()



MESHimplementForDatasets()