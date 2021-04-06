import FWCore.ParameterSet.Config as cms
from RecoHGCal.TICL.TICLSeedingRegions_cff import ticlSeedingGlobal

filteredLayerClustersEM1 = cms.EDProducer("FilteredLayerClustersProducer",
    LayerClusters = cms.InputTag("hgcalLayerClusters"),
    LayerClustersInputMask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    algo_number = cms.int32(8),
    clusterFilter = cms.string('ClusterFilterByAlgoAndSizeAndLayerRange'),
    iteration_label = cms.string('EM1'),
    max_cluster_size = cms.int32(9999),
    max_layerId = cms.int32(30),
    mightGet = cms.optional.untracked.vstring,
    min_cluster_size = cms.int32(1),
    min_layerId = cms.int32(0)
)

filteredLayerClustersEM2 = filteredLayerClustersEM1.clone()
filteredLayerClustersEM2.min_cluster_size = cms.int32(2)
filteredLayerClustersEM2.iteration_label = cms.string('EM2')

filteredLayerClustersEM3 = filteredLayerClustersEM1.clone()
filteredLayerClustersEM3.min_cluster_size = cms.int32(3)
filteredLayerClustersEM3.iteration_label = cms.string('EM3')

ticlTrackstersEM1 = cms.EDProducer(
    "TrackstersProducer",
    algo_verbosity = cms.int32(0),
    detector = cms.string('HGCAL'),
    eid_graph_path = cms.string('RecoHGCal/TICL/data/tf_models/energy_id_v0.pb'),
    eid_input_name = cms.string('input'),
    eid_min_cluster_energy = cms.double(1),
    eid_n_clusters = cms.int32(10),
    eid_n_layers = cms.int32(50),
    eid_output_name_energy = cms.string('output/regressed_energy'),
    eid_output_name_id = cms.string('output/id_probabilities'),
    energy_em_over_total_threshold = cms.double(0.0),
    etaLimitIncreaseWindow = cms.double(2.1),
    filter_on_categories = cms.vint32(0, 1),
    filtered_mask = cms.InputTag("filteredLayerClustersEM1","EM1"),
    itername = cms.string('EM1'),
    layer_clusters = cms.InputTag("hgcalLayerClusters"),
    layer_clusters_hfnose_tiles = cms.InputTag("ticlLayerTileHFNose"),
    layer_clusters_tiles = cms.InputTag("ticlLayerTileProducer"),
    max_delta_time = cms.double(3),
    max_longitudinal_sigmaPCA = cms.double(9999),
    max_missing_layers_in_trackster = cms.int32(1),
    max_out_in_hops = cms.int32(1),
    mightGet = cms.optional.untracked.vstring,
    min_cos_pointing = cms.double(0.9),
    min_cos_theta = cms.double(0.97),
    maxLayer_cospointing = cms.int32(999),
    maxLayer_costheta = cms.int32(999),
    min_layers_per_trackster = cms.int32(5),
    oneTracksterPerTrackSeed = cms.bool(False),
    original_mask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    out_in_dfs = cms.bool(True),
    pid_threshold = cms.double(-1.0),
    promoteEmptyRegionToTrackster = cms.bool(False),
    root_doublet_max_distance_from_seed_squared = cms.double(9999),
    seeding_regions = cms.InputTag("ticlSeedingGlobal"),
    shower_start_max_layer = cms.int32(9999),
    skip_layers = cms.int32(1),
    time_layerclusters = cms.InputTag("hgcalLayerClusters","timeLayerCluster")
)

ticlTrackstersEM2 = ticlTrackstersEM1.clone()
ticlTrackstersEM2.filtered_mask = cms.InputTag("filteredLayerClustersEM2","EM2")
ticlTrackstersEM2.itername = cms.string('EM2')

ticlTrackstersEM3 = ticlTrackstersEM1.clone()
ticlTrackstersEM3.filtered_mask = cms.InputTag("filteredLayerClustersEM3","EM3")
ticlTrackstersEM3.itername = cms.string('EM3')

ticlTrackstersEM3a = ticlTrackstersEM3.clone()
ticlTrackstersEM3a.itername = cms.string('EM3a')
ticlTrackstersEM3a.skip_layers = cms.int32(2)
ticlTrackstersEM3a.max_missing_layers_in_trackster = cms.int32(1)

ticlTrackstersEM3b = ticlTrackstersEM3.clone()
ticlTrackstersEM3b.itername = cms.string('EM3b')
ticlTrackstersEM3b.skip_layers = cms.int32(2)
ticlTrackstersEM3b.max_missing_layers_in_trackster = cms.int32(9999)

ticlTrackstersEM3c = ticlTrackstersEM3.clone()
ticlTrackstersEM3c.itername = cms.string('EM3c')
ticlTrackstersEM3c.skip_layers = cms.int32(1)
ticlTrackstersEM3c.max_missing_layers_in_trackster = cms.int32(9999)




#max_missing_layers_in_trackster = cms.int32(1),
#skip_layers = cms.int32(2),
#max_out_in_hops = cms.int32(1),

em_task =  cms.Task(
    ticlSeedingGlobal,filteredLayerClustersEM1,ticlTrackstersEM1,
    ticlSeedingGlobal,filteredLayerClustersEM2,ticlTrackstersEM2,
    ticlSeedingGlobal,filteredLayerClustersEM3,ticlTrackstersEM3,
    ticlTrackstersEM3a,ticlTrackstersEM3b,ticlTrackstersEM3c
)
