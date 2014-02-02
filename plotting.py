#!/usr/bin/env python
import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt



from misc import zeros
from main import load_data


def main():
    data = load_data()

    hgraph = nx.Graph(data.humanppi)
    fgraph = nx.Graph(data.functions)

    #plot_cp_degree(hgraph)
    #plot_fn_degree(hgraph, fgraph)
    #plot_fn_cp_weight(hgraph, fgraph)

def plot_cp_degree(hgraph):
    cps = [p for p in hgraph.nodes() if p.is_cancer_protein()]
    ps = [p for p in hgraph.nodes() if not p.is_cancer_protein()]

    cp_degrees_cp = [p.cp_degree(hgraph) for p in cps]
    avg_cp = round(np.mean(cp_degrees_cp), 2)
    std_cp = round(np.std(cp_degrees_cp), 2)

    cp_degrees = [p.cp_degree(hgraph) for p in ps]
    avg = round(np.mean(cp_degrees), 2)
    std = round(np.std(cp_degrees), 2)


    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    kwargs = {'bins':50,
              'normed':True,
              'histtype':'step',
              'color':'k'}
 
    ax1.hist(cp_degrees_cp, **kwargs)
    ax1.set_title('Cancer Proteins Only')
    ax1.set_xlim(0,15)
    ax1.set_ylabel('Normalized frequency')
    ax1.text(5, 0.3, 'Avg: %s   Std: %s'%(str(avg_cp), str(std_cp)))

    ax2.hist(cp_degrees, **kwargs)
    ax2.set_title('Non-Cancer Proteins Only')
    ax2.set_xlim(0,15)
    ax2.set_ylabel('Normalized frequency')
    ax2.set_xlabel('Number of Cancer Protein Neighbors')
    ax2.text(5, 0.3, 'Avg: %s   Std: %s'%(str(avg), str(std)))

    filepathname = 'report/img/cp_degrees.png'
    plt.savefig(filepathname,  bbox_inches='tight')
    print 'Written to: '+filepathname
    fig.clf()
    plt.close()
    del fig

def plot_fn_degree(hgraph, fgraph):
    proteins_in_fgraph = [p for p in fgraph.nodes() \
                              if not p.is_function()]
   
    cps = [p for p in proteins_in_fgraph if p.is_cancer_protein()]
    ps = [p for p in proteins_in_fgraph if not p.is_cancer_protein()]

    cps_fn_degrees = [p.degree(fgraph) for p in cps]
    ps_fn_degrees = [p.degree(fgraph) for p in ps]

    avg_cp = round(np.mean(cps_fn_degrees), 2)
    std_cp = round(np.std(cps_fn_degrees), 2)

    avg = round(np.mean(ps_fn_degrees), 2)
    std = round(np.std(ps_fn_degrees), 2)

    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    kwargs = {'bins':50,
              'normed':True,
              'histtype':'step',
              'color':'k'}
 
    ax1.hist(cps_fn_degrees, **kwargs)
    ax1.set_title('Cancer Proteins Only')
    ax1.set_xlim(0,80)
    ax1.set_ylabel('Normalized frequency')
    ax1.text(50, 0.03, 'Avg: %s   Std: %s'%(str(avg_cp), str(std_cp)))

    ax2.hist(ps_fn_degrees, **kwargs)
    ax2.set_title('Non-Cancer Proteins Only')
    ax2.set_xlim(0,80)
    ax2.set_ylabel('Normalized frequency')
    ax2.set_xlabel('Number of Functions')
    ax2.text(50, 0.03, 'Avg: %s   Std: %s'%(str(avg), str(std)))

    filepathname = 'report/img/fn_degrees.png'
    plt.savefig(filepathname,  bbox_inches='tight')
    print 'Written to: '+filepathname
    fig.clf()
    plt.close()
    del fig

def plot_fn_cp_weight(hgraph, fgraph):
    proteins_in_fgraph = [p for p in fgraph.nodes() \
                              if not p.is_function()]
   
    cps = [p for p in proteins_in_fgraph if p.is_cancer_protein()]
    ps = [p for p in proteins_in_fgraph if not p.is_cancer_protein()]

    cps_fn_cp_weight = [p.fn_cp_weight(hgraph, fgraph) for p in cps]
    ps_fn_cp_weight = [p.fn_cp_weight(hgraph, fgraph) for p in ps]

    avg_cp = round(np.mean(cps_fn_cp_weight), 2)
    std_cp = round(np.std(cps_fn_cp_weight), 2)

    avg = round(np.mean(ps_fn_cp_weight), 2)
    std = round(np.std(ps_fn_cp_weight), 2)

    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    kwargs = {'bins':50,
              'normed':True,
              'histtype':'step',
              'color':'k'}
 
    ax1.hist(cps_fn_cp_weight, **kwargs)
    ax1.set_title('Cancer Proteins Only')
    ax1.set_ylabel('Normalized frequency')
    #ax1.set_xlim(0,80)
    #ax1.text(50, 0.03, 'Avg: %s   Std: %s'%(str(avg_cp), str(std_cp)))

    ax2.hist(ps_fn_cp_weight, **kwargs)
    ax2.set_title('Non-Cancer Proteins Only')
    ax2.set_ylabel('Normalized frequency')
    ax2.set_xlabel('Number of Functions')
    #ax2.set_xlim(0,80)
    #ax2.text(50, 0.03, 'Avg: %s   Std: %s'%(str(avg), str(std)))

    filepathname = 'report/img/fn_cp_weights.png'
    plt.savefig(filepathname,  bbox_inches='tight')
    print 'Written to: '+filepathname
    fig.clf()
    plt.close()
    del fig


def make_function_graphs(data):
    fgraph = nx.Graph(data.functions, name='Functions')

    drawkwargs = {'font_size': 10,\
                  'linewidths': 1,\
                  'width': 2,\
                  'with_labels': True,\
                  'node_size': 700,\
                  'node_color':'w',\
                  'node_shape':'o',\
                  'style':'solid',\
                  'alpha':1,\
                  'cmap': mpl.cm.jet}

    filepath = 'images'+'/functions/'

    for function in data.functions_only:
        g = nx.Graph() 
        nbrs = fgraph.neighbors(function)
        edges_to_add = [tuple([function, i]) for i in nbrs]
        g.add_edges_from(edges_to_add)

        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        pos=nx.spring_layout(g, iterations=20)
        nx.draw(g, pos, **drawkwargs )
        ax.set_title(function)

        filepathname = filepath+zeros(function, padlength=4)+'.jpg'
        plt.savefig(filepathname,  bbox_inches='tight')
        print 'Written to: '+filepathname
        fig.clf()
        plt.close()
        del fig

##Deprecated, don't call this function
def find_shortest_paths_to_cps(data):
    """
    for every protein:
        for every cp:
            find shortest path from protein to cp.
            add path to graph if path is shorter then x.

    plot graph
    """

    Tc, Tnonc = ppi.misc.get_Tc_Tnonc(data.cancer, data.test1)
    ppigraph = nx.Graph(data.humanppi, name='HumanPPI')

    for protein in Tc+Tnonc:
        g = nx.Graph()
        for cp in data.cancer:
            path = nx.shortest_path(ppigraph, source=protein, target=cp)
            if len(path) < 4:
                g.add_path(path)
            subst = (protein, cp, str(path))

        nodecolor = ['r' if node in data.cancer else 'w' for node in\
                      g.nodes()]
        nodesize = []
        nodesymbol = ['^' if node in data.cancer else 'o' for node in\
                      g.nodes()]
        plot_graph(g, protein, Tc, nodecolor, nodesymbol)
        
##Deprecated, don't call this function
def plot_graph(graph, protein, Tc, nodecolor, nodesymbol):

    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    drawkwargs = {'font_size': 10,\
                  'linewidths': 1,\
                  'width': 2,\
                  'with_labels': True,\
                  'node_size': 700,\
                  'node_color':nodecolor,\
                  'node_shape':'o',\
                  'style':'solid',\
                  'alpha':1,\
                  'cmap': mpl.cm.jet}

    pos=nx.spring_layout(graph, iterations=200)
    nx.draw(graph, pos, **drawkwargs )

    if protein in Tc:
        string = "Protein: %i  Cancer"
        string_s = (protein)
        title=string%string_s
    else:
        string = "Protein: %i  Non-Cancer"
        string_s = (protein)
        title=string%string_s
    
    ax.set_title(title)
    filepath = 'images'+'/'+zeros(protein, padlength=4)+'.jpg'
    plt.savefig(filepath,  bbox_inches='tight')
    print 'Written to: '+filepath
    fig.clf()
    plt.close()
    del fig

##Deprecated, don't call this function
def plot_degrees_histogram(degree_sorted):
    fig = plt.figure(figsize=(5,5))
    ax1 = fig.add_subplot(111)
    ax1.hist(degrees, bins=50, range=(0,50),\
             normed=True, histtype='step', color='k')
    ax1.set_xlabel('Degree')
    ax1.set_ylabel('Normalized frequency')
    plt.savefig('pictures/degrees_histogram.png', bbox_inches='tight')
    fig.clf()
    plt.close()

if __name__ == '__main__':
    main()

