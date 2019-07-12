from pyclustering.cluster.clarans import clarans;
from pyclustering.cluster import cluster_visualizer;

from pyclustering.utils import read_sample;
from pyclustering.utils import draw_clusters;
from pyclustering.utils import timedcall;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES, SEQUOIA_SAMPLES;

tempos_clarans = []

def template_clustering(number_clusters, path, iterations, maxneighbors):
    sample = read_sample(path);

    clarans_instance = clarans(sample, number_clusters, iterations, maxneighbors);
    (ticks, result) = timedcall(clarans_instance.process);

    print("Sample: ", path, "\t\tExecution time: ", ticks, "\n");
    tempos_clarans.append(ticks)

    clusters = clarans_instance.get_clusters();
    #draw_clusters(sample, clusters);
    return sample, clusters


#Função para medir tempo de execução do algoritmo CLARANS no conjunto de dados SEQUOIA.
def experiment_execution_time_sequoia_clarans():
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA1252, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA2503, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA3910, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA5213, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA6256, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA7820, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA8937, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA10426, 2, 2)
    template_clustering_time(2, SEQUOIA_SAMPLES.SAMPLE_SEQUOIA12512, 2, 2)
    print(tempos_clarans)


#Clusterização de oito conjunto de dados SIMPLE utilizando o CLARANS.
def display_simple_clarans_results():
        (simple1, simple1_clusters) = template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 10, 3);
        (simple2, simple2_clusters) = template_clustering(3, SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 10, 3);
        (simple3, simple3_clusters) = template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 10, 3);
        (simple4, simple4_clusters) = template_clustering(5, SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 10, 4);
        (simple5, simple5_clusters) = template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 10, 5);
        (simple6, simple6_clusters) = template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE6, 10, 3);
        (simple7, simple7_clusters) = template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE7, 10, 3);
        (simple8, simple8_clusters) = template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE8, 15, 5);


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


#Clusterização de oito conjunto de dados do FCPS utilizando o CLARANS.
def display_fcps_clarans_results():
    (lsun, lsun_clusters) = template_clustering(3, FCPS_SAMPLES.SAMPLE_LSUN, 10, 5);
    (target, target_clusters) = template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET, 10, 5);
    (two_diamonds, two_diamonds_clusters) = template_clustering(2, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 2, 2);
    (wing_nut, wing_nut_clusters) = template_clustering(2, FCPS_SAMPLES.SAMPLE_WING_NUT, 2, 2);
    (chainlink, chainlink_clusters) = template_clustering(2, FCPS_SAMPLES.SAMPLE_CHAINLINK, 2, 2);
    (hepta, hepta_clusters) = template_clustering(7, FCPS_SAMPLES.SAMPLE_HEPTA, 2, 2);
    (tetra, tetra_clusters) = template_clustering(4, FCPS_SAMPLES.SAMPLE_TETRA, 2, 2);
    (atom, atom_clusters) = template_clustering(2, FCPS_SAMPLES.SAMPLE_ATOM, 2, 2);

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

