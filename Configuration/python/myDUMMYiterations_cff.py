import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLSeedingRegions_cff import ticlSeedingGlobal

filteredLayerClustersALL1 = cms.EDProducer(
    "FilteredLayerClustersProducer",
    LayerClusters = cms.InputTag("hgcalLayerClusters"),
    LayerClustersInputMask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    algo_number = cms.int32(8),
    clusterFilter = cms.string('ClusterFilterByAlgoAndSize'),
    iteration_label = cms.string('ALL1'),
    max_cluster_size = cms.int32(9999),
    max_layerId = cms.int32(9999),
    mightGet = cms.optional.untracked.vstring,
    min_cluster_size = cms.int32(0),
    min_layerId = cms.int32(0)
)

filteredLayerClustersALL2 = filteredLayerClustersALL1.clone()
filteredLayerClustersALL2.min_cluster_size = cms.int32(2)
filteredLayerClustersALL2.iteration_label = cms.string('ALL2')

filteredLayerClustersALL3 = filteredLayerClustersALL1.clone()
filteredLayerClustersALL3.min_cluster_size = cms.int32(3)
filteredLayerClustersALL3.iteration_label = cms.string('ALL3')

ticlTrackstersDummy1 = cms.EDProducer(
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
    filter_on_categories = cms.vint32(),
    filtered_mask = cms.InputTag("filteredLayerClustersALL1","ALL1"),
    itername = cms.string('DUMMY1'),
    layer_clusters = cms.InputTag("hgcalLayerClusters"),
    layer_clusters_hfnose_tiles = cms.InputTag("ticlLayerTileHFNose"),
    layer_clusters_tiles = cms.InputTag("ticlLayerTileProducer"),
    max_delta_time = cms.double(-1.),
    max_longitudinal_sigmaPCA = cms.double(9999),
    max_missing_layers_in_trackster = cms.int32(9999),
    max_out_in_hops = cms.int32(10),
    mightGet = cms.optional.untracked.vstring,
    min_cos_pointing = cms.double(0.),
    min_cos_theta = cms.double(0.),
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


ticlTrackstersDummy2 = ticlTrackstersDummy1.clone()
ticlTrackstersDummy2.filtered_mask = cms.InputTag("filteredLayerClustersALL2", "ALL2")
ticlTrackstersDummy2.itername = "DUMMY2"

ticlTrackstersDummy3 = ticlTrackstersDummy1.clone()
ticlTrackstersDummy3.filtered_mask = cms.InputTag("filteredLayerClustersALL3", "ALL3")
ticlTrackstersDummy3.itername = "DUMMY3"


dummy_task =  cms.Task(
    #ticlSeedingGlobal,filteredLayerClustersALL1,ticlTrackstersDummy1,
    #ticlSeedingGlobal,filteredLayerClustersALL2,ticlTrackstersDummy2,
    ticlSeedingGlobal,filteredLayerClustersALL3,ticlTrackstersDummy3
)
