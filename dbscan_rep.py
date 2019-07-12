from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.dbscan import dbscan

from pyclustering.utils import read_sample
from pyclustering.utils import timedcall

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES, SEQUOIA_SAMPLES

tempos_dbscan = []


def template_clustering(radius, neighb, path, invisible_axes = False, ccore = False, show = True, tempos = tempos_dbscan):
    sample = read_sample(path)
    
    dbscan_instance = dbscan(sample, radius, neighb, ccore)
    (ticks, _) = timedcall(dbscan_instance.process)
    
    clusters = dbscan_instance.get_clusters()
    noise = dbscan_instance.get_noise()
    
    print([len(cluster) for cluster in clusters])
    
    if show:
        visualizer = cluster_visualizer()
        visualizer.append_clusters(clusters, sample)
        visualizer.append_cluster(noise, sample, marker = 'x')
        visualizer.show()
    
    print("Sample: ", path, "\t\tExecution time: ", ticks, "\n")

    tempos_dbscan.append(ticks)

    return sample, clusters, noise

#Função para medir tempo de execução do algoritmo DBSCAN no conjunto de dados SEQUOIA.
def experiment_execution_time_sequoia(ccore = False, show = False):
    "Performance measurement"
    template_clustering(23000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA1252, False, ccore, show)
    template_clustering(22000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA2503, False, ccore, show)
    template_clustering(18000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA3910, False, ccore, show)
    template_clustering(17000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA5213, False, ccore, show)
    template_clustering(16000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA6256, False, ccore, show)
    template_clustering(13000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA7820, False, ccore, show)
    template_clustering(12000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA8937, False, ccore, show)
    template_clustering(12000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA10426, False, ccore, show)
    template_clustering(12000, 4, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA12512, False, ccore, show)
    print(tempos_dbscan)

#Clusterização de oito conjunto de dados do FCPS utilizando o DBSCAN.
def display_fcps_clustering_results():
    (lsun, lsun_clusters, _) = template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_LSUN, False, True, False)
    (target, target_clusters, _) = template_clustering(0.5, 2, FCPS_SAMPLES.SAMPLE_TARGET, False, True, False)
    (two_diamonds, two_diamonds_clusters, _) = template_clustering(0.15, 7, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, False, True, False)
    (wing_nut, wing_nut_clusters, _) = template_clustering(0.25, 2, FCPS_SAMPLES.SAMPLE_WING_NUT, False, True, False)
    (chainlink, chainlink_clusters, _) = template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_CHAINLINK, False, True, False)
    (hepta, hepta_clusters, _) = template_clustering(1, 3, FCPS_SAMPLES.SAMPLE_HEPTA, False, True, False)
    (tetra, tetra_clusters, _) = template_clustering(0.4, 3, FCPS_SAMPLES.SAMPLE_TETRA, False, True, False)
    (atom, atom_clusters, _) = template_clustering(15, 3, FCPS_SAMPLES.SAMPLE_ATOM, False, True, False)
    
    visualizer = cluster_visualizer(8, 4)
    visualizer.append_clusters(lsun_clusters, lsun, 0)
    visualizer.append_clusters(target_clusters, target, 1)
    visualizer.append_clusters(two_diamonds_clusters, two_diamonds, 2)
    visualizer.append_clusters(wing_nut_clusters, wing_nut, 3)
    visualizer.append_clusters(chainlink_clusters, chainlink, 4)
    visualizer.append_clusters(hepta_clusters, hepta, 5)
    visualizer.append_clusters(tetra_clusters, tetra, 6)
    visualizer.append_clusters(atom_clusters, atom, 7)
    visualizer.show()

#Clusterização de oito conjunto de dados SIMPLE utilizando o DBSCAN.
def display_simple_dbscan_results():
        (simple1, simple1_clusters, _) = template_clustering(0.4, 2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1)
        (simple2, simple2_clusters, _) = template_clustering(1, 2, SIMPLE_SAMPLES.SAMPLE_SIMPLE2)
        (simple3, simple3_clusters, _) = template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE3)
        (simple4, simple4_clusters, _) = template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE4)
        (simple5, simple5_clusters, _) = template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE5)
        (simple6, simple6_clusters, _) = template_clustering(1, 2, SIMPLE_SAMPLES.SAMPLE_SIMPLE6)
        (simple7, simple7_clusters, _) = template_clustering(1.0, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE7)
        (simple8, simple8_clusters, _) = template_clustering(1.0, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE8)

        visualizer = cluster_visualizer(8, 4)
        visualizer.append_clusters(simple1_clusters, simple1, 0)
        visualizer.append_clusters(simple2_clusters, simple2, 1)
        visualizer.append_clusters(simple3_clusters, simple3, 2)
        visualizer.append_clusters(simple4_clusters, simple4, 3)
        visualizer.append_clusters(simple5_clusters, simple5, 4)
        visualizer.append_clusters(simple6_clusters, simple6, 5)
        visualizer.append_clusters(simple7_clusters, simple7, 6)
        visualizer.append_clusters(simple8_clusters, simple8, 7)
        visualizer.show()




